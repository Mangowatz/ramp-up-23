import discount

def test3():
    assert discount.discount(100,4) == 96

def test4():
    assert discount.discount(100,90) == 9.999999999999998#because python