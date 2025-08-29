# *****
# *****
# *****
# *****
# *****


# lines = 5
# for i in range(1, lines + 1):       
#     for j in range(1, lines + 1):    
#         print("*", end="")           
#     print()                          

# -------------------------------------------------------------



# *
# **
# ***
# ****
# *****



# lines = 5
# startcount = 1
# for i in range(1,lines+1):
#     for j in range(1,startcount+1):
#         print("*",end="")
#     print()
#     startcount+=1

#----------------------------------------------------------------


# *****
# ****
# ***
# **
# *

# lines = 5
# startcount = lines
# for i in range(1,lines+1):
#     for j in range(1,startcount+1):
#         print("*",end="")
#     print()
#     startcount-=1

#-----------------------------------------------------------------

#     *
#    **
#   ***
#  ****
# *****

# lines = 5
# startcount = 1
# spacecount=lines
# for i in range(1,lines+1):
#     for k in range(1,spacecount):
#         print(" ",end="")
#     for j in range(1,startcount+1):
#         print("*",end="")
#     print()
#     startcount+=1
#     spacecount-=1

#---------------------------------------------------------------------


# *****
#  ****
#   ***
#    **
#     *


# lines = 5
# startcount = lines
# spacecount=0
# for i in range(1,lines+1):
#     for k in range(1,spacecount+1):
#         print(" ",end="")
#     for j in range(1,startcount+1):
#         print("*",end="")
#     print()
#     startcount-=1
#     spacecount+=1

#--------------------------------------------------------------------

#    *
#   * *
#  * * *
# * * * *


# lines = 5
# startcount = 1
# spacecount=lines
# for i in range(1,lines+1):
#     for k in range(1,spacecount):
#         print(" ",end="")
#     for j in range(1,startcount+1):
#         print("* ",end="")
#     print()
#     startcount+=1
#     spacecount-=1


#--------------------------------------------------------------------

#    *
#   ***
#  *****
# *******


# lines = 5
# startcount = 1
# spacecount=lines
# for i in range(1,lines+1):
#     for k in range(1,spacecount):
#         print(" ",end="")
#     for j in range(1,startcount+1):
#         print("*",end="")
#     print()
#     startcount+=2
#     spacecount-=1


#--------------------------------------------------------------------

#    *
#   * *
#  * * *
#   * *
#    *


# lines = 15
# startcount = 1
# spacecount=lines
# mid = (lines//2)+1
# for i in range(1,lines+1):
#     for k in range(1,spacecount):
#         print(" ",end="")
#     for j in range(1,startcount+1):
#         print("*",end="")
#     print()
#     if i<mid :
#         startcount+=2
#         spacecount-=1
#     else :
#         startcount-=2
#         spacecount+=1
        
#---------------------------------------------------------------------------

#               *
#              * *
#             *   *
#            *     *
#           *       *
#          *         *
#         *           *
#        *             *
#         *           *
#          *         *
#           *       *
#            *     *
#             *   *
#              * *
#               *

# lines = 15
# startcount = 1
# spacecount=lines
# mid = (lines//2)+1
# for i in range(1,lines+1):
#     for k in range(1,spacecount):
#         print(" ",end="")
#     for j in range(1,startcount+1):
#         if j==1 or j==startcount:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
#     if i<mid :
#         startcount+=2
#         spacecount-=1
#     else :
#         startcount-=2
#         spacecount+=1

#--------------------------------------------------------------------------

# *   *
# ** **
# * * *
# ** **
# *   *



# lines = 5
# for i in range(1,lines+1):
#     for j in range(1,lines+1):
#         if j==1 or j==lines or j==i or j==lines+1-i:
#             print("*",end="")
#         else :
#             print(" ",end="")
#     print()

#--------------------------------------------------------------------------

# A
# BC
# DEF
# GHIJ
# KLMNO



# lines = 5
# startcount = 1
# char = 'A'
# for i in range(1,lines+1):
#     for j in range(1,startcount+1):
#         print(char,end="")
#         char =  chr(ord(char)+1)   
#     print()
#     startcount+=1