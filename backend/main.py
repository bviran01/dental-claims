from fastapi import FastAPI
from dentalxchange import get_era

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

