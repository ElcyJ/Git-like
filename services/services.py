from copy import copy

class Repo:
    def __init__(self):
        self.files = []
        self.remote = False

    def create_file(self, name, content):
        file = File(name, content)
        self.files.append(file)

    def add(self, name):
        for file in self.files:
            if file.name == name:
                file.add_file()

    def edit(self, name, content):
        for file in self.files:
            if file.name == name:
                file.alter_file(content)

    def remove_file(self, name):
        for file in self.files:
            if file.name == name:
                file.remove_file()


class File:
    def __init__(self, name, content):
        self.name = name
        self.content = content
        self.status = None
        self.tracked = False

    def add_file(self):
        if self.tracked is False:
            self.tracked = True
            stage = Stage('new_file')
            stage.become_staged()
            self.status = stage

    def alter_file(self, new_content):
        if self.tracked:
            if self.status.staged:
                file2 = copy(self)
                stage = Stage('modified')
                stage.become_unstaged()
                file2.status = stage
                file2.content = new_content
            else:
                self.content = new_content
        else:
            self.content = new_content

    def remove_file(self):
        if self.tracked:
            self.status.append(Stage('modified').become_unstaged())


class Stage:
    def __init__(self, type):
        self.files = []
        self.staged = False
        self.type = type

    def become_staged(self):
        self.staged = True

    def become_unstaged(self):
        self.staged = False


