class calculator:
    print(
          '''
          Please note your operators: 
          *, +, -, /
          + : Addition
          - : Subtraction
          * : Multiplication
          / : Division
          These are the only valid operators
          
          ----------------------------------------------
          This program runs in 0.02ms

          Note: You can uncomment the last part of this document to test user input and the correctness of the algorithm
          '''
        )

    def __init__(self, readInputValue):
        #this input is the string mathematical expression from the user
        self.readInputValue = readInputValue

    def addition(self, initial, later):
        return float(initial) + float(later)

    def subtraction(self, first_number, second_number):
        return float(first_number) - float(second_number)

    def division(self, numerator, denominator):
        return float(numerator)/float(denominator)

    def multiply(self, first_number, second_number):
        return float(first_number) * float(second_number)

        
    # def checkIfNumber(number):
    #   if(isinstance(number, (int, float))):
    #     return True;
    #   return False


    #Examining input and Making Sure the input data is valid  
    def sanitizeString(self):
      getInputExpression = self.readInputValue
      operators = ["-", "+", "*", "/"]

      #this empty list would contain all input reads, separate the operates from operators individually in a list.
      sanitizedHashObject = []

      #temporary variable to store each operand before pushing to list, gets re-initialized to default after every push
      holdNumberStrings = ""

      #loop through the each string and separate them into individual operands and operator and save in a list
      for i in range(len(getInputExpression)):
        if getInputExpression[i] not in operators:
          holdNumberStrings += getInputExpression[i]
          print(holdNumberStrings)
          if(holdNumberStrings.isnumeric()):
            if i == len(getInputExpression) - 1:
              sanitizedHashObject.append(holdNumberStrings)
          else:
            return print("Invalid input")
                
        elif getInputExpression[i] in operators: 
          try:
            theNumbervalue = float(holdNumberStrings)
            if(isinstance(theNumbervalue, (int, float))):
              sanitizedHashObject.append(holdNumberStrings)
              holdNumberStrings = ""
            else:
              return print("Invalid input, check your input for float or int and try again")
              break
          except ValueError: 
            return print("Invalid input, please check and try again")
            break
              
            
          if i != 0  and getInputExpression[i-1] not in operators:
            sanitizedHashObject.append(getInputExpression[i])
          else:
            return print("Invalid Input")
            break
              

      #print(sanitizedHashObject) 
      return sanitizedHashObject

    #performing Calculation in line with bodmas principle 
    def bodmasConsistency(self, sanitizedHashObject):

      #A dictionary to store the bodmas structure - this would be used to check the sequence of operations
      bodmasStructure = {"Division":"/", "Multiplication":"*", "Addition":"+", "Subtraction":"-"}
      
      calculate = 0

      #loop through the sanitized input elements and pop out calculated operations until it is left with one element
      try:
        while len(sanitizedHashObject) > 1:
          if bodmasStructure.get('Division') in sanitizedHashObject:
            i = 0
            #ensuring all occurences of division is handled first
            while i < sanitizedHashObject.count(bodmasStructure.get('Division')):
              calculate += self.evaluateBasedOnOperator(sanitizedHashObject, bodmasStructure, "Division")
              i += 1
            
          elif bodmasStructure.get('Multiplication') in sanitizedHashObject:
            i = 0
            #ensuring all occurences of multiplication is handled here
            while i < sanitizedHashObject.count(bodmasStructure.get('Multiplication')):
              calculate += self.evaluateBasedOnOperator(sanitizedHashObject, bodmasStructure, "Multiplication")
              i += 1
              
          elif bodmasStructure.get('Addition') in sanitizedHashObject: 
            i = 0 
            #ensuring all occurences of addition is handled here
            while i < sanitizedHashObject.count(bodmasStructure.get('Addition')):
              calculate += self.evaluateBasedOnOperator(sanitizedHashObject, bodmasStructure, "Addition")
              i += 1

          elif bodmasStructure.get('Subtraction') in sanitizedHashObject: 
            i = 0
            #ensuring all occurences of addition is handled
            while i < sanitizedHashObject.count(bodmasStructure.get('Subtraction')): 
              calculate += self.evaluateBasedOnOperator(sanitizedHashObject, bodmasStructure, "Subtraction")
              i += 1
        print("Ans:-----------")      
        print(sanitizedHashObject[0])
        return sanitizedHashObject[0]
    
      except TypeError:
        return print("A fatal error occured previously")

    #do the actual calculation depending on which operation we are doing during the loop
    def evaluateBasedOnOperator(self, sanitisedArray, bodmasStructure, operation):

      #Getting the positin of the operand in the list and checking the opreands next to it
      position = sanitisedArray.index(bodmasStructure.get(operation))
      result = 0
      leftOperand = sanitisedArray[position-1]
      rightOperand = sanitisedArray[position+1]
      operator = sanitisedArray[position]

      if operation == "Division":
        result = self.division(leftOperand, rightOperand)
        
      elif operation == "Multiplication":
        result = self.multiply(leftOperand, rightOperand)
        
      elif operation == "Addition":
        result = self.addition(leftOperand, rightOperand)
        
      elif operation == "Subtraction":    
        result = self.subtraction(leftOperand, rightOperand)

      #Decongesting our sanitized List(Array) by removing evaluated expresions and adding the evaluated value to the array. so that we have the important operators and operands per time

      sanitisedArray.remove(leftOperand)
      sanitisedArray.remove(operator)
      sanitisedArray.remove(rightOperand)
      sanitisedArray.append(result) 

      #print(sanitisedArray)  
      return result  

#The block below can be uncommented to test this file alone 
newcalculator = calculator(input("Enter your math expression e.g. 7+3+4 :"))
evaluteSanitizedInput = newcalculator.sanitizeString()
newcalculator.bodmasConsistency(evaluteSanitizedInput)




