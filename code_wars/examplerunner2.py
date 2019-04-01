import time
def GCD(x, y):
# =============================================================================
#     def primechecker(n):
#         def checkby2(n):
#             if n%2 == 0:
#                 if n == 2:
#                     return True
#                 return False
#         if n == 1:
#             return False
#         if checkby2(n) == False:
#             return False
#         for k in range(3, round(n**(0.5)) + 2,2):
#             if n % k == 0:
#                 return False
#             break
#         return True
# =============================================================================
    
# =============================================================================
#     def lcm (x, y):
#         if (primechecker(x) or primechecker(y)) == True:
#             return x * y
#         
#         i = 1
#         factors1 = []
#         factors2 = []
#         while x != 1:
#             i += 1
#             if x % i == 0:
#                 x = x//i
#                 factors1.append(i)
#                 i = 1
#         
#         while y != 1:
#             i += 1
#             if y % i == 0:
#                 y = y//i
#                 factors2.append(i)
#                 i = 1                
#         mult_sum = 1
#         factors = []
#         for n in factors1[:]:
#             if n in factors2:
#                 factors.append(n)
#                 factors1.remove(n)
#                 factors2.remove(n)
#             else:
#                 factors.append(n)
#                 
#         for k in factors:
#             mult_sum *= k
#         for k in factors2:
#             mult_sum *= k
#         return mult_sum
#     
#     return x*y/lcm(x,y)
# =============================================================================
    
    while(y): 
       x, y = y, x % y 
    return x 
        
def primechecker(n):
    def checkby2(n):
        if n%2 == 0:
            if n == 2:
                return "It's Prime"
            return "Not Prime"
    if n == 1:
        return "Not Prime"
    if checkby2(n) == "Not Prime":
        return "Not Prime"
    else:
        for k in range(3, round(n**(0.5)) +1 ,2):
            if n % k == 0:
                return "Not Prime"
                break
        return "It's Prime"


def prime_gentor(n):
    primecount = 0
    i = 3
    prime_ls = []
    while primecount <= n:
        if primechecker(i) == "It's Prime":
            prime_ls.append(i)
            primecount += 1
        i += 1
    return prime_ls

def multby4(n):
    return n*2


x = prime_gentor(5000)
feed_ls = list(map(multby4, x))
final_ls = x[:] + feed_ls[:]
cpfinal_ls = final_ls[:]
count = 0
i = 0
st = time.time()
while i < len(cpfinal_ls):
    first = cpfinal_ls[0]
    k = i+1
    while k < len(cpfinal_ls):
        second = cpfinal_ls[k]
        if GCD(first, second) > 1:
            count += 1
            break
        k+=1
    i += 1       

print(time.time() - st)
print(count)

#import time

# =============================================================================
# def primechecker(n):
#     def checkby2(n):
#         if n%2 == 0:
#             if n == 2:
#                 return True
#             return False
#     if n == 1:
#         return False
#     if checkby2(n) == False:
#         return False
#     for k in range(3, round(n**(0.5)) + 2,2):
#         if n % k == 0:
#             return False
#         break
#     return True
# 
# def lcm (x, y):
#     if (primechecker(x) or primechecker(y)) == True:
#         return x * y
#     
#     i = 1
#     factors1 = []
#     factors2 = []
#     while x != 1:
#         i += 1
#         if x % i == 0:
#             x = x//i
#             factors1.append(i)
#             i = 1
#     
#     while y != 1:
#         i += 1
#         if y % i == 0:
#             y = y//i
#             factors2.append(i)
#             i = 1                
#     mult_sum = 1
#     factors = []
#     for n in factors1[:]:
#         if n in factors2:
#             factors.append(n)
#             factors1.remove(n)
#             factors2.remove(n)
#         else:
#             factors.append(n)
#             
#     for k in factors:
#         mult_sum *= k
#     for k in factors2:
#         mult_sum *= k
#     return mult_sum
# 
# st = time.time()
# print(lcm(6,21))
# print(time.time() - st)
# 
# =============================================================================
