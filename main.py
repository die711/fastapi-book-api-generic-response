from fastapi import FastAPI
import uvicorn

from app.db.config import Base
from app.db.config import engine
from app.routes.routes import router as router_crud

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(router=router_crud, tags=['CRUD'], prefix='/books')


@app.get('/')
def hello_world_check():
    return {
        'msg': 'Hola Mundo'
    }


if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', reload=True, port=8000)
