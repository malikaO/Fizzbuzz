for x in xrange(1, 200):
 
    fizz = not x % 3
    buzz = not x % 5
 
    if fizz and buzz :
        print "Hello word"
    elif fizz:
        print "fizz"
    elif buzz:
        print "Buzz"
    else:
        print x