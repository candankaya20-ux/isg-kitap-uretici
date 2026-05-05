
import os
from pathlib import Path
from openai import OpenAI

OUTPUT = Path("outputs")
OUTPUT.mkdir(exist_ok=True)

prompt = Path("prompt.md").read_text(encoding="utf-8")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

segment_prompt = f"""
{prompt}

ŞİMDİ SADECE 25 SORULUK GEÇİCİ SEGMENT ÜRET.

Kurallar:
- 25 soru blok değildir.
- 50 soru ana blok değildir.
- 100 soru ana üretim bloğudur.
- Bu çalıştırmada yalnız Soru 1-25 üret.
- Cevap ve ayrıntılı çözümleri yaz.
- Mevzuat Zaman Kilidi ekle.
- Sonunda devam aralığını bildir.
"""

response = client.responses.create(
    model="gpt-5",
    input=segment_prompt
)

text = response.output_text

Path("outputs/segment_001_025.md").write_text(text, encoding="utf-8")

print("Tamamlandı.")
print("Çıktı: outputs/segment_001_025.md")
