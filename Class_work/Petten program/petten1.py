# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# for j in range(5):
#     for i in range(5):
#         print("*",end="")
#     print()    


# for i in range(5):
#     print("*"*5)

#---------------------------------------------------------------------------------

# *
# * *
# * * *
# * * * *
# * * * * * 


# for i in range(5):
#     for j in range(i+1):
#         print("*",end="")
#     print()    

# for i in range(5):
#     print("*"*(i+1))

#------------------------------------------------------------------------------------

# * * * * *
# * * * *
# * * *
# * *
# *


# for i in range(5,0,-1):
#     for j in range(i+1):
#         print("*",end="")
#     print( )    

# for i in range(5,0,-1):
#    print("*"*i,end="")
#    print()   

#--------------------------------------------------------------------------------------

#         *
#       * *
#     * * *
#   * * * *
# * * * * *

# for i in range(5):
#     for k in range(5-i):
#         print(" ",end="")
#     for j in range(i+1):
#         print(" *",end="")
#     print()    


#--------------------------------------------------------------------------------------


# * * * * *
#   * * * *
#     * * *
#       * *
#         *


# for i in range(5):
#     for k in range(i):
#         print("  ", end="") 
#     for j in range(5 - i):
#         print("* ", end="")
#     print()
    
#-------------------------------------------------------------------------------------


#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# for i in range(5):
#     for k in range(5-i):
#         print(" " ,end=" ")
#     for j in range(i+1):
#         print(" * ",end=" ")
#     print()   



# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# for i in range(5,0,-1):
#     for k in range(5-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print(" * ",end=" ")
#     print()        

#--------------------------------------------------------------------------------------------


#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *


# for i in range(5):
#     for k in range(4 - i):
#         print(" ", end="")
#     for j in range(i + 1):
#         print("* ", end="")
#     print()

# for i in range(4, 0, -1):
#     for k in range(5 - i):
#         print(" ", end="")
#     for j in range(i):
#         print("* ", end="")
#     print()


#----------------------------------------------------------------------------------------------

#      *
#     * *
#    *   *
#     * *
#      *


# lines = 8


# for i in range(lines):
#     for k in range(lines - i):
#         print(" ", end="")
#     for j in range(i + 1):
#         if j == 0 or j == i:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()

# for i in range(lines - 2, -1, -1):
#     for k in range(lines - i):
#         print(" ", end="")
#     for j in range(i + 1):
#         if j == 0 or j == i:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()


#---------------------------------------------------------------------------------------------



# 1
# 12
# 123
# 1234
# 12345


# for i in range(5):
#     for j in range(i+1):
#         print(j+1,end="")
#     print()    


#--------------------------------------------------------------------------------------------------

# 1
# 23
# 456
# 78910
# 1112131415

# for i in range(1,6):
#     for j in range(i):
#           print((i*(i-1))//2 + 1 + j,end="")  
#     print()    


#--------------------------------------------------------------------------------------------------


# 5
# 45
# 345
# 2345
# 12345

# for i in range(5,0,-1):
#     for j in range(i,6):
#         print(j,end="")
#     print()

#--------------------------------------------------------------------------------------------------

# 0
# 10
# 010
# 1010
# 01010

# for i in range(1,6):
#     for j in range(1,i+1):
#         print((i+j)%2,end="")
#     print()


#-------------------------------------------------------------------------------------------------    

# *****
#   *
#   * 
#   *
#   *

# for i in range(5):
#     if i == 0:
#         print('*' * 5)
#     else:
#         print('  *')


#-------------------------------------------------------------------------------------------------



# *   *
# *   *
# *****
# *   *
# *   *


# for i in range(5):
#     if i == 2:
#         print('*' * 5)
#     else:
#         print('*   *')


#-------------------------------------------------------------------------------------------------


# A
# BC 
# DEF 
# GHIJ
# KLMNO

# rows = 5
# ch = ord('A')  

# for i in range(1, rows + 1):
#     for j in range(i):
#         print(chr(ch), end='')
#         ch += 1
#     print()

#-------------------------------------------------------------------------------------------------


# *      *
# * *  * *
# *  *   *
# * *  * *
# *      *


# rows = 5
# cols = 7

# for i in range(rows):
#     for j in range(cols):
#         if j == 0 or j == cols - 1: 
#                 print('*', end='')
#         elif i == 1 or i == 3:
#             if j == 2 or j == 4:
#                 print('*', end='')
#             else:
#                 print(' ', end='')
#         elif i == 2 and j == 3:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()


#--------------------------------------------------------------------------------------------

#     *
# * * * *
#         *
# * * * *
#     *


# rows = 5
# cols = 9

# for i in range(rows):
#     for j in range(cols):
#         if i == 0 or i == 4:
#             print('*' if j == 4 else ' ', end='')
#         elif i == 1 or i == 3:
#             print('*' if j % 2 == 0 and j < 7 else ' ', end='')
#         elif i == 2:
#             print('*' if j == 8 else ' ', end='')
#     print()


#------------------------------------------------------------------------------------------------


#     *
#    * *
#   *   *
#   *****
#   *****
#   *****

# rows = 6

# for i in range(rows):
#     if i == 0:
#         print("    *")
#     elif i == 1:
#         print("   * *")
#     elif i == 2:
#         print("  *   *")
#     else:
#         print("  *****")
