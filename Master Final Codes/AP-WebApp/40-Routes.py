import os
import sys
import time


File = open("/lib/dhcpcd/dhcpcd-hooks/40-route","r")
R1=File.readline()
R2=File.readline()
R3=File.readline()
R4=File.readline()

row1=13
row2=13
row3=13
row4=13

i=0

Cl=[]
Cl_R1=[]
Cl_R2=[]
Cl_R3=[]
Cl_R4=[]


#Row_1
while(True):
	if(len(R1) != 1):
		if(len(R1) != 0):
			if(R1[row1] == '1'):
				while(True):
					if(R1[row1] != ' '):
						Cl_R1.append(R1[row1])
					else:
						break
					row1=row1+1
				break
		else:
			break
	else:
		break

i=row1+5
while(True):
	if(len(R1) != 1 and len(R1) != 0):
		if(R1[i] == '1'):
			while(True):
				if(R1[i] != '\n'):
					Cl.append(R1[i])
				else:
					break
				i=i+1
			break
		else:
			break
	else:
		break


#Row_2
while(True):
	if(len(R2) != 1 and len(R2) != 0):
		if(R2[row2] == '1'):
			while(True):
				if(R2[row2] != ' '):
					Cl_R2.append(R2[row2])
				else:
					break
				row2=row2+1
			break
		else:
			break
	else:
		break


#Row_3
while(True):
	if(len(R3) != 1 and len(R3) != 0):
		if(R3[row3] == '1'):
			while(True):
				if(R3[row3] != ' '):
					Cl_R3.append(R3[row3])
				else:
					break
				row3=row3+1
			break
		else:
			break
	else:
		break

#Row_4
while(True):
	if(len(R4) != 1 and len(R4) !=0):
		if(R4[row4] == '1'):
			while(True):
				if(R4[row4] != ' '):
					Cl_R4.append(R4[row4])
				else:
					break
				row4=row4+1
			break
		else:
			break
	else:
		break



Cl=''.join(Cl)
#print(Cl)


Cl_R1=''.join(Cl_R1)
#print(Cl_R1)
Cl_R2=''.join(Cl_R2)
#print(Cl_R2)
Cl_R3=''.join(Cl_R3)
#print(Cl_R3)
Cl_R4=''.join(Cl_R4)
#print(Cl_R4)


File.close()



File = open("/lib/dhcpcd/dhcpcd-hooks/Write-40-route","w+")
File.write(Cl + '\n')
File.write(Cl_R1 + '\n')
File.write(Cl_R2 + '\n')
File.write(Cl_R3 + '\n')
File.write(Cl_R4 + '\n')
File.close()
