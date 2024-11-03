import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))
screen.fill((255,255,255))
pygame.display.update()

subway_surfer = pygame.image.load("Matching\subwaysurfer.png")
ludo = pygame.image.load("Matching\ludo.png")
candy_crush = pygame.image.load("Matching\candycrush.jpg")
temple_run = pygame.image.load("Matching/templerun.png")


screen.blit(subway_surfer,(100,100))
screen.blit(ludo,(100,200))
screen.blit(candy_crush,(100,300))
screen.blit(temple_run,(100,400))

font=pygame.font.SysFont("Times New Roman",36)
text=font.render("Ludo",True,(0,0,255))
text1=font.render("Candy Crush",True,(255,0,0))
text2=font.render("Temple Run",True,(0,255,0))
text3=font.render("Subway Surfer",True,(0,0,0))

screen.blit(text,(300,130))
screen.blit(text1,(300,230))
screen.blit(text2,(300,330))
screen.blit(text3,(300,430))


pygame.display.update()

running = True
while running:
    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen,(0,0,0),(pos),20,0)
        pygame.display.update()
        
    elif event.type == pygame.MOUSEBUTTONUP:
        pos1 = pygame.mouse.get_pos()
        pygame.draw.line(screen,(0,0,0),(pos),(pos1),6)
        pygame.draw.circle(screen,(0,0,0),(pos1),20,0)
        pygame.display.update()  
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()