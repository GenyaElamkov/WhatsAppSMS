"""
Скрипт отправляет сообщения в WhatsApp.
по пятницам
00 6 ? * FRI *
"""

from src.sms.main import main


def start():
    text = 'Доброе утро. На этой неделе планируем уволить кого-нибудь?'
    main(text)


if __name__ == '__main__':
    start()
