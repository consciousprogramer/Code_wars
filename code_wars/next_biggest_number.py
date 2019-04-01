# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 07:29:35 2018

@author: RAVI SHANKAR SINGH
"""

# =============================================================================
# def next_bigger(n):
#     s = str(n)
#     def reverser(s): 
#         stri = "" 
#         for i in s: 
#             stri = i + stri
#         return stri
#     rev_s = reverser(s)
#     for i in range(1, len(rev_s)):
#         if rev_s[i] <= rev_s[i + 1]:
#             pass
#         else:
#             revs_ls = list(rev_s)
#             print(revs_ls)
#             x = revs_ls[i]
#             revs_ls[i] = revs_ls[i + 1]
#             revs_ls[i + 1] = x
#             revs_ls.reverse
#             final = "".join(revs_ls)
#             break
#     return final
# =============================================================================



# =============================================================================
# 
# def next_bigger(n):
#     s = str(n)
#     def reverser(s): 
#         stri = "" 
#         for i in s: 
#             stri = i + stri
#         return stri
#     for i in range(len(s) - 1, 0,-1):
#         x = s[i - 1]
#         y = s[i]
#         if s[i - 1] >= s[i]:
#             pass
#         else:
#            s1 = s[:i - 1]
#            s2 = s[i - 1:i + 1]
#            s22 = reverser(s2)
#            s3 = s[i + 1:len(s) - 1]
#            s33 = reverser(s3)
#            break
#     return s1 + s22 + s33
# print(next_bigger(34521))
# =============================================================================

#Shri Ravi shankar ji maharaj
# =============================================================================
# def zeroes (base, number):
#     L1=[]
#     div=6
#     while(div >= 5):
#         div=number//5
#         L1.append(div)
#         number=div
#     return sum(L1)
# 
# =============================================================================



def find(x, y):
    counter = 0
    n = 0
    for i in range(x,y+1):
        if i%2 == 0:
            counter += 1
        else:
            n += 1
    return counter, n
