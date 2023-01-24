def create_hello_string(name):
    return "hello, " + name + "!"

def test_create_hello_string():
    assert create_hello_string("world") == "hello, world!"

if __name__ == "__main__":
    test_create_hello_string()
    print("pass.")