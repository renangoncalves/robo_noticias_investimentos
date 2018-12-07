import json
import requests

SLACK_INCOMING_WEB_HOOK = '' #self explanatory


def send_msg(text, channel='#teste_goncalves'):

    SLACK_INCOMING_CHANNEL = channel

    payload = {
        "text": str(text),                  # message you want to send
        "channel": SLACK_INCOMING_CHANNEL   # Channel set above
    }
    req = requests.post(SLACK_INCOMING_WEB_HOOK, json.dumps(payload), headers={'content-type': 'application/json'}) #request to post the message

# slack_msg('mensagem')
