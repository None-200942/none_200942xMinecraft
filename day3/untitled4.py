from mcpi.minecraft import Minecraft as mc
mcs = mc.create()
x,y,z = mcs.player.getPos()
def planttree(x,y,z,mcs):
        mcs.setBlocks(x-2,y+4,z-2,x+2,y+10,z+2,35,5)
        mcs.setBlocks(x,y,z,x,y+4,z,20)
for i in range (0,30,4):
    for j in range(5):
        for a in range(5):
            planttree(x+i*3,y,z+i*5,mcs)

