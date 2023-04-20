import os

from dotenv import load_dotenv
from whatsapp_api_client_python import API

load_dotenv()


def main():
    API_TOKEN_INSTANCE = os.getenv('API_TOKEN_INSTANCE')
    ID_INSTANCE = os.getenv('ID_INSTANCE')
    NUMBER_PHONE = os.getenv('NUMBER_PHONE')

    greenAPI = API.GreenApi(ID_INSTANCE, API_TOKEN_INSTANCE)
    text = 'Приветик. Работает скрипт. Ответь если увидела сообщения.'
    result = greenAPI.sending.sendMessage(NUMBER_PHONE, text)

    print(result)

if __name__ == '__main__':
    main()
