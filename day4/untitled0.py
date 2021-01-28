from mcpi.minecraft import Minecraft as mc
mcs = mc.create()
from time import sleep
import random
myID = mcs.getPlayerEntityId("None_200942")
mineral = [14,15,16,56,73,129]
while True :
    sleep(0.5)
    r = random.choice(mineral)
    x,y,z = mcs.entity.getTilePos(myID)
    mcs.setBlocks(x,y-1,z,x+1,y-2,z-1,r)

