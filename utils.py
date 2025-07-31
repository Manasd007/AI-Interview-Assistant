import re
import json
import os
import uuid
from datetime import datetime

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    digits_only = re.sub(r'\D', '', phone)
    return len(digits_only) >= 10

def validate_experience_years(years):
    try:
        years_int = int(years)
        return 0 <= years_int <= 50
    except ValueError:
        return False

def sanitize_input(text):
    if not text:
        return ""
    dangerous_chars = ['<', '>', '"', "'", '&']
    for char in dangerous_chars:
        text = text.replace(char, '')
    return text.strip()

def format_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def calculate_score(responses):
    if not responses:
        return 0
    
    total_score = sum(response.get('score', 0) for response in responses)
    return round(total_score / len(responses), 2)

def generate_session_id():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    import random
    random_suffix = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))
    return f"session_{timestamp}_{random_suffix}"

def generate_anonymous_session_id():
    return f"user_{uuid.uuid4().hex[:8]}"

DATA_FILE = "data/candidates.json"

def save_candidate_data(session_id, candidate_data):
    if not os.path.exists("data"):
        os.makedirs("data")

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    else:
        data = {}

    data[session_id] = candidate_data

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def load_candidate_data(session_id):
    if not os.path.exists(DATA_FILE):
        return None
    
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        return data.get(session_id)
    except Exception:
        return None

def anonymize_candidate_info(candidate_info):
    if not candidate_info:
        return {}
    
    anonymized = {
        "experience_years": candidate_info.get("experience", 0),
        "position": candidate_info.get("position", ""),
        "location": candidate_info.get("location", ""),
        "email_hash": hash(candidate_info.get("email", "")) if candidate_info.get("email") else None,
    }
    
    return anonymized 