# Part 1

"I am 6'2\" tall." # Escape double-quote inside string
'I am 6\'2" Tall.' # Escape single-quote inside string

# Part 2

tabby_cat = "\tI'm tabben in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'l do a list:
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Part 3

while True:
	for i in ["/","-","\\","|"]:
		print "%s\r" % i * 10,