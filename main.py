import csv
import re
import Models.models as D




if __name__ == '__main__':
    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(D.correct_phonebook)


