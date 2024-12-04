try:
    # the two arguments here are the 1) name of the file and the operation "w"
    fh = open("testfile","w")
    fh.write("This is my test file for exception handling")
except IOError:
    print("error: can't find file or read data")
else:
    print("written content in the file successfully")
    fh.close()

def new_try():
    try:
    # The with statement ensures that the file is properly closed after the operation, even if an exception occurs.
     with open("hi.txt","w") as ch :
        ch.write("this is my for error exception handling")
    except IOError:
     print("error: can't find file or read data")
    else:
     print("written content in the file successfully")
    #  ch.close()

new_try()

# The finally block runs unconditionally, regardless of whether an error occurs. By printing Error: can't find file or read data, you're implying that something went wrong, even though the try block executed successfully.

# this is a a bad practice
def different():
    try:
     with open("da", "w") as sh:
      sh.write("This is my test file for exception handling!!")
    finally:
     print ("Error: can\'t find file or read data")

different()

# so the finally block is used to release resources and stuff

