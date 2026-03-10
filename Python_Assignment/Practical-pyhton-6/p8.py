#  Practical Example 7: Write a Python program to calculate grades based on percentage using if-else ladder

percentage = int(input("Enter your percentage :- "))

if percentage >= 90 :
    print("You are A+ Garde")
elif percentage >= 80:
    print("You are A Garde")    
elif percentage >= 70:
    print("You are B Garde")
elif percentage >= 60:
    print("You are C Garde")        
elif percentage >= 50:
    print("You are D Garde")
elif percentage > 40:
    print("You are pass")    
else:
    print("You are fail ! ")

print("Your percentage is",percentage,"%")    


