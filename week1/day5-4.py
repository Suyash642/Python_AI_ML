lines = """A computer file is a computer resource for recording data discretely in a computer storage device. 
Just as words can be written to paper, so can information be written to a computer file. 
Files can be edited and transferred through the internet on that particular computer system."""

lines.split("\n")

try:
    with open("C:\Codewayy Tasks\week1\demo.txt", 'w') as f:
        for line in lines:
            f.write(line)
            
except FileNotFoundError:
    print("file doesnot exist")

else:
    print("file updated")
    f.close()
