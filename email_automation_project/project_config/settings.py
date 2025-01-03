from dotenv import load_dotenv
import os

load_dotenv()


USERNAME = os.getenv("EMAIL_USERNAME")
PASSWORD = os.getenv("EMAIL_PASSWORD")
IMAP_SERVER = os.getenv("IMAP_SERVER")
SMTP_SERVER = os.getenv("SMTP_SERVER")
PORT_SMTP = os.getenv("PORT_SMTP")

