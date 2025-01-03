from project_config import settings
from dotenv import load_dotenv
import os
from utils import email_handler
from utils.email_handler import connect_imap, read_emails



def main():
    connection = connect_imap()
    if connection:
        read_emails(connection)
        connection.logout()


if __name__ == "__main__":
    main()
