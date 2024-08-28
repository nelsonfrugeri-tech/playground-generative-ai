import torch
from transformers import Pipeline, pipeline

prompt = "How to set up a FastAPI project?"
system_prompt = """
Your name is FastAPI bot and you are a helpful
chatbot responsible for teaching FastAPI to your users.
Always respond in markdown.
"""

def load_text_model():
    print("pass step 1")
    pipe = pipeline(
        "text-generation",
        model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        torch_dtype=torch.bfloat16,
    )
    print("pass step 2")
    return pipe


def generate_text(pipe: Pipeline, prompt: str, temperature: float = 0.7) -> str:
    print("pass step 3")
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt},
    ]
    prompt = pipe.tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    predictions = pipe(
        prompt,
        temperature=temperature,
        max_new_tokens=256,
        do_sample=True,
        top_k=50,
        top_p=0.95,
    )
    output = predictions[0]["generated_text"].split("</s>\n<|assistant|>\n")[-1]
    print("pass step 4")
    return output