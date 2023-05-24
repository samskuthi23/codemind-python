x,y,z=map(int,input().split())
if x>50 and y>60 and z>100:
    print("10")
elif x>50 and y>60:
    print("9")
elif y>60 and z>100:
    print("8")
elif x>50 and z>100:
    print("7")
elif x>50 or y>60 or z>100:
    print("6")
else:
    print("5")