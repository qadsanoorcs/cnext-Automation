# utils/config.py

BASE_URL = "https://alpha.cnext.revdev.it/"

# Credentials: keep local, DO NOT commit to public repos
CREDENTIALS = {
    "super_admin": {
        "email": "admin@cnext.com",
        "password": "Secure@CNext88$"
    },
    "sara": {
        "email": "sara.abbonizio@revelopsrl.com",
        "password": "3~65Is~4TJe"
    }
}

# Checkbox label texts to try clicking (Italian labels you mentioned)
CHECKBOX_LABELS = [
    "Accetto i Termini e le Condizioni",
    "Accetto i Termini",   # alternative shorter text
    "Ricordami"
]

# Generic waits
DEFAULT_TIMEOUT = 12
