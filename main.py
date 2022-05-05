import uvicorn
from fastapi import FastAPI
from app.config import app_config

# app = FastAPI()
app = FastAPI(docs_url='/thor-scrapping/docs',openapi_url='/thor-cscrapping/openapi.json')
# app.include_router(post_route)

@app.get("/thor-stock-data/secure/health")
def healthcheck():
    return {"status":"Service is Running"}

@app.get("/check")
def check():
    return "YOYO"


if __name__ == '__main__':
    uvicorn.run("main:app",host=app_config.HOST,port=app_config.PORT,debug=app_config.DEBUGMODE)
    