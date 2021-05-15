from sys import argv
from actions import LIST, ADD, DELETE
from actions import list_notes, add_note, delete_note


def main():
    action = argv[1].lower()

    if action == ADD:
        note = input('Please enter note: ')
        date_time = input('Please enter date (required) and time (optional): ')
        add_note(note, date_time)
    elif action == LIST:
        list_notes()
    elif action == DELETE:
        note_id = input('Please enter note ID: ')
        delete_note(note_id)
    else:
        print('Invalid action ' + action + '. Valid actions: ' + ADD + ', ' + LIST +
              ',' + DELETE)


if __name__ == '__main__':
    main()
