def doubler(function):
    def subfunction():
        function()
        function()

    return subfunction

@doubler
def test():
    print("done")

test()