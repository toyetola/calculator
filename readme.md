# BODMAS Calculator

### This calculator solution is written in python and it defines a class named __calculator__ with its attributes amongs which are:

- additon - which handles sum operation
- subtraction - handles subtraction or difference
- multiplication - handles numerical mulplication
- handles - division of given values

Other attributes are the 1. the constructor ( `__init__` ) which ensures there is an input given to the object of the class when used

This input can either be gotten be typing in the string expression e.g.  *3+5/2* or user input:

An example of user input method is *commented*  on the later part of [calculator.py](./calculator.py) , You can uncomment the block and run the file standalone to see how user input works

### A few ithe attributes are:
* sanitizeString - this sanitizes the input to ensure that the right format is followed
    > Input Format is : 
    7+2/3  or   3*2+1

* bodmasConsistency - this helps to ensure the calculation is preformed inline with  BODMAS rule
* evaluateBasedOnOperator - This method separately does the actual mathematical calculations and feeds back to bodmasConsistency

# Error Handling

The algorithm made sure to return messages when user inputs what is not undersood. Throws user readable messages.

# Tests

You can run the [test.py](./test.py) file either through shell command (_python test.py_) or pressing the run button on the IDE to see the results of the example test in this file. The test uses the inbuilt [unittest](https://docs.python.org/3/library/unittest.html) to check the correctness of the algorithm
