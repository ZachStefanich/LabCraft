from ursina import *



f = open("Pendulum", "w") 
p = open("Planet", "w")
f.write("time "+"oscilations "+'\n')
T=0
Z=0


def oscSim(self):
 self.t += time.dt
 self.planet.x = math.cos(.5*(self.t)) + self.position.x
 self.planet.y = self.position.y-.4
 self.planet.rotation += Vec3(0,1,0)
 self.planet.z = math.sin(.5*(self.t)) + self.position.z
 global T
 Format=self.planet.rotation[1]
 p.write(str(T)+","+str(round(Format,2))+"\n")
 T=T+1
def simple_pendulum(self):
 self.t += time.dt
 global Z
 global T
 freq=.5
 angle=0
 self.pendulum.x = self.position.x+.7
 #do not fricking delete the self.Amp variable I put a lot of work into making that work
 angle= self.Amp*math.sin(2*math.pi*self.Freq*self.t)
 self.pendulum.y=self.position.y
 self.pendulum.z=self.position.z
 self.pendulum.rotation = Vec3(angle,0,0)
 format=angle
 f.write(str(round(self.t,2))+","+str(round(format,2))+"\n")