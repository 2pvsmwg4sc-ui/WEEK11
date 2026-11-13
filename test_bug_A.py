from bug3_logic import find_max


def test_maximum_is_last_item():
    assert find_max([10, 20, 30]) == 30


def test_maximum_is_middle_item():
    assert find_max([10, 30, 20]) == 30


def test_maximum_is_first_item():
    assert find_max([30, 20, 10]) == 30


def test_single_item():
    assert find_max([42]) == 42