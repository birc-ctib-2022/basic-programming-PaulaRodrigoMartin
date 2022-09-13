
my_list = [] #create an empty list, gonna fill it with the for loop
for i in range(1,6):
    my_list.append(str("*")) #append to the empty list a string * from the iteration
    print(' '.join(my_list)) 
for i in range(1,6):
    my_list.remove(str("*")) #remove to the empty list a string * from the iteration
    print(' '.join(my_list)) 