from fastapi import FastAPI, HTTPException
from app.schemas import EmailRequest
from app.email_sender import EmailSender

app = FastAPI()
email_sender = EmailSender()

@app.get("/")
def root():
    return {"message": "Email service is running"}

@app.post("/send-email/")
def send_email(request: EmailRequest):
    try:
        email_sender.send_email(request.to_email, request.subject, request.body)
        return {"message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
