import re
import pandas as pd

def validate_email(email):
    """Valida el formato de un correo electrónico."""
    if not isinstance(email, str):  # Verifica que sea una cadena
        return False
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))

def validate_date_format(date):
    """Valida si una fecha tiene un formato correcto."""
    try:
        pd.to_datetime(date, format="%Y-%m-%d")
        return True
    except ValueError:
        return False
