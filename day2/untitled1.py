from mcpi.minecraft import Minecraft as mc
mcs = mc.create()
import time
import random
x , y , z = mcs.player.getPos()
w , h = 8 , 8
while True : 
    color1 = random.randint(0,15)
    color2 = random.randint(0,15)
    time.sleep(1)
    mcs.setBlocks(x + 10 , y + 20 , z + 10 , x - 10 , y + 20 , z -10 , 35 , color1)
    mcs.setBlocks(x + w , y + h+21 , z + w , x - w , y+21 , z -w , 95 , color2)
    mcs.setBlocks(x + w -1 , y + h + 21 -1 , z + w - 1 , x - w + 1 , y +21 , z-w+1 , 0)


