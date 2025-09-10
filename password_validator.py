import re

def is_valid_password(password: str) -> bool:
    """
    Smart-but-friendly password validation function.
    Returns True if the password meets the rules like length, uppercase, lowercase, digit, and special characters,otherwise False.
    """

    # Rule 1: Length check it should lie between 8 and 15.
    if not (8 < len(password) < 15):
        return False

    # Rule 2: Count character categories
    categories = 0
    if any(ch.islower() for ch in password): categories += 1
    if any(ch.isupper() for ch in password): categories += 1
    if any(ch.isdigit() for ch in password): categories += 1
    if any(ch in "@#$%_!" for ch in password): categories += 1
    if categories < 2:  
        return False

    # Rule 3: No spaces
    if " " in password:
        return False

    # Rule 4: Reject common bad patterns
    bad_patterns = ["password", "qwerty", "123456", "abcdef", "letmein", "welcome"]
    lower_pwd = password.lower()
    if any(bp in lower_pwd for bp in bad_patterns):
        return False

    # Rule 5: Reject repeated single characters (8+ times)
    if re.fullmatch(r"(.)\1{7,}", password):
        return False

    # Rule 6: Reject obvious sequences
    sequences = ["abcdefghijklmnopqrstuvwxyz", "1234567890"]
    for seq in sequences:
        if password.lower() in seq or password in seq:
            return False

    # Rule 7: Avoid too many special chars in a row (unfriendly)
    if re.search(r"[@#$%!_]{4,}", password):
        return False
    # If all the above rules are satisfied, password is valid. 
    return True


"""
✅ 10 Accepted Passwords (according to my logic):
1. Travel2025!
2. My_Home99
3. Hackathon@25
4. CoffeeLover1
5. Secure#Life8
6. Happy_Day2024
7. Good#Team7
8. Study@Night9
9. RoadTrip_55
10. StrongPass!2

❌ 10 Rejected Passwords (according to my logic):
1. password123
2. qwerty2025
3. 12345678
4. abcdefgh
5. !!!!!!!!
6. AAAAAAAA
7. weakpass
8. Spaces not1!
9. Too$$$$$Much
10. letmein2024
"""

# Demo test run (no _name_ guard, works everywhere)
test_passwords = [
    "Travel2025!", "password123", "Hackathon@25", "!!!!!!!!!", "Good#Team7"
]
for pwd in test_passwords:
    print(f"{pwd:15} -> {is_valid_password(pwd)}")