# for i in range(int(input())):
#     a=input().split()
#     for b in a:
#         if all(map(lambda x: x in "0123456789ABCDEF",''.join(b.split('-')))):print(b)


# for i in range(int(input())):print(''.join([b if all(map(lambda x: x in "0123456789ABCDEF",list(b.replace("-",''))))else ''for b in input().split() ]))

# for i in range(int(input())):
#     for j in input().split():
#         try:int(j.replace('-',''),16);print(j)
#         except:0

# for i in [z:=input]*int(z()):print(*filter(lambda j:set(j).issubset(set('0123456789ABCDEF-')),z().split()))

# for i in [z:=input]*int(z()):print(''.join(j*+set(j).issubset(set('0123456789ABCDEF-'))for j in z().split()))


# for i in [z:=input]*int(z()):
#     for j in z().split():
#         if max(j)<"G":
#             print(j)

# for i in[z:=input]*int(z()):print(''.join(j*+(max(j)<"G")for j in z().split()))



# for i in[z:=input]*int(z()):print(*filter(lambda x:max(x)<"G",z().split()))

# for i in"G"*int(input()):print(*filter(lambda x:max(x)<i,input().split()))







