
from dotenv import load_dotenv
import os


# folders
OUTPUT_FOLDER = "output/"
INPUT_FOLDER = "data/"
CHART_FOLDER = "output/charts/"

# parametros de reportes
DEFAULT_REPORT_NAME = "Reporte_{date}.pdf"
DEFAULT_GROUP_COLUMN = "region"
DEFAULT_AGGREGATE_COLUMN = "sales"


#para notificaciones de correo
load_dotenv()

USERNAME = os.getenv("EMAIL_USERNAME")
PASSWORD = os.getenv("EMAIL_PASSWORD")
IMAP_SERVER = os.getenv("IMAP_SERVER")
SMTP_SERVER = os.getenv("SMTP_SERVER")
PORT_SMTP = os.getenv("PORT_SMTP")
NOTIFY_EMAIL = os.getenv("NOTIFY_EMAIL")
