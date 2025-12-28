from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, text
from fastapi.middleware.cors import CORSMiddleware

DATABASE_URL = "postgresql://postgres:abc12345@localhost:5432/postgres"
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

app = FastAPI(title="navi navi app banan laggi hoi hai")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/users")
def get_users():
    with engine.connect() as conn:
        rows = conn.execute(
            text("SELECT id, email FROM users")
        ).fetchall()

    return [dict(row._mapping) for row in rows]

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    with engine.begin() as conn:
        result = conn.execute(
            text("DELETE FROM users WHERE id = :id"),
            {"id": user_id}
        )

    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User deleted"}

@app.delete("/users")
def delete_table():
    with engine.begin() as conn:
        result = conn.execute(
            text("TRUNCATE TABLE users;"),
        )

    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="No table here")

    return {"message": "table deleted"}