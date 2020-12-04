# Exception Handling
# encapsulation take all data associated with an object and put it in one class
# data hiding
# inheritance
# polymorphism ; function that syntactically looks same is different based on how you use it
"""
# basic syntax
try:
    # Your normal code goes here.
    # Your code should include function calls which might raise exceptions.
except:
    # If any exception was raised, then execute this code block


# catching specific exceptions
try:
    # Your normal code goes here.
    # Your code should include function calls which might raise exceptions.
except ExceptionName:
    # If ExceptionName was raise, then execute this block


# catching multiple specific exceptions
try:
    # Your normal code goes here.
    # Your code should include function calls which might raise exceptions.
except Exception_one:
    # If Exception_one was raised, then execute this block
except Exception_two:
    # If Exception_two was raised, then execute this block
else:
    # If there was no exception, then execute this block


# clean-up after exceptions (if you have code that you want to be executed even if exceptions occur)
try:
    # Your normal code goes here.
    # Your code might include functions which might raise exceptions.
    # If an exception is raised, some of these statements might not be executed
finally:
    # This block of code WILL ALWAYS execute, even if there are exceptions raised
"""

# example with some file I/O (great place to include exception handling
try:
    # the outer try:except: block takes care of a missing file or the fact that the file can't be opened for writing
    f = open("my_file.txt", "w")
    try:
        # the inner: except: block protects against output errors, such as trying to write to a device that is full
        f.write("Writing some data to the file")
    finally:
        # the finally code guarantees that the file is closed properly, even if there are errors during writing
        f.close()
except IOError:
    print("Error: my_file.txt does not exist or it can't be opened for output.")

# as long as a function that is capable of handling an exception exists above where the exception is raised in the stack
# the exception can be handled
def main()
    A()


def A():
    B()


def B():
    C()


def C():
    # processes
    try:
        if condition:
            raise MyException
    except MyException:
        # what to do if this exception occurs
