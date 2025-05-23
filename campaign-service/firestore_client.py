import firebase_admin
from firebase_admin import credentials, firestore
import json

# Paste your service account JSON as a Python dict (or load it from a JSON string)
service_account_info = {
    "type": "service_account",
    "project_id": "devops-project-460606",
    "private_key_id": "e013b1fe2465c10d5334c0efc982c98119ce7d95",
    "private_key": """-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCrxMsi62NX83rJ
SPTt6RqyGr5NexvUoqiMqpVqFR76rO3VWcFNj7n/7Q5vkJZS4WEt6FOgmC7IT+KT
NWewSklwJYenZFfPMdOgKLd+1NDLn45e9UNiNNkCvacsFB6MdFbBV7GP69lE00JS
Np0ySK0JqE8Vx6321Q3DMMjUt3k2TbbJMDn1Co/LiC/rIms0JGJWaR+x9RJZCJ/b
gNeJ28a6PaAJSA2PYQB5cr3Ar0/gSbzOgxesjYROnc+fs6pye1FLRTg8+ImqJwcC
v0iT44hm6tVQO3zQe0FWre/tJvtj6Y/py/lJQ1Ofd1fJ/+BC33FRV0fGNcosSM98
38z6G/M9AgMBAAECggEADDBOQ9+VMJgH9gGV084PRWUtbN0YB/o04Kp4KMtv49Ti
mZmhZGoXBkihlhwZ9q6kkTfju0khRLiaeNy4y2MyG+Gl4yR1MLA19q78+mSKnnBn
j2hzDCR4479mffO9iTT2NQkOggp34/Djy2axt/A9Syqk1gRR3WqX6+ppzeJpGQfD
8y5Fwmsw/7D7D7yxNguEDa+/ViGUTt1Nmil3gc18GjctmNgjnf2wGsqct638v59V
fGJh3491/lOLGumhiI/BjEfH3qEa0eGUEUSfiBqjM1L49iNWfzFr8f6cmLs6nTay
zOd/y5dA7VnOikVGxzGuQVIG0tkOTYVQo0GcqRRppwKBgQDX/V5roE3oDPNLeDLh
jCyBvaNMbXAIH2gbmsLyuiRTDHKCDOIyB8Z4IgLLoplZFHUvgW6tB8sfjEB5Rctp
sS79uOEB4jVefQrM2bKXbGu0eCoRBIfvmXLV6tz8Yj2XQCL5iz3FWS8iVwiE8cx5
5OntJ7bWSU4mtlkkCOyy6KaeuwKBgQDLlmIlDGEWc77FFlTNE6Ed04wbOMyT9TlU
zbcrLNumq3A+U0ckmTrMkxHXSwxx2YFQS8sbL2gOnv6MdzUMM4i1OYaxCJrZUiKy
uTymUyOkl/XmVjLz0owrRHs8oJUmIaqtZrat+VMASNxDxVtjsuZvmigSwen4Qfbt
ZXVSdEPiZwKBgQCcTSxA8laucIC3wpn/gnLKyLMdoayLFD9AirQ89ttGhiFvX2dp
ERtc4C/psRcL0bQj1qSC7rrdb59Qo2NabvA0h8+8jzhT0mU4bOnCjqE6jiLTAdZl
W0Qw7a9RrL4pcC5fK5Zd8/YaAaWWn2x7YV6vUigL1iyJ8zd6zkKMDbRV9QKBgEbt
LWQa2/gmet/O19xaalcpzDXvo9YoKMESqi2wgxWdxIzyFmb5uzJqSlznGH7Rd+ux
fCEMcwQlACmPnjuR+J6qW/JxPQFZTB1Xy3lmnZRKHLESds3bHFo2kXiduVh/gibH
Ef2qTvBaceJqb1xch0t6OVvPkuOal5w9LJJ9TukhAoGBAKkglC+tefbdiLMftVa6
u8Lbx6h8pDPFFts4VBT6Z3/+eMeHPKnU9bD6pZSi1IBUVh6Ov6CCvMFLV0Yyo9bC
DYWEDTkOdGDU99Pbi4GX6cCVPAlGQ4nBJM0f0f8H+pquQFIHGYHhByO/jlBUwlRr
duNZ9WMbxycf9oM+Uygv6E9Y
-----END PRIVATE KEY-----\n""",
    "client_email": "devops-email-campaign-sa@devops-project-460606.iam.gserviceaccount.com",
    "client_id": "113547365645327649472",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/devops-email-campaign-sa%40devops-project-460606.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}

# Initialize Firebase Admin with this dict
cred = credentials.Certificate(service_account_info)
firebase_admin.initialize_app(cred)

db = firestore.client()
