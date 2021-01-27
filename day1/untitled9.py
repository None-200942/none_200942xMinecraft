from mcpi.minecraft import Minecraft as mc
mcs = mc.create()
print(mcs.player.getTilePos())
mcs.player.setTilePos(100 , 100 , 100)