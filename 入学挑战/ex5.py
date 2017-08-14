name = 'zhucunli'
age = 25
height = 164
weight = 46
eyes = 'Black'
teeth = 'White'
hair = "Black"

print "Let's talk about %s." % name
print "She is %d centimeters tall" % height
print "She is %d kilograms heavy" % weight
print "Actually it's not heavy."
print "She's got %s eyes and %s hair" % (eyes,hair)
print "Her teeth are usually %s depending on the coffee" % teeth
#This line is tricky,tyy to get it exactly right
print "If I add %d,%d and %d I get %d." % (age,height,weight,age+height+weight)
