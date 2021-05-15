import re
import smtplib
from email.message import EmailMessage
from os import listdir
from actions import NOTES_PATH, delete_note
from datetime import datetime
from time import sleep

DATETIME_FORMAT = '%d/%m/%Y %H:%M'

smtp_host = 'smtp.gmail.com'
smtp_login = ''
smtp_pass = ''

smtp = smtplib.SMTP(smtp_host)
smtp.connect(smtp_host, 587)
smtp.ehlo()
smtp.starttls()
smtp.login(smtp_login, smtp_pass)


def should_send(date_time):
    date_dict = parse_date_time(date_time)

    return datetime.now().strftime(DATETIME_FORMAT) == datetime(
        date_dict['year'],
        date_dict['month'],
        date_dict['day'],
        date_dict['hour'],
        date_dict['minute'],
    ).strftime(DATETIME_FORMAT)


def parse_date_time(date_time):
    str_list = re.split(' |-|:', date_time)

    date_dict = {
        'year': int(str_list[0]),
        'month': int(str_list[1]),
        'day': int(str_list[2]),
        'hour': int(str_list[3]),
        'minute': int(str_list[4])
    }

    return date_dict


while True:
    print('Checking notes...')

    notes = listdir(NOTES_PATH)

    if not len(notes):
        print('Empty storage.')

    for note_id in notes:
        with open(NOTES_PATH + '/' + note_id) as fp:
            lines = fp.readlines()

            if should_send(lines[2]):
                print(f'Sending the note #{note_id}...')

                message = EmailMessage()
                message.set_content(lines[1])
                # me == the sender's email address
                # you == the recipient's email address
                message['Subject'] = f'Note #{note_id}'
                message['From'] = 'notes@example.com'
                message['To'] = ''

                smtp.send_message(message)
                delete_note(note_id)

                print(f'Note {note_id} has been sent and removed from the storage.')

    sleep(60)
