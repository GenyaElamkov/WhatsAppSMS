import os

from dotenv import load_dotenv
from loguru import logger
from whatsapp_api_client_python import API
from whatsapp_api_client_python.API import GreenApi

from src.sms.error import error_authorized, error_block, sms_no_pull, sms_pull

load_dotenv()

logger.add("debug.log", format="{time} {level} {message}",
           level="DEBUG", rotation="10 KB", compression="zip")


def get_status_instanse(green_API: GreenApi) -> bool:
    """
    Получаем статус аккаунта.
    """
    authorized_true = green_API.account.getStateInstance().data[
        'stateInstance']
    if authorized_true == 'notAuthorized':
        logger.error(error_authorized)
        return False

    if authorized_true == 'blocked':
        logger.error(error_block)
        return False
    return True


def main() -> None:
    api_token_instance = os.getenv('API_TOKEN_INSTANCE')
    id_instance = os.getenv('ID_INSTANCE')
    number_phone = os.getenv('NUMBER_PHONE')

    phones = [phone.strip() for phone in number_phone.split(',')]

    green_api = API.GreenApi(id_instance, api_token_instance)

    if get_status_instanse(green_api):
        text = 'Доброе утро. На этой неделе планируем уволить кого-нибудь?'
        for phone in phones:
            if not phone:
                continue

            result = green_api.sending.sendMessage(phone, text)

            # Статус сообщения.
            status_ok = 200
            if result.code == status_ok:
                logger.info(f'{sms_pull} Статус ({result.code})')
            else:
                logger.warning(f'{sms_no_pull} Статус ({result.code})')


if __name__ == '__main__':
    main()
