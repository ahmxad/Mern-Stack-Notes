## TO-DO APP

Basic Roadmap:
#### SQL
- What we need in database:

- - CREATE TABLE

- - INSERT INTO

- - SELECT

- - UPDATE

- - DELETE

- - PRIMARY 

- - NOT NULL / DEFAULT

1) App basics

### FastAPI()

@app.get

@app.post

@app.put / @app.patch

@app.delete

2) Request & Response

Path params (/todos/{id})

Query params (?completed=true)

Request body (Pydantic BaseModel)

Response JSON

3) Status codes

status_code=201

404 Not Found

400 Bad Request

4) Validation

Pydantic schemas

Optional fields

Required fields

5) Database connection

SQLAlchemy engine

engine.connect() / engine.begin()

text() queries

6) Error handling

HTTPException

7) CORS

CORSMiddleware

#### React

1) Basics

Components

JSX

props

2) State

useState

3) Side effects

useEffect (API call)

4) API integration

fetch / axios

GET / POST / PUT / DELETE

5) Forms

Controlled inputs

onChange

onSubmit

6) Conditional rendering

loading

empty list

7) Lists

.map()

key

8) Simple UI logic

add todo

delete todo

mark completed