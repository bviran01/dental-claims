from fastapi import FastAPI
from dentalxchange import get_era
from bank_verification import get_bank_transaction

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
