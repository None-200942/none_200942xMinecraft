from mcpi.minecraft import Minecraft as mc
mcs = mc.create()
import time
import random
while True :
    d = random.randint(-10, 10)
    time.sleep(0.01)
    x , y , z = mcs.player.getPos()
    mcs.setBlock(x+d, y + 10 , z+d, 145)

