import hashlib
import requests

def check_breach(password):
    sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix = sha1_password[:5]
    suffix = sha1_password[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code != 200:
        return "Error checking breach"

    hashes = response.text.splitlines()

    for line in hashes:
        h, count = line.split(":")
        if h == suffix:
            return f"⚠️ Breached! Found {count} times"

    return "✅ Safe (Not found in breaches)"