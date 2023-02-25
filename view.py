from controller import Controller
from commands import *


class View:

    def __init__(self, controller: Controller):
        self.controller = controller

    def run(self):
        try:
            while True:
                command = input(commands).lower().strip()
                match command:
                    case 'show':
                        notes = self.controller.read_notebook()
                        for note in notes:
                            print(f'ID: {note.get_id()} Title: {note.get_title()} Content: {note.get_content()}\
                             Date: {note.get_date()}\n')
                        continue
                    case 'create':
                        title = input('Enter title: ')
                        content = input('Enter content: ')
                        self.controller.create_note(title, content)
                        continue
                    case 'update':
                        id = int(input('Enter ID: '))
                        new_title = input('Enter new title: ')
                        new_content = input('Enter new content: ')
                        self.controller.update_note(id, new_title, new_content)
                        continue
                    case 'delete':
                        id = int(input('Enter ID: '))
                        self.controller.delete_note(id)
                        continue
                    case 'find':
                        id = int(input('Enter ID: '))
                        note = self.controller.find_by_id(id)
                        print(f'ID: {note.get_id()} Title: {note.get_title()} Content: {note.get_content()}\
                        Date: {note.get_date()}\n')
                        continue
                    case 'exit':
                        break
        except Exception:
            print('You did something wrong. Try again.')
