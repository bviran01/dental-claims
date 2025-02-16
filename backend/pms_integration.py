# pms_integration.py

def fetch_open_claims():
    """
    Simulate fetching open claims from a local PMS.
    In the final product, this function would interact with the PMS through local methods,
    such as reading exported files, desktop automation, or direct database queries.
    """
    return [
        {"claim_id": "CLAIM123", "patient_name": "John Doe", "status": "open"},
        {"claim_id": "CLAIM124", "patient_name": "Jane Smith", "status": "open"}
    ]

def post_payment(claim_id: str, payment_data: dict) -> bool:
    """
    Simulate posting payment data to a local PMS to close a claim.
    In a real scenario, this function would update the PMS with the verified payment data.
    Returns True if the operation is successful.
    """
    # For simulation, we print the action and return True.
    print(f"Simulated posting payment for claim {claim_id} with data: {payment_data}")
    return True
