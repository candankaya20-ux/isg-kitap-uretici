import os
from pathlib import Path
from openai import OpenAI

Path("outputs").mkdir(exist_ok=True)

prompt = Path("prompt.md").read_text(encoding="utf-8")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("Üretim başlıyor...")

response = client.responses.create(
    model="gpt-5",
    input=prompt + "\n\nSoru 1-25 arası 25 soruluk segment üret. Açıklamalı olsun."
)

text = response.output_text

Path("outputs/segment_001_025.md").write_text(text, encoding="utf-8")

print("Tamamlandı ✅")
