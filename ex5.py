# -- coding: utf-8 --

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 #lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %s pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee" % my_teeth

# this line is tricky, try to get ite exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
    
# format
print '"97" format %%c is %c' % 97
print "What is format %%r is %r" % "Format this characters ' %&#7$@*"
print "This is format %%s is %s" % '"Format this characters google.python"'
print "This is format %%d is %d, %i" % (-98, 76.0)
print "This is format %%u is %u" % 108
print "This is format %%o is %o" % 108
print "This is format %%e or %%E is %e, %E" % (1234.567890, 1234.567890)
print "This is format %%.f or %%F is %.1f, %.1F" % (1234.567890, 1234.567890)
print "This is format %%.g or %%G is %.1g, %.1G" % (1234.567890, 1234.567890)
print "This is format %%#x is %#X" % 1254
print "This is format MM/DD/YY, %02d/%02d/%04d" % (2, 4, 20)