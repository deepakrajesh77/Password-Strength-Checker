import re
import math

def calculate_entropy(password):
    charset = 0
    if re.search(r"[a-z]", password): charset += 26
    if re.search(r"[A-Z]", password): charset += 26
    if re.search(r"[0-9]", password): charset += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): charset += 32

    if charset == 0:
        return 0

    entropy = len(password) * math.log2(charset)
    return entropy

def check_password_strength(password):
    score = 0

    if len(password) >= 8: score += 1
    if len(password) >= 12: score += 1
    if re.search(r"[A-Z]", password): score += 1
    if re.search(r"[a-z]", password): score += 1
    if re.search(r"[0-9]", password): score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): score += 1

    entropy = calculate_entropy(password)

    if entropy < 40 or score <= 2:
        return "Weak"
    elif entropy < 60 or score <= 4:
        return "Medium"
    else:
        return "Strong"