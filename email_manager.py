"""
author: Timothy Breitenfeldt
version: Python 3.8.6
description: Provides utility functions for sending and managing emails from a GMail account.
"""

from smtplib import SMTP
from imaplib import IMAP4_SSL
from email.message import EmailMessage
from typing import Dict
class EmailManager:

    def __init__(self) -> None:
        self.smtp_server: SMTP = None
        self.imap_server: IMAP4_SSL = None

    def open_smtp_connection(self, server_information: Dict[str, str], credentials: Dict[str, str]) -> None:
        """
        Opens a connection to a SMTP mail server

        Parameters:
        server_information (Dict[str, str]): A dictionary used to configure the SMTP object. Must be in the format {'server': '', 'port': 0}
        credentials (Dict[str, str]): A dictionary that is used to authenticate to the SMTP server. Must be in the format {'username': '', 'password': ''}
        """
        self.smtp_server = SMTP(server_information["server"], server_information["port"])
        self.smtp_server.starttls()
        self.smtp_server.login(credentials["username"], credentials["password"])

    def open_imap_connection(self, server_information: Dict[str, str], credentials: Dict[str, str]) -> None:
        """
        Opens a connection to an Imap mail server

        Parameters:
        server_information (Dict[str, str]): A dictionary used to configure the IMAP4_SSL object. Must be in the format {'server': '', 'port': 0}
        credentials (Dict[str, str]): A dictionary that is used to authenticate to the IMAP4_SSL server. Must be in the format {'username': '', 'password': ''}
        """
        self.imap_server = IMAP4_SSL(server_information["server"])
        self.imap_server.login(credentials["username"], credentials["password"])
    
    def send_email(self, sending_address: str, to: str, subject: str, body: str) -> None:
        if self.smtp_server is None:
            raise ValueError("You must open the SMTP connection first by calling \"open_smtp_connection\"")

        email: EmailMessage = EmailMessage()
        email.set_content(body)
        email["Subject"] = subject
        email["From"] = sending_address
        email["To"] = to
        self.smtp_server.send_message(email)
    
    def delete_all_emails(self, folder: str) -> None:
        if self.imap_server is None:
            raise ValueError("You must connect to the IMap server first by calling \"open_imap_connection\"")

        self.imap_server.select(f"[Gmail]/{folder}")
        self.imap_server.store("1:*", "+FLAGS", "\\Deleted")
        self.imap_server.expunge()
    
    def close_smtp_connection(self) -> None:
        if self.smtp_server is None:
            raise ValueError("You must open the SMTP connection first by calling \"open_smtp_connection\"")

        self.smtp_server.quit()

    def close_imap_connection(self) -> None:
        if self.imap_server is None:
            raise ValueError("You must connect to the IMap server first by calling \"open_imap_connection\"")

        self.imap_server.close()
        self.imap_server.logout()
