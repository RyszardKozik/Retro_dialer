import random

def generate_number():
    # Example: US/Canasda format
    prefix = "+1"
    area_code = random.choice(["202", "305", "416", "613", "647", "212", "408"])
    middle = str(random.randint(100, 999))
    last = str(random.randint(1000, 9999))
    return f"{prefix}{area_code}{middle}{last}"