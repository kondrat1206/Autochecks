def get_grade(key):
    grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
    return grade.get(key, None)


def get_description(key):
    description = {
        "A": "Perfectly",
        "B": "Very good",
        "C": "Good",
        "D": "Satisfactorily",
        "E": "Enough",
        "FX": "Unsatisfactorily",
        "F": "Unsatisfactorily",
    }
    return description.get(key, None)


keys = ["A", "B", "C", "D", "E", "FX", "F"]

values_grade = map(get_grade, keys)
values_description = map(get_description, keys)

grades_dict = dict(zip(keys, values_grade))
descriptions_dict = dict(zip(keys, values_description))



option = 5

if option in grades_dict.values():
    for key, value in grades_dict.items():
        if option == value:
            get_grade(key)

elif option in values_description:
    for key, value in descriptions_dict.items():
        if option == value:
            get_description(key)
else:
    #return None
    pass

