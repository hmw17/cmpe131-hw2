def func_counter(f):
    def sub(*args):
        sub.counter += 1
        f(*args)

    sub.counter = 0
    return sub


@func_counter
def foo(y):
    return y+2**3-34

y=1
foo(y)
foo(y)

print(foo.counter)