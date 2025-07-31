from fastapi import FastAPI, HTTPException
from xgb_model import calculate_probs_for_match, calculate_probs_for_ids
from cryptography.fernet import Fernet

app = FastAPI()

key = Fernet.generate_key()
fernet = Fernet(key)


@app.get("/match-probabilities/{match_id}")
def calculate_chances(encrypted_match_id: str):
    try:
        match_id = int(fernet.decrypt(encrypted_match_id).decode())
        return calculate_probs_for_match(match_id)
    except Exception:
        raise HTTPException(500, detail="An error occurred.")
    
@app.get("/match-probabilities-by-id")
def calculate_chances_for_ids(encrypted_male_id: str, encrypted_female_id: str ):
    try:
        male_id = int(fernet.decrypt(encrypted_male_id).decode())
        female_id = int(fernet.decrypt(encrypted_female_id).decode())
        return calculate_probs_for_ids(male_id, female_id)
    except Exception:
        raise HTTPException(500, detail="An error occurred.")

@app.post("/encrypt/{id}")
def encrypt_id(id: int):
    id_string = str(id)
    return fernet.encrypt(id_string.encode())
