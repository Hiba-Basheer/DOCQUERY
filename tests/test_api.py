import io
import pytest
from fastapi.testclient import TestClient
from app.main import app

# unit test for the API
client = TestClient(app)

# health test
def test_health():
    response = client.get('/health')
    print("Health endpoint response:", response.json())
    assert response.status_code == 200
    # checking if if the response is ok for the status
    assert response.json()['status'] == 'ok'
    
# test upload endpoint
def test_upload():
    # creating a fake image file in memory
    fake_image = io.BytesIO(b'fake image bytes')
    fake_image.name = 'sample.jpg'
    
    response = client.post(
        '/upload',
        files={'file': ('sample.jpg', fake_image, 'image/jpeg')}
    )
    
    print("Upload response:", response.json())
    assert response.status_code == 200
    data = response.json()
    assert "doc_id" in data
    assert "metadata" in data
    
# test create_question end point
def test_ask():
    # uploading tje fake document
    fake_image = io.BytesIO(b"fake image bytes")
    fake_image.name = "sample2.jpg"

    upload_resp = client.post(
        "/upload",
        files={"file": ("sample2.jpg", fake_image, "image/jpeg")}
    )
    doc_id = upload_resp.json().get("doc_id")

    # asking a simple question
    question_payload = {"doc_id": doc_id, "question": "What is the invoice date?"}
    ask_resp = client.post("/ask", json=question_payload)

    print("Ask response:", ask_resp.json())
    assert ask_resp.status_code == 200
    data = ask_resp.json()
    assert "answer" in data