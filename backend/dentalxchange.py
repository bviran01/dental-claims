# dentalxchange.py

def get_era(claim_id: str) -> dict:
    """
    Simulate retrieving an ERA from DentalXchange for the given claim_id.
    In a production system, this function would make an HTTP request to the DentalXchange API.
    """
    # Simulated ERA response with candidate data fields
    simulated_era = {
        "claim_id": claim_id,
        "patient_name": "John Doe",
        "date_of_service": "2024-01-15",
        "date_paid": "2024-01-20",
        "eft_reference_number": "EFT123456",
        "ada_codes": ["D1110", "D2740"],
        "claim_amount": 250.00,
        "contracted_amount": 220.00,
        "allowed_amount": 210.00,
        "amount_paid": 210.00,
        "patient_responsibility": 40.00,
        "payment_method": "direct_deposit",
        "insurance_carrier": "Generic Insurance Co."
    }
    return simulated_era
