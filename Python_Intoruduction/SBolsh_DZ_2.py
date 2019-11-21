my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

for val in my_list_2:
    val=int(val)
    if val in my_list_1:
        my_list_1.remove(val)

print(my_list_1)



