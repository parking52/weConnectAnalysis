__author__ = 'melchior'

import pandas as pd
import nltk
import pickle
from person import Person
import string

# nltk.download('punkt')
# nltk.download('stopwords')
working_data_frame = pd.read_excel('survey_result.xlsx')

# print(working_data_frame)
print(list(working_data_frame.columns.values))
# print(working_data_frame['Languages'])
# print(working_data_frame.iloc[7])

# print(working_data_frame.count)
list_of_berlin_person = []
list_of_newcomer_person = []

gender_mapping = {'Man': True, 'Woman': False}


for i in range(len(working_data_frame.index)):

    string_that_should_contain_germany = working_data_frame['Where are you from?'].iloc[i]
    gender = working_data_frame['Gender'].map(gender_mapping).iloc[i]
    name = working_data_frame['First name'].iloc[i]
    contact = working_data_frame['Contact details'].iloc[i]

    try:
        age = int(working_data_frame['How old are you?'].iloc[i])
    except ValueError:
        age = 30 #TODO fix


    try:

        languages_tokens = nltk.word_tokenize(working_data_frame['Languages'].iloc[i])
        stopset = nltk.corpus.stopwords.words('english') + list(string.punctuation)
        cleanup_language_words = [i for i in nltk.word_tokenize(working_data_frame['Languages'].iloc[i]) if i not in stopset]
        cleanup_language_words = [word.lower() for word in cleanup_language_words]
        print(cleanup_language_words)

    except TypeError:
        continue

    if isinstance(gender, float):
        continue


    if 'Germany' in string_that_should_contain_germany or 'germany' in string_that_should_contain_germany:

        person_creation = Person(i, False, gender, age, [], [], cleanup_language_words, name, contact)
        list_of_berlin_person.append(person_creation)

    else:

        person_creation = Person(i, True, gender, age, [], [], cleanup_language_words, name, contact)
        list_of_newcomer_person.append(person_creation)

print('number of berlin people then newcomers')
print(len(list_of_berlin_person))
print(len(list_of_newcomer_person))

pickle.dump(list_of_berlin_person, open("berlin_persons.p", "wb"))
pickle.dump(list_of_newcomer_person, open("newcomer_persons.p", "wb"))










