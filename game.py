import pygame
import time

from pygame.locals import*
from time import sleep

class Sprite():
	def __init__(self, x1, y1, w1, h1, image_url):
		self.x = x1
		self.y = y1
		self.w = w1
		self.h = h1
		self.leftSide = self.x
		self.rightSide = self.x + self.w
		self.top = self.y
		self.bottom = self.y + self.h
		self.roomXPos = 0
		self.roomYPos = 0
		self.isValid = True
		self.image = pygame.image.load(image_url)
		
class Link(Sprite):
		def __init__(self, x1, y1, w1, h1, image_url):
			Sprite.__init__(self, x1, y1, w1, h1, image_url)
			self.speed = 9
			self.imageNumb = 0
			self.isMovingRight = bool(False)
			self.isMovingLeft = bool(False)
			self.isMovingUp = bool(False)
			self.isMovingDown = bool(False)
			self.isFacingRight = bool(False)
			self.isFacingLeft = bool(False)
			self.isFacingUp = bool(False)
			self.isFacingDown = bool(False)

			self.linkRight = []
			self.linkLeft = []
			self.linkUp = []
			self.linkDown = []

			self.imageNames = ["link0.png", "link1.png", "link2.png", "link3.png", "link4.png", "link5.png", "link6.png", "link7.png", "link8.png", "link9.png", "link10.png", "link11.png", "link12.png", "link13.png", "link14.png", "link15.png", "link16.png", "link17.png", "link18.png", "link19.png", "link20.png", "link21.png", "link22.png", "link23.png", "link24.png","link25.png", "link26.png", "link27.png", "link28.png", "link29.png", "link30.png", "link31.png", "link32.png", "link33.png", "link34.png", "link35.png", "link36.png", "link37.png", "link38.png", "link39.png", "link40.png", "link41.png", "link42.png", "link43.png", "link44.png", "link45.png", "link46.png", "link47.png", "link48.png"]

			for i in range(49):
				img = pygame.image.load(self.imageNames[i])
				if i < 13:
					self.linkDown.append(img)
				if i >= 13 and i <= 24: 
					self.linkLeft.append(img)
				if i >= 25 and i <= 37:
					self.linkRight.append(img)
				if i >= 38 and i <= 48:
					self.linkUp.append(img)
		
		def update(self):
			self.top = self.y
			self.bottom = self.y + self.h
			self.rightSide = self.x + self.w
			self.leftSide = self.x

			if bool(self.isMovingRight):
				#Restarts iteration over array with images
				if self.imageNumb >= len(self.linkRight):
					self.imageNumb = 0

				#Loads images
				self.image = self.linkRight[self.imageNumb]

				#Sets variables for next take on this branch
				self.imageNumb = self.imageNumb + 1
				self.isMovingRight = bool(False)

				self.isFacingRight = bool(True)
				self.isFacingLeft = bool(False)
				self.isFacingUp = bool(False)
				self.isFacingDown = bool(False)	
			
			if bool(self.isMovingLeft):

				if self.imageNumb >= len(self.linkLeft):
					self.imageNumb = 0

				self.image = self.linkLeft[self.imageNumb]

				self.imageNumb = self.imageNumb + 1
				self.isMovingLeft = bool(False)

				self.isFacingRight = bool(False)
				self.isFacingLeft = bool(True)
				self.isFacingUp = bool(False)
				self.isFacingDown = bool(False)

			if bool(self.isMovingDown):

				if self.imageNumb >= len(self.linkDown):
					self.imageNumb = 0

				self.image = self.linkDown[self.imageNumb]
				self.imageNumb = self.imageNumb + 1
				self.isMovingDown = bool(False)

				self.isFacingRight = bool(False)
				self.isFacingLeft = bool(False)
				self.isFacingUp = bool(False)
				self.isFacingDown = bool(True)

			if bool(self.isMovingUp):

				if self.imageNumb >= len(self.linkUp):
					self.imageNumb = 0

				self.image = self.linkUp[self.imageNumb];
				self.imageNumb = self.imageNumb + 1

				self.isMovingUp = bool(False)

				self.isFacingRight = bool(False)
				self.isFacingLeft = bool(False)
				self.isFacingUp = bool(True)
				self.isFacingDown = bool(False)

		def setPrevPos(self):
			self.prevX = self.x
			self.prevY = self.y

		def getOut(self, sprite):
			#up
			if self.y + self.h >= sprite.y and self.prevY + self.h <= sprite.y :
				self.y = sprite.y - self.h
			
			#down
			if self.y <= sprite.y + sprite.h and self.prevY >= sprite.y + sprite.h :
				self.y = sprite.y + sprite.h
				
			#right
			if self.x + self.w >= sprite.x and self.prevX + self.w <= sprite.x :
				self.x = sprite.x - self.w
				
			#left
			if self.x <= sprite.x + sprite.w and self.prevX >= sprite.x + sprite.w :
				self.x = sprite.x + sprite.w

		def draw(self, screen, x, y):
			screen.blit(self.image ,(x, y))
			pygame.display.flip

class Tile(Sprite):
	def __init__(self, x1, y1, w1, h1, image_url):
			Sprite.__init__(self, x1, y1, w1, h1, image_url)

	def update(self):
		pass

	def draw(self, screen, x, y):
		screen.blit(self.image ,(x, y))
		pygame.display.flip

class Boomerang(Sprite):
	def __init__(self, x1, y1, w1, h1, image_url):
		Sprite.__init__(self, x1, y1, w1, h1, image_url)
		self.xDirection = 0
		self.yDirection = 0
		self.speed = 10
	
	def update(self):
		self.x += self.xDirection * self.speed
		self.y += self.yDirection * self.speed

		self.leftSide = self.x
		self.rightSide = self.x + self.w
		self.top = self.y
		self.bottom = self.y + self.h

	def draw(self, screen, x, y):
		screen.blit(self.image ,(x, y))
		pygame.display.flip

class Pot(Sprite):
	def __init__(self, x1, y1, w1, h1, image_url):
		Sprite.__init__(self, x1, y1, w1, h1, image_url)
		self.speed = 7
		self.xDirection = 0
		self.yDirection = 0
		self.isBroken = False
		self.counter = 0
		self.potImg = pygame.image.load("pot.png")
		self.brokenPotimg = pygame.image.load("brokenPot.png")

	def update(self):
		self.setPrevPos()
		self.x += self.xDirection * self.speed
		self.y += self.yDirection * self.speed

		self.leftSide = self.x
		self.rightSide = self.x + self.w
		self.top = self.y
		self.bottom = self.y + self.h

		if self.isValid:
			if self.isBroken:
				self.image = self.brokenPotimg
				self.counter += 1

		if self.counter > 40:
			self.isValid = False

	def setPrevPos(self):
		self.prevX = self.x
		self.prevY = self.y

	def getOut(self, sprite):
		#up
		if self.y + self.h >= sprite.y and self.prevY + self.h <= sprite.y :
			self.y = sprite.y - self.h
			
		#down
		if self.y <= sprite.y + sprite.h and self.prevY >= sprite.y + sprite.h :
			self.y = sprite.y + sprite.h
				
		#right
		if self.x + self.w >= sprite.x and self.prevX + self.w <= sprite.x :
			self.x = sprite.x - self.w
				
		#left
		if self.x <= sprite.x + sprite.w and self.prevX >= sprite.x + sprite.w :
			self.x = sprite.x + sprite.w

	def draw(self, screen, x, y):
		screen.blit(self.image ,(x, y))
		pygame.display.flip

class Model():
	def __init__(self):
		self.dest_x = 0
		self.dest_y = 0
		self.sprites = []
		self.link = Link(300, 100, 75, 85, "link0.png")
		self.sprites.append(self.link)
		self.sprites.append(Tile(0 , 0 , 50, 50, "tile.png"))
		self.sprites.append(Tile(0, 50, 50, 50, "tile.png"))
		self.sprites.append(Tile(0, 150, 50, 50, "tile.png"))
		self.sprites.append(Tile(0, 100, 50, 50, "tile.png"))
		self.sprites.append(Tile(0, 200, 50, 50, "tile.png"))
		self.sprites.append(Tile(0, 250, 50, 50, "tile.png"))
		self.sprites.append(Tile(0, 300, 50, 50, "tile.png"))
		self.sprites.append(Tile(0, 350, 50, 50, "tile.png"))
		self.sprites.append(Tile(0, 400, 50, 50, "tile.png"))
		self.sprites.append(Tile(0, 450, 50, 50, "tile.png"))
		self.sprites.append(Tile(50, 450, 50, 50, "tile.png"))
		self.sprites.append(Tile(100, 450, 50, 50, "tile.png"))
		self.sprites.append(Tile(150, 450, 50, 50, "tile.png"))
		self.sprites.append(Tile(200, 450, 50, 50, "tile.png"))
		self.sprites.append(Tile(350, 450, 50, 50, "tile.png"))
		self.sprites.append(Tile(400, 450, 50, 50, "tile.png"))
		self.sprites.append(Tile(450, 450, 50, 50, "tile.png"))
		self.sprites.append(Tile(450, 400, 50, 50,"tile.png"))
		self.sprites.append(Tile(450, 350, 50, 50, "tile.png"))
		self.sprites.append(Tile(450, 300, 50, 50, "tile.png"))
		self.sprites.append(Tile(450, 150, 50, 50, "tile.png"))
		self.sprites.append(Tile(450, 100, 50, 50, "tile.png"))
		self.sprites.append(Tile(450, 50, 50, 50, "tile.png"))
		self.sprites.append(Tile(450, 0, 50, 50, "tile.png"))
		self.sprites.append(Tile(400, 0, 50, 50, "tile.png"))
		self.sprites.append(Tile(350, 0, 50, 50, "tile.png"))
		self.sprites.append(Tile(300, 0, 50, 50, "tile.png"))
		self.sprites.append(Tile(50, 0, 50, 50, "tile.png"))
		self.sprites.append(Tile(100,0, 50, 50, "tile.png"))
		self.sprites.append(Tile(150,0, 50, 50, "tile.png"))
		self.sprites.append(Tile(50,150, 50, 50, "tile.png"))
		self.sprites.append(Tile(100, 150, 50, 50, "tile.png"))
		self.sprites.append(Tile(200, 150, 50, 50, "tile.png"))
		self.sprites.append(Tile(150, 150, 50, 50, "tile.png"))
		self.sprites.append(Tile(200, 200, 50, 50, "tile.png"))
		self.sprites.append(Tile(200, 250, 50, 50, "tile.png"))
		self.sprites.append(Tile(500, 350, 50, 50, "tile.png"))
		self.sprites.append(Tile(500, 300, 50, 50, "tile.png"))
		self.sprites.append(Tile(500, 150, 50, 50, "tile.png"))
		self.sprites.append(Tile(500, 100, 50, 50, "tile.png"))
		self.sprites.append(Tile(500, 50, 50, 50, "tile.png"))
		self.sprites.append(Tile(500, 0, 50, 50, "tile.png"))
		self.sprites.append(Tile(550, 0, 50, 50, "tile.png"))
		self.sprites.append(Tile(600, 0, 50, 50, "tile.png"))
		self.sprites.append(Tile(650, 0, 50, 50, "tile.png"))
		self.sprites.append(Tile(700, 0, 50, 50, "tile.png"))
		self.sprites.append(Tile(950, 0, 50, 50, "tile.png"))
		self.sprites.append(Tile(900, 0, 50, 50, "tile.png"))
		self.sprites.append(Tile(850, 0, 50, 50, "tile.png"))
		self.sprites.append(Tile(950, 50, 50, 50, "tile.png"))
		self.sprites.append(Tile(950, 150,  50, 50, "tile.png"))
		self.sprites.append(Tile(950, 100, 50, 50, "tile.png"))
		self.sprites.append(Tile(950, 200, 50, 50, "tile.png"))
		self.sprites.append(Tile(950, 300, 50, 50, "tile.png"))
		self.sprites.append(Tile(950, 350, 50, 50, "tile.png"))
		self.sprites.append(Tile(950, 400, 50, 50, "tile.png"))
		self.sprites.append(Tile(950, 250, 50, 50, "tile.png"))
		self.sprites.append(Tile(950, 450, 50, 50, "tile.png"))
		self.sprites.append(Tile(900, 450, 50, 50, "tile.png"))
		self.sprites.append(Tile(850, 450, 50, 50, "tile.png"))
		self.sprites.append(Tile(550, 400, 50, 50, "tile.png"))
		self.sprites.append(Tile(500, 400, 50, 50, "tile.png"))
		self.sprites.append(Tile(500, 450, 50, 50, "tile.png"))
		self.sprites.append(Tile(550, 450, 50, 50, "tile.png"))
		self.sprites.append(Tile(850, 400, 50, 50, "tile.png"))
		self.sprites.append(Tile(900, 400, 50, 50, "tile.png"))
		self.sprites.append(Tile(50, 400, 50, 50, "tile.png"))
		self.sprites.append(Tile(100, 400, 50, 50, "tile.png"))
		self.sprites.append(Tile(150, 400, 50, 50, "tile.png"))
		self.sprites.append(Tile(200, 400, 50, 50, "tile.png"))
		self.sprites.append(Tile(350, 400, 50, 50, "tile.png"))
		self.sprites.append(Tile(400, 400, 50, 50, "tile.png"))
		self.sprites.append(Tile(550, 150, 50, 50, "tile.png")) 
		self.sprites.append(Tile(850, 50, 50, 50, "tile.png"))
		self.sprites.append(Tile(850, 900, 50, 50, "tile.png"))
		self.sprites.append(Tile(900, 900, 50, 50, "tile.png"))
		self.sprites.append(Tile(950, 900, 50, 50, "tile.png"))
		self.sprites.append(Tile(950, 950, 50, 50, "tile.png"))
		self.sprites.append(Tile(900, 950, 50, 50, "tile.png"))
		self.sprites.append(Tile(850, 950, 50, 50, "tile.png"))
		self.sprites.append(Tile(650, 900, 50, 50, "tile.png"))
		self.sprites.append(Tile(650, 950, 50, 50, "tile.png"))
		self.sprites.append(Tile(600, 950, 50, 50, "tile.png"))
		self.sprites.append(Tile(600, 900, 50, 50, "tile.png"))
		self.sprites.append(Tile(550, 900, 50, 50, "tile.png"))
		self.sprites.append(Tile(550, 950, 50, 50, "tile.png"))
		self.sprites.append(Tile(500, 900, 50, 50, "tile.png"))
		self.sprites.append(Tile(500, 950, 50, 50, "tile.png"))
		self.sprites.append(Tile(500, 500, 50, 50, "tile.png"))
		self.sprites.append(Tile(550, 500, 50, 50, "tile.png"))
		self.sprites.append(Tile(850, 500, 50, 50, "tile.png"))
		self.sprites.append(Tile(900, 500, 50, 50, "tile.png"))
		self.sprites.append(Tile(950, 500, 50, 50, "tile.png"))
		self.sprites.append(Tile(950, 550, 50, 50, "tile.png"))
		self.sprites.append(Tile(950, 600, 50, 50, "tile.png"))
		self.sprites.append(Tile(950, 650, 50, 50, "tile.png"))
		self.sprites.append(Tile(950, 700, 50, 50, "tile.png"))
		self.sprites.append(Tile(950, 800, 50, 50, "tile.png"))
		self.sprites.append(Tile(950, 850, 50, 50, "tile.png"))
		self.sprites.append(Tile(950, 750, 50, 50, "tile.png"))
		self.sprites.append(Tile(500, 850, 50, 50, "tile.png"))
		self.sprites.append(Tile(500, 800, 50, 50, "tile.png"))
		self.sprites.append(Tile(500, 700, 50, 50, "tile.png"))
		self.sprites.append(Tile(500, 750, 50, 50, "tile.png"))
		self.sprites.append(Tile(550, 750, 50, 50, "tile.png"))
		self.sprites.append(Tile(600, 750, 50, 50, "tile.png"))
		self.sprites.append(Tile(650, 750, 50, 50, "tile.png"))
		self.sprites.append(Tile(650, 700, 50, 50, "tile.png"))
		self.sprites.append(Tile(650, 650, 50, 50, "tile.png"))
		self.sprites.append(Tile(700, 650, 50, 50, "tile.png"))
		self.sprites.append(Tile(750, 650, 50, 50, "tile.png"))
		self.sprites.append(Tile(0, 500, 50, 50, "tile.png"))
		self.sprites.append(Tile(50, 500, 50, 50, "tile.png"))
		self.sprites.append(Tile(100, 500, 50, 50, "tile.png"))
		self.sprites.append(Tile(0, 600, 50, 50, "tile.png"))
		self.sprites.append(Tile(0, 650, 50, 50, "tile.png"))
		self.sprites.append(Tile(0, 700, 50, 50, "tile.png"))
		self.sprites.append(Tile(0, 750, 50, 50, "tile.png"))
		self.sprites.append(Tile(0, 800, 50, 50, "tile.png"))
		self.sprites.append(Tile(0, 850, 50, 50, "tile.png"))
		self.sprites.append(Tile(0, 900, 50, 50, "tile.png"))
		self.sprites.append(Tile(150, 500, 50, 50, "tile.png"))
		self.sprites.append(Tile(200, 500, 50, 50, "tile.png"))
		self.sprites.append(Tile(350, 500, 50, 50, "tile.png"))
		self.sprites.append(Tile(450, 500, 50, 50, "tile.png"))
		self.sprites.append(Tile(400, 500, 50, 50, "tile.png"))
		self.sprites.append(Tile(450, 650, 50, 50, "tile.png"))
		self.sprites.append(Tile(450, 700, 50, 50, "tile.png"))
		self.sprites.append(Tile(700, 900, 50, 50, "tile.png"))
		self.sprites.append(Tile(700, 950, 50, 50, "tile.png"))
		self.sprites.append(Tile(0, 950, 50, 50, "tile.png"))
		self.sprites.append(Tile(150, 900, 50, 50, "tile.png"))
		self.sprites.append(Tile(400, 900, 50, 50, "tile.png"))
		self.sprites.append(Tile(350, 900, 50, 50, "tile.png"))
		self.sprites.append(Tile(450, 850, 50, 50, "tile.png"))
		self.sprites.append(Tile(450, 750, 50, 50, "tile.png"))
		#mistake in y coordinate
		self.sprites.append(Tile(450, 800, 50, 50, "tile.png"))
		self.sprites.append(Tile(450, 900, 50, 50, "tile.png"))
		self.sprites.append(Tile(450, 950, 50, 50, "tile.png"))
		self.sprites.append(Tile(400, 950, 50, 50, "tile.png"))
		self.sprites.append(Tile(350, 950, 50, 50, "tile.png"))
		self.sprites.append(Tile(300, 900, 50, 50, "tile.png"))
		self.sprites.append(Tile(300, 950, 50, 50, "tile.png"))
		self.sprites.append(Tile(150, 950, 50, 50, "tile.png"))
		self.sprites.append(Tile(100, 900, 50, 50, "tile.png"))
		self.sprites.append(Tile(50, 900, 50, 50, "tile.png"))
		self.sprites.append(Tile(50, 950, 50, 50, "tile.png"))
		self.sprites.append(Tile(100, 950, 50, 50, "tile.png"))
		self.sprites.append(Tile(200, 0, 50, 50, "tile.png"))
		self.sprites.append(Tile(250, 0, 50, 50, "tile.png"))
		self.sprites.append(Tile(200, 900, 50, 50, "tile.png"))
		self.sprites.append(Tile(250, 900, 50, 50, "tile.png"))
		self.sprites.append(Tile(750, 900, 50, 50, "tile.png"))
		self.sprites.append(Tile(800, 900, 50, 50, "tile.png"))
		self.sprites.append(Tile(750, 0, 50, 50, "tile.png"))
		self.sprites.append(Tile(800, 0, 50, 50, "tile.png"))
		self.sprites.append(Tile(500, 650, 50, 50, "tile.png"))
		self.sprites.append(Tile(600, 400, 50, 50, "tile.png"))
		self.sprites.append(Tile(600, 500, 50, 50, "tile.png"))
		self.sprites.append(Tile(600, 450, 50, 50, "tile.png"))
		self.sprites.append(Tile(650, 450, 50, 50, "tile.png"))
		self.sprites.append(Tile(700, 250, 50, 50, "tile.png"))
		self.sprites.append(Tile(750, 250, 50, 50, "tile.png"))
		self.sprites.append(Tile(250, 950, 50, 50, "tile.png"))
		self.sprites.append(Tile(200, 950, 50, 50, "tile.png"))
		self.sprites.append(Tile(800, 950, 50, 50, "tile.png"))
		self.sprites.append(Tile(750, 950, 50, 50, "tile.png"))
		self.sprites.append(Tile(650, 400, 50, 50, "tile.png"))
		self.sprites.append(Tile(700, 400, 50, 50, "tile.png"))
		self.sprites.append(Tile(700, 450, 50, 50, "tile.png"))
		self.sprites.append(Tile(700, 500, 50, 50, "tile.png"))
		self.sprites.append(Tile(650, 500, 50, 50, "tile.png"))
		self.sprites.append(Tile(150, 650, 50, 50, "tile.png"))
		self.sprites.append(Tile(150, 700, 50, 50, "tile.png"))
		self.sprites.append(Tile(150, 750, 50, 50, "tile.png"))
		self.sprites.append(Tile(200, 750, 50, 50, "tile.png"))
		self.sprites.append(Tile(250, 750, 50, 50, "tile.png"))
		self.sprites.append(Tile(300, 750, 50,50, "tile.png"))
		self.sprites.append(Pot(850, 750, 40, 40, "pot.png"))
		self.sprites.append(Pot(244, 300, 40, 40, "pot.png"))
		self.sprites.append(Pot(244, 350, 40, 40, "pot.png"))
		self.sprites.append(Pot(444, 200, 40, 40, "pot.png"))
		self.sprites.append(Pot(444, 250, 40, 40, "pot.png"))
		self.sprites.append(Pot(700, 100, 40, 40, "pot.png"))
		self.sprites.append(Pot(900, 150, 40, 40, "pot.png"))
		self.sprites.append(Pot(800, 300, 40, 40, "pot.png"))
		self.sprites.append(Pot(220, 680, 40, 40, "pot.png"))
		self.sprites.append(Pot(380, 680, 40, 40, "pot.png"))
		self.sprites.append(Pot(830, 680, 40, 40, "pot.png"))
		self.sprites.append(Tile(0, 550, 50, 50, "tile.png"))
		

	def update(self):

		for i in range(len(self.sprites)):
			self.sprites[i].update()
			sprite = self.sprites[i]
			if not sprite.isValid:
				self.sprites.remove(self.sprites[i])
				break
			if isinstance(sprite,Tile):
				continue
			for j in range(len(self.sprites) - 1):
				sprite2 = self.sprites[j]
				if isinstance(sprite, Link) and isinstance(sprite2, Tile):
					if self.isColliding(sprite, sprite2):
						sprite.getOut(sprite2)
				if isinstance(sprite, Link) and isinstance(sprite2, Pot):
					if self.isColliding(sprite, sprite2) and not sprite2.isBroken:
						sprite.getOut(sprite2)
						self.movePot(sprite2)
					if self.isColliding(sprite, sprite2) and sprite2.isBroken:
						sprite.getOut(sprite2)
				if isinstance(sprite, Boomerang) and isinstance(sprite2, Tile):
					if self.isColliding(sprite, sprite2):
						sprite.isValid = False
				if isinstance(sprite, Boomerang) and isinstance(sprite2, Pot):
					if self.isColliding(sprite, sprite2):
						sprite.isValid = False
						sprite2.isBroken = True
				if isinstance(sprite, Pot) and isinstance(sprite2, Tile):
					if self.isColliding(sprite, sprite2):
						sprite.getOut(sprite2)
						sprite.isBroken = True

	def isColliding(self, sprite1, sprite2):
			
		#left lower corner of link is touching a tile
		if sprite1.rightSide > sprite2.leftSide and sprite1.leftSide < sprite2.rightSide and sprite1.top < sprite2.bottom and sprite1.bottom > sprite2.top:
			return True

		#right lower corner of link is touching a tile	
		if sprite1.leftSide < sprite2.rightSide and sprite1.rightSide > sprite2.leftSide and sprite1.top < sprite2.bottom and sprite1.bottom > sprite2.top:	
			return True

		#right lower corner of link is touching a tile
		if sprite1.top < sprite2.bottom and sprite1.bottom > sprite2.top and sprite1.rightSide > sprite2.leftSide and sprite1.leftSide < sprite2.rightSide:
			return True

		#right upper corner of link is touching a tile
		if sprite1.bottom > sprite2.top and sprite1.top < sprite2.bottom and sprite1.rightSide > sprite2.leftSide and sprite1.leftSide < sprite2.rightSide:
			return True

		return False

	def shootBoomerang(self):
		if self.link.isFacingRight:
			self.boomerang = Boomerang(self.link.rightSide, self.link.top + (self.link.h/2), 10, 10, "boomerang0.png")
			self.boomerang.xDirection = 1
			self.sprites.append(self.boomerang)

		if self.link.isFacingLeft:
			self.boomerang = Boomerang(self.link.leftSide, self.link.top + (self.link.h/2), 10, 10, "boomerang2.png")
			self.boomerang.xDirection = -1
			self.sprites.append(self.boomerang)

		if self.link.isFacingDown:
			self.boomerang = Boomerang(self.link.leftSide + (self.link.w/2), self.link.bottom, 10, 10, "boomerang1.png")
			self.boomerang.yDirection = 1
			self.sprites.append(self.boomerang)
	
		if self.link.isFacingUp:
			self.boomerang = Boomerang(self.link.rightSide - (self.link.w/2), self.link.top, 10, 10, "boomerang3.png")
			self.boomerang.yDirection = -1
			self.sprites.append(self.boomerang)
			

	def movePot(self, sprite):
		if self.link.isFacingRight:
			sprite.xDirection = 1
		if self.link.isFacingLeft:
			sprite.xDirection = -1
		if self.link.isFacingDown:
			sprite.yDirection = 1
		if self.link.isFacingUp:
			sprite.yDirection = -1

class View():
	def __init__(self, model):
		screen_size = (500,500)
		self.screen = pygame.display.set_mode(screen_size, 32)
		self.model = model
		self.roomXPos = 0
		self.roomYPos = 0

	def update(self):
		self.screen.fill([0,200,100])
		for i in range(len(self.model.sprites)):
			sprite = self.model.sprites[i]
			sprite.draw(self.screen, sprite.x - self.roomXPos, sprite.y - self.roomYPos)
		pygame.display.flip()	

class Controller():
	def __init__(self, model, view):
		self.view = view
		self.model = model
		self.keep_going = True
		self.ctrl_pressed = False

	def update(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				self.keep_going = False
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE or event.key == K_q:	
					self.keep_going = False
				if event.key == K_LCTRL:
					self.ctrl_pressed = True
				if event.key == K_RCTRL:
					self.ctrl_pressed = True
	
		keys = pygame.key.get_pressed()

		self.model.link.setPrevPos()
		if keys[K_LEFT]:
			self.model.link.isMovingLeft = True
			self.model.link.x = self.model.link.x - self.model.link.speed
			if self.model.link.x < 500:
				self.view.roomXPos = 0
		if keys[K_RIGHT]:
			self.model.link.isMovingRight = True
			self.model.link.x = self.model.link.x + self.model.link.speed
			if self.model.link.x > 500 :
				self.view.roomXPos = 500
		if keys[K_UP]:
			self.model.link.isMovingUp = True
			self.model.link.y = self.model.link.y - self.model.link.speed
			if self.model.link.y < 500:
				self.view.roomYPos = 0
		if keys[K_DOWN]:
			self.model.link.isMovingDown = True
			self.model.link.y = self.model.link.y + self.model.link.speed
			if self.model.link.y > 500:
				self.view.roomYPos = 500
		if self.ctrl_pressed:
			self.model.shootBoomerang()
			self.ctrl_pressed = False
		
print("Use the arrow keys to move. Press Esc to quit.")
pygame.init()
m = Model()
v = View(m)
c = Controller(m, v)
while c.keep_going:
	c.update()
	m.update()
	v.update()
	sleep(0.04)
print("Goodbye")