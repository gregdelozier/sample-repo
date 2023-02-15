from mathstuff import add, sub, div

def test_add():
    print("test_add")
    assert add(2,3) == 5

def test_sub():
    print("test_sub")
    assert sub(2,1) == 1

def test_div():
    print("test_div")
    assert div(4,2) == 2

if __name__ == "__main__":
   test_add()
   print("done.")

