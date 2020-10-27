"""
author: Timothy Breitenfeldt
version: python 3.8.6
description: Provides utilities for reading and writing JSON files.
"""

import json
from typing import Dict

def read_json(filename: str) -> Dict:
    data: Dict[str, str] = {}

    with open(filename) as file:
        data = json.load(file)

    return data

def write_json(filename: str, data: Dict) -> None:
    with open(filename, "w") as file:
        json.dump(data, file, indent=2)
