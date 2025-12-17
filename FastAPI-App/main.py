from fastapi import FastAPI
from sqlalchemy import create_engine, text
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

DATABASE_URL = "postgresql://postgres:abc12345@localhost:5432/demo_db"
engine = create_engine(DATABASE_URL)

# -------- Schema (request body) --------
class UserCreate(BaseModel):
    email: str
    password: str

class UserUpdate(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None

# -------- GET: sab users laao --------
@app.get("/users")
def get_users():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT id, email FROM users")) # you can also retrive password 😹
        rows = result.fetchall()

    return [dict(row._mapping) for row in rows]

@app.get("/users/{user_id}")
def get_user(user_id: int):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT id, email FROM users WHERE id = :id"),
            {"id": user_id}
        )
        row = result.fetchone()

    if row is None:
        return {"error": "user not found"}

    return dict(row._mapping)


# -------- POST: naya user banao --------
@app.post("/users")
def create_user(user: UserCreate):
    with engine.connect() as conn:
        conn.execute(
            text("""
                INSERT INTO users (email, password)
                VALUES (:email, :password)
            """),
            {
                "email": user.email,
                "password": user.password
            }
        )
        conn.commit()

    return {"status": "user created"}

@app.patch("/users/{user_id}")
def update_user(user_id: int, user: UserUpdate):
    if user.email is None and user.password is None:
        return {"error": "nothing to update"}

    fields = []
    values = {"id": user_id}

    if user.email is not None:
        fields.append("email = :email")
        values["email"] = user.email

    if user.password is not None:
        fields.append("password = :password")
        values["password"] = user.password

    query = f"""
        UPDATE users
        SET {", ".join(fields)}
        WHERE id = :id
    """

    with engine.connect() as conn:
        result = conn.execute(text(query), values)
        conn.commit()

    if result.rowcount == 0:
        return {"error": "user not found"}

    return {"status": "user updated"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    with engine.connect() as conn:
        result = conn.execute(
            text("DELETE FROM users WHERE id = :id"),
            {"id": user_id}
        )
        conn.commit()

    if result.rowcount == 0:
        return {"error": "user not found"}

    return {"status": "user deleted"}
