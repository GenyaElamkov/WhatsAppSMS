'''
Отследить статут активированного аккаутнта GetStateInstanse
Продумать над логирование скрипта.
Скрипт будет запускаться в определенное время
Где будет хранится скрипт? в облаке или на компе.
'''

import os

from dotenv import load_dotenv
from whatsapp_api_client_python import API
from whatsapp_api_client_python.API import GreenApi

from src.error import error_authorized, error_block

load_dotenv()


def get_status_instanse(greenAPI: GreenApi) -> str:
    '''
    Получаем статус аккаунта.
    '''
    authorized_true = greenAPI.account.getStateInstance().data['stateInstance']
    if authorized_true == 'notAuthorized':
        return error_authorized
    if authorized_true == 'blocked':
        return error_block


def main() -> None:
    API_TOKEN_INSTANCE = os.getenv('API_TOKEN_INSTANCE')
    ID_INSTANCE = os.getenv('ID_INSTANCE')
    NUMBER_PHONE = os.getenv('NUMBER_PHONE')

    greenAPI = API.GreenApi(ID_INSTANCE, API_TOKEN_INSTANCE)
    print(get_status_instanse(greenAPI))
    text = 'Привет. Работает скрипт. Ответь если увидела сообщения.'
    # result = greenAPI.sending.sendMessage(NUMBER_PHONE, text)
    # print(result.code)


if __name__ == '__main__':
    main()
