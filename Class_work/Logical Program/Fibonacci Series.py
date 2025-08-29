
# example for Fibonacci Series

#for loop

fibonacci = int(input("Please enter your number: "))
temp = 0
pr = 0
pe = 1
for i in range(fibonacci):
  temp = pr + pe       
  pr = pe             
  pe = temp 

  print(temp ,"Fibonacci Series ")



