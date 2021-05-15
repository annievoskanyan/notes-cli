from os import listdir
from os import remove

NOTES_PATH = './storage'

ADD = 'add'
DELETE = 'delete'
LIST = 'list'


def add_note(note, date_time):
    notes = listdir(NOTES_PATH)

    if len(notes) > 0:
        last_id = int(notes[-1])
    else:
        last_id = 0

    note_id = str(last_id + 1)

    note_str = note_id + '\n'
    note_str += note + '\n'
    note_str += date_time

    file_path = NOTES_PATH + '/' + note_id

    file = open(file_path, 'w+')
    file.write(note_str)
    file.close()

    print('New note added successfully.')
    print(note_str)


def list_notes():
    notes = listdir(NOTES_PATH)

    for note in notes:
        file = open(NOTES_PATH + '/' + note, 'r')
        lines = file.readlines()

        print(lines[0] + lines[1] + lines[2] + '\n')


def delete_note(note_id):
    remove(NOTES_PATH + '/' + note_id)



