from fastapi import FastAPI, UploadFile, File, Form
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer, util

app = FastAPI()
model = SentenceTransformer("all-MiniLM-L6-v2")


def extract_text(file):
    reader = PdfReader(file.file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


@app.get("/")
def home():
    return {"message": "AI CV Matcher çalışıyor"}


@app.post("/match/")
async def match_cv(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):

    cv_text = extract_text(file)

    cv_emb = model.encode(cv_text, convert_to_tensor=True)
    job_emb = model.encode(job_description, convert_to_tensor=True)

    score = util.pytorch_cos_sim(cv_emb, job_emb).item()
    score = round(score * 100, 2)

    return {
        "match_score": score,
        "status": "success"
    }

