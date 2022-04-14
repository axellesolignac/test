from lib import average, get_median
from main import class_average_median

def test_average():
    li = [0,10,20]
    expected_result = average(li)
    assert expected_result == 10

def test_get_median():
    li = [0,1,6,5]
    expected_result = get_median(li)
    assert expected_result == 3

def test_class_average_median():
    l2d = [[0,10,20],[18,20,22]]
    expected_average = 15
    expected_median = 15
    expected_result = (15,15)
    assert class_average_median(l2d) == expected_result