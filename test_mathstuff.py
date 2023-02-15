from mathstuff import add, sub

def test_add():
    print("test_add")
    assert add(2,3) == 5

def test_sub():
    print("test_sub")
    assert sub(2,1) == 1

if __name__ == "__main__":
   test_add()
   print("done.")

