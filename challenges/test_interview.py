import interview

def test1():
    assert interview.interview([5, 5, 10, 10, 15, 15, 20, 20], 120) == "qualified"

def test2():
    assert interview.interview([2, 3, 8, 6, 5, 12, 10, 18], 64) == "qualified"

def test3():
    assert interview.interview([5, 5, 10, 10, 25, 15, 20, 20], 120) == "disqualified"

def test4():
    assert interview.interview([5, 5, 10, 10, 15, 15, 20], 120) == "disqualified"

def test5():
    assert interview.interview([5, 5, 10, 10, 15, 15, 20, 20], 130) == "disqualified"