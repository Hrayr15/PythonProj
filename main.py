# def printValues():      #2
#     l = list()
#     for i in range(1, 21):
#         l.append(i ** 2)
#     print(l)
#
# printValues()

                        # 4
# poem = '''All that is gold does not glitter Not all those who wander are lost The old that is strong does not wither
# Deep roots are not reached by the frost From the ashes a fire shall be woken A light from the shadows shall spring Renewed shall be blade that was broken The crownless again shall be king'''
# #
# test_lst = (poem).split
# list1 = []
# for i in test_lst:
#     if i[0] in "aeiouAEIOU":
#       list1.append(i)
# print(list1)


# def make_chocolate(small, big, goal):     #5
#
#   total = 0
#
#   if goal < 5:
#     big = 0
#   for i in xrange(big):
#     total += 5
#     if total == goal:
#       return 0
#     elif total+5>goal:
#       break
#   for k in xrange(small):
#     total +=1
#     if total == goal:
#       return (k+1)
#
#   return -1

# def close_far(a, b, c):       #6
#   if abs(b-c) >= 2:
#     if (abs(a-b) <= 1 and abs(a-c) >= 2) or ( abs(a-c) <= 1 and abs(a-b) >=  2):
#         return True
#   return False
#
# lst = list(range(1, 101))
# # print(lst)
# # new_list
# filtered =  list(filter(lambda x: x % 10 == 7, lst))
# # new_list.append()
# print(lst(filtered))



# def sum(numbers):             #7 ??????
#     total = 0
#     for x in numbers:
#         while x != 13:
#             total += 1
#         if x == 13:
#     return total
# print(sum("1, 3, 31, 2, 3, 13, 48, 4 "))



# poww = lambda x: x**2            #8.1
# print(poww(int(input("Enter a number x!"))))

# poww1 = lambda r, pi=3.14: pi * r ** 2      #8.2
# print(poww1(int(input("Enter a number r!"))))

# poww2 = lambda x, y, p: (x + y) ** p   #8.3
# print(poww2(2, 8, 4))


# lst = list(range(0,101))            #9
# lst1 =list(filter(lambda x: x % 10 == 7, lst))
# print(lst1)








# def factorial(n):           #6
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# n = int(input("Input a number to compute the factiorial :"))
# print(factorial(n))


# def palindrome(s):         #4
#  if s == s[::-1]:
#     return(True)
#  else:
#     return(False)
# print(palindrome(input("enter any string!"))
