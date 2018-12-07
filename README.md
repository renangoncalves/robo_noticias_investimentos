# robo_noticias_investimentos
Robô para monitorar e noticias relacionadas ao mercado de ações

## Configuração:

### Instalação de Dependncias:
```
    virtualenv -p python3 ./venv
    source venv/bin/activate
    pip install -r requirements.txt
```
### Ajustes envio de mensagem:
```
É necessário informar a url do web hook.
Arquivo msg_slack, constante SLACK_INCOMING_WEB_HOOK
```
