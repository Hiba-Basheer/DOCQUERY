# DOCQUERY – AI-Powered Document Intelligence System

This is a simple document intelligence system. You can upload images of invoices or receipts, it extracts text and answers questions about the content.

---

## 1. Architecture Overview

The system pipeline:
User → FastAPI API → OCR (Tesseract) → SQLite DB → LLM (T5-small) → Answer



- FastAPI: REST API with `/upload`, `/ask`, `/health`  
- OCR (pytesseract): extract text from images or PDFs  
- SQLite: store document text and metadata  
- LLM (T5-small): answer questions about uploaded documents  
- Logging: simple info/error logs  
- Docker: containerized app for easy running  

---

## 2. Model and Library Choices

| Component      | Choice                | Reason |
|----------------|---------------------|--------|
| OCR            | pytesseract          | Simple, works well for invoices and receipts |
| LLM            | google/flat-t5-small | Lightweight, fast, open-source |
| Web Framework  | FastAPI              | Easy to create endpoints and test them |
| Database       | SQLite               | Lightweight, simple, good for this assignment |
| Docker         | python:3.11-slim     | Easy to containerize, reproducible |

---

## 3. Completed Features

- Upload images/PDFs and extract text  
- Store text and metadata in SQLite  
- Question answering using T5-small LLM  
- Health endpoint to check API  
- Logging and error handling  
- Dockerized for easy deployment  
- Unit tests for `/health`, `/upload`, `/ask`  

---

## 4. Incomplete / Skipped Features

- Multi-page PDF support not added  
- Asynchronous processing for faster uploads/questions  
- Authentication/user management missing  
- More unit tests for edge cases can be added  

---

## 5. Improvements With More Time

- Use larger LLM or chunking for better QA  
- Move from SQLite to PostgreSQL/MongoDB  
- Use PaddleOCR/EasyOCR for better OCR accuracy  
- Add frontend for user-friendly upload and QA  
- Add caching for repeated questions  
- More robust logging  

---

## Project Structure


```
DOCQUERY/
├── app/
│ ├── main.py # FastAPI app
│ ├── ocr_utils.py
│ ├── qa_utils.py 
│ ├── database.py 
│ └── helpers.py
│
├── tests/
│ └── test_api.py 
│
├── Dockerfile # containerization
├── requirements.txt # dependencies
└── README.md 
```


- Clear separation of code, tests, and deployment  
- Dockerfile for running anywhere  

---


