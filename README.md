# name-drawing-application

An accessible name drawing program written in Python 3.8.6. This application is used for a secret Santa drawing that is done durring Christmas.

This application takes a list of dictionaries that represent each individual involved in the name drawing, and will randomly assign each person a name from amungst those individuals who are participating. The application insures that an individual will not draw themselves, and that everyone gets drawn. The output of this application is an email to each person involved in the drawing, so a GMail account that has Less secure app access enabled is required. A JSON file is used to easily change the participants in the drawing. You must include a name and email for each object in the array of participants.

## How to Run

The most important part is the JSON file, which has all of the information about the individuals participating in the name drawing. Since this application uses emails as output, names, email, and an optional attachment field must be provided for each person. The file by default is expected to be participants.json, although you can pass a filename as a commandline argument into the application.  
example:

```
[
{
"name": "name1",
"email": "name1@gmail.com"
},
{
"name": "name2",
"email": "name2@gmail.com"
},
{
"name": "name3",
"email": "name3@gmail.com"
},
{
"name": "name4",
"email": "name4@gmail.com"
}
]
```

You can indent your JSON, as long as your JSON is valid.

Note that this application is using GMail for sending the names, you need to enable less secure app access for the GMail account that is being used. The application does not save the username and password for your email account, so it will request you to enter your username and password every time.

After sending the emails with the names to each participant, the program will connect to IMAP, and clear your sent mail/Trash to insure you do not know who got sent which name.

## Tests

Tests were written to test the draw_names function in main.py. This is the algorithm that actually randomly assigns names for each participant insuring that no one will ever draw themselves.

The tests are ran several times using different input. 9 tests that are exicuted 10000 times each are performed to test 2 through 10 participants. A single participant throws an error and should not be possible. The test is looking for anomalies in the random behavior to insure that no case will result in someone not getting drawn, or draw themselves.

## How it Works

The main draw_names function takes a list of dictionaries for participants, and a list of names that are extracted from the participants list. So, the names list and participants list should be identical. This seperation was made so that the algorithm itself did not have to handle the extraction of all of the names from the participants dictionaries.

The participants are iterated over once to randomly choose a name from the names list, and assign it to the participant dictionary with a key of drawn_name. Several checks are performed to first determine if the participants name is in the names list, in which case it needs to be removed, then a randomly chosen index is generated from the range of 0 to the length of names -1. An edge case is handled where if there are only two remaining participants, and the next/last participant's name is in the list still, then the current participant must draw their name to avoid the last participant drawing themselves.
