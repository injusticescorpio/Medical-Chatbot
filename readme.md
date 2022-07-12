# Arista_2.0
Arista is a medical chatbot having so many features like disease prediction from symptoms, calorie tracking, hospital booking and much more.

<h2>Arista Installation</h2>

<pre>
First add venv into your /anancona3/envs inorder to get all dependencies of chatbot
Run the following commands in seperate terminals
    >  D:\Arista 2.O\Terminal_run_code> python .\hospital_booking_main.py
    >  D:\Arista 2.O\Terminal_run_code>  python .\pill_remainder_main.py
    >  D:\Arista 2.O> rasa run actions
    >  D:\Arista 2.O> rasa shell --debug or simply rasa shell if you don't prefer to run on debug mode.

Inorder to run globally instead of the 3 and 4 commands use the following the commands
    >  D:\Arista 2.O> rasa run actions --cors "*" --debug
    >  D:\Arista 2.O> rasa run -m models --enable-api --cors "*" --debug
</pre>
