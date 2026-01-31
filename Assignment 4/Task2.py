user_write = input("Enter Text to write to the file: ")
with open("output.text", "wt") as f:
    f.write(user_write)
    f.write("\n")
    print("data succussfully written to output.text.\n")

user_append = input("Enter additional text to be append: ") 
with open("output.text", "at") as f:
    f.write(user_append,)
    print("Data successfully appended.\n")
print("Final Contents Of output.txt: ")
with open("output.text", "rt") as f:
    contents = f.readlines()
for content in contents:
    print(content)



