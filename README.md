📄 CV Reader API (FastAPI + PDF Extraction + AI Parsing)

A simple backend system that allows users to upload CVs (PDFs), extract text, and prepare structured data for further processing (like AI parsing or storage).

🚀 Features
📤 Upload PDF CV files via API
📄 Extract raw text from PDFs
💾 Store uploaded files locally
⚡ Built with FastAPI (fast & modern Python backend)
🧠 Ready for AI-based CV parsing (Claude / GPT integration)
🗄️ Extensible for database storage (SQLite / vector DB)


⚙️ Installation
1. Clone repo
git clone https://github.com/your-username/cv-reader.git
cd cv-reader
2. Create virtual environment
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
3. Install dependencies
pip install -r requirements.txt
▶️ Run the project
uvicorn main:app --reload

Server will run at:

http://127.0.0.1:8000
📤 API Usage
Upload CV

Endpoint:

POST /upload
Test via Swagger UI:
http://127.0.0.1:8000/docs
Response:
{
  "message": "File uploaded successfully",
  "file_path": "uploaded_cvs/john_cv.pdf",
  "preview": "first extracted text..."
}