ans = __import__('0-safe_print_list').safe_print_list

my_list = [1, 2, 3, 4, 5]

nb_p = ans(my_list, 2)
print("nb: {:d}".format(nb_p))
nb_p = ans(my_list, len(my_list))
print("nb: {:d}".format(nb_p))
nb_p = ans(my_list, len(my_list) + 2)
print("nb: {:d}".format(nb_p))