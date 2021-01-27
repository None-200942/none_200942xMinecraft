from mcpi.minecraft import Minecraft as mc
mcs = mc.create()
import random
import time
while True:
    color1 = random.randint(0,16)
    color2 = random.randint(0,16)
    color3 = random.randint(0,16)
    color4 = random.randint(0,16)
    color5 = random.randint(0,16)
    color6 = random.randint(0,16)
    color7 = random.randint(0,16)
    color8 = random.randint(0,16)
    color9 = random.randint(0,16)
    x,y,z = mcs.player.getTilePos()
    mcs.setBlock(x,y-1,z,95,color1)
    mcs.setBlock(x-1,y-1,z-1,95,color2)
    mcs.setBlock(x-1,y-1,z,95,color3)
    mcs.setBlock(x-1,y-1,z+1,95,color4)
    mcs.setBlock(x,y-1,z-1,95,color5)
    mcs.setBlock(x,y-1,z+1,95,color6)
    mcs.setBlock(x+1,y-1,z+1,95,color7)
    mcs.setBlock(x+1,y-1,z-1,95,color8)
    mcs.setBlock(x+1,y-1,z,95,color9)
while True :
    a = random.randint(-10, 10)
    x , y , z = mcs.player.getPos()
    mcs.setBlock(x+a, y + 10 , z+a, 145)
    time.sleep(0.01)
    #mcs.setBlock(x+a, y + 10 , z+a, 12)
    #mcs.setBlock(x+a, y + 10 , z+a, 13)
    #time.sleep(0.01)

    