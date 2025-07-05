from fastapi import FastAPI, Request
from openai import OpenAI
import os

app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.post("/generate-review")
async def generate_review(req: Request):
    data = await req.json()
    name = data.get("name")
    description = data.get("description")

    prompt = f"Viết một đánh giá 5 sao, thân thiện cho sản phẩm: {name}. Mô tả: {description}"

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        review_text = response.choices[0].message.content
        return {"review": review_text}
    except Exception as e:
        return {"error": str(e)}
