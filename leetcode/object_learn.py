# coding: utf-8


class Student(object):

    def __init__(self, name):
        self.name = name

    def age(self):
        return 20

    def home(self):
        return Student.get_user_home('beijing')

    @classmethod
    def get_user_home(cls, local):
        if local:
            return local
        return 'Beijing'


if __name__ == '__main__':
    print Student('xiaoming').home()
