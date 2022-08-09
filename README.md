# Bini_Bambini_TEST_TASK
Test task for the Trainee Data Engineer

Write a test project using:

- Python3.8+, requests, argparse, psycopg2 etc.
- REST API rickandmortyapi.com
- REST API sv443.net/jokeapi/v2

# Test must be able to do the next instruction:

1 Let's SQUANCH!

You need to write a squanch.py script:

- Creates a "squanch" folder at launch, if you don't have one.
- Inside the folder creates a text file "<file creation date>_squanch.txt" with the text line "let's <randomly generated word from the letters of 'squanch'>"


2 Rick and Morty Stand-Up Show

You need to write ram_standup.py script:

- When you run the script randomly selects any character from the Rick and Morty cartoon series (using rickandmortyapi API) and makes him host of the evening, and 7 characters who will be the participants of the evening as comedians.
- The host on his own behalf ("<hostname>: - <text>") outputs the welcome text into the console and announces tonight's 7 comedians.
- The console then waits for the typing of the enter key to start the show.
- After the signal from the user, the host announces the first contestant and invites him to the stage; a waiting time of 2 seconds and the comedian tells a random joke, taken from a jokeapi (if the joke has two parts, you must print second part  in the same way after 2 seconds). 
- Then the script waits again for the enter key to continue the show and it continues until all the comedians have told their material.
- After the last comedian has performed, the host thanks all the comedians and asks the audience to vote for the best comedian.
- After a pause of 3 seconds, the host announces the best comedian (randomly chosen from the list of performers) and says goodbye to the audience.
- After typing enter the window closes.


3 This is The Base

Required:

- Connect to the database using psycopg2 library
- Create tables of characters, locations, episodes from the Rick and Morty world.
- Write the ram_parse.py script, which collects the information from the API Writes it into the database.

Important, the data must not be duplicated, at each run the data must be updated and actualized in to the database.


4 Percent Moments...

You need to write the ram_top.py script with the parameters -value (int: 1 - 100) and -type (str: characters / episodes):

- If the -type argument is "characters", the script should output the names of characters that have appeared in more than value% of all episodes of the cartoon series, and the number of episodes in which they have appeared in descending order (no more than 10).
- If the -type argument is "episodes" - the script should output the names of episodes in which the character appeared with ID value sorted by series names (no more than 10).

Important, the data must be taken from the database, filled in task 3.

5 And Last but not Least

Needed:

- Create a private git repository.
- Put the results of the work into it.
- Provide access to the mail that will go with the task.

It is important that the repository should not contain data for connecting to the database.
It is necessary to specify in the README file, the option of correct launching, if needed.
In case of errors with this task, the files can be dropped in an archive.


# Copying the repository and installing dependencies:
```
git clone https://github.com/MrIvanDii/ASFERO_test_mail_sending
cd ASFERO_test_mail_sending/ASFERO
python -m venv bini_env
bini_env\Scripts\activate (для OS Windows)
source rest_env/bin/activate (для OS Mac/Linux)
pip install -r requirements.txt
```
# Running tests:

Before running the tests, you should change pwd to the 'bini_test_task' project directory


# Start commands:

```
~ python squanch.py
~ python ram_standup.py
~ python ram_parse.py
~ python ram_top.py
```
