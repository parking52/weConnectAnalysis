__author__ = 'melchior'

import pandas as pd
import nltk
from person import Person

# nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
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
    try:
        languages_tokens = nltk.word_tokenize(working_data_frame['Languages'].iloc[i])
        words = [w.lower() for w in languages_tokens]
        nltk.pos_tag(words)

        print(words)
        print(nltk.pos_tag(words))

    except TypeError:
        continue

    if isinstance(gender, float):
        continue

    if 'Germany' in string_that_should_contain_germany or 'germany' in string_that_should_contain_germany:

        person_creation = Person(False, gender, [], [], [])
        list_of_berlin_person.append(person_creation)

    else:

        person_creation = Person(True, gender, [], [], [])
        list_of_newcomer_person.append(person_creation)

print('number of berlin people then newcomers')
print(len(list_of_berlin_person))
print(len(list_of_newcomer_person))








