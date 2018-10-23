from services.attributes import *


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

    def insert_file(self, file):
        self.files.append(file)

   # def do_commit(self, packed):
    #    commit = Commits()
     #   commit.do_commit()


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
                self.content = new_content
                self.status.become_unstaged()
                self.status.type = 'modified'

            else:
                self.content = new_content
        else:
            self.content = new_content

    def remove_file(self):
        if self.tracked:
            self.status.append(Stage('modified').become_unstaged())


class Stage:
    def __init__(self, type):
        self.staged = False
        self.type = type

    def become_staged(self):
        self.staged = True

    def become_unstaged(self):
        self.staged = False






