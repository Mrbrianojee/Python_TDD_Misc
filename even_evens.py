# 2
def is_even(num):
     return num % 2 == 0
# 1
# def even_number_of_evens(numbers):
#     if numbers == []:
#         return False
#     else:
#         count = 0
#         for num in numbers:
#             if num % 2 == 0:
#                 count+=1
#                 print(count)
                
#         if count % 2 == 0:
#             return True
#         else:
#             return  False
        
# 3

def even_number_of_evens(numbers):
    evens = sum([1 for num in numbers if is_even(num)])
    return False if evens == 0 else is_even(evens)



assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three are even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four are even"
# assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

print("All tests passed!")