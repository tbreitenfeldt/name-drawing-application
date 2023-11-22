"""
author: Timothy Breitenfeldt
version: Python 3.11.4
description: Draws names based on a JSON file, and sends an email to the respective individual.
"""

import random
import getpass
import os
import sys
from typing import Dict, List
import imaplib

import yagmail

import json_utils


def main(args: List[str]) -> None:
    filename: str = "config.json"

    if len(args) == 2:
        filename = args[1]

    print("Name Drawing")

    config: Dict[str, any] = read_json_config(filename)
    participants: List[Dict[str, str]] = config["participants"]
    names: List[str] = extract_names(participants)
    sending_email_credentials: Dict[str, str] = config["gmail_credentials"]

    print("Drawing names...")
    draw_names(participants, names)
    print("Sending emails with names...")
    send_emails_with_names(sending_email_credentials, participants)
    permanently_remove_sent_mail(sending_email_credentials)


def read_json_config(filename) -> Dict:
    try:
        return json_utils.read_json(filename)
    except FileNotFoundError:
        print(f"Unable to find  the file \"{filename}\"")
        print("The file should be in the format:")
        print(
            "{\n\"gmail_credentials\": {\n\"username\": \"\",\,\"password\": \"\"\n},\n\"participants\": [\n{\n\"name\": \"example name\",\n\"email\": \"example@domain.com\"\n}\n]\n}")
        sys.exit()


def extract_names(participants: List[Dict[str, str]]) -> List[str]:
    return [participant["name"] for participant in participants]


def draw_names(participants: List[Dict[str, str]], names: List[str]) -> List[Dict[str, str]]:
    if len(participants) != len(names):
        raise ValueError(
            f"the participants and names arrays must be equal, participants have {str(len(participants))} and names has {str(len(names))}")
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


def send_emails_with_names(credentials: Dict[str, str], participants: List[Dict[str, str]]) -> None:
    with yagmail.SMTP(credentials["username"], credentials["password"]) as yag:
        for participant in participants:
            print(
                f"Sending email to {participant['name']} at {participant['email']}...")
            sending_address: str = credentials["username"]
            to: str = participant["email"]
            body: str = f"Hi {participant['name']},\nYou drew {participant['drawn_name']}\n\nThis is an automated message, do not respond."
            subject: str = "Name Drawing"
            yag.send(to, subject, body)


def permanently_remove_sent_mail(credentials: Dict[str, str]):
    connection = imaplib.IMAP4_SSL('imap.gmail.com')
    connection.login(credentials["username"], credentials["password"])
    # delete sent mail
    connection.select(mailbox='"[Gmail]/Sent Mail"')
    connection.store("1:*", '+FLAGS', '\\Deleted')
    connection.expunge()
    # delete trash
    connection.select(mailbox='"[Gmail]/Trash"', readonly=False)
    connection.store("1:*", '+FLAGS', '\\Deleted')
    connection.expunge()
    connection.close()
    connection.logout()


if __name__ == "__main__":
    main(sys.argv)
