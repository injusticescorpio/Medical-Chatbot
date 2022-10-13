# Arista_2.0
Arista is a medical chatbot having so many features like disease prediction from symptoms, calorie tracking, hospital booking and much more.
This repo is participating in hacktoberfest 2022.

<h2>How to contribute</h2>
<li>Go through the issues assigned</li>
<li>Make changes as per the issue</li>
<li>Create pull request</li>

<h2>Arista Installation</h2>

- First the clone the repository to your local machine.
    ```
    git clone https://github.com/injusticescorpio/Arista_2.0_CS492.git
    ```
    If you are using ssh use the following command.
    ```
    git clone git@github.com:injusticescorpio/Arista_2.0_CS492.git
    ```

- Add venv into your /anancona3/envs inorder to get all dependencies of chatbot.

- Run the following commands in seperate terminals.<br>
        Note:  Here I'm assuming that Arista_2.0_CS492 is the current working directory.
        <pre>
            > Arista 2.O\Terminal_run_code> python .\hospital_booking_main.py
            > Arista 2.O\Terminal_run_code>  python .\pill_remainder_main.py
            > Arista 2.O> rasa run actions
            > Arista 2.O> rasa shell --debug or simply rasa shell if you don't prefer to run on debug mode.
        </pre>
        Inorder to run globally instead of the 3 and 4 commands use the following the commands.

      > Arista 2.O> rasa run actions --cors "*" --debug
      > Arista 2.O> rasa run -m models --enable-api --cors "*" --debug
- Inorder to run the Medical website then navigate to Arista_WEB_APP/aristaweb
- perform
    ```
    python manage.py runserver
    ```
- Test the bot with the [link](http://localhost:8000)
    

 
        
 



