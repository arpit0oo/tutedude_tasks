'''with open("sample.text", "rt") as f:
    f.write("This is a sample text file \nThis file is created for Tutedude 4th assignment \nThanks You!!")
'''
# Now that our sample file is create we'll read it line by line

try:
    with open("sample.text", "rt") as f:
        contents = f.readlines()
except FileNotFoundError:
    print("Error : The file 'sample.text' was not found.")

print("Reading File Contents: \n")
for i in range(3):
    try:
        if contents[i]=="":
            break
        else:
            print(f"Line {i+1}: {contents[i]}")
    except NameError:
        print("Error : Can't read files content")
        break