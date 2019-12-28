words = input("Enter words: ")


new_string = ""
a = words.split()
print()
a.sort(key = len)
for i in a:
	i = i + " "
	new_string += (str(i))

print(new_string)
print()