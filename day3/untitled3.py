from mcpi.minecraft import Minecraft as mc
mcs = mc.create()
x,y,z = mcs.player.getPos()
def planttree(x,y,z,mcs):
    for i in range(1,10,2):
        mcs.setBlocks(x-i,y-i,z-i,x+i,y+i,z+i,35,5)
        mcs.setBlocks(x,y-14,z,x,y-10,z,17)
for a in range (5) :
    planttree(x+a*50,y,z,mcs)
    
    
    
        