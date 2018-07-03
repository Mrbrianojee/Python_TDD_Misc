def numer_of_evens(numbers):
    return 2
    

def test_are_equal(actual, expected):
    assert actual == expected, "Expected {0}, but got a value of {1}".format(expected, actual)
    
def test_are_not_equal(actual, expected):
    assert actual != expected, "{0} == {1} and we don't want that ". format(actual, expected)
    
def test_is_in(collection, item):
    assert item in collection, "{0} is not in {1}".format(item, collection)
    
def test_is_not_in(collection, item):
    assert item not in collection, "{0} is in {1} but we don't want that ".format(item, collection)
    
def test_is_between(possible_lower, possible_upper, actual_lower, actual_upper):
    assert actual_lower >= possible_lower and actual_upper <= possible_upper, \
    "Expected lower = {0} Actual lower = {1}, Expected upper={2} and Actual upper ={3}".format(possible_lower, actual_lower, possible_upper, actual_upper)
    
    
test_are_equal(numer_of_evens([1,2,3,4]), 2)

test_is_in([1,2,3,4], 4)

test_is_not_in([1,2,3,4], 5)

test_is_between(3,10, 3,10)