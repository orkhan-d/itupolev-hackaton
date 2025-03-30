from fastapi import FastAPI, HTTPException
from fastapi.params import Depends
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.middleware.cors import CORSMiddleware

from db.crud.notes import add_note, get_notes
from db.crud.students import get_user_by_credentials
from db.crud.timestables import get_teacher_timetable, get_class_timetable
from db.base import get_db
from datetime import datetime as dt
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/ping')
async def pong(session: AsyncSession = Depends(get_db)):
    async with session:
        res = await session.execute(text("SELECT 1"))
        return {"res": res.scalar_one()}
    # return {"ping": "pong"}


@app.post("/autorisation", tags=["Авторизация"])
async def autorisation(login: str,
                       password: str,
                       session: AsyncSession = Depends(get_db)):
    student = await get_user_by_credentials(login, password, session)
    if student is None:
        raise HTTPException(status_code=401, detail="auth faild")
    else:
        return student
    
@app.get("/timetable", tags=["Сходство"])
async def similarity(
    class_id: int | None = None,
    teacher_id: int | None = None,
    session: AsyncSession = Depends(get_db)
):

    if class_id:
        timetable = await get_class_timetable(class_id, session)
    elif teacher_id:
        timetable = await get_teacher_timetable(teacher_id, session)
    else:
        raise HTTPException(
            status_code=422,
            detail="Invalid data"
        )

    return timetable


class NoteCreate(BaseModel):
    title: str
    content: str
    teacher_id: int
    student_id: int
    deadline: dt


@app.post("/notes")
async def create_note_api(
        note: NoteCreate,
        session: AsyncSession = Depends(get_db)
):
    note = await add_note(**note.model_dump(), session=session)
    return note


@app.get("/notes")
async def create_note_api(
    student_id: int,
    session: AsyncSession = Depends(get_db)
):
    notes = await get_notes(student_id, session=session)
    return notes
