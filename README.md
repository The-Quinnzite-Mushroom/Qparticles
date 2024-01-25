A particle module that can do a lot of things.
![red](https://github.com/JAQuinnT/Qparticles/assets/152278657/028f6138-518b-4d31-9d9c-37304deeca76)

the main class:
qparticles.Particle(Shape = "circle",Colour = [0,0,0,255],Size = [10,10],Pos=[0,0],Light = 0,Timer = -1,Cpos=0,Csize =0,Ccolour = 0,A=0,Create_particle= 0,Bounce=0,Tag=0,RealPos=0,Fname=0,Border =0, Cborder = 0, Rotation = 0, Crotation = 0)
Those are the default values of the possible arguments.
Parameters:
Shape - can be 'circle','rect' or a pygame surface object
Colour - [r,g,b,alpha]
Size - [length,width] size that the picture will display as, circles only use value in position 0
Pos - [x,y]
Light - if not 0 the particle will blend for a lighting effect
Timer - counts down and deletes when = 0 when -1 the particle will last forever
A - change in Cpos
Tag - a place to store extra information
Fname - if Shape = 0 then fname will be used to load an image based on file name
Border -curently only works on circles: if >0 circle will be hollow and describes border thinkness coming in from the outside
Rotation -number in degrees for the rotation
Real pos - if not = 0 then will be used to show relative to a point

#any parameter with a C before it will change that value evrey time the particle.run()
#also should be formated the same as the atribute
Cpos - AKA velocity change in position
Csize - change in size
Ccolour - change in colour
Cborder - change in border
Crotation - change in rotation

create_particle and bounce curently are a work in progress

class functions:
Particle.show(surf,RelPos= 0)
  shows the particle
  RelPos is only needed if the particle has .RealPos atribute, then will be shown relitavly on the surf
return surf

Particle.run()
  does things like counting down the timer and changing the position
Particle.save(name='name',folder='')
  saves folder/name as a .json 

other functions:
load_particle(fname="name",folder ="")
  loads folder/name as a .json 
return particle

particles is a list of particle objects

run_particles(particles)
  uses the run() function on all the particles
return particles

show_particles(surf,particles,RelPos=0)
  RelPos is only needed if the particle has .RealPos atribute, then will be shown relitavly on the surf
  shows all the particles on the surface
return surf

purge_particles(particles)
  deletes all the particles that have run out of time
return particles





