def test_star(*args):   # here  using * we are defining that function will take the multiple argument...i.e the use may pass 1 or 2 or 3  etc argument to cal this function
    print(args)
    for x in args:
        print(x)


test_star(0,1,2,3,4,5) # here we passed 6 arguments .....we can pass any number of argument

# please note......on line 2...as we can obseve ....the args is in effect is a tuple