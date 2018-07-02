def numer_of_evens(numbers):
    return 2
    

def test_are_equal(actual, expected):
    assert actual == expected, "Expected {0}, but got a value of {1}".format(expected, actual)
    
def test_are_not_equal(a, b):
    assert a != b, "{0} == {1} and we don't want that ". format(a, b)
    
def test_is_in(collection, item):
    assert item in collection, "{0} is not in {1}".format(item, collection)
    
    
test_are_equal(numer_of_evens([1,2,3,4]), 2)

test_is_in([1,2,3,4], 5)
