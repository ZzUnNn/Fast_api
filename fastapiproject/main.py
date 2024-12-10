from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
import uvicorn
from api.student import student_api
from api.group import group_api
from settings import TORTOISE_ORM
app=FastAPI()
app.include_router(student_api,prefix="/student",tags=["Student"])
app.include_router(group_api,prefix="/group",tags=["Group"])
register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,

)
if __name__=='__main__':
     uvicorn.run("main:app",host='127.0.0.1',port=8080,reload=True,workers=1)
 