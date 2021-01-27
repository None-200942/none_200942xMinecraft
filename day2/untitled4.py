from mcpi.minecraft import Minecraft as mc
mcs = mc.create()
while True :
    userName = input("What\'s ur name ?")
    message = input("What\'s ur message ?")
    mcs.postToChat("<"+userName+">"+message)
