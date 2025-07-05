from fastapi import FastAPI, Request
import openai
import os

app = FastAPI()

# Đảm bảo khóa API được nạp từ biến môi trường
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/generate-review")
async def generate_review(req: Request):
    data = await req.json()
    name = data.get("name", "")
    description = data.get("description", "")
    
    prompt = f"Viết một đánh giá 5 sao, thân thiện cho sản phẩm: {name}. Mô tả: {description}."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # hoặc gpt-4 nếu bạn có quyền truy cập
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    review_text = response['choices'][0]['message']['content']
    return {"review": review_text}

# Chạy server với cổng 8080 (bắt buộc với Railway)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
