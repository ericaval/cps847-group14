import slack
import os
import requests
from pathlib import Path
from dotenv import load_dotenv
# Import Flask
from flask import Flask

# Handles events from Slack
from slackeventsapi import SlackEventAdapter

# Load the Token from .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Configure Flask application
app = Flask(__name__)

# Configure SlackEventAdapter to handle events
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'],'/slack/events', app)

# Using WebClient in slack, there are other clients built-in as well
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

# Get Bot ID
BOT_ID = client.api_call("auth.test")['user_id']

# Handling Message Events
@slack_event_adapter.on('message')
def message(payload):
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    city = event.get('text')
    if BOT_ID != user_id:
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=96d8a90e51ade1a30915d9e1ec5c42e0'.format(city)
        res = requests.get(url)
        if res.status_code == 404:
            client.chat_postMessage(channel=channel_id, text= event.get('text'))
        else:
            data = res.json()
            temp = round(data['main']['temp'] - 273.15, 2)
            feels = round(data['main']['feels_like'] - 273.15, 2)
            weather = data['weather'][0]['description']
            text2 = city +' Weather Details' + '\nWeather: '+weather +'\nTemperature: '+str(temp)+' degree Celsius'+'\nFeels Like: '+str(feels)+' degree Celsius'+'\nPressure: '+str(data['main']['pressure'])+' hPa'+'\nHumidity: '+str(data['main']['humidity'])+'\nWind Speed: '+str(data['wind']['speed'])
            client.chat_postMessage(channel=channel_id, text=text2)

# Run the webserver micro-service
if __name__ == "__main__":
    app.run(debug=True)
