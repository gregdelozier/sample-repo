""" example programming experiment """

def add(x):
    return sum(x)

def evaluate(s, e):
    """evaluate the structure s in the environment e"""
    print("s=", s)
    if type(s) is list:
        f = evaluate(s[0], e)
        assert callable(f)
        return(f([evaluate(t, e) for t in s[1:]]))
    elif type(s) is str:
        assert s in e
        return e[s]
    else:
        return s

program = ["+", ['+', 4, 5], 2]
environment = {
    '+':add,
}

print(evaluate(program, environment))
