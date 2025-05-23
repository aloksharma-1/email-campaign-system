from fastapi import FastAPI, HTTPException
from model import Campaign
from firestore_client import db
from uuid import uuid4
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Campaign Service")

# CORS if needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # adjust for security
    allow_methods=["*"],
    allow_headers=["*"],
)

COLLECTION_NAME = "campaigns"

@app.post("/campaigns/", response_model=Campaign)
async def create_campaign(campaign: Campaign):
    campaign.id = str(uuid4())
    doc_ref = db.collection(COLLECTION_NAME).document(campaign.id)
    doc_ref.set(campaign.dict())
    return campaign

@app.get("/campaigns/", response_model=List[Campaign])
async def list_campaigns():
    campaigns = []
    docs = db.collection(COLLECTION_NAME).stream()
    for doc in docs:
        data = doc.to_dict()
        campaigns.append(Campaign(**data))
    return campaigns

@app.get("/campaigns/{campaign_id}", response_model=Campaign)
async def get_campaign(campaign_id: str):
    doc_ref = db.collection(COLLECTION_NAME).document(campaign_id)
    doc = doc_ref.get()
    if not doc.exists:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return Campaign(**doc.to_dict())

@app.put("/campaigns/{campaign_id}", response_model=Campaign)
async def update_campaign(campaign_id: str, campaign: Campaign):
    doc_ref = db.collection(COLLECTION_NAME).document(campaign_id)
    doc = doc_ref.get()
    if not doc.exists:
        raise HTTPException(status_code=404, detail="Campaign not found")
    doc_ref.update(campaign.dict(exclude_unset=True))
    updated_doc = doc_ref.get()
    return Campaign(**updated_doc.to_dict())
