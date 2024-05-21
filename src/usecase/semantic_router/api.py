from fastapi import FastAPI
from router import Router


app = FastAPI()
router = Router()

@app.post(
    "/router",
    response_model=str,
    response_model_exclude_none=True,
    status_code=200,
)
def text(request_body: dict):
    content = request_body["prompt"]["messages"][0]["content"]
    print(f"***CONTENT {content}")
    return router.handler(content)