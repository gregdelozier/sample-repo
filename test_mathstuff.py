from mathstuff import add, sub, div, mul, info

def test_add():
    print("test_add")
    assert add(2,3) == 5

def test_sub():
    print("test_sub")
    assert sub(2,1) == 1

def test_mul():
    print("test_mul")
    assert mul(4,2) == 8

def test_div():
    print("test_div")
    assert div(4,2) == 2

def test_info():
    print("test_info")
    assert type(info()) is str

if __name__ == "__main__":
   test_add()
   print("done.")

