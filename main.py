"""
author: Timothy Breitenfeldt
version: Python 3.8.6
description: Draws names based on a JSON file, and sends an email to the respective individual.
"""

import random 
import getpass
import os
import sys
from typing import Dict, List

import json_utils
from email_manager import EmailManager

def main(args: List[str]) -> None:
    filename: str = "participants.json"

    if len(args) == 2:
        filename = args[1]

    print("Name Drawing")

    participants: List[Dict[str, str]] = get_participants(filename)
    names: List[str] = extract_names(participants)
    sending_email_credentials: Dict[str, str] = read_sending_email_credentials()

    print("Drawing names...")
    draw_names(participants, names)
    print("Sending emails with names...")
    send_emails_with_names(sending_email_credentials, participants)

def get_participants(filename) -> List:
    try:
        return json_utils.read_json(filename)
    except FileNotFoundError:
        print(f"Unable to find  the file \"{filename}\"")
        print("The file should be in the format:")
        print("[\n{\n\"name\": \"example name\",\n\"email\": \"example@domain.com\"\n}\n]")
        sys.exit()

def extract_names(participants: List[Dict[str, str]]) -> List[str]:
    return [participant["name"] for participant in participants]

def draw_names(participants: List[Dict[str, str]], names: List[str]) -> List[Dict[str, str]]:
    if len(participants) != len(names):
        raise ValueError(f"the participants and names arrays must be equal, participants have {str(len(participants))} and names has {str(len(names))}")
    if len(participants) == 1:
        raise ValueError("Need at least two participants to draw.")

    for i in range(len(participants)):
        participant: Dict[str, str] = participants[i]
        name_index: int = 0
        nameWasRemoved: bool = False

        if participant["name"] in names:
            names.remove(participant["name"])
            nameWasRemoved = True
            name_index = random.randint(0, len(names)-1)
        elif i == len(participants) - 2 and participants[i+1]["name"] in names:
            # select the index of the name from amungst the last two names that is equal to the next participant to insure the last participant who draws does not draw themselves.
            name_index = 1 if participants[i+1]["name"] == names[1] else 0
        else:
            name_index = random.randint(0, len(names)-1)

        participant["drawn_name"] = names[name_index]
        del names[name_index]

        if nameWasRemoved:
            names.append(participant["name"])

    return participants

def read_sending_email_credentials() -> Dict[str, str]:
    username: str = input("Enter Sending email account username: ")
    password: str = getpass.getpass("Enter Password: ")
    return {"username": username, "password": password}

def send_emails_with_names(credentials: Dict[str, str], participants: List[Dict[str, str]]) -> None:
    email_manager: EmailManager = EmailManager()
    smtp_server_information: Dict = {"server": "smtp.gmail.com", "port": 587}
    imap_server_information: Dict[str, str] = {"server": "imap.gmail.com"}
    email_manager.open_smtp_connection(smtp_server_information, credentials)
    email_manager.open_imap_connection(imap_server_information, credentials)

    for participant in participants:
        print(f"Sending email to {participant['name']} at {participant['email']}...")
        sending_address: str = credentials["username"]
        to: str = participant["email"]
        body: str = f"Hi {participant['name']},\nYou drew {participant['drawn_name']}\n\nThis is an automated message, do not respond."
        subject: str = "Name Drawing"
        email_manager.send_email(sending_address, to, subject, body)

    email_manager.delete_all_emails("Trash")
    email_manager.close_smtp_connection()
    email_manager.close_imap_connection()

if __name__ == "__main__":
    main(sys.argv)