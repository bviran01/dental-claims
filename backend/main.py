from fastapi import FastAPI
from dentalxchange import get_era
from bank_verification import get_bank_transaction
from pms_integration import fetch_open_claims, post_payment

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Dental AI!"}

@app.get("/era/{claim_id}")
def fetch_era(claim_id: str):
    """
    Endpoint to simulate fetching ERA data for a given claim_id.
    """
    era_data = get_era(claim_id)
    return era_data

@app.get("/bank/{eft_reference}")
def fetch_bank_transaction(eft_reference: str):
    """
    Endpoint to simulate retrieving bank transaction details for a given EFT reference.
    """
    transaction_data = get_bank_transaction(eft_reference)
    return transaction_data

@app.get("/pms/claims")
def get_open_claims():
    """
    Endpoint to simulate fetching open claims from a local PMS.
    """
    return fetch_open_claims()

@app.post("/pms/payment/{claim_id}")
def submit_payment(claim_id: str, payment_data: dict):
    """
    Endpoint to simulate posting payment data to the local PMS to close a claim.
    Expects a JSON payload for payment_data.
    """
    success = post_payment(claim_id, payment_data)
    return {"success": success, "claim_id": claim_id}
