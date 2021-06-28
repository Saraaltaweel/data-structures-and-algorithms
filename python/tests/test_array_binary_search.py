from challenges.array_binary_search.array_binary_search import BinarySearch


def BinarySearch_one():

    expected = 2
    actual = BinarySearch([4,8,15,16,23,42], 15)
    assert actual == expected
