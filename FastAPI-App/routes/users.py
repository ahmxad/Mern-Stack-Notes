from fastapi import APIRouter, HTTPException
from sqlalchemy import text
from database import engine
from schemas import UserCreate, UserUpdate

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("")
def get_users():
    with engine.connect() as conn:
        rows = conn.execute(
            text("SELECT id, email FROM users")
        ).fetchall()

    return [dict(r._mapping) for r in rows]


@router.get("/{user_id}")
def get_user(user_id: int):
    with engine.connect() as conn:
        row = conn.execute(
            text("SELECT id, email FROM users WHERE id = :id"),
            {"id": user_id}
        ).fetchone()

    if not row:
        raise HTTPException(status_code=404, detail="User not found")

    return dict(row._mapping)


@router.post("", status_code=201)
def create_user(user: UserCreate):
    with engine.begin() as conn:
        conn.execute(
            text("""
                INSERT INTO users (email, password)
                VALUES (:email, :password)
            """),
            user.model_dump()
        )

    return {"message": "User created"}


@router.patch("/{user_id}")
def update_user(user_id: int, user: UserUpdate):
    data = user.model_dump(exclude_none=True)

    if not data:
        raise HTTPException(status_code=400, detail="Nothing to update")

    fields = ", ".join(f"{k} = :{k}" for k in data)
    data["id"] = user_id

    with engine.begin() as conn:
        result = conn.execute(
            text(f"UPDATE users SET {fields} WHERE id = :id"),
            data
        )

    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User updated"}


@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int):
    with engine.begin() as conn:
        result = conn.execute(
            text("DELETE FROM users WHERE id = :id"),
            {"id": user_id}
        )

    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="User not found")
