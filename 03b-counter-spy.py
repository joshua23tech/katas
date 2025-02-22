# This function takes a list of names.
# The function should return a list containing the names of the people who
#  aren't spies.
# Recent intelligence has revealed that all spies codenames include the
#  letters 's', 'p' or 'y'.
# You can't afford to take any chances, and all names that include those
#  letters should be removed.


def counter_spy(people):
    lst_valid_persons = []
    for person in people:
        lst_person_chars = list(person)
        if "s" not in lst_person_chars and "S" not in lst_person_chars:
            if "p" not in lst_person_chars and "P" not in lst_person_chars:
                if "y" not in lst_person_chars and "Y" not in lst_person_chars:
                    lst_valid_persons.append(person)
    
    lst_valid_persons_sorted = sorted(lst_valid_persons)
    return lst_valid_persons_sorted