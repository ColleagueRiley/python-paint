import pygame,pickle,PyZenity,easygui
class Screen():
	def __init__(self,width,heigth):
		self.width = width
		self.heigth = heigth
		self.display = pygame.display.set_mode([self.width,self.heigth])

class Dot():
	def __init__(self,x,y,radius,color):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
	def draw(self):
		self.sprite = pygame.draw.circle(screen.display,self.color,[self.x,self.y],self.radius)

def checkEvents():
	global state
	global states
	global dots
	global i
	global color
	global size
	global mode
	global running
	keys = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		deldots = []
		if pygame.mouse.get_pressed()[0]:
			mousex, mousey = pygame.mouse.get_pos()
			if mode == 1:
				dots[f'Dot{len(dots)+1}'] = Dot(mousex,mousey,size,color)
				states.insert(0,pickle.dumps(dots))
			elif mode == 2:
				for dot in dots:
					click = dots[dot].sprite.collidepoint([mousex,mousey])
					if click:
						deldots.append(dot)
			for dot in deldots:
				del dots[dot]
				states.insert(0,pickle.dumps(dots))
			deldots = []


		if keys[pygame.K_ESCAPE]:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:		
			if event.button == 4:
				size += 1
			elif event.button == 5:
				size -= 1
			elif pygame.mouse.get_pressed()[2]:
				if mode == 2:
					mode = 0
				mode += 1
		if keys[pygame.K_LCTRL] and keys[pygame.K_x]:
			i+=1
			if i == len(colors)-1:
				i = 0
			color = colors[i]
		if keys[pygame.K_LCTRL] and keys[pygame.K_c]:
			dots = {}
		if keys[pygame.K_LCTRL] and keys[pygame.K_s]:
			file = easygui.filesavebox(filetypes='*.pyp')
			if file != None:
				if file[-3] + file[-2] + file[-1] != 'pyp':
					file += '.pyp'
				pickle.dump(dots, open(file, "wb"))
		if keys[pygame.K_LCTRL] and keys[pygame.K_d]:
			file = easygui.fileopenbox(filetypes=['*.pyp'])
			if file != None:
				if file[-3] + file[-2] + file[-1] != 'pyp':
					Question = PyZenity.Warning("That is not compatible filetype, save files have to be '.pyp' please try again with a '.pyp' file.")
				else:
					dots = pickle.loads(open(file,'rb').read())
					states.insert(0,pickle.dumps(dots))
		if keys[pygame.K_LSHIFT] and keys[pygame.K_LCTRL] and keys[pygame.K_z]:
			if state-1 > 0:
				state -= 1
				dots = pickle.loads(states[state])
		elif not keys[pygame.K_LSHIFT] and keys[pygame.K_LCTRL] and keys[pygame.K_z]:
			if state+1 < len(states):
				state += 1
				dots = pickle.loads(states[state])

i=0
state = 0
colors = [[0,0,0],[255,255,255],[255,0,0],[0,255,0],[0,0,255],[255,251,0],[255,105,180],[255,69,0],[128,0,128]]
color = [0,0,0]
size = 25
mode = 1
dots = {}
states = [pickle.dumps(dots)]
def main():
	screen.display.fill([255,255,255])
	for dot in dots:
		dots[dot].draw()
	pygame.display.flip()
	checkEvents()



pygame.init()
screen = Screen(500,500)
running = True
while running:
	main()
pygame.quit()