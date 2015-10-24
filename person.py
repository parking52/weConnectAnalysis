__author__ = 'melchior'


class Person:

    def __init__(self, id, type, gender, age, like_list, unlike_list, language_list, name, contact):

        self.id = id
        self.type = type  # False Berlin, true newcomer
        self.gender = gender  # True man, False woman
        self.age = age
        self.like_list = like_list
        self.unlike_list = unlike_list
        self.language_list = language_list
        self.name = name
        self.contact = contact

    def distance_of_two_persons(self, person_to_compare):

        age_coeff = abs(self.age - person_to_compare.age)

        # print(self.language_list)
        # print(person_to_compare.language_list)
        # print(set(self.language_list).intersection(person_to_compare.language_list))
        # print('_______________________________________')

        nb_common_language = len(list(set(self.language_list).intersection(person_to_compare.language_list)))
        lang_coef = nb_common_language / (len(self.language_list) + len(person_to_compare.language_list))
        gender_diff = (1 - abs(self.gender - person_to_compare.gender))

        return (gender_diff * lang_coef) / (age_coeff + 1)



if __name__ == '__main__':

    p1 = Person(1, False, 1, 30, [], [], ['english', 'arabic', 'italian'], "Joelie", "aaaaaa")
    p2 = Person(1, False, 1, 20, [], [], ['german', 'hindu', 'english'], "Simeon", "bbbbbb")
    p3 = Person(1, False, 1, 30, [], [], ['hindu', 'swedish', 'german'], "Aekoel", "cccccc")
    p4 = Person(1, False, 1, 30, [], [], ['hindu', 'swedish', 'german', 'spanish'], "Women", "contact")

    print(p1.distance_of_two_persons(p2))
    print(p2.distance_of_two_persons(p1))

    print(p3.distance_of_two_persons(p1))
    print(p1.distance_of_two_persons(p3))

    print(p1.distance_of_two_persons(p4))
    print(p4.distance_of_two_persons(p1))

    print(p2.distance_of_two_persons(p3))
    print(p3.distance_of_two_persons(p2))

    print(p2.distance_of_two_persons(p4))
    print(p4.distance_of_two_persons(p2))

    print(p3.distance_of_two_persons(p4))
    print(p4.distance_of_two_persons(p3))

    # print(p3.distance_of_two_persons(p3))
    # print(p3.distance_of_two_persons(p3))
