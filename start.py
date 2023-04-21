"""
Скрипт отправляет сообщения в WhatsApp.
Триггер: Еженедельно по понедельникам в 9:00.
Cron: 00 6 ? * MON *
"""

from src.sms.main import main


def start():
    text = 'Доброе утро. На этой неделе планируем уволить кого-нибудь?'
    main(text)


if __name__ == '__main__':
    start()
