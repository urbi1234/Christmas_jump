import pygame
import threading
import time

#hello
pygame.init()

clock = pygame.time.Clock()
čas=0
#naredimo kanvas
canvas = pygame.display.set_mode((500, 500))

canvas_color = (255, 255, 255)

#našemu oknu damo naslov
pygame.display.set_caption("Moje prvo okno")
speed=10

def štoparica():
	global čas
	while True:
		time.sleep(1)
		čas+=1
    
def hitrost():
	global speed, čas
	while True:
		if čas >90:
			speed=70
			continue
		elif čas >70:
			speed=50
		elif čas >50:
			speed=40
		elif čas >30:
			speed=30
		elif čas >15:
			speed=20
        
    
runner = pygame.Rect(240, 240, 20, 20)
skala=pygame.Rect(500, 250, 10, 10)
skala1=pygame.Rect(750, 250, 10, 10)
skok=0
ex = False
threading.Thread(target=štoparica, daemon=True).start()
threading.Thread(target=hitrost, daemon=True).start()
while not ex:
	clock.tick(speed)


	canvas.fill(canvas_color)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			ex = True



	keys = pygame.key.get_pressed()
	#print(keys[pygame.K_UP], keys[pygame.K_DOWN], keys[pygame.K_LEFT], keys[pygame.K_RIGHT])
	if runner.y==240 and keys[pygame.K_UP]:
		skok += 40
	'''if keys[pygame.K_DOWN]:
		runner.y += 5
	if keys[pygame.K_LEFT]:
		runner.x -= 5
	if keys[pygame.K_RIGHT]:
		runner.x += 5'''
	if runner.y!=240 and skok==0:
		runner.y+=4
  
	if runner.colliderect(skala) or runner.colliderect(skala1):
		print('game over')
		ex=True
	if skok > 0:
		skok-=4
		runner.y-=4
     
	
	if skala.x==0:
		skala.x=500
	else:
		skala.x-=5
	
	if skala1.x==0:
		skala1.x=500
	else:
		skala1.x-=5

	print(speed, čas)
	pygame.draw.rect(canvas, (0, 0, 0), runner)
	pygame.draw.rect(canvas, (0, 0, 0), skala)
	pygame.draw.rect(canvas, (0, 0, 0), skala1)

	pygame.display.update() 