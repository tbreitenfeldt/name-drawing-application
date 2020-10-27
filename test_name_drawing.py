"""
author: Timothy Breitenfeldt
version: Python 3.8.6
description: Tests the draw_names method for validation, insuring that no participant draws them-self, and that every person gets drawn.
"""

import sys

import main
from typing import Dict, List

def run_tests() -> None:
    test_participants2: List[Dict[str, str]] = [
        {"name": "test1", "email": "test1@gmail.com"},
        {"name": "test2", "email": "test2@gmail.com"}
    ]
    test_names2: List[str] = ["test1", "test2"]
    test_draw_names(test_participants2, test_names2, exicution_times=10000)
    print(f"Tests successful for {len(test_participants2)} participants")

    test_participants3: List[Dict[str, str]] = [
        {"name": "test1", "email": "test1@gmail.com"},
        {"name": "test2", "email": "test2@gmail.com"},
        {"name": "test3", "email": "test3@gmail.com"}
    ]
    test_names3: List[str] = ["test1", "test2", "test3"]
    test_draw_names(test_participants3, test_names3, exicution_times=10000)
    print(f"Tests successful for {len(test_participants3)} participants")

    test_participants4: List[Dict[str, str]] = [
        {"name": "test1", "email": "test1@gmail.com"},
        {"name": "test2", "email": "test2@gmail.com"},
        {"name": "test3", "email": "test3@gmail.com"},
        {"name": "test4", "email": "test4@gmail.com"}
    ]
    test_names4: List[str] = ["test1", "test2", "test3", "test4"]
    test_draw_names(test_participants4, test_names4, exicution_times=10000)
    print(f"Tests successful for {len(test_participants4)} participants")

    test_participants5: List[Dict[str, str]] = [
        {"name": "test1", "email": "test1@gmail.com"},
        {"name": "test2", "email": "test2@gmail.com"},
        {"name": "test3", "email": "test3@gmail.com"},
        {"name": "test4", "email": "test4@gmail.com"},
        {"name": "test5", "email": "test5@gmail.com"}
    ]
    test_names5: List[str] = ["test1", "test2", "test3", "test4", "test5"]
    test_draw_names(test_participants5, test_names5, exicution_times=10000)
    print(f"Tests successful for {len(test_participants5)} participants")

    test_participants6: List[Dict[str, str]] = [
        {"name": "test1", "email": "test1@gmail.com"},
        {"name": "test2", "email": "test2@gmail.com"},
        {"name": "test3", "email": "test3@gmail.com"},
        {"name": "test4", "email": "test4@gmail.com"},
        {"name": "test5", "email": "test5@gmail.com"},
        {"name": "test6", "email": "test6@gmail.com"}
    ]
    test_names6: List[str] = ["test1", "test2", "test3", "test4", "test5", "test6"]
    test_draw_names(test_participants6, test_names6, exicution_times=10000)
    print(f"Tests successful for {len(test_participants6)} participants")

    test_participants7: List[Dict[str, str]] = [
        {"name": "test1", "email": "test1@gmail.com"},
        {"name": "test2", "email": "test2@gmail.com"},
        {"name": "test3", "email": "test3@gmail.com"},
        {"name": "test4", "email": "test4@gmail.com"},
        {"name": "test5", "email": "test5@gmail.com"},
        {"name": "test6", "email": "test6@gmail.com"},
        {"name": "test7", "email": "test7@gmail.com"}
    ]
    test_names7: List[str] = ["test1", "test2", "test3", "test4", "test5", "test6", "test7"]
    test_draw_names(test_participants7, test_names7, exicution_times=10000)
    print(f"Tests successful for {len(test_participants7)} participants")

    test_participants8: List[Dict[str, str]] = [
        {"name": "test1", "email": "test1@gmail.com"},
        {"name": "test2", "email": "test2@gmail.com"},
        {"name": "test3", "email": "test3@gmail.com"},
        {"name": "test4", "email": "test4@gmail.com"},
        {"name": "test5", "email": "test5@gmail.com"},
        {"name": "test6", "email": "test6@gmail.com"},
        {"name": "test7", "email": "test7@gmail.com"},
        {"name": "test8", "email": "test8@gmail.com"}
    ]
    test_names8: List[str] = ["test1", "test2", "test3", "test4", "test5", "test6", "test7", "test8"]
    test_draw_names(test_participants8, test_names8, exicution_times=10000)
    print(f"Tests successful for {len(test_participants8)} participants")

    test_participants9: List[Dict[str, str]] = [
        {"name": "test1", "email": "test1@gmail.com"},
        {"name": "test2", "email": "test2@gmail.com"},
        {"name": "test3", "email": "test3@gmail.com"},
        {"name": "test4", "email": "test4@gmail.com"},
        {"name": "test5", "email": "test5@gmail.com"},
        {"name": "test6", "email": "test6@gmail.com"},
        {"name": "test7", "email": "test7@gmail.com"},
        {"name": "test8", "email": "test8@gmail.com"},
        {"name": "test9", "email": "test9@gmail.com"}
    ]
    test_names9: List[str] = ["test1", "test2", "test3", "test4", "test5", "test6", "test7", "test8", "test9"]
    test_draw_names(test_participants9, test_names9, exicution_times=10000)
    print(f"Tests successful for {len(test_participants9)} participants")

    test_participants10: List[Dict[str, str]] = [
        {"name": "test1", "email": "test1@gmail.com"},
        {"name": "test2", "email": "test2@gmail.com"},
        {"name": "test3", "email": "test3@gmail.com"},
        {"name": "test4", "email": "test4@gmail.com"},
        {"name": "test5", "email": "test5@gmail.com"},
        {"name": "test6", "email": "test6@gmail.com"},
        {"name": "test7", "email": "test7@gmail.com"},
        {"name": "test8", "email": "test8@gmail.com"},
        {"name": "test9", "email": "test9@gmail.com"},
        {"name": "test10", "email": "test10@gmail.com"}
    ]
    test_names10: List[str] = ["test1", "test2", "test3", "test4", "test5", "test6", "test7", "test8", "test9", "test10"]
    test_draw_names(test_participants10, test_names10, exicution_times=10000)
    print(f"Tests successful for {len(test_participants10)} participants")

def test_draw_names(participants: List[Dict[str, str]], names: List[str], exicution_times: int = 1000) -> None:
    comparison_list: List[str] = names[:]  # clone names

    try:
        for i in range(exicution_times):
            test_participants: List[Dict[str, str]] = participants[:]
            test_names: List[str, str] = names[:]
            main.draw_names(test_participants, test_names)
            count: int = 0

            for participant in participants:
                if participant["name"] == participant["drawn_name"]:
                    raise ValueError(f"participant: {participant['name']} drew there own name.")
                if participant["drawn_name"] in comparison_list:
                    count += 1

            if count != len(comparison_list):
                raise ValueError(f"Not all names got drawn, there are supposed to be {len(comparison_list)}, but only {count} names were drawn.\nExpecting: {comparison_list}")
    except Exception as e:
        print(e)
        print(f"exicution time: {i}")
        print(f"Participants:\n{participants}")
        print(f"Names:\n{names}")
        sys.exit()

run_tests()