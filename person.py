__author__ = 'melchior'


class Person:

    def __init__(self, type, gender, like_list, unlike_list, language_list, name, contact):

        self.type = type  # False Berlin, true newcomer
        self.gender = gender  # True man, False woman
        self.like_list = like_list
        self.unlike_list = unlike_list
        self.language_list = language_list
        self.name = name
        self.contact = contact
