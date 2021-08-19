def funct(p1, p2, *args, k, **kwargs):
    print("positional-or-keyword:........{},{}".format(p1, p2))
    print("var-postional(* args):........{}".format(args))  # note how this line prints a tuple
    print("keyword:......................{}".format(k))
    print("var-keyword:..................{}".format(kwargs))


funct(1, 2, 3, 4, 5, k=6, key1=7, key2=8)

# in above case we have to pass the  parameter value k as key word argument because else it will cause ambiguty....
# as we dont know exactly how  many argument to be included in   *args
