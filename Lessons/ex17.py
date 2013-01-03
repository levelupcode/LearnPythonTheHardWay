from sys import argv
from os.path import exists

script, from_file, to_file = argv



# We could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Copied the information from %s to %s" % (from_file, to_file)

out_file.close()
in_file.close()