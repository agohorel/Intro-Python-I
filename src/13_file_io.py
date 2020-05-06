"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

text_file = open("foo.txt", "r")
text = text_file.read()
text_file.close()
print(text)


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

text_to_write = "hello world \nit me \nur boi"
new_file = open("bar.txt", "w")
new_file.write(text_to_write)
new_file.close()

new_file = open("bar.txt", "r")
new_file_contents = new_file.read()
new_file.close()
print(new_file_contents)
