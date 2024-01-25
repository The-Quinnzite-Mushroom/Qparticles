import pygame,random
import qparticles as qp


#pygame initialization
pygame.init()

#Screen Constants
background_colour = (200,200,200)

#window setup
WINDOW_SIZE = (900,700) # set up window size
screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate screen

#screen things
pygame.display.set_caption('particles demo')


#variable inizialization
clock = pygame.time.Clock()

#empty list of particles
particles = []


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    

    
    screen.fill(background_colour)
    
    pos = pygame.mouse.get_pos()
    
    #blue falling particles
    particles.append(qp.Particle(Shape = 'rect',Size = [20,20],Csize = [0.5,0.5] ,Colour = [100,150,200],Ccolour = [-1,-1,-1],Cpos = [random.randint(-3,3),random.randint(3,6)],Timer = 250,Pos = [random.randint(0,WINDOW_SIZE[0]),0],Rotation = 0,Crotation = 10))
    # red trail
    particles.append(qp.Particle(Colour = [200,70,60],Pos= [pos[0],pos[1]],Size = 10,Ccolour = [0,0,0,-1],Csize = 0.1,Cpos = [0,0],Timer = 100))#adding a new particle to the particle list
    
    screen = qp.show_particles(screen,particles)#place the particles onto a surface
    particles = qp.run_particles(particles)#make the particles change position,rotation,size,colour and all that stuff
    particles = qp.purge_particles(particles)#destroy particles that the timer has ranout
    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()