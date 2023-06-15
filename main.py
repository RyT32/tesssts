# ctrl + /
# input -> "aabc"
# output ->  a - 2   b - 1 c - 1

#N**2
# N = len(data)
# def str_count(data):
#     for sym in data:# a b c d 
#         count = 0
#         for sym2 in data: # a b c d
#             if sym in sym2:
#                 count += 1
#         print(sym, count)


# str_count("aabcde")



#N*M
# N = len(data)   M - кол-во уникальных значений
# def str_count(data):
#     for sym in set(data):# a b c d 
#         count = 0
#         for sym2 in data: # a a  b c d
#             if sym in sym2:
#                 count += 1
#         print(sym, count)


# str_count("aabcd")



#N
# N = len(data)   

def str_count(data):
    sym_counter = {}
    for sym in data:# len(data)  
        sym_counter[sym] = sym_counter.get(sym,0)  + 1 
    
    print(sym_counter)


str_count("aabcd")


# https://github.com/ - зарегистрироваться 
# https://gitforwindows.org/ - скачать
# https://desktop.github.com/ - скачать


# 1 способ
# git init
# git add .
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/RyT32/tesssts.git
# git push -u origin main
















#dict

# famaly = {"dad":1}
# print(famaly)
# print(famaly['dad'])
# print(famaly.get('dad'))
# famaly['mom'] = 1 # add
# print(famaly)
# # famaly['child'] = 1 # add
# # print(famaly)
# famaly['child'] = famaly.get('child',0)  + 1  # update
# print(famaly)















# set - множество, неупорядоченный тип данных уникальных элементов


# z = set()
# y = {1,1,2,3}
# print(y)

# l = [1,1,2,2,3,4,5,5]
# s_l = set(l) # list -> set
# print(s_l)
# l = list(s_l)# set -> list

# str_s = set("привет")
# print(str_s)

# v = {}

# print(type(v))












