# 🤖 AI CV Matcher

PDF formatındaki CV'leri iş ilanı açıklamalarıyla yapay zeka kullanarak eşleştiren bir REST API.

---

## 🚀 Özellikler

- PDF CV yükleme ve otomatik metin çıkarma
- Semantic similarity (anlamsal benzerlik) tabanlı eşleştirme
- 0–100 arası uyum skoru döndürme
- Hafif ve hızlı: `all-MiniLM-L6-v2` modeli ile düşük gecikme

---

## 🛠️ Kurulum

### Gereksinimler

- Python 3.9+
- pip

### Adımlar

```bash
# Repoyu klonla
git clone https://github.com/kullanici/ai-cv-matcher.git
cd ai-cv-matcher

# Sanal ortam oluştur (önerilir)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Bağımlılıkları yükle
pip install fastapi uvicorn pypdf sentence-transformers torch
```

---

## ▶️ Çalıştırma

```bash
uvicorn main:app --reload
```

API varsayılan olarak `http://localhost:8000` adresinde çalışır.

---

## 📡 API Referansı

### `GET /`

Servisin ayakta olduğunu doğrular.

**Yanıt:**
```json
{
  "message": "AI CV Matcher çalışıyor"
}
```

---

### `POST /match/`

CV ile iş ilanını karşılaştırır ve uyum skoru döndürür.

**İstek (multipart/form-data):**

| Alan | Tür | Açıklama |
|---|---|---|
| `file` | `UploadFile` | PDF formatında CV dosyası |
| `job_description` | `string` | İş ilanı metni |

**Örnek (curl):**
```bash
curl -X POST "http://localhost:8000/match/" \
  -F "file=@cv.pdf" \
  -F "job_description=Python ve FastAPI konusunda deneyimli backend geliştirici arıyoruz."
```

**Başarılı Yanıt:**
```json
{
  "match_score": 78.43,
  "status": "success"
}
```

> `match_score`: 0 ile 100 arasında bir değer. Ne kadar yüksekse CV ile ilan o kadar uyumludur.

---

## 🧠 Nasıl Çalışır?

1. Yüklenen PDF dosyasından `pypdf` ile ham metin çıkarılır.
2. CV metni ve iş ilanı metni, `sentence-transformers` kütüphanesi ile vektöre dönüştürülür (`all-MiniLM-L6-v2` modeli).
3. İki vektör arasındaki **cosine similarity** hesaplanır ve 100 üzerinden skorlanır.

```
CV Metni ──► Embedding ──┐
                          ├──► Cosine Similarity ──► Match Score
İş İlanı ──► Embedding ──┘
```

---

## 📦 Bağımlılıklar

| Paket | Amaç |
|---|---|
| `fastapi` | Web API framework |
| `uvicorn` | ASGI sunucusu |
| `pypdf` | PDF'ten metin çıkarma |
| `sentence-transformers` | Embedding modeli |
| `torch` | Tensor işlemleri (cosine similarity) |

---
