import time, sys

argfile = str(sys.argv[1])
#
# filename = open(argfile, 'r').replace('\n', '')
# f = filename.readlines()
# filename.close()

with open (argfile, "r") as filename:
    data=filename.read().replace('\n', ' ')
filename.close()

# for line in f:
#     print line[:140]
#     print "THIS IS 140"

if len(data) > 140:
    print "Input exceeds 140 characters."
    data = data[:140]
    print data
