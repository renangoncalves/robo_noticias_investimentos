import requests
import datetime
import time
from msg_slack import send_msg


def get_url(action):
    time_seconds = timestamp_seconds()
    mount_url = 'http://cotacoes.economia.uol.com.br/snapQuote.html?code=' + action + '.SA&_=' + str(time_seconds)
    print(mount_url)
    return mount_url


def timestamp_seconds():
    mount_time = time.strftime("%s", time.gmtime())
    return mount_time


def timestamp_date_time():
    time_seconds = timestamp_seconds()
    readable = datetime.datetime.fromtimestamp(float(time_seconds)).isoformat()
    return readable


def send_message(message):
    send_msg(message)
    print(message)


def get_actions():
    list_actions = {
        'HAPV3': ['R$ 26,00', 'R$ 33,00'],
        'ITSA4': ['R$ 9,54', 'R$ 10,00'],
        'CIEL3': ['R$ 8,00', 'R$ 10,00']
         }
    msg = 'Acao ------ Vl. Atual -- Variacao -- Vl. Desejo -- Vl. Max \n'
    for acao in list_actions.keys():
        url = get_url(acao)
        data = requests.get(url).json()
        msg = msg + data['code'] + \
              ' -- R$ ' + data['bid'] + \
              ' -- R$ ' + data['change'] + \
              ' -- R$ ' + list_actions[acao][0] + \
              ' -- R$ ' + list_actions[acao][1] + '\n'

    send_message(msg)


# get_actions()
