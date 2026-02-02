from fastapi import FastAPI, UploadFile, File, HTTPException
import uuid
import logging
from PIL import Image

# importing functions from other files
from app.ocr_utils import text_creation
from app.database import create_tab, save_contents, get_document_text
from app.qa_utils import create_ans
from app.helpers import set_logging

app = FastAPI()

# logging setup
set_logging()
logging.info('Starting DOCQUERY API')

# checking the health of the end points
@app.get('/health')
def checking_status():
    return {'status': 'okay'}

# processing OCR for the uploaded image
@app.post('/upload')
async def process_image(file: UploadFile = File(...)):
    # checking the file having the right format
    if not file.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.pdf')):
        raise HTTPException(status_code=400, detail='file not in the correct format')
    
    # reading the file
    content = await file.read()
    
    # processing OCR
    text, metadata = text_creation(content)
    
    doc_id = str(uuid.uuid4())
    # saving document
    save_contents(doc_id, file.filename, text, metadata)
    
    logging.info(f'Document {doc_id} processed and saved')
    return {'doc_id': doc_id, 'metadata': metadata}

# setting the question-answering part
@app.post('/ask')
def ask_que(doc_id: str, question: str):
    text = get_document_text(doc_id)
    if not text:
        raise HTTPException(status_code=404, detail="Document isn't found")
    answer = create_ans(text, question)
    logging.info(f'Question asked for the document: {doc_id}')
    return {'answer': answer}