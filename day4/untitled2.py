from mcpi.minecraft import Minecraft as mc
mcs = mc.create()
x,y,z = mcs.player.getPos()
import random
for i in range(3):
    for j in range(8):
        r = random.randint(1,6)
        color = random.randint(0,15)
        if r == 1 :
            mcs.setBlocks(x,y,z,x+4,y,z,35,color)
            x = x + 4
        elif r == 2 :
            mcs.setBlocks(x,y,z,x+4,y,z,35,color)
            x = x + 4
            
        elif r == 3 :
            mcs.setBlocks(x,y,z,x,y-4,z,35,color)
            y = y - 4
            
        elif r == 4 :
            mcs.setBlocks(x,y,z,x,y+4,z,35,color)
            y = y + 4
            
        elif r == 5:
            mcs.setBlocks(x,y,z,x+4,y,z-4,35,color)
            z = z - 4
        elif r == 6 :
            mcs.setBlocks(x,y,z,x,y,z+4,35,color)
            z = z + 4
            
            