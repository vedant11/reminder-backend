# reminder-backend
Send people certain reminders on WhatsApp. Directly deployable.

## Files

#### twilio-api-script.py

Py script, that makes the request to the twilio API.

#### clock.py

Using APScheduler, runs sendText function from api-script after certain intervals. Edit the interval at 9:37 if needed.

#### Procfile

To handle the clock management while deploying.

#### requirements.txt

Just two requirements:

- Twilio
- APS

## Geting started, host your script

1) You will require a twilio account. In the `Console`, under `Programmable SMS` select `WhatsApp beta`
2) Copy the sandbox code and on the WhatsApp accounts you want to connect, text
  `join <sandbox-code>`
3) Edit the script as per your account and sandbox credentials. Copy the script directly from Twilio if you want.
4)Create a new app on heroku and push your repo
5) After the build, you might want to start clock.py under `Resources > Dyno`.
6) The hosted script is up now!
