NAME_OUTPUT = "name.txt"

out_file = open(NAME_OUTPUT, "w")
name = input("Please enter your name: ")
print(out_file.write(name))
out_file.close()

in_file = open(NAME_OUTPUT, "r")
name = in_file.read()
print("Your name is", name)
in_file.close()