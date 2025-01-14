import re
import pandas as pd
from fetch_data import fetch_data


def validate_email(email):
    """Valida el formato de un correo electrónico."""
    if not isinstance(email, str):
        return False
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))

def validate_phone(phone):
    """Valida el formato de un número de teléfono (10 dígitos)."""
    if not isinstance(phone, str):
        return False
    return phone.isdigit() and len(phone) == 10

def process_data(data):
    """
    Limpia y valida datos de entrada.
    """
    df = pd.DataFrame(data)

    # Validar columnas
    df["email_is_valid"] = df["email"].apply(validate_email)
    df["phone_is_valid"] = df["phone"].apply(validate_phone)

    # Eliminar registros inválidos
    valid_data = df[df["email_is_valid"] & df["phone_is_valid"]]

    return valid_data

if __name__ == "__main__":
    # Datos simulados
    sample_data = [
        {"name": "John Doe", "email": "john@example.com", "phone": "1234567890"},
        {"name": "Invalid User", "email": "invalid@", "phone": "abc123"}
    ]

    processed_data = process_data(sample_data)
    print("Datos procesados:")
    print(processed_data)
