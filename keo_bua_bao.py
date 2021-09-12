import random
import os
print("0: kéo\n1: búa\n2: bao\n")
a = input("Bạn: ")
may = random.randint(0,2)
if may == 0:
	print("Máy: kéo\n")
elif may == 1:
	print("Máy: búa\n")
else: 
	print("Máy: bao\n")
if a == "keo" and may == 0 or a == "bua" and may == 1 or a == "bao" and  may == 2:
	print("Hoà\n")
elif a == "keo" and may == 1 or a == "bua" and may == 2 or a == "bao" and may == 0:
	print("Máy thắng")
elif a == "keo" and may == 2 or a == "bua" and may == 0 or a == "bao" and may == 1:
	print("Người thắng")
os.system("pause")
