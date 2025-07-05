from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

# Khai báo schema cho dữ liệu đầu vào
class ProductInfo(BaseModel):
    name: str
    description: str

# API với input kiểu ProductInfo
@app.post("/generate-review")
async def generate_review(data: ProductInfo):
    prompt = f"Viết một đánh giá 5 sao, thân thiện cho sản phẩm: {data.name}. Mô tả: {data.description}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return {"review": response['choices'][0]['message']['content']}
