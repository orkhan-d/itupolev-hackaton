from fastapi import FastAPI, HTTPException
from fastapi.params import Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from db.crud.students import get_user_by_credentials

from db.base import get_db

app = FastAPI()


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
