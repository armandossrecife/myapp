import bcrypt
import string
import os

SECRET_KEY = "your_secret_key"  # Replace with a strong secret key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

API_PORT = "8000"
API_URL = f"http://localhost:{API_PORT}"
CURRENT_PATH = os.getcwd()
IMAGES_PATH = os.path.join(CURRENT_PATH, 'images')
IMAGES_PATH_PROFILE = os.path.join(IMAGES_PATH, 'profile')
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png"}  # Add more extensions as needed

def hash_password(password: str) -> str:
    # Recommended work factor based on current hardware speeds
    work_factor = 14  # Adjust as needed, higher is more secure but slower
    salt = bcrypt.gensalt(work_factor)
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)

    # Use base64 encoding for safe storage and transmission
    return hashed_password.decode("utf-8")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    hashed_password = hashed_password.encode("utf-8")
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password)
    
def validate_filename(filename: str) -> str:
    """Sanitizes filename to prevent potential vulnerabilities.
    Args:
        filename (str): The filename to sanitize.
    Returns:
        str: The sanitized filename.
    """
    allowed_chars = set(string.ascii_letters + string.digits + "-_.")
    sanitized_filename = "".join([char for char in filename if char in allowed_chars])
    return sanitized_filename