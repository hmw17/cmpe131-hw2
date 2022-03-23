def func_counter(f):  #declar the decorator
    def cnt(y):
        cnt.counter += 1
        return f
    cnt.counter = 0
    return cnt


@func_counter
def foo(y):
    return y+2**3-34

y=5 #you can input
foo(y)
foo(y)
foo(y)
print(foo.counter)