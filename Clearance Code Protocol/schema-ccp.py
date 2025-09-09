# SCHEMA ID: 0-4-20250909-Schumacher.Personal-SCCP
import random
import string

def random_letters(n):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(n))

def random_digits(n):
    return ''.join(random.choice(string.digits) for _ in range(n))

def random_alphanumeric(n):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))

def generate_clearance_code(level: int) -> str:
    """
    Generate a randomized clearance code based on SCHEMA Security Clearance Level (0–5).
    
    Level 0: Public – No code required
    Level 1: Tier 1 (LDD-LDD)
    Level 2: Tier 2 (LLDD-LLDD)
    Level 3: Tier 3 (LLLL-DDDD-LL)
    Level 4: Tier 4 (LLLL-DDDD-LLDD)
    Level 5: Tier 5 (LLLL-DDDD-LLDD-CHK)
    """
    if level == 0:
        return "PUBLIC"  # no code required
    
    elif level == 1:  # Tier 1
        return f"{random_letters(1)}{random_digits(2)}-{random_letters(1)}{random_digits(2)}"
    
    elif level == 2:  # Tier 2
        return f"{random_letters(2)}{random_digits(2)}-{random_letters(2)}{random_digits(2)}"
    
    elif level == 3:  # Tier 3
        return f"{random_letters(4)}-{random_digits(4)}-{random_letters(2)}"
    
    elif level == 4:  # Tier 4
        return f"{random_letters(4)}-{random_digits(4)}-{random_letters(2)}{random_digits(2)}"
    
    elif level == 5:  # Tier 5 (fixed -TOP suffix)
        base = f"{random_letters(4)}-{random_digits(4)}-{random_letters(2)}{random_digits(2)}"
        return f"{base}-TOP"
    
    else:
        raise ValueError("Level must be between 0 and 5")

for lvl in range(6):
    print(f"Level {lvl}: {generate_clearance_code(lvl)}")