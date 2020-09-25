pythonist_skills = [
    {"Gohar" : "Python Basics"},
    {"Lilit" : "OOP"},
    {"Janna" : "Git"},
    {"Luiza" : "C++"},
    {"Lilit" : "Business Analyst"},
    {"Janna" : "Numpy"},
    {"Luiza" : "Animation"},
    {"Gohar" : "Business Consultant"}
]

only_keys_dict = dict()
for dict in pythonist_skills:
    for list in dict:
        if list in only_keys_dict:
            only_keys_dict[list] += ", " + (dict[list])
        else:
            only_keys_dict[list] = dict[list]
print(only_keys_dict)
