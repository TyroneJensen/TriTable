#this program prints a pyramid of numbers

StartNum = 1 #declare variable, define first loop start number

while StartNum < 10: # Initiate first loop for any number less than 10
  NextNum = 1   #declare variable, define second loop start number
  for NextNum in range (1,10): #initiate and define range of second loop
    if (NextNum <= StartNum ): #if number in second loop less than start number
      print (StartNum*NextNum, end="\t")  #prints calculation and adds a tab indent
    else: 
      print (end= "\n") #inserts newline
      break #ends second loop and goes back to while loop and executes code again
    NextNum+=1 #increase counter in  for loop
  StartNum+=1#increase counter in while loop
 
