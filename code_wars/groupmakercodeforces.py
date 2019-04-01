# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 06:30:21 2019

@author: RAVI SHANKAR SINGH
"""

def GCD(x, y): 
   while(y): 
       x, y = y, x % y 
   return x 

for i in range(int(input())):
    total = int(input())
    lsp = input().split()
    lsg = input().split()
    gpcount = 0
    singlegpls = []
    while len(lsp) != 1:
        gender = lsg[0]
        k = 0
        while len(lsp) != 0:
            k += 1
            if GCD(int(lsp[0]), int(lsp[k])) != 1:
                if gender != lsg[k]:
                    gpcount += 1
                    lsp.remove(lsp[0])
                    lsp.remove(lsp[k - 1])
                    lsg.remove(lsg[0])
                    lsg.remove(lsg[k - 1])
                    break
                else:
                    singlegpls.append(lsp[0])
                    singlegpls.append(lsp[k])
                    lsp.remove(lsp[0])
                    lsp.remove(lsp[k - 1])
                    lsg.remove(lsg[0])
                    lsg.remove(lsg[k - 1])
                    break
    print(gpcount + len(singlegpls) + 1)





# =============================================================================
# def GCD(x, y): 
#    while(y): 
#        x, y = y, x % y 
#    return x 
# 
# for i in range(1):#int(input("times: "))):
#     lsp = [5,6,7,10,21] #input("lsp: ").split()
#     lsg = ["F","F","F","M",""]#input("lsg: ").split()
#     gpcount = 0
#     singlegpls = []
#     while len(lsp) != 1:
#         gender = lsg[0]
#         k = 0
#         while len(lsp) != 0:
#             k += 1
#             x = lsp[0]
#             y = lsp[k]
#             if GCD(int(lsp[0]), int(lsp[k])) != 1:
#                 if gender != lsg[k]:
#                     gpcount += 1
#                     lsp.remove(lsp[0])
#                     lsp.remove(lsp[k - 1])
#                     lsg.remove(lsg[0])
#                     lsg.remove(lsg[k - 1])
#                     break
#                 else:
#                     singlegpls.append(lsp[0])
#                     singlegpls.append(lsp[k])
#                     lsp.remove(lsp[0])
#                     lsp.remove(lsp[k - 1])
#                     lsg.remove(lsg[0])
#                     lsg.remove(lsg[k - 1])
#                     break
#     print(gpcount + len(singlegpls) + len(lsp),":Groups can be formed")
# =============================================================================





# =============================================================================
# def GCD(x, y): 
#   
#    while(y): 
#        x, y = y, x % y 
#   
#    return x 
# 
# for i in range(int(input("times: "))):
#     lsp = input("lsp: ").split()
#     lsg = input("lsg: ").split()
#     gpcount = 0
#     i = 0
#     singlegpls = []
#     while len(lsp) != 0:
#         gender = lsg[i]
#         for k in range(1,len(lsp)):
#             x = lsp[i]
#             y = lsp[k]
#             if GCD(int(lsp[i]), int(lsp[k])) != 1:
#                 if gender != lsg[k]:
#                     gpcount += 1
#                     lsp.remove(lsp[i])
#                     lsp.remove(lsp[k])
#                     lsg.remove(lsp[i])
#                     lsg.remove(lsp[k])
#                     break
#                 else:
#                     singlegpls.append(lsp[i])
#                     singlegpls.append(lsp[k])
#                     lsp.remove(lsp[i])
#                     lsp.remove(lsp[k])
#                     lsg.remove(lsp[i])
#                     lsg.remove(lsp[k])
#                     break
#     print(gpcount + len(singlegpls))
# =============================================================================
