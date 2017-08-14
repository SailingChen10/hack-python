# this one is like your script with argv.
def print_two(*args):
    arg1,arg2 = args
    print "arg1:%r,arg2:%r"%(arg1,arg2)

    #ok,that *args is actually pointless,we can just do this

def print_two_again(arg1,arg2):
    print "arg1:%r,arg2:%r"%(arg1,arg2)

# this just takes one arguement
def print_one(arg1):
    print "arg1:%r"% arg1

# this one takes no arguement
def print_none():
    print "I got nothin'."

print_two("Zhu","Cunli")
print_two_again("Zhu","Cunli")
print_one("First")
print_none()
