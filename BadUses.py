# really bad uses of try: except:

# don't
try:
    average = sum(a_list) / len(a_list)
except ZeroDivisionError:
    average = 0

# do
if len(a_list) > 0:
    average = sum(a_list) / len(a_list)
else:
    average = 0


# don't
try:
    value = my_list[index]
except IndexError:
    value = -1

# do
if 0 <= index < len(my_list):
    value = my_list[index]
else:
    value = -1


# don't
try:
    value = my_dictionary[key]
except KeyError:
    value = -1

# do
if key in my_dictionary.keys():
    value = my_dictionary[key]
else:
    value = -1


