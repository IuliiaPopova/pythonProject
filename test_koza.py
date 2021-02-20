import pytest


def func(a):
    if a < 0:
        return "negative"
    elif a == 0:
        return "zero"
    else:
        return "positive"


@pytest.mark.parametrize("a, result", [
    (-1, "negative"),
    (0, "zero"),
    (1, "positive")
])
def test_all_cases(a, result):
    assert func(a) == result

