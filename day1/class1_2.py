from mcpi.minecraft import Minecraft as mc
import time
mcs = mc.create()
print(mcs.player.getTilePos())
x , y , z = 100 , 100 , 100
i = 0
while i  < 25 :
    mcs.player.setTilePos(x , y  , z )
    time.sleep(1)
    y = y + 1
    x = x + 1
    i = i + 1
    

    


