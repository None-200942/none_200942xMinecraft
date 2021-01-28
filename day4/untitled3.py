from mcpi.minecraft import Minecraft as mc
mcs = mc.create()
x,y,z = mcs.player.getPos()
from random import randint
com = randint(0,15)

for i in range(20):
    for j in range(20):
        color = randint(0,15)
        mcs.setBlock(x+i,y-1,z+j,35,color)

while True :
    hits = mcs.events.pollBlockHits()
    if len(hits) > 0:
        hit = hits[0]
        block = mcs.getBlockWithData(hit.pos)
        data = block.data
        if data == com :
            mcs.postToChat("U got the right Ans !")
            break
        else :
            mcs.postToChat("Try again !")
        