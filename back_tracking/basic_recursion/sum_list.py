# Problem 2: Sum all elements in a list

# Write:

# recursive_sum(numbers)
# Examples
# recursive_sum([2, 4, 6])       # 12
# recursive_sum([5])             # 5
# recursive_sum([])              # 0
# recursive_sum([1, 3, 5, 7])    # 16

def recursive_sum(i_list):
    if len(i_list) == 0:
        return 0
    
    return i_list[0] + recursive_sum(i_list[1:len(i_list)])

print(recursive_sum([]))