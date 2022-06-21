import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3,venn3_circles,venn2_circles

chooseColor = 'skyblue'
notChooseColor= 'white'
checks = True 
venn3Index = ['100', '010', '110', '001', '101', '011', '111']
venn2Index = ['10','01','11']
aList3 = [i for i in venn3Index if i[0] == '1']
bList3 = [i for i in venn3Index if i[1] == '1']
cList3 = [i for i in venn3Index if i[2] == '1']

changeColorIndex = []
changeColorIndex2=[]
listFor2nd=[]
def vennOperators(A,operators,B):
	index1=''
	index2=''
	index3=''
	index4=''
	for area in ['01', '10', '11']:
		txt = v.get_label_by_id(area)
		if txt: txt.set_text('')
	if operators == 'AND':
		index1 = index2 = '11'
		index3 = '01'
		index4 = '10'
		vennName = A + ' ∩ ' + B
	elif operators == 'OR':
		index1 = '01'
		index2 = '10'
		index3 = index4 = '11'
		vennName = A + '∪ ' + B
	elif operators == "-":
		index1 = '10'
		index2 = '10'
		index3 = '11'
		index4 = '01'
		vennName = A + " - " + B
	v.get_patch_by_id(index3).set_color(notChooseColor)
	v.get_patch_by_id(index4).set_color(notChooseColor)
	#object color
	v.get_patch_by_id(index1).set_color(chooseColor)
	v.get_patch_by_id(index2).set_color(chooseColor)
	if operators == "AND":
		v.get_patch_by_id(index3).set_color(notChooseColor)
		v.get_patch_by_id(index4).set_color(notChooseColor)
	elif operators == 'OR':
		v.get_patch_by_id(index3).set_color(chooseColor)
		v.get_patch_by_id(index4).set_color(chooseColor)
	# changing background
	#plt.gca().set_axis_on()
	plt.gca().set_facecolor(notChooseColor)
	plt.title(vennName, fontsize=30)
	plt.show()
def notA(a):
	index1=''
	index2=''
	index3=''
	index4=''
	if a.isupper():
		c = venn2(subsets=(3,3,1))
		venn2_circles(subsets=(3,3,1))
		index1 = '01'
		index2 = '01'
		index3 = '11'
		index4 = '10'	
		# remove numbers
		for area in ['01', '10', '11']:
			txt = c.get_label_by_id(area)
			if txt: txt.set_text('')
		
		c.get_patch_by_id(index3).set_color(notChooseColor)
		c.get_patch_by_id(index4).set_color(notChooseColor)
		#object color
		c.get_patch_by_id(index1).set_color(chooseColor)
		c.get_patch_by_id(index2).set_color(chooseColor)

		# changing background
		plt.gca().set_axis_on()
		plt.gca().set_facecolor(chooseColor)
		plt.title("NOT A", fontsize=30)
		plt.show()
	return a
def notB(a):
	index1=''
	index2=''
	index3=''
	index4=''
	if a.isupper():
		v = venn2(subsets=(3,3,1))
		venn2_circles(subsets=(3,3,1))
		index1 = '10'
		index2 = '10'
		index3 = '11'
		index4 = '01'	
		# remove numbers
		for area in ['01', '10', '11']:
			txt = v.get_label_by_id(area)
			if txt: txt.set_text('')
		
		plt.gca().set_facecolor(chooseColor)
		v.get_patch_by_id(index3).set_color(notChooseColor)
		v.get_patch_by_id(index4).set_color(notChooseColor)
		#object color
		v.get_patch_by_id(index1).set_color(chooseColor)
		v.get_patch_by_id(index2).set_color(chooseColor)

		# changing background
		plt.gca().set_axis_on()
		plt.title("NOT B", fontsize=30)
		plt.show()
	return a
def not3(a):
	if a == 'A':
		changeColorIndex = [i for i in venn3Index if i[0] != '1']
	elif a == 'B':
		changeColorIndex = [i for i in venn3Index if i[1] != '1']
	elif a == 'C':
		changeColorIndex = [i for i in venn3Index if i[2] != '1']

	for i in changeColorIndex:
		v.get_patch_by_id(str(i)).set_color(chooseColor)
	for i in venn3Index:
		if i not in changeColorIndex: 
			v.get_patch_by_id(str(i)).set_color(notChooseColor)
	plt.gca().set_axis_on()
	plt.gca().set_facecolor(chooseColor)
	plt.title("NOT A", fontsize=30)
	plt.show()
def clearNum3(v):
	for area in venn3Index:
		txt = v.get_label_by_id(area)
		if txt: txt.set_text('') 

while( checks == True):
	print('Inerst operators:',end= ' ')
	ope = [i for i in input().split()]
	a = len(ope)
	if (a <= 3):
		#A, operators,B = input("Insert operator: ").split()
		if ope[1].upper() == 'AND': 
			v = venn2(subsets=(3, 3, 1))
			venn2_circles(subsets=(3,3,1))
			vennOperators(ope[0],ope[1].upper(),ope[2])
		elif ope[1].upper() == 'OR':
			v = venn2(subsets=(3, 3, 1))
			venn2_circles(subsets=(3,3,1))
			vennOperators(ope[0],ope[1].upper(),ope[2])
		elif ope[1] == '-':
			v = venn2(subsets=(3, 3, 1))
			venn2_circles(subsets=(3,3,1))
			vennOperators(ope[0],ope[1].upper(),ope[2])
		elif ope[1].upper() == 'C' or  ope[1].upper() == 'IN':
			v = venn2(subsets=(0, 6, 3))
			venn2_circles(subsets=(0,6,3))
			for area in ['01', '10', '11']:
				txt = v.get_label_by_id(area)
				if txt: txt.set_text('')
			plt.gca().set_axis_on()
			plt.show()
		elif ope[0].upper() == 'NOT':
			if ope[1].upper() == "A": 
				notA(ope[1].upper())
			elif ope[1].upper() == "B": 
				notB(ope[1].upper())

	elif a > 3:

		
		#ope = list(map(str, input().split()))
		
		print(ope)
		v = venn3(subsets=(1, 1, 1, 1, 1, 1, 1), set_labels = ('A', 'B', 'C'))
		venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1))
		clearNum3(v)
		if ope[2].upper() == 'B':
			if(ope[1].upper() == 'AND'):
				changeColorIndex = listFor2nd = list(set([i for i in venn3Index if (i[0] == '1' and i[1] == '1')]))
						
				for i in changeColorIndex:
					v.get_patch_by_id(str(i)).set_color(chooseColor)
				for i in venn3Index:
					if i not in changeColorIndex: 
						v.get_patch_by_id(str(i)).set_color(notChooseColor)
						
			elif(ope[1].upper() == 'OR'):
				for i in venn3Index:
					if i[0] =='1' or i[1] == '1': 
						listFor2nd.append(i)
						changeColorIndex.append(i)
				listFor2nd = changeColorIndex= list(set(listFor2nd))
				for i in changeColorIndex:
					v.get_patch_by_id(str(i)).set_color(chooseColor)
				for i in venn3Index:
					if i not in changeColorIndex: 
						v.get_patch_by_id(str(i)).set_color(notChooseColor)	
			elif(ope[1].upper() == '-'):
				for i in venn3Index:
					if i[0] =='1' and i[1] == '0': 
						listFor2nd.append(i)
						changeColorIndex.append(i)
				listFor2nd = changeColorIndex= list(set(listFor2nd))
				
				for i in changeColorIndex:
					v.get_patch_by_id(str(i)).set_color(chooseColor)
				for i in venn3Index:
					if i not in changeColorIndex: 
						v.get_patch_by_id(str(i)).set_color(notChooseColor)	
			if(ope[3].upper() == "AND"):
				for i in venn3Index:
					if i[2] == '1':
						for j in listFor2nd:
							if j[2] == i[2]:
								changeColorIndex2.append(j)
				print(changeColorIndex2)
				listFor2nd = changeColorIndex= list(set(listFor2nd))

				for i in changeColorIndex2:
					v.get_patch_by_id(str(i)).set_color(chooseColor)
				for i in venn3Index:
					if i not in changeColorIndex2: 
						v.get_patch_by_id(str(i)).set_color(notChooseColor)	
				plt.show()
			if(ope[3].upper() == "OR"):
				cList3 = [i for i in venn3Index if i[2] == '1']
				changeColorIndex2 = set(cList3).union(listFor2nd)
				print(changeColorIndex2)

				for i in changeColorIndex2:
					v.get_patch_by_id(str(i)).set_color(chooseColor)
				for i in venn3Index:
					if i not in changeColorIndex2: 
						v.get_patch_by_id(str(i)).set_color(notChooseColor)	
				plt.show()
			if(ope[3].upper() == "-"):
				changeColorIndex2 = list(set([i for i in listFor2nd if i[2] != '1']))
				print(changeColorIndex2)

				for i in changeColorIndex2:
					v.get_patch_by_id(str(i)).set_color(chooseColor)
				for i in venn3Index:
					if i not in changeColorIndex2: 
						v.get_patch_by_id(str(i)).set_color(notChooseColor)	
				plt.show()
		elif(ope[0].upper() == "NOT"):
			not3(ope[1].upper())
		
		
		
		elif (ope[2] == '(' or ope[-1] == ')'):
			if(ope[4].upper() == 'AND'):
				changeColorIndex = listFor2nd = list(set([i for i in venn3Index if (i[2] == '1' and i[1] == '1')]))
				for i in changeColorIndex:
					v.get_patch_by_id(str(i)).set_color(chooseColor)
				for i in venn3Index:
					if i not in changeColorIndex: 
						v.get_patch_by_id(str(i)).set_color(notChooseColor)	
			elif(ope[4].upper() == 'OR'):
				listFor2nd = changeColorIndex = list(set([i for i in venn3Index if i[2] =='1' or i[1] == '1' ]))
				for i in changeColorIndex:
					v.get_patch_by_id(str(i)).set_color(chooseColor)
				for i in venn3Index:
					if i not in changeColorIndex: 
						v.get_patch_by_id(str(i)).set_color(notChooseColor)
			elif(ope[4].upper() == '-'):
				listFor2nd = changeColorIndex = list(set([i for i in venn3Index if i[1] == '1' and i[2] == '0']))
				for i in changeColorIndex:
					v.get_patch_by_id(str(i)).set_color(chooseColor)
				for i in venn3Index:
					if i not in changeColorIndex: 
						v.get_patch_by_id(str(i)).set_color(notChooseColor)
			if(ope[1].upper() == "AND"):
				changeColorIndex2 = list(set([i for i in aList3 if i in listFor2nd]))
				print(changeColorIndex2)
				for i in changeColorIndex2:
					v.get_patch_by_id(str(i)).set_color(chooseColor)
				for i in venn3Index:
					if i not in changeColorIndex2: 
						v.get_patch_by_id(str(i)).set_color(notChooseColor)	
				plt.show()
			elif(ope[1].upper() == "OR"):
				changeColorIndex2 = set(aList3).union(listFor2nd)
				print(changeColorIndex2)
				for i in changeColorIndex2:
					v.get_patch_by_id(str(i)).set_color(chooseColor)
				for i in venn3Index:
					if i not in changeColorIndex2: 
						v.get_patch_by_id(str(i)).set_color(notChooseColor)	
				plt.show()
			elif(ope[1].upper() == "-"):
				changeColorIndex2 = [i for i in aList3 if i not in listFor2nd]
				print(changeColorIndex2)
				for i in changeColorIndex2:
					v.get_patch_by_id(str(i)).set_color(chooseColor)
				for i in venn3Index:
					if i not in changeColorIndex2: 
						v.get_patch_by_id(str(i)).set_color(notChooseColor)
				plt.show()
	plt.close()
	while(True):
		checkContinue  = input("Do you want to continue (yes/no)? ")
		if( checkContinue.upper() == "NO"):
			print("Finished program!")
			checks = False
			break
		elif ( checkContinue.upper() == "YES"):
			break