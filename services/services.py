class Repo:
    def __init__(self):
        self.files = []
        self.remote = False


class File:
    def __init__(self, name, content):
        self.name = name
        self.content = content
        self.changes = []
        self.tracked = False

    def add_file(self, name, tracked=False):
        pass

    def alter_file(self, new_content, tracked=False):
        if tracked is False:
            self.content = new_content
        else:
            self.content = new_content
            self.changes.append(Stage('modified').become_staged())


    def remove_file(self, name):
        pass


class Stage:
    def __init__(self, type):
        self.staged = False
        self.type = type

    def become_staged(self):
        self.staged = True

    def become_unstaged(self):
        self.staged = False