#create game connect4
#each player has n discs

import os
import time


fh=open("rules.txt","r")
for line in fh.readlines():
	line=line.strip()
	print(line)
	time.sleep(1.5)

class bigger(Exception):
	def __init__(self,str):
		self.str=str

def star():
	for i in range(n):							#empty matrix with *
		m.append([])
		for j in range(n):
			m[i].append('*')


def display():
	print(" ",end=" ")
	for k in range(1,n+1):
		print(k,end=" ")
	print()
	for i in range(n):
		print(i+1,end=" ")
		for j in range(n):
			print(m[i][j],end=" ")
		print()


def enter(i):
	global ctr
	if(i%2==0):
		print("PLAYER 1's(R) turn")
	else:
		print("PLAYER 2's(Y) turn")
	x,y=input("Enter coordinates").split(" ")
	x,y=int(x),int(y)
	try:
		if(x>=n+1 or y>=n+1):
			ctr+=1
			raise bigger("Invalid Coordinates!! You miss a chance!!")
		elif(x<n+1 and y<n+1 and m[x-1][y-1]=="*"):
				if(i%2==0):
					m[x-1][y-1]="R"
				else:
					m[x-1][y-1]="Y"
		elif(m[x-1][y-1]!="*"):
			print("ALREADY TAKEN, YOU MISS A CHANCE!!")
			ctr+=1
		
	except bigger as error:
		print(error)


def rowcheck():								#checks all rows
	flag=0
	for i in range(n):
		for j in range(n-3):
			if(m[i][j]==m[i][j+1]==m[i][j+2]==m[i][j+3]=='R'):
					flag=1
			if(m[i][j]==m[i][j+1]==m[i][j+2]==m[i][j+3]=='Y'):
					flag=2
	if(flag==1):
		return('R ie PLAYER 1 WINS!!!')
	elif(flag==2):
		return('Y ie PLAYER 2 WINS!!!')


def columncheck():							#checks all columns
	flag=0
	for j in range(n):
		for i in range(n-3):
			if(m[i][j]==m[i+1][j]==m[i+2][j]==m[i+3][j]=='R'):
					flag=1
			if(m[i][j]==m[i+1][j]==m[i+2][j]==m[i+3][j]=='Y'):
					flag=2
	if(flag==1):
		return('R ie PLAYER 1 WINS!!!')
	elif(flag==2):
		return('Y ie PLAYER 2 WINS!!!')



def rdiagonalcheck():						#diagonals from top right to bottom left
	flag=0
	for i in range(3,n):
		for j in range(n-3):
			if(m[i][j]==m[i-1][j+1]==m[i-2][j+2]==m[i-3][j+3]=='R'):
					flag=1
			if(m[i][j]==m[i-1][j+1]==m[i-2][j+2]==m[i-3][j+3]=='Y'):
					flag=2
	if(flag==1):
		return('R ie PLAYER 1 WINS!!!')
	elif(flag==2):
		return('Y ie PLAYER 2 WINS!!!')



def ldiagonalcheck():						#diagonals from top left to bottom right
	flag=0
	for i in range(n-3):
		for j in range(n-3):
			if(m[i][j]==m[i+1][j+1]==m[i+2][j+2]==m[i+3][j+3]=='R'):
					flag=1
			if(m[i][j]==m[i+1][j+1]==m[i+2][j+2]==m[i+3][j+3]=='Y'):
					flag=2
	if(flag==1):
		return('R ie PLAYER 1 WINS!!!')
	elif(flag==2):
		return('Y ie PLAYER 2 WINS!!!')







ch='Y'
ctr=0
while(ch=='Y'):
	n=int(input("Enter the matrix size you wish to play (min size:4)"))
	m=[]
	star()
	flag=0;i=0
	while(i in range(n*n+ctr) and flag==0):
		display()
		enter(i)
		time.sleep(0.5)
		os.system("cls")
		if(rowcheck()):
			print(rowcheck())
			flag=1
		elif(columncheck()):
			print(columncheck())
			flag=1
		elif(rdiagonalcheck()):
			print(rdiagonalcheck())
			flag=1
		elif(ldiagonalcheck()):
			print(ldiagonalcheck())
			flag=1
		i+=1
	if(flag==0):
		print("DRAW!!!!!")
	print("Wish to play again???")
	ch=input("Y/N ").upper()




