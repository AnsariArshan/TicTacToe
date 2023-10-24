import pygame
import random
from time import sleep
arr = [ [-1,-1,-1],
		[-1,-1,-1],
		[-1,-1,-1]
					]
choices = [0,1,2,3,4,5,6,7,8]
ch = random.randint(0,1)

run = True
sw = 600
sh = 600
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)




pygame.init()
pygame.display.set_caption('TIK TAK')
win = pygame.display.set_mode((sw,sh))
myFont = pygame.font.SysFont('comicsansms', 100)
textFont = pygame.font.SysFont('comicsansms', 70)
oText = myFont.render("O",True,black)
xText = myFont.render("X",True,black)
oWins = textFont.render("O wins",True,red)
xWins = textFont.render("X wins",True,red)
def O(x,y):
	win.blit(oText,(x,y))
def X(x,y):
	win.blit(xText,(x,y))

while run:
	win.fill(white)
	box0 = pygame.draw.rect(win, black, (0, 0, 200, 200), 1)
	box1 = pygame.draw.rect(win, black, (200, 0, 200, 200), 1)
	box2 = pygame.draw.rect(win, black, (400, 0, 200, 200), 1)
	box3 = pygame.draw.rect(win, black, (0, 200, 200, 200), 1)
	box4 = pygame.draw.rect(win, black, (200, 200, 200, 200), 1)
	box5 = pygame.draw.rect(win, black, (400, 200, 200, 200), 1)
	box6 = pygame.draw.rect(win, black, (0, 400, 200, 200), 1)	
	box7 = pygame.draw.rect(win, black, (200, 400, 200, 200), 1)
	box8 = pygame.draw.rect(win, black, (400, 400, 200, 200), 1)

	
	if ch == 0:
		place = random.choice(choices)
		i = place//3
		j = place%3
		if arr[i][j] == -1:
			arr[i][j] = "X"
		else:
			continue
		ch = 1
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		if ch == 1:
			if event.type == pygame.MOUSEBUTTONDOWN:
					if box0.collidepoint(event.pos):
						if arr[0][0] == -1:
							arr[0][0] = "O"
							choices.remove(0)
							ch = 0

			if event.type == pygame.MOUSEBUTTONDOWN:
					if box1.collidepoint(event.pos):
						if arr[1][0] == -1:
							arr[1][0] = "O"
							ch = 0

			if event.type == pygame.MOUSEBUTTONDOWN:
					if box2.collidepoint(event.pos):
						if arr[2][0] == -1:
							arr[2][0] = "O"
							ch = 0

			if event.type == pygame.MOUSEBUTTONDOWN:
					if box3.collidepoint(event.pos):
						if arr[0][1] == -1:
							arr[0][1] = "O"
							ch = 0

			if event.type == pygame.MOUSEBUTTONDOWN:
					if box4.collidepoint(event.pos):
						if arr[1][1] == -1:
							arr[1][1] = "O"
							ch = 0

			if event.type == pygame.MOUSEBUTTONDOWN:
					if box5.collidepoint(event.pos):
						if arr[2][1] == -1:
							arr[2][1] = "O"
							
							ch = 0

			if event.type == pygame.MOUSEBUTTONDOWN:
					if box6.collidepoint(event.pos):
						if arr[0][2] == -1:
							arr[0][2] = "O"
							
							ch = 0

			if event.type == pygame.MOUSEBUTTONDOWN:
					if box7.collidepoint(event.pos):
						if arr[1][2] == -1:
							arr[1][2] = "O"
							ch = 0

			if event.type == pygame.MOUSEBUTTONDOWN:
					if box8.collidepoint(event.pos):
						if arr[2][2] == -1:
							arr[2][2] = "O"
							ch = 0

	for i in range(3):
		for j in range(3):
			if arr[i][j] != -1:
				if arr[i][j] == "O":
					O(i*200+50,j*200+50) 
				elif arr[i][j] == "X":
					X(i*200+50,j*200+50)

	for i in range(3):
		if(arr[i][0]==arr[i][1] and arr[i][0]==arr[i][2] and arr[i][0]!=-1):
			if arr[i][0] == "O":
				win.blit(oWins,(250,250))
			else:
				win.blit(xWins,(250,250))
			choices =[]
			
			run = False

	for j in range(3):
		if(arr[0][j]==arr[1][j] and arr[0][j]==arr[2][j] and arr[0][j]!=-1):
			if arr[0][j] == "O":
				win.blit(oWins,(250,250))
			else:
				win.blit(xWins,(250,250))

			choices =[]
			
			run = False

	if(arr[0][0]==arr[1][1] and arr[0][0]==arr[2][2] and arr[0][0]!=-1):
			if arr[0][0] == "O":
				win.blit(oWins,(250,250))
			else:
				win.blit(xWins,(250,250))
			choices =[]
			run = False

	if(arr[2][0]==arr[1][1] and arr[2][0]==arr[0][2] and arr[2][0]!=-1):
			if arr[2][0] == "O":
				win.blit(oWins,(250,250))
			else:
				win.blit(xWins,(250,250))
			choices =[]
			run = False
	pygame.display.update()

