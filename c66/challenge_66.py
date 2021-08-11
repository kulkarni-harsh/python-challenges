for i in range(int(input())):
    z=input()
    print(z.rfind("2020")==len(z)-4 or z.find("2020")==0 or (z.find("2")==0 and z.rfind("020")==len(z)-3) or (z.find("202")==0 and z.rfind("0")==len(z)-1)or (z.find("20")==0 and z.rfind("20")==len(z)-2) ) 
