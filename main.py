from PIL import Image, ImageDraw 
from random import randint 
import re

def decrypt():
	
	a = []						    
	keys = []
	img = Image.open(input("path to image: "))				
	pix = img.load()
	f = open(input('path to keys: '),'r')
	y = str([line.strip() for line in f])				
															
	for i in range(len(re.findall(r'\((\d+)\,',y))):
		keys.append((int(re.findall(r'\((\d+)\,',y)[i]),int(re.findall(r'\,\s(\d+)\)',y)[i]))) 	
	for key in keys:
		a.append(pix[tuple(key)][0])							
	return ''.join([chr(elem) for elem in a])	

def encrypt():	
	
	keys = [] 					
	img = Image.open(input("path to image: ")) 	
	draw = ImageDraw.Draw(img)	   		
	width = img.size[0]  		   		
	height = img.size[1]		   		
	pix = img.load()				
	f = open('keys.txt','w')			

	for elem in ([ord(elem) for elem in input("text here: ")]):
		key = (randint(1,width-10),randint(1,height-10))		
		g, b = pix[key][1:3]
		draw.point(key, (elem,g , b))														
		f.write(str(key)+'\n')								
	
	print('keys were written to the keys.txt file')
	img.save("newimage.png", "PNG")
	f.close()


task = input("Select task: Encrypt/Decrypt(E/D)?")
if task == 'E' or task == 'e':
	encrypt()
elif task =='D' or task == 'd':
	print("you message: ",decrypt())
else:
	print("wrong task!")
