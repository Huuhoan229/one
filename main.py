from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import openai
import os

app = FastAPI()

# Lấy API key từ biến môi trường
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/generate-review")
async def generate_review(req: Request):
    try:
        data = await req.json()
        name = data.get("name")
        description = data.get("description")

        # Kiểm tra dữ liệu đầu vào
        if not name or not description:
            return JSONResponse(status_code=400, content={"error": "Thiếu tên hoặc mô tả sản phẩm"})

        # Kiểm tra API key
        if not openai.api_key:
            return JSONResponse(status_code=500, content={"error": "Chưa thiết lập OPENAI_API_KEY"})

        prompt = f"Viết một đánh giá 5 sao, thân thiện cho sản phẩm: {name}. Mô tả: {description}"

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )

        review_text = response['choic]()_
