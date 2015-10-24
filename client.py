__author__ = 'melchior'


import clustering_persons
from person import Person
import pickle
from operator import itemgetter

p1 = Person(1, False, True, 40, [], [], ['arabic', 'german', 'english'], "new_guy_name", "contact me")
# man berliner which is 25

p2 = Person(1, False, False, 25, [], [], ['arabic', 'german', 'english'], "new_guy_name", "contact me")
# man berliner which is 25

advised_persons_index, refused_persons_index = clustering_persons.getting_cluster_for_new_guy(p1)

if p1.type:  # newcomer
    list_of_people = pickle.load(open("berlin_persons.p", "rb"))

else:  # berliner
    list_of_people = pickle.load(open("newcomer_persons.p", "rb"))

list_of_interesting_people = [list_of_people[i] for i in advised_persons_index]
list_of_not_interesting_people = [list_of_people[i] for i in refused_persons_index]

print('---------------------')
print('INTERESTING')
print('---------------------')

for people in list_of_interesting_people:
    print(str(people.age) + str(people.gender) + str(people.language_list) + (10 * '') + str(people.contact))

print('---------------------')
print('NOT INTERESTING')
print('---------------------')

for people in list_of_not_interesting_people:
    print(str(people.age) + str(people.gender) + str(people.language_list) + (10 * '') + str(people.contact))


