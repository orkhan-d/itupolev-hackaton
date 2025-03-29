from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from db.base import get_db

app = FastAPI()


@app.get('/ping')
async def pong(session: AsyncSession = Depends(get_db)):
    async with session:
        res = await session.execute(text("SELECT 1"))
        return {"res": res.scalar_one()}
    # return {"ping": "pong"}