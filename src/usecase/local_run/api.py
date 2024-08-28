from fastapi import FastAPI, Query
# from generate_text import load_text_model, generate_text
import uvicorn

app = FastAPI()


@app.get("/generate/text")
def serve_language_model_controller(prompt=Query(...)):
    pipe = load_text_model()
    output = generate_text(pipe, prompt)
    return output

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)