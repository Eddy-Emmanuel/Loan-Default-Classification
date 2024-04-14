import  uvicorn
from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html

from database.session import Base, engine
from routes.api_routes import USER_ROUTER, MODEL_ROUTER

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router=USER_ROUTER)
app.include_router(router=MODEL_ROUTER)

@app.get("/")
def GetHomePage():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="HomePage")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="127.0.0.1", port=8000)