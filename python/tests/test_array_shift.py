from challenges.array_shift.array_shift import insertShiftArray

def test_array():

    expected = [4,8,16,15,23,42]
    actual = insertShiftArray([4,8,15,23,42], 16)
    assert actual == expected
