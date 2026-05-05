import os
from pathlib import Path
from openai import OpenAI

# klasör oluştur
Path("outputs").mkdir(exist_ok=True)

# prompt oku
prompt = Path("prompt.md").read_text(encoding="utf-8")

# API bağlan
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("Üretim başlıyor...")

# OpenAI çağrısı
response = client.responses.create(
    model="gpt-5",
    input=prompt + "\n\nSadece 25 soruluk segment üret (Soru 1-25)"
)

# metni al
text = response.output_text

# dosyaya yaz
Path("outputs/segment_001_025.md").write_text(text, encoding="utf-8")

print("Tamamlandı ✅")
print("outputs/segment_001_025.md oluşturuldu")
