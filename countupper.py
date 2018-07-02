# def count_upper_case(message):
#     count = 0
#     for c in message:
#         if c.isupper():
#             count +=1
#     return count


def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])
    
assert count_upper_case("") == 0, "this should be 0"
assert count_upper_case("ABCF") == 4, "Four uppercase expected"

print("All tests pass!")



