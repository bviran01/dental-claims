# bank_verification.py

def get_bank_transaction(eft_reference: str) -> dict:
    """
    Simulate retrieving bank transaction details using the EFT reference number.
    In a production system, this function would call a bank API (such as Plaid)
    to retrieve transaction details.
    """
    # Simulated bank transaction response (placeholder data)
    simulated_transaction = {
        "eft_reference": eft_reference,
        "transaction_date": "2024-01-20",
        "amount": 210.00,
        "status": "completed",
        "bank_name": "Generic Bank",
        "confirmation_number": "CONF123456"
    }
    return simulated_transaction
