from mcpi.minecraft import Minecraft as mc
mcs = mc.create()
x,y,z = mcs.player.getPos()
def build(x,y,z,mcs):
    while True :
        try :
            sh = int(input('請輸入高度:'))
            break
        except:
            print("這不是數字!")
    h = (sh//2) + 1
    for i in range(h):
        x1 = x + i
        y1 = y + i
        z1 = z + i
        x2 = x + sh - i
        z2 = z + sh - i
        mcs.setBlocks(x1,y1,z1,x2,y1,z2,24)
build(x,y,z,mcs)

    
