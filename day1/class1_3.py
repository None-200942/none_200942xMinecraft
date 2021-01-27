from mcpi.minecraft import Minecraft as mc
mcs = mc.create()
import time 
x,y,z = mcs.player.getTilePos()
while True :
    x, y ,z = mcs.player.getTilePos()
    mcs.postToChat("You are located on X : " +str(x) +" Y: " +str(y) + " Z: " +str(z))
    time.sleep(1)
    
