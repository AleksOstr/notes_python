import datetime


class Note:
    def __init__(self, id: int, title: str, content: str):
        self.id = id
        self.title = title
        self.content = content
        self.date = datetime.datetime.now()

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content

    def set_new_date(self):
        self.date = datetime.datetime.now()

    def set_new_title(self, new_title: str):
        self.title = new_title

    def set_new_content(self, new_content: str):
        self.content = new_content
