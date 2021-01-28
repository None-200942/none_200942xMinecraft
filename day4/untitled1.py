from mcpi.minecraft import Minecraft as mc
mcs = mc.create()
x,y,z = mcs.player.getPos()
number = 1
for i in range(8):
    for j in range(number):
        mcs.spawnEntity(x,y,z,60)
    number = number*2
    mcs.postToChat("生成了"+str(number)+"fish")

