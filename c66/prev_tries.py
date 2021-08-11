
# Try1
# for i in range(int(input())):
#     z=input()
#     print(z.rfind("2020")==len(z)-4 or z.find("2020")==0 or (z.find("2")==0 and z.rfind("020")==len(z)-3) or (z.find("202")==0 and z.rfind("0")==len(z)-1)or (z.find("20")==0 and z.rfind("20")==len(z)-2) ) 


#consecutive tries
for i in range(int(input())):
    z=input()
    a=len(z)
    b="2020"

    # print(z.rfind("2020")==len(z)-4 or z.find("2020")==0 or (z.find("2")==0 and z.rfind("020")==len(z)-3) or (z.find("202")==0 and z.rfind("0")==len(z)-1)or (z.find("20")==0 and z.rfind("20")==len(z)-2) ) 
    # print([False,[[[[False,True][z[:2]==z[-1:-3]=="20"],True][z[:3]=='202'and z[-1]=='0'],True][z[0]=="2"and z[-1:-4]=='020'],True][z[:4]==b or z[-1:-5]==b]][a>3])
    # print([False,[[[[False,True][z[:2]=="20"and z[-1:-3:-1]=="02"],True][z[:3]=='202'and z[-1]=='0'],True][z[0]=="2"and z[-1:-4:-1]=='020'],True][z[:4]==b or z[-1:-5:-1]=="0202"]][a>3])
    