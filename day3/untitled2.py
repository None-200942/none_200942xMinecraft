from mcpi.minecraft import Minecraft as mc
mcs = mc.create()
x,y,z = mcs.player.getPos()
for i in range(50):
    mcs.setBlock(x+i,y+i,z+i,155)
    mcs.setBlock(x+i+1,y+i,z+i+1,44,7)

    
   