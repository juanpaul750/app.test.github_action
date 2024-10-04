from src.math_operations import add,sub

def test_add():
    assert add(2,3)==5
    assert add(-1,3)==2
    assert add(4,5)==9
    print("Test operation is running")


def test_sub():
    assert sub(4,0)==4
    assert sub(1,-1)==2
    assert sub(3,2)==1
    print("Test operation is running")
