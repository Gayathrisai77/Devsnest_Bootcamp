########### SElECTION SORT ALOGARITHM #########
my_array = [23,5,6,2,1,77]
print("Given Array:",my_array)

for i in range(len(my_array)):
    min_value = min(my_array[i:])
    min_index = my_array.index(min_value,i)
    my_array[i],my_array[min_index] = my_array[min_index],my_array[i]
    
print("After sorting:",my_array)
