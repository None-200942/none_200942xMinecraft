from mcpi.minecraft import Minecraft as mc
mcs = mc.create()
import random
import time
x,y,z = mcs.player.getPos()
while True :
    time.sleep(10)
    x = x + random.uniform(10,-10)
    y = y + 30
    z = z + random.uniform(10,-10)
    mcs.spawnEntity(x,y,z,63)