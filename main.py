from fastapi import FastAPI, Request
import openai
import os

# Khởi tạo API client theo cách mới
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

@app.post("/generate-review")
async def generate_review(req: Request):
    data = await req.json()
    name = data.get("name")
    description = data.get("description")
    prompt = f"Viết một đánh giá 5 sao, thân thiện cho sản phẩm: {name}. Mô tả: {description}"

    # Gọi OpenAI GPT-4 theo SDK mới
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return {"review": response.choices[0].message.content}
