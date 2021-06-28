from linked_list.linked_list import *


def test_insert(list_test):
    excpected = "{3} -> {4} -> {5} ->  NULL"
    actual = f"{list_test}"
    assert excpected == actual

def test_includes(list_test):
    actual = [list_test.includes(4),list_test.includes("5"),list_test.includes(6)]
    excpected = [False, True , False]
    assert excpected == actual


def list_test():
    linked = Linked_list()
    linked.insert(1)
    linked.insert(2)
    linked.insert(3)
    return linked