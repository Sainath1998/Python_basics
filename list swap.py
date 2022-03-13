def swap_list(new_list):
    size = len(new_list)
    temp = new_list[0]
    new_list[0] = new_list[size-1]
    new_list[size-1] = temp
    return new_list
 
new_list = [10,20,30,40,50]
print(new_list)
print(swap_list(new_list))