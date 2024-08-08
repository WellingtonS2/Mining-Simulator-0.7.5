import pygame as pg
import sys,math,datasave,random
pg.init()
y=222
gameDisplay=pg.display.set_mode((640,640))
pg.display.set_caption('Mining Simulator')
selectionBox=pg.image.load('ores/select.png').convert_alpha()
grass=pg.image.load('ores/grass.png').convert()
stone=pg.image.load('ores/stone.png').convert()
minedStone=pg.image.load('ores/minedStone.png').convert()
minedDeepstone=pg.image.load('ores/minedDeepstone.png').convert()
coal=pg.image.load('ores/coal_ore.png').convert()
iron=pg.image.load('ores/iron_ore.png').convert()
gold=pg.image.load('ores/gold_ore.png').convert()
ruby=pg.image.load('ores/ruby_ore.png').convert()
sapphire=pg.image.load('ores/sapphire_ore.png').convert()
amethyst=pg.image.load('ores/amethyst_ore.png').convert()
diamond=pg.image.load('ores/diamond_ore.png').convert()
uranium=pg.image.load('ores/uranium_ore.png').convert()
emerald=pg.image.load('ores/emerald_ore.png').convert()
magnetite=pg.image.load('ores/magnetite_ore.png').convert()
kalite=pg.image.load('ores/kalite_ore.png').convert()
platinum=pg.image.load('ores/platinum_ore.png').convert()
malachite=pg.image.load('ores/malachite_ore.png').convert()
deepstone=pg.image.load('ores/deepstone.png').convert()
lavastone=pg.image.load('ores/lavastone.png').convert()
minedLavastone=pg.image.load('ores/minedLavastone.png').convert()
minedGrass=pg.image.load('ores/minedGrass.png').convert()
illuminite=pg.image.load('ores/illuminite_ore.png').convert()
mithril=pg.image.load('ores/mithril_ore.png').convert()
hafnium=pg.image.load('ores/hafnium_ore.png').convert()
plutonium=pg.image.load('ores/plutonium_ore.png').convert()
bedrock=pg.image.load('ores/bedrock.png').convert()
glowstone=pg.image.load('ores/glowstone_ore.png').convert()
sand=pg.image.load('ores/sand.png').convert()
sandstone=pg.image.load('ores/sandstone.png').convert()
slate=pg.image.load('ores/slate.png').convert()
quartzite=pg.image.load('ores/quartzite.png').convert()
coral=pg.image.load('ores/coral.png').convert()
treasure=pg.image.load('ores/treasure.png').convert()
fossils=pg.image.load('ores/fossils.png').convert()
seashells=pg.image.load('ores/seashells.png').convert()
minedSand=pg.image.load('ores/minedSand.png').convert()
minedSandstone=pg.image.load('ores/minedSandstone.png').convert()
minedSlate=pg.image.load('ores/minedSlate.png').convert()
minedQuartzite=pg.image.load('ores/minedQuartzite.png').convert()
beryllium=pg.image.load('ores/beryllium_ore.png').convert()
topaz=pg.image.load('ores/topaz_ore.png').convert()
corundum=pg.image.load('ores/corundum_ore.png').convert()
zirconium=pg.image.load('ores/zirconium_ore.png').convert()
rubidium=pg.image.load('ores/rubidium_ore.png').convert()
strontium=pg.image.load('ores/strontium_ore.png').convert()
yttrium=pg.image.load('ores/yttrium_ore.png').convert()
dravite=pg.image.load('ores/dravite_ore.png').convert()
iridium=pg.image.load('ores/iridium_ore.png').convert()
regolith=pg.image.load('ores/regolith.png').convert()
anorthite=pg.image.load('ores/anorthite.png').convert()
minedAnorthite=pg.image.load('ores/minedAnorthite.png').convert()
moonstone=pg.image.load('ores/moonstone.png').convert()
minedRegolith=pg.image.load('ores/minedRegolith.png').convert()
minedMoonstone=pg.image.load('ores/minedMoonstone.png').convert()
augite=pg.image.load('ores/augite_ore.png').convert()
chromite=pg.image.load('ores/chromite_ore.png').convert()
hercynite=pg.image.load('ores/hercynite_ore.png').convert()
enstatite=pg.image.load('ores/enstatite_ore.png').convert()
troilite=pg.image.load('ores/troilite_ore.png').convert()
apatite=pg.image.load('ores/apatite_ore.png').convert()
spinel=pg.image.load('ores/spinel_ore.png').convert()
fayalite=pg.image.load('ores/fayalite_ore.png').convert()
forsterite=pg.image.load('ores/forsterite_ore.png').convert()
bytownite=pg.image.load('ores/bytownite_ore.png').convert()
labradorite=pg.image.load('ores/labradorite_ore.png').convert()
pyroxene=pg.image.load('ores/pyroxene_ore.png').convert()
ulvite=pg.image.load('ores/ulvite_ore.png').convert()
plagioclase=pg.image.load('ores/plagioclase_ore.png').convert()
aquamarine=pg.image.load('ores/aquamarine_ore.png').convert()
molybdenum=pg.image.load('ores/molybdenum_ore.png').convert()
player=pg.image.load('miner/miner.png').convert_alpha()
playerLeft=pg.image.load('miner/minerLeft.png').convert_alpha()
wpImg=pg.image.load('ores/worldProg.png').convert_alpha()
locked=pg.image.load('ores/locked.png')
minerAnimation=[pg.image.load('miner/miner.png').convert_alpha(),pg.image.load('miner/miner2.png').convert_alpha(),pg.image.load('miner/miner3.png').convert_alpha(),pg.image.load('miner/miner2.png').convert_alpha()]
minerAnimationLeft=[pg.image.load('miner/minerLeft.png').convert_alpha(),pg.image.load('miner/minerLeft2.png').convert_alpha(),pg.image.load('miner/minerLeft3.png').convert_alpha(),pg.image.load('miner/minerLeft2.png').convert_alpha()]
x=random.randint(1,15)*32
movingLeft=False
movingRight=False
facingLeft=False
playerFalling=False
canMoveLeft=True
canMoveRight=True
mouseClicked=False
playerJumping=False
playerRectLeft=pg.Rect(x,222,21,25)
playerRectRight=pg.Rect(x+21,222,21,25)
playerBottomRect=pg.Rect(x+50,272,42,4)
playerBottomRect2=pg.Rect(x+3,y+50,35,6)
playerTopRect=pg.Rect(x,y-20,35,20)
clock=pg.time.Clock()
blocks=[]
font=pg.font.Font(None,30)
sfont=pg.font.Font(None,20)
depth=1
downAccel=1
pickaxeList=['Basic Pickaxe','Stone Pickaxe','Steel Pickaxe','Aluminum Pickaxe','Diamond Pickaxe','Magic Pickaxe','Sledgehammer','Katana','Jackhammer',
             'Strange Pickaxe','THE PICKAXE OF DOOM','Nuclear Pickaxe','Dark Mass','Lightsaber','Flaming Pickaxe','Mythical Sword','Plasma Pickaxe',
             'Rock Vaporizer',"Thor's Hammer",'Lucky Charm','Comically Large Spoon','Haunted Pickaxe',"Godly Pickaxe",'Nokia Phone']
pickaxeImgList=[pg.transform.scale(pg.image.load('pickaxes/1.png'),(320,320)),
                pg.transform.scale(pg.image.load('pickaxes/2.png'),(320,320)),
                pg.transform.scale(pg.image.load('pickaxes/3.png'),(320,320)),
                pg.transform.scale(pg.image.load('pickaxes/4.png'),(320,320)),
                pg.transform.scale(pg.image.load('pickaxes/5.png'),(320,320)),
                pg.transform.scale(pg.image.load('pickaxes/6.png'),(320,320)),
                pg.transform.scale(pg.image.load('pickaxes/7.png'),(320,320)),
                pg.transform.scale(pg.image.load('pickaxes/8.png'),(320,320)),
                pg.transform.scale(pg.image.load('pickaxes/9.png'),(320,320)),
                pg.transform.scale(pg.image.load('pickaxes/10.png'),(320,320)),
                pg.transform.scale(pg.image.load('pickaxes/11.png'),(320,320)),
                pg.transform.scale(pg.image.load('pickaxes/12.png'),(320,320)),
                pg.transform.scale(pg.image.load('pickaxes/13.png'),(320,320)),
                pg.transform.scale(pg.image.load('pickaxes/14.png'),(320,320)),
                pg.transform.scale(pg.image.load('pickaxes/15.png'),(320,320)),
                pg.transform.scale(pg.image.load('pickaxes/16.png'),(320,320)),
                pg.transform.scale(pg.image.load('pickaxes/17.png'),(320,320)),
                pg.transform.scale(pg.image.load('pickaxes/18.png'),(320,320)),
                pg.transform.scale(pg.image.load('pickaxes/19.png'),(320,320)),
                pg.transform.scale(pg.image.load('pickaxes/20.png'),(320,320)),
                pg.transform.scale(pg.image.load('pickaxes/21.png'),(320,320)),
                pg.transform.scale(pg.image.load('pickaxes/22.png'),(320,320)),
                pg.transform.scale(pg.image.load('pickaxes/23.png'),(320,320)),
                pg.transform.scale(pg.image.load('pickaxes/24.png'),(320,320)),  
                ]
pickaxeDescList=['Its basic, but can get the job done',
                 'Slight upgrade from the beginner pickaxe',
                 'This steel pickaxe will carry you to your dreams.',
                 'A tough but lightweight pickaxe',
                 'Can be a gift to your significant other',
                 'Its magical',
                 'Can smash its way through the toughest rocks.',
                 'Slice your way to riches',
                 'Only disadvantage is you annoy the neighbors from its noise',
                 'Nobody knows the true origins of this pickaxe',
                 'I got lazy with naming',
                 'Slightly radioactive, may cause radiation poisoning',
                 '[DATA EXPUNGED]',
                 'May the Force be with you',
                 'You can also use it to cook burgers',
                 'A powerful sword, crafted from nothing but my coding',
                 'You can also use it to cook burgers',
                 'Vaporizes rocks in a fraction of a second.',
                 'Radiates strange energy as you pick it up',
                 'Tikki, Spots On',
                 'For breaking comically large rocks',
                 'Be careful of the demonic ghost type thing in this pickaxe',
                 'Radiates godly energy as you pick it up',
                 '???',]
pickaxeStrs=[1,1.2,1.5,2,2.5,3.5,5,7,10,12,15,20,25,35,50,75,120,170,200,250,400,600,950,1200,1500]
pickaxePrices=[0,20,30,50,75,100,150,200,250,350,420,540,600,720,850,999,1200,1400,2000,3000,4500,6666,7500,9000]
backpackList=['Small Backpack','Backpack','Fair Backpack','Large Backpack','Military Backpack','Hiking Pack','Barrel','Crate','Potato Sack','Dishwasher','Refrigerator','Washing Machine','Shipping Container',
              'Truck','Boeing 747','House','Magic Box','Comically Large Box','Galactic Backpack','Pocket Dimension']
backpackCapacity=[250,15,25,40,50,69,80,100,120,150,200,250,300,400,500,700,1000,1250,1500,2500]
hit1=pg.mixer.Sound('sounds/metal1.aif')
hit2=pg.mixer.Sound('sounds/metal2.aif')
hit3=pg.mixer.Sound('sounds/metal3.aif')
hit4=pg.mixer.Sound('sounds/metal4.aif')
hit5=pg.mixer.Sound('sounds/metal5.aif')
pg.mixer.music.load('sounds/entanglement.mp3')
pg.mixer.music.play(-1)
equippedBackpack=0
stuffInBackpack=0
moneyInBackpack=0
money=datasave.load.load_int('saves/money.dsi')
currentWorld=0
pg.display.set_icon(pickaxeImgList[random.randint(0,19)])
sellButton=pg.Rect(1,1,1,1)
equippedPickaxe=datasave.load.load_int('saves/equippedpickaxe.dsi')
ownedPickaxes=datasave.load.load_list('saves/pickaxes.dsi')
blocksMined=datasave.load.load_int('saves/mined.dsi')
generatedL2=False
rangeTop=pg.Rect(1,1,1,1)
rangeSide=pg.Rect(1,1,1,1)
rangeBottom=pg.Rect(1,1,1,1)
starPositions=[]
for _ in range(0,100):
    starPositions.append((random.randint(0,640),random.randint(0,640)))
while depth<150:
    for i in range(0,20):
        class block:
            x=0
            y=0
            ore='Stone'
            rect=pg.Rect(x,y,32,32)
            hardness=60
            mined=False
            reqPick=0
        blocks.append(block)
        blocks[-1].x=i*32
        blocks[-1].y=350+(depth*32)
        blocks[-1].rect=pg.Rect(i,350,32,32)
        if currentWorld==0:
            blocks[-1].ore='Stone'
            if depth==1:
                blocks[-1].ore='Grass'
                blocks[-1].hardness=60
                blocks[-1].reqPick=0
            elif depth==145:
                blocks[-1].ore=random.choice(['Stone','Stone','Stone','Stone','Stone','Deepstone'])
                if blocks[-1].ore=='Deepstone':
                    blocks[-1].hardness=140*(round(depth/30)+1)
                    blocks[-1].reqPick=4
                else:
                    blocks[-1].hardness=120*(round(depth/30)+1)
                    blocks[-1].reqPick=0
            elif depth==146:
                blocks[-1].ore=random.choice(['Stone','Stone','Stone','Stone','Deepstone'])
                if blocks[-1].ore=='Deepstone':
                    blocks[-1].hardness=140*(round(depth/30)+1)
                    blocks[-1].reqPick=4
                else:
                    blocks[-1].hardness=120*(round(depth/30)+1)
                    blocks[-1].reqPick=0
            elif depth==147:
                blocks[-1].ore=random.choice(['Stone','Stone','Stone','Deepstone'])
                if blocks[-1].ore=='Deepstone':
                    blocks[-1].hardness=140*(round(depth/30)+1)
                    blocks[-1].reqPick=4
                else:
                    blocks[-1].hardness=120*(round(depth/30)+1)
                    blocks[-1].reqPick=0
            elif depth==148:
                blocks[-1].ore=random.choice(['Stone','Stone','Deepstone'])
                if blocks[-1].ore=='Deepstone':
                    blocks[-1].hardness=140*(round(depth/30)+1)
                    blocks[-1].reqPick=4
                else:
                    blocks[-1].hardness=120*(round(depth/30)+1)
                    blocks[-1].reqPick=0
            elif depth==149:
                blocks[-1].ore=random.choice(['Stone','Deepstone','Deepstone'])
                if blocks[-1].ore=='Deepstone':
                    blocks[-1].hardness=140*(round(depth/30)+1)
                    blocks[-1].reqPick=4
                else:
                    blocks[-1].hardness=120*(round(depth/30)+1)
                    blocks[-1].reqPick=0
            elif depth==150:
                blocks[-1].ore='Deepstone'
                blocks[-1].hardness=140*(round(depth/30)+1)
                blocks[-1].reqPick=4
            else:
                blocks[-1].ore='Stone'
                blocks[-1].hardness=120*(round(depth/30)+1)
                blocks[-1].reqPick=0
            if depth>5 and random.randint(1,20+depth)==1:
                blocks[-1].ore='Coal'
                blocks[-1].hardness=180
                blocks[-1].reqPick=1
            if depth>10 and random.randint(1,30+depth)==1:
                blocks[-1].ore='Iron'
                blocks[-1].hardness=200
                blocks[-1].reqPick=2
            if depth>25 and random.randint(1,60)==1:
                blocks[-1].ore='Gold'
                blocks[-1].hardness=240
                blocks[-1].reqPick=3
            if depth>35 and random.randint(1,220)==1:
                blocks[-1].ore='Sapphire'
                blocks[-1].hardness=240
                blocks[-1].reqPick=4
            if depth>45 and random.randint(1,240)==1:
                blocks[-1].ore='Ruby'
                blocks[-1].hardness=240
                blocks[-1].reqPick=4
            if depth>55 and random.randint(1,240)==1:
                blocks[-1].ore='Emerald'
                blocks[-1].hardness=240
                blocks[-1].reqPick=4
            if depth>15 and random.randint(1,240)==1:
                blocks[-1].ore='Amethyst'
                blocks[-1].hardness=180
                blocks[-1].reqPick=2
            if depth>60 and random.randint(1,300)==1:
                blocks[-1].ore='Diamond'
                blocks[-1].hardness=600
                blocks[-1].reqPick=4
            if depth>45 and random.randint(1,200)==1:
                blocks[-1].ore='Uranium'
                blocks[-1].hardness=480
                blocks[-1].reqPick=4
        if currentWorld==1:
            blocks[-1].ore='Sandstone'
            blocks[-1].hardness=120*(round(depth/30)+1)
            blocks[-1].reqPick=0
            if depth==1:
                blocks[-1].ore='Sand'
                blocks[-1].hardness=60
                blocks[-1].reqPick=0
            if depth>5 and random.randint(1,20+depth)==1:
                blocks[-1].ore='Seashells'
                blocks[-1].hardness=180
                blocks[-1].reqPick=1
            if depth>10 and random.randint(1,30+depth)==1:
                blocks[-1].ore='Coral'
                print('coral')
                blocks[-1].hardness=200
                blocks[-1].reqPick=2
            if depth>25 and random.randint(1,260)==1:
                blocks[-1].ore='Treasure'
                blocks[-1].hardness=240
                blocks[-1].reqPick=3
            if depth>35 and random.randint(1,70)==1:
                blocks[-1].ore='Fossils'
                blocks[-1].hardness=240
                blocks[-1].reqPick=4
            elif depth==145:
                blocks[-1].ore=random.choice(['Sandstone','Sandstone','Sandstone','Sandstone','Sandstone','Slate'])
                if blocks[-1].ore=='Deepstone':
                    blocks[-1].hardness=140*(round(depth/30)+1)
                    blocks[-1].reqPick=4
                else:
                    blocks[-1].hardness=120*(round(depth/30)+1)
                    blocks[-1].reqPick=0
            elif depth==146:
                blocks[-1].ore=random.choice(['Sandstone','Sandstone','Sandstone','Sandstone','Slate'])
                if blocks[-1].ore=='Deepstone':
                    blocks[-1].hardness=140*(round(depth/30)+1)
                    blocks[-1].reqPick=4
                else:
                    blocks[-1].hardness=120*(round(depth/30)+1)
                    blocks[-1].reqPick=0
            elif depth==147:
                blocks[-1].ore=random.choice(['Sandstone','Sandstone','Sandstone','Slate'])
                if blocks[-1].ore=='Deepstone':
                    blocks[-1].hardness=140*(round(depth/30)+1)
                    blocks[-1].reqPick=4
                else:
                    blocks[-1].hardness=120*(round(depth/30)+1)
                    blocks[-1].reqPick=0
            elif depth==148:
                blocks[-1].ore=random.choice(['Sandstone','Sandstone','Slate'])
                if blocks[-1].ore=='Deepstone':
                    blocks[-1].hardness=140*(round(depth/30)+1)
                    blocks[-1].reqPick=4
                else:
                    blocks[-1].hardness=120*(round(depth/30)+1)
                    blocks[-1].reqPick=0
            elif depth==149:
                blocks[-1].ore=random.choice(['Sandstone','Slate'])
                if blocks[-1].ore=='Deepstone':
                    blocks[-1].hardness=140*(round(depth/30)+1)
                    blocks[-1].reqPick=4
                else:
                    blocks[-1].hardness=120*(round(depth/30)+1)
                    blocks[-1].reqPick=0
            elif depth==150:
                blocks[-1].ore='Slate'
                blocks[-1].hardness=140*(round(depth/30)+1)
                blocks[-1].reqPick=4
        if currentWorld==2:
            blocks[-1].ore='Regolith'
            blocks[-1].hardness=120*(round(depth/30)+1)
            blocks[-1].reqPick=0
            if depth>5 and random.randint(1,20+depth)==1:
                blocks[-1].ore='Augite'
                blocks[-1].hardness=180
                blocks[-1].reqPick=3
            if depth>10 and random.randint(1,30+depth)==1:
                blocks[-1].ore='Chromite'
                blocks[-1].hardness=200
                blocks[-1].reqPick=4
            if depth>25 and random.randint(1,60)==1:
                blocks[-1].ore='Enstatite'
                blocks[-1].hardness=240
                blocks[-1].reqPick=5
            if depth>35 and random.randint(1,120)==1:
                blocks[-1].ore='Hercynite'
                blocks[-1].hardness=240
                blocks[-1].reqPick=6
            if depth>35 and random.randint(1,120)==1:
                blocks[-1].ore='Troilite'
                blocks[-1].hardness=240
                blocks[-1].reqPick=6
            if depth==145:
                blocks[-1].ore=random.choice(['Regolith','Regolith','Regolith','Regolith','Regolith','Moonstone'])
                if blocks[-1].ore=='Moonstone':
                    blocks[-1].hardness=140*(round(depth/30)+1)
                    blocks[-1].reqPick=4
                else:
                    blocks[-1].hardness=120*(round(depth/30)+1)
                    blocks[-1].reqPick=0
            elif depth==146:
                blocks[-1].ore=random.choice(['Regolith','Regolith','Regolith','Regolith','Moonstone'])
                if blocks[-1].ore=='Moonstone':
                    blocks[-1].hardness=140*(round(depth/30)+1)
                    blocks[-1].reqPick=4
                else:
                    blocks[-1].hardness=120*(round(depth/30)+1)
                    blocks[-1].reqPick=0
            elif depth==147:
                blocks[-1].ore=random.choice(['Regolith','Regolith','Regolith','Moonstone'])
                if blocks[-1].ore=='Moonstone':
                    blocks[-1].hardness=140*(round(depth/30)+1)
                    blocks[-1].reqPick=4
                else:
                    blocks[-1].hardness=120*(round(depth/30)+1)
                    blocks[-1].reqPick=0
            elif depth==148:
                blocks[-1].ore=random.choice(['Regolith','Moonstone'])
                if blocks[-1].ore=='Moonstone':
                    blocks[-1].hardness=140*(round(depth/30)+1)
                    blocks[-1].reqPick=4
                else:
                    blocks[-1].hardness=120*(round(depth/30)+1)
                    blocks[-1].reqPick=0
            elif depth==149:
                blocks[-1].ore=random.choice(['Regolith','Moonstone'])
                if blocks[-1].ore=='Moonstone':
                    blocks[-1].hardness=140*(round(depth/30)+1)
                    blocks[-1].reqPick=4
                else:
                    blocks[-1].hardness=120*(round(depth/30)+1)
                    blocks[-1].reqPick=0
            elif depth==150:
                blocks[-1].ore='Moonstone'
                blocks[-1].hardness=140*(round(depth/30)+1)
                blocks[-1].reqPick=4
                
        
    depth+=1
while depth<300:
    for i in range(0,20):
        class block:
            x=0
            y=0
            ore='Deepstone'
            rect=pg.Rect(x,y,32,32)
            hardness=60
            mined=False
            reqPick=0
        blocks.append(block)
        blocks[-1].x=i*32
        blocks[-1].y=350+(depth*32)
        blocks[-1].rect=pg.Rect(i,350,32,32)
        blocks[-1].reqPick=2
        blocks[-1].hardness=120*(round(depth/30)+1)
        if currentWorld==0:
            blocks[-1].ore='Deepstone'
            if random.randint(0,100)==0:
                blocks[-1].ore='Magnetite'
                blocks[-1].hardness=600
                blocks[-1].reqPick=5
            elif random.randint(0,100)==0:
                blocks[-1].ore='Kalite'
                blocks[-1].hardness=600
                blocks[-1].reqPick=6
            elif random.randint(0,100)==0:
                blocks[-1].ore='Platinum'
                blocks[-1].hardness=800
                blocks[-1].reqPick=6
            elif random.randint(0,80)==0:
                blocks[-1].ore='Malachite'
                blocks[-1].hardness=600
                blocks[-1].reqPick=5
            elif random.randint(0,80)==0:
                blocks[-1].ore='Aquamarine'
                blocks[-1].hardness=600
                blocks[-1].reqPick=5
            if depth==294:
                if random.randint(1,2)==1:
                    blocks[-1].ore='Lavastone'
                    blocks[-1].hardness=120*(round(depth/30)+1)
                    blocks[-1].reqPick=4
            if depth==295:
                if random.randint(1,3) in range(1,2):
                    blocks[-1].ore='Lavastone'
                    blocks[-1].hardness=120*(round(depth/30)+1)
                    blocks[-1].reqPick=4
            if depth==296:
                if random.randint(1,4) in range(1,3):
                    blocks[-1].ore='Lavastone'
                    blocks[-1].hardness=120*(round(depth/30)+1)
                    blocks[-1].reqPick=4
            if depth==297:
                if random.randint(1,5) in range(1,4):
                    blocks[-1].ore='Lavastone'
                    blocks[-1].hardness=120*(round(depth/30)+1)
                    blocks[-1].reqPick=4
            if depth==298:
                if random.randint(1,6) in range(1,5):
                    blocks[-1].ore='Lavastone'
                    blocks[-1].hardness=120*(round(depth/30)+1)
                    blocks[-1].reqPick=4
            if depth==299:
                if random.randint(1,7) in range(1,6):
                    blocks[-1].ore='Lavastone'
                    blocks[-1].hardness=120*(round(depth/30)+1)
                    blocks[-1].reqPick=4
        if currentWorld==1:
            blocks[-1].ore='Slate'
            if random.randint(0,100)==0:
                blocks[-1].ore='Beryllium'
                blocks[-1].hardness=600
                blocks[-1].reqPick=5
            elif random.randint(0,100)==0:
                blocks[-1].ore='Corundum'
                blocks[-1].hardness=600
                blocks[-1].reqPick=5
            elif random.randint(0,100)==0:
                blocks[-1].ore='Zirconium'
                blocks[-1].hardness=800
                blocks[-1].reqPick=5
            elif random.randint(0,80)==0:
                blocks[-1].ore='Topaz'
                blocks[-1].hardness=600
                blocks[-1].reqPick=6
            elif random.randint(0,110)==0:
                blocks[-1].ore='Molybdenum'
                blocks[-1].hardness=700
                blocks[-1].reqPick=6
            if depth==294:
                if random.randint(1,2)==1:
                    blocks[-1].ore='Quartzite'
                    blocks[-1].hardness=120*(round(depth/30)+1)
                    blocks[-1].reqPick=4
            if depth==295:
                if random.randint(1,3) in range(1,2):
                    blocks[-1].ore='Quartzite'
                    blocks[-1].hardness=120*(round(depth/30)+1)
                    blocks[-1].reqPick=4
            if depth==296:
                if random.randint(1,4) in range(1,3):
                    blocks[-1].ore='Quartzite'
                    blocks[-1].hardness=120*(round(depth/30)+1)
                    blocks[-1].reqPick=4
            if depth==297:
                if random.randint(1,5) in range(1,4):
                    blocks[-1].ore='Quartzite'
                    blocks[-1].hardness=120*(round(depth/30)+1)
                    blocks[-1].reqPick=4
            if depth==298:
                if random.randint(1,6) in range(1,5):
                    blocks[-1].ore='Quartzite'
                    blocks[-1].hardness=120*(round(depth/30)+1)
                    blocks[-1].reqPick=4
            if depth==299:
                if random.randint(1,7) in range(1,6):
                    blocks[-1].ore='Quartzite'
                    blocks[-1].hardness=120*(round(depth/30)+1)
                    blocks[-1].reqPick=4
        if currentWorld==2:
            blocks[-1].ore='Moonstone'
            if random.randint(0,100)==0:
                blocks[-1].ore='Apatite'
                blocks[-1].hardness=600
                blocks[-1].reqPick=6
            elif random.randint(0,100)==0:
                blocks[-1].ore='Forsterite'
                blocks[-1].hardness=600
                blocks[-1].reqPick=7
            elif random.randint(0,100)==0:
                blocks[-1].ore='Fayalite'
                blocks[-1].hardness=800
                blocks[-1].reqPick=7
            elif random.randint(0,80)==0:
                blocks[-1].ore='Spinel'
                blocks[-1].hardness=600
                blocks[-1].reqPick=6
            if depth==294:
                if random.randint(1,2)==1:
                    blocks[-1].ore='Anorthite'
                    blocks[-1].hardness=120*(round(depth/30)+1)
                    blocks[-1].reqPick=4
            if depth==295:
                if random.randint(1,3) in range(1,2):
                    blocks[-1].ore='Anorthite'
                    blocks[-1].hardness=120*(round(depth/30)+1)
                    blocks[-1].reqPick=4
            if depth==296:
                if random.randint(1,4) in range(1,3):
                    blocks[-1].ore='Anorthite'
                    blocks[-1].hardness=120*(round(depth/30)+1)
                    blocks[-1].reqPick=4
            if depth==297:
                if random.randint(1,5) in range(1,4):
                    blocks[-1].ore='Anorthite'
                    blocks[-1].hardness=120*(round(depth/30)+1)
                    blocks[-1].reqPick=4
            if depth==298:
                if random.randint(1,6) in range(1,5):
                    blocks[-1].ore='Anorthite'
                    blocks[-1].hardness=120*(round(depth/30)+1)
                    blocks[-1].reqPick=4
            if depth==299:
                if random.randint(1,7) in range(1,6):
                    blocks[-1].ore='Anorthite'
                    blocks[-1].hardness=120*(round(depth/30)+1)
                    blocks[-1].reqPick=4       
    depth+=1
while depth<500:
    for i in range(0,20):
        class block:
            x=0
            y=0
            ore='Lavastone'
            rect=pg.Rect(x,y,32,32)
            hardness=60
            mined=False
            reqPick=0
        blocks.append(block)
        blocks[-1].x=i*32
        blocks[-1].y=350+(depth*32)
        blocks[-1].rect=pg.Rect(i,350,32,32)
        blocks[-1].reqPick=4
        blocks[-1].hardness=120*(round(depth/30)+1)
        if currentWorld==0:
            blocks[-1].ore='Lavastone'
            if random.randint(0,100)==0:
                blocks[-1].ore='Hafnium'
                blocks[-1].hardness=1200
                blocks[-1].reqPick=6
            elif random.randint(0,100)==0:
                blocks[-1].ore='Glowstone'
                blocks[-1].hardness=1800
                blocks[-1].reqPick=7
            elif random.randint(0,100)==0:
                blocks[-1].ore='Mithril'
                blocks[-1].hardness=1800
                blocks[-1].reqPick=7
            elif random.randint(0,80)==0:
                blocks[-1].ore='Illuminite'
                blocks[-1].hardness=2400
                blocks[-1].reqPick=8
            elif random.randint(0,80)==0:
                blocks[-1].ore='Plutonium'
                blocks[-1].hardness=3000
                blocks[-1].reqPick=8
        if currentWorld==1:
            blocks[-1].ore='Quartzite'
            if random.randint(0,100)==0:
                blocks[-1].ore='Rubidium'
                blocks[-1].hardness=1200
                blocks[-1].reqPick=6
            elif random.randint(0,120)==0:
                blocks[-1].ore='Dravite'
                blocks[-1].hardness=1800
                blocks[-1].reqPick=7
            elif random.randint(0,120)==0:
                blocks[-1].ore='Strontium'
                blocks[-1].hardness=1800
                blocks[-1].reqPick=7
            elif random.randint(0,100)==0:
                blocks[-1].ore='Yttrium'
                blocks[-1].hardness=2400
                blocks[-1].reqPick=8
            elif random.randint(0,100)==0:
                blocks[-1].ore='Iridium'
                blocks[-1].hardness=3000
                blocks[-1].reqPick=9
        if currentWorld==2:
            blocks[-1].ore='Anorthite'
            blocks[-1].hardness=120*(round(depth/30)+1)
            if random.randint(0,100)==0:
                blocks[-1].ore='Bytownite'
                blocks[-1].hardness=1200
                blocks[-1].reqPick=7
            elif random.randint(0,120)==0:
                blocks[-1].ore='Labradorite'
                blocks[-1].hardness=1800
                blocks[-1].reqPick=8
            elif random.randint(0,120)==0:
                blocks[-1].ore='Pyroxene'
                blocks[-1].hardness=1800
                blocks[-1].reqPick=8
            elif random.randint(0,100)==0:
                blocks[-1].ore='Ulvite'
                blocks[-1].hardness=2400
                blocks[-1].reqPick=9
            elif random.randint(0,100)==0:
                blocks[-1].ore='Plagioclase'
                blocks[-1].hardness=2000
                blocks[-1].reqPick=8
    depth+=1
while depth<520:
    for i in range(0,20):
        class block:
            x=0
            y=0
            ore='Bedrock'
            rect=pg.Rect(x,y,32,32)
            hardness=60
            mined=False
            reqPick=0
        blocks.append(block)
        blocks[-1].x=i*32
        blocks[-1].y=350+(depth*32)
        blocks[-1].rect=pg.Rect(i,350,32,32)
        blocks[-1].reqPick=0
        blocks[-1].hardness=900000000000000000000000000000000000000
    depth+=1
mouserect=pg.Rect(1,1,1,1)
mousex=0
mousey=0
miraculousLadybug=0
shopIndex=0
playerDepth=0
jumping=False
jumpCounter=0
jumpable=True
kPressed=False
music2Played=False
music1Played=True
music3Played=False
progMenu=False
blocksminedRect=pg.Rect(1,2,3,4)
while True:
    miraculousLadybug+=1
    playerDepth=round(abs(blocks[0].y-272)/32)
    if playerDepth in range(150,270) and not music2Played:
        pg.mixer.music.load('sounds/level2.ogg')
        pg.mixer.music.play(-1)
        music2Played=True
        music1Played=False
        music3Plated=False
    if playerDepth<145 and not music1Played:
        pg.mixer.music.load('sounds/entanglement.mp3')
        pg.mixer.music.play(-1)
        music1Played=True
        music2Played=False
        music3Played=False
    if playerDepth>270 and not music3Played:
        pg.mixer.music.load('sounds/level3.ogg')
        pg.mixer.music.play(-1)
        music1Played=False
        music2Played=False
        music3Played=True
    class block:
        x=0
        y=0
        ore='Stone'
        rect=pg.Rect(x,y,32,32)
        hardness=60
        mined=False
        reqPick=0
    if currentWorld==0:
        gameDisplay.fill((50,200,255))
    if currentWorld==1:
        gameDisplay.fill((0,50,100))
    if currentWorld==2:
        gameDisplay.fill((0,0,30))
        for _ in range(1,100):
            pg.draw.rect(gameDisplay,(255,255,255),pg.Rect(starPositions[_][0],starPositions[_][1]+blocks[0].y/2-320,2,2))
    for event in pg.event.get():
        if event.type==pg.QUIT:
            datasave.save.save_str('saves/money.dsi',money)
            datasave.save.save_str('saves/equippedpickaxe.dsi',equippedPickaxe)
            datasave.save.save_str('saves/mined.dsi',blocksMined)
            datasave.save.save_list('saves/pickaxes.dsi',ownedPickaxes)
            pg.quit()
            sys.exit()
        if event.type==pg.MOUSEMOTION:
            mouserect=pg.Rect(event.pos,(1,1))
            mousex=event.pos[0]
            mousey=event.pos[1]
        if event.type==pg.MOUSEBUTTONDOWN:
            if event.button==1:
                mouseClicked=True
                if mouserect.colliderect(sellButton) and stuffInBackpack>0:
                    money+=moneyInBackpack
                    moneyInBackpack=0
                    stuffInBackpack=0
                    for i in blocks:
                        i.y+=(playerDepth*32)
                    downAccel=1
                if mouserect.colliderect(surfaceButton):
                    for i in blocks:
                        i.y+=(playerDepth*32)
                    downAccel=1
                if mouserect.colliderect(shopButton):
                    shop=True
                    while shop:
                        for event in pg.event.get():
                            if event.type==pg.QUIT:
                                datasave.save.save_str('saves/money.dsi',money)
                                datasave.save.save_list('saves/pickaxes.dsi',ownedPickaxes)
                                datasave.save.save_str('saves/equippedpickaxe.dsi',equippedPickaxe)
                                datasave.save.save_str('saves/mined.dsi',blocksMined)
                                pg.quit()
                                sys.exit()
                            if event.type==pg.MOUSEBUTTONDOWN:
                                if event.button==1:
                                    if mouserect.colliderect(sellButton):
                                        if not progMenu:
                                            shop=False
                                        else:
                                            progMenu=False
                                    if mouserect.colliderect(blocksminedRect):
                                        progMenu=True
                                    if mouserect.colliderect(shopButton):
                                        if pickaxeList[shopIndex] in ownedPickaxes:
                                            equippedPickaxe=shopIndex
                                        else:
                                            if money>=pickaxePrices[shopIndex]:
                                                ownedPickaxes.append(pickaxeList[shopIndex])
                                                money-=pickaxePrices[shopIndex]
                                    if mousex in range(104,104+47) and mousey in range(200,247) and currentWorld!=0:
                                        currentWorld=0
                                        blocks=[]
                                        depth=1
                                        while depth<150:
                                            for i in range(0,20):
                                                class block:
                                                    x=0
                                                    y=0
                                                    ore='Stone'
                                                    rect=pg.Rect(x,y,32,32)
                                                    hardness=60
                                                    mined=False
                                                    reqPick=0
                                                blocks.append(block)
                                                blocks[-1].x=i*32
                                                blocks[-1].y=350+(depth*32)
                                                blocks[-1].rect=pg.Rect(i,350,32,32)
                                                if currentWorld==0:
                                                    blocks[-1].ore='Stone'
                                                    if depth==1:
                                                        blocks[-1].ore='Grass'
                                                        blocks[-1].hardness=60
                                                        blocks[-1].reqPick=0
                                                    elif depth==145:
                                                        blocks[-1].ore=random.choice(['Stone','Stone','Stone','Stone','Stone','Deepstone'])
                                                        if blocks[-1].ore=='Deepstone':
                                                            blocks[-1].hardness=140*(round(depth/30)+1)
                                                            blocks[-1].reqPick=4
                                                        else:
                                                            blocks[-1].hardness=120*(round(depth/30)+1)
                                                            blocks[-1].reqPick=0
                                                    elif depth==146:
                                                        blocks[-1].ore=random.choice(['Stone','Stone','Stone','Stone','Deepstone'])
                                                        if blocks[-1].ore=='Deepstone':
                                                            blocks[-1].hardness=140*(round(depth/30)+1)
                                                            blocks[-1].reqPick=4
                                                        else:
                                                            blocks[-1].hardness=120*(round(depth/30)+1)
                                                            blocks[-1].reqPick=0
                                                    elif depth==147:
                                                        blocks[-1].ore=random.choice(['Stone','Stone','Stone','Deepstone'])
                                                        if blocks[-1].ore=='Deepstone':
                                                            blocks[-1].hardness=140*(round(depth/30)+1)
                                                            blocks[-1].reqPick=4
                                                        else:
                                                            blocks[-1].hardness=120*(round(depth/30)+1)
                                                            blocks[-1].reqPick=0
                                                    elif depth==148:
                                                        blocks[-1].ore=random.choice(['Stone','Stone','Deepstone'])
                                                        if blocks[-1].ore=='Deepstone':
                                                            blocks[-1].hardness=140*(round(depth/30)+1)
                                                            blocks[-1].reqPick=4
                                                        else:
                                                            blocks[-1].hardness=120*(round(depth/30)+1)
                                                            blocks[-1].reqPick=0
                                                    elif depth==149:
                                                        blocks[-1].ore=random.choice(['Stone','Deepstone','Deepstone'])
                                                        if blocks[-1].ore=='Deepstone':
                                                            blocks[-1].hardness=140*(round(depth/30)+1)
                                                            blocks[-1].reqPick=4
                                                        else:
                                                            blocks[-1].hardness=120*(round(depth/30)+1)
                                                            blocks[-1].reqPick=0
                                                    elif depth==150:
                                                        blocks[-1].ore='Deepstone'
                                                        blocks[-1].hardness=140*(round(depth/30)+1)
                                                        blocks[-1].reqPick=4
                                                    else:
                                                        blocks[-1].ore='Stone'
                                                        blocks[-1].hardness=120*(round(depth/30)+1)
                                                        blocks[-1].reqPick=0
                                                    if depth>5 and random.randint(1,20+depth)==1:
                                                        blocks[-1].ore='Coal'
                                                        blocks[-1].hardness=180
                                                        blocks[-1].reqPick=1
                                                    if depth>10 and random.randint(1,30+depth)==1:
                                                        blocks[-1].ore='Iron'
                                                        blocks[-1].hardness=200
                                                        blocks[-1].reqPick=2
                                                    if depth>25 and random.randint(1,60)==1:
                                                        blocks[-1].ore='Gold'
                                                        blocks[-1].hardness=240
                                                        blocks[-1].reqPick=3
                                                    if depth>35 and random.randint(1,220)==1:
                                                        blocks[-1].ore='Sapphire'
                                                        blocks[-1].hardness=240
                                                        blocks[-1].reqPick=4
                                                    if depth>45 and random.randint(1,240)==1:
                                                        blocks[-1].ore='Ruby'
                                                        blocks[-1].hardness=240
                                                        blocks[-1].reqPick=4
                                                    if depth>55 and random.randint(1,240)==1:
                                                        blocks[-1].ore='Emerald'
                                                        blocks[-1].hardness=240
                                                        blocks[-1].reqPick=4
                                                    if depth>15 and random.randint(1,240)==1:
                                                        blocks[-1].ore='Amethyst'
                                                        blocks[-1].hardness=180
                                                        blocks[-1].reqPick=2
                                                    if depth>60 and random.randint(1,300)==1:
                                                        blocks[-1].ore='Diamond'
                                                        blocks[-1].hardness=600
                                                        blocks[-1].reqPick=4
                                                    if depth>45 and random.randint(1,200)==1:
                                                        blocks[-1].ore='Uranium'
                                                        blocks[-1].hardness=480
                                                        blocks[-1].reqPick=4
                                            depth+=1
                                        while depth<300:
                                            for i in range(0,20):
                                                class block:
                                                    x=0
                                                    y=0
                                                    ore='Deepstone'
                                                    rect=pg.Rect(x,y,32,32)
                                                    hardness=60
                                                    mined=False
                                                    reqPick=0
                                                blocks.append(block)
                                                blocks[-1].x=i*32
                                                blocks[-1].y=350+(depth*32)
                                                blocks[-1].rect=pg.Rect(i,350,32,32)
                                                blocks[-1].reqPick=2
                                                blocks[-1].hardness=120*(round(depth/30)+1)
                                                if currentWorld==0:
                                                    blocks[-1].ore='Deepstone'
                                                    if random.randint(0,100)==0:
                                                        blocks[-1].ore='Magnetite'
                                                        blocks[-1].hardness=600
                                                        blocks[-1].reqPick=5
                                                    elif random.randint(0,100)==0:
                                                        blocks[-1].ore='Kalite'
                                                        blocks[-1].hardness=600
                                                        blocks[-1].reqPick=6
                                                    elif random.randint(0,100)==0:
                                                        blocks[-1].ore='Platinum'
                                                        blocks[-1].hardness=800
                                                        blocks[-1].reqPick=6
                                                    elif random.randint(0,80)==0:
                                                        blocks[-1].ore='Malachite'
                                                        blocks[-1].hardness=600
                                                        blocks[-1].reqPick=5
                                                    elif random.randint(0,80)==0:
                                                        blocks[-1].ore='Aquamarine'
                                                        blocks[-1].hardness=600
                                                        blocks[-1].reqPick=5
                                                    if depth==294:
                                                        if random.randint(1,2)==1:
                                                            blocks[-1].ore='Lavastone'
                                                            blocks[-1].hardness=120*(round(depth/30)+1)
                                                            blocks[-1].reqPick=4
                                                    if depth==295:
                                                        if random.randint(1,3) in range(1,2):
                                                            blocks[-1].ore='Lavastone'
                                                            blocks[-1].hardness=120*(round(depth/30)+1)
                                                            blocks[-1].reqPick=4
                                                    if depth==296:
                                                        if random.randint(1,4) in range(1,3):
                                                            blocks[-1].ore='Lavastone'
                                                            blocks[-1].hardness=120*(round(depth/30)+1)
                                                            blocks[-1].reqPick=4
                                                    if depth==297:
                                                        if random.randint(1,5) in range(1,4):
                                                            blocks[-1].ore='Lavastone'
                                                            blocks[-1].hardness=120*(round(depth/30)+1)
                                                            blocks[-1].reqPick=4
                                                    if depth==298:
                                                        if random.randint(1,6) in range(1,5):
                                                            blocks[-1].ore='Lavastone'
                                                            blocks[-1].hardness=120*(round(depth/30)+1)
                                                            blocks[-1].reqPick=4
                                                    if depth==299:
                                                        if random.randint(1,7) in range(1,6):
                                                            blocks[-1].ore='Lavastone'
                                                            blocks[-1].hardness=120*(round(depth/30)+1)
                                                            blocks[-1].reqPick=4
                                            depth+=1
                                        while depth<500:
                                            for i in range(0,20):
                                                class block:
                                                    x=0
                                                    y=0
                                                    ore='Lavastone'
                                                    rect=pg.Rect(x,y,32,32)
                                                    hardness=60
                                                    mined=False
                                                    reqPick=0
                                                blocks.append(block)
                                                blocks[-1].x=i*32
                                                blocks[-1].y=350+(depth*32)
                                                blocks[-1].rect=pg.Rect(i,350,32,32)
                                                blocks[-1].reqPick=4
                                                blocks[-1].hardness=120*(round(depth/30)+1)
                                                if currentWorld==0:
                                                    blocks[-1].ore='Lavastone'
                                                    if random.randint(0,100)==0:
                                                        blocks[-1].ore='Hafnium'
                                                        blocks[-1].hardness=1200
                                                        blocks[-1].reqPick=6
                                                    elif random.randint(0,100)==0:
                                                        blocks[-1].ore='Glowstone'
                                                        blocks[-1].hardness=1800
                                                        blocks[-1].reqPick=7
                                                    elif random.randint(0,100)==0:
                                                        blocks[-1].ore='Mithril'
                                                        blocks[-1].hardness=1800
                                                        blocks[-1].reqPick=7
                                                    elif random.randint(0,80)==0:
                                                        blocks[-1].ore='Illuminite'
                                                        blocks[-1].hardness=2400
                                                        blocks[-1].reqPick=8
                                                    elif random.randint(0,80)==0:
                                                        blocks[-1].ore='Plutonium'
                                                        blocks[-1].hardness=3000
                                                        blocks[-1].reqPick=8
                                            depth+=1
                                        while depth<520:
                                            for i in range(0,20):
                                                class block:
                                                    x=0
                                                    y=0
                                                    ore='Bedrock'
                                                    rect=pg.Rect(x,y,32,32)
                                                    hardness=60
                                                    mined=False
                                                    reqPick=0
                                                blocks.append(block)
                                                blocks[-1].x=i*32
                                                blocks[-1].y=350+(depth*32)
                                                blocks[-1].rect=pg.Rect(i,350,32,32)
                                                blocks[-1].reqPick=0
                                                blocks[-1].hardness=99999999999999999999999999999999999
                                            depth+=1
                                    if mousex in range(104+194,104+239) and mousey in range(200,247) and blocksMined>=2500 and currentWorld!=1:
                                        currentWorld=1
                                        blocks=[]
                                        depth=1
                                        while depth<150:
                                            for i in range(0,20):
                                                class block:
                                                    x=0
                                                    y=0
                                                    ore='Stone'
                                                    rect=pg.Rect(x,y,32,32)
                                                    hardness=60
                                                    mined=False
                                                    reqPick=0
                                                blocks.append(block)
                                                blocks[-1].x=i*32
                                                blocks[-1].y=350+(depth*32)
                                                blocks[-1].rect=pg.Rect(i,350,32,32)
                                                if currentWorld==1:
                                                    blocks[-1].ore='Sandstone'
                                                    blocks[-1].hardness=120*(round(depth/30)+1)
                                                    blocks[-1].reqPick=0
                                                    if depth==1:
                                                        blocks[-1].ore='Sand'
                                                        blocks[-1].hardness=60
                                                        blocks[-1].reqPick=0
                                                    if depth>5 and random.randint(1,20+depth)==1:
                                                        blocks[-1].ore='Seashells'
                                                        blocks[-1].hardness=180
                                                        blocks[-1].reqPick=1
                                                    if depth>10 and random.randint(1,30+depth)==1:
                                                        blocks[-1].ore='Coral'
                                                        blocks[-1].hardness=200
                                                        blocks[-1].reqPick=2
                                                    if depth>25 and random.randint(1,260)==1:
                                                        blocks[-1].ore='Treasure'
                                                        blocks[-1].hardness=240
                                                        blocks[-1].reqPick=3
                                                    if depth>35 and random.randint(1,70)==1:
                                                        blocks[-1].ore='Fossils'
                                                        blocks[-1].hardness=240
                                                        blocks[-1].reqPick=4
                                                    elif depth==145:
                                                        blocks[-1].ore=random.choice(['Sandstone','Sandstone','Sandstone','Sandstone','Sandstone','Slate'])
                                                        if blocks[-1].ore=='Deepstone':
                                                            blocks[-1].hardness=140*(round(depth/30)+1)
                                                            blocks[-1].reqPick=4
                                                        else:
                                                            blocks[-1].hardness=120*(round(depth/30)+1)
                                                            blocks[-1].reqPick=0
                                                    elif depth==146:
                                                        blocks[-1].ore=random.choice(['Sandstone','Sandstone','Sandstone','Sandstone','Slate'])
                                                        if blocks[-1].ore=='Deepstone':
                                                            blocks[-1].hardness=140*(round(depth/30)+1)
                                                            blocks[-1].reqPick=4
                                                        else:
                                                            blocks[-1].hardness=120*(round(depth/30)+1)
                                                            blocks[-1].reqPick=0
                                                    elif depth==147:
                                                        blocks[-1].ore=random.choice(['Sandstone','Sandstone','Sandstone','Slate'])
                                                        if blocks[-1].ore=='Deepstone':
                                                            blocks[-1].hardness=140*(round(depth/30)+1)
                                                            blocks[-1].reqPick=4
                                                        else:
                                                            blocks[-1].hardness=120*(round(depth/30)+1)
                                                            blocks[-1].reqPick=0
                                                    elif depth==148:
                                                        blocks[-1].ore=random.choice(['Sandstone','Sandstone','Slate'])
                                                        if blocks[-1].ore=='Deepstone':
                                                            blocks[-1].hardness=140*(round(depth/30)+1)
                                                            blocks[-1].reqPick=4
                                                        else:
                                                            blocks[-1].hardness=120*(round(depth/30)+1)
                                                            blocks[-1].reqPick=0
                                                    elif depth==149:
                                                        blocks[-1].ore=random.choice(['Sandstone','Slate'])
                                                        if blocks[-1].ore=='Deepstone':
                                                            blocks[-1].hardness=140*(round(depth/30)+1)
                                                            blocks[-1].reqPick=4
                                                        else:
                                                            blocks[-1].hardness=120*(round(depth/30)+1)
                                                            blocks[-1].reqPick=0
                                                    elif depth==150:
                                                        blocks[-1].ore='Slate'
                                                        blocks[-1].hardness=140*(round(depth/30)+1)
                                                        blocks[-1].reqPick=4
                                                        
                                                
                                            depth+=1
                                        while depth<300:
                                            for i in range(0,20):
                                                class block:
                                                    x=0
                                                    y=0
                                                    ore='Deepstone'
                                                    rect=pg.Rect(x,y,32,32)
                                                    hardness=60
                                                    mined=False
                                                    reqPick=0
                                                blocks.append(block)
                                                blocks[-1].x=i*32
                                                blocks[-1].y=350+(depth*32)
                                                blocks[-1].rect=pg.Rect(i,350,32,32)
                                                blocks[-1].reqPick=2
                                                blocks[-1].hardness=120*(round(depth/30)+1)
                                                
                                                if currentWorld==1:
                                                    blocks[-1].ore='Slate'
                                                    if random.randint(0,100)==0:
                                                        blocks[-1].ore='Beryllium'
                                                        blocks[-1].hardness=600
                                                        blocks[-1].reqPick=5
                                                    elif random.randint(0,100)==0:
                                                        blocks[-1].ore='Corundum'
                                                        blocks[-1].hardness=600
                                                        blocks[-1].reqPick=5
                                                    elif random.randint(0,100)==0:
                                                        blocks[-1].ore='Zirconium'
                                                        blocks[-1].hardness=800
                                                        blocks[-1].reqPick=5
                                                    elif random.randint(0,80)==0:
                                                        blocks[-1].ore='Topaz'
                                                        blocks[-1].hardness=600
                                                        blocks[-1].reqPick=6
                                                    elif random.randint(0,110)==0:
                                                        blocks[-1].ore='Molybdenum'
                                                        blocks[-1].hardness=700
                                                        blocks[-1].reqPick=6
                                                    if depth==294:
                                                        if random.randint(1,2)==1:
                                                            blocks[-1].ore='Quartzite'
                                                            blocks[-1].hardness=120*(round(depth/30)+1)
                                                            blocks[-1].reqPick=4
                                                    if depth==295:
                                                        if random.randint(1,3) in range(1,2):
                                                            blocks[-1].ore='Quartzite'
                                                            blocks[-1].hardness=120*(round(depth/30)+1)
                                                            blocks[-1].reqPick=4
                                                    if depth==296:
                                                        if random.randint(1,4) in range(1,3):
                                                            blocks[-1].ore='Quartzite'
                                                            blocks[-1].hardness=120*(round(depth/30)+1)
                                                            blocks[-1].reqPick=4
                                                    if depth==297:
                                                        if random.randint(1,5) in range(1,4):
                                                            blocks[-1].ore='Quartzite'
                                                            blocks[-1].hardness=120*(round(depth/30)+1)
                                                            blocks[-1].reqPick=4
                                                    if depth==298:
                                                        if random.randint(1,6) in range(1,5):
                                                            blocks[-1].ore='Quartzite'
                                                            blocks[-1].hardness=120*(round(depth/30)+1)
                                                            blocks[-1].reqPick=4
                                                    if depth==299:
                                                        if random.randint(1,7) in range(1,6):
                                                            blocks[-1].ore='Quartzite'
                                                            blocks[-1].hardness=120*(round(depth/30)+1)
                                                            blocks[-1].reqPick=4
                                            depth+=1
                                        while depth<500:
                                            for i in range(0,20):
                                                class block:
                                                    x=0
                                                    y=0
                                                    ore='Lavastone'
                                                    rect=pg.Rect(x,y,32,32)
                                                    hardness=60
                                                    mined=False
                                                    reqPick=0
                                                blocks.append(block)
                                                blocks[-1].x=i*32
                                                blocks[-1].y=350+(depth*32)
                                                blocks[-1].rect=pg.Rect(i,350,32,32)
                                                blocks[-1].reqPick=4
                                                blocks[-1].hardness=120*(round(depth/30)+1)
                                                if currentWorld==1:
                                                    blocks[-1].ore='Quartzite'
                                                    if random.randint(0,100)==0:
                                                        blocks[-1].ore='Rubidium'
                                                        blocks[-1].hardness=1200
                                                        blocks[-1].reqPick=6
                                                    elif random.randint(0,120)==0:
                                                        blocks[-1].ore='Dravite'
                                                        blocks[-1].hardness=1800
                                                        blocks[-1].reqPick=7
                                                    elif random.randint(0,120)==0:
                                                        blocks[-1].ore='Strontium'
                                                        blocks[-1].hardness=1800
                                                        blocks[-1].reqPick=7
                                                    elif random.randint(0,100)==0:
                                                        blocks[-1].ore='Yttrium'
                                                        blocks[-1].hardness=2400
                                                        blocks[-1].reqPick=8
                                                    elif random.randint(0,100)==0:
                                                        blocks[-1].ore='Iridium'
                                                        blocks[-1].hardness=3000
                                                        blocks[-1].reqPick=9
                                            depth+=1
                                        while depth<520:
                                            for i in range(0,20):
                                                class block:
                                                    x=0
                                                    y=0
                                                    ore='Bedrock'
                                                    rect=pg.Rect(x,y,32,32)
                                                    hardness=60
                                                    mined=False
                                                    reqPick=0
                                                blocks.append(block)
                                                blocks[-1].x=i*32
                                                blocks[-1].y=350+(depth*32)
                                                blocks[-1].rect=pg.Rect(i,350,32,32)
                                                blocks[-1].reqPick=0
                                                blocks[-1].hardness=99999999999999999999999999999999999
                                            depth+=1
                                    if mousex in range(104+384,104+431) and mousey in range(200,247) and blocksMined>=5000:
                                        currentWorld=2
                                        depth=1
                                        blocks=[]
                                        while depth<150:
                                            for i in range(0,20):
                                                class block:
                                                    x=0
                                                    y=0
                                                    ore='Stone'
                                                    rect=pg.Rect(x,y,32,32)
                                                    hardness=60
                                                    mined=False
                                                    reqPick=0
                                                blocks.append(block)
                                                blocks[-1].x=i*32
                                                blocks[-1].y=350+(depth*32)
                                                blocks[-1].rect=pg.Rect(i,350,32,32)
                                                if currentWorld==2:
                                                    blocks[-1].ore='Regolith'
                                                    blocks[-1].hardness=120*(round(depth/30)+1)
                                                    blocks[-1].reqPick=0
                                                    if depth>5 and random.randint(1,20+depth)==1:
                                                        blocks[-1].ore='Augite'
                                                        blocks[-1].hardness=180
                                                        blocks[-1].reqPick=3
                                                    if depth>10 and random.randint(1,30+depth)==1:
                                                        blocks[-1].ore='Chromite'
                                                        blocks[-1].hardness=200
                                                        blocks[-1].reqPick=4
                                                    if depth>25 and random.randint(1,60)==1:
                                                        blocks[-1].ore='Enstatite'
                                                        blocks[-1].hardness=240
                                                        blocks[-1].reqPick=5
                                                    if depth>35 and random.randint(1,120)==1:
                                                        blocks[-1].ore='Hercynite'
                                                        blocks[-1].hardness=240
                                                        blocks[-1].reqPick=6
                                                    if depth>35 and random.randint(1,120)==1:
                                                        blocks[-1].ore='Troilite'
                                                        blocks[-1].hardness=240
                                                        blocks[-1].reqPick=6
                                                    if depth==145:
                                                        blocks[-1].ore=random.choice(['Regolith','Regolith','Regolith','Regolith','Regolith','Moonstone'])
                                                        if blocks[-1].ore=='Moonstone':
                                                            blocks[-1].hardness=140*(round(depth/30)+1)
                                                            blocks[-1].reqPick=4
                                                        else:
                                                            blocks[-1].hardness=120*(round(depth/30)+1)
                                                            blocks[-1].reqPick=0
                                                    elif depth==146:
                                                        blocks[-1].ore=random.choice(['Regolith','Regolith','Regolith','Regolith','Moonstone'])
                                                        if blocks[-1].ore=='Moonstone':
                                                            blocks[-1].hardness=140*(round(depth/30)+1)
                                                            blocks[-1].reqPick=4
                                                        else:
                                                            blocks[-1].hardness=120*(round(depth/30)+1)
                                                            blocks[-1].reqPick=0
                                                    elif depth==147:
                                                        blocks[-1].ore=random.choice(['Regolith','Regolith','Regolith','Moonstone'])
                                                        if blocks[-1].ore=='Moonstone':
                                                            blocks[-1].hardness=140*(round(depth/30)+1)
                                                            blocks[-1].reqPick=4
                                                        else:
                                                            blocks[-1].hardness=120*(round(depth/30)+1)
                                                            blocks[-1].reqPick=0
                                                    elif depth==148:
                                                        blocks[-1].ore=random.choice(['Regolith','Moonstone'])
                                                        if blocks[-1].ore=='Moonstone':
                                                            blocks[-1].hardness=140*(round(depth/30)+1)
                                                            blocks[-1].reqPick=4
                                                        else:
                                                            blocks[-1].hardness=120*(round(depth/30)+1)
                                                            blocks[-1].reqPick=0
                                                    elif depth==149:
                                                        blocks[-1].ore=random.choice(['Regolith','Moonstone'])
                                                        if blocks[-1].ore=='Moonstone':
                                                            blocks[-1].hardness=140*(round(depth/30)+1)
                                                            blocks[-1].reqPick=4
                                                        else:
                                                            blocks[-1].hardness=120*(round(depth/30)+1)
                                                            blocks[-1].reqPick=0
                                                    elif depth==150:
                                                        blocks[-1].ore='Moonstone'
                                                        blocks[-1].hardness=140*(round(depth/30)+1)
                                                        blocks[-1].reqPick=4
                                                        
                                                
                                            depth+=1
                                        while depth<300:
                                            for i in range(0,20):
                                                class block:
                                                    x=0
                                                    y=0
                                                    ore='Deepstone'
                                                    rect=pg.Rect(x,y,32,32)
                                                    hardness=60
                                                    mined=False
                                                    reqPick=0
                                                blocks.append(block)
                                                blocks[-1].x=i*32
                                                blocks[-1].y=350+(depth*32)
                                                blocks[-1].rect=pg.Rect(i,350,32,32)
                                                blocks[-1].reqPick=2
                                                blocks[-1].hardness=120*(round(depth/30)+1)
                                                if currentWorld==2:
                                                    blocks[-1].ore='Moonstone'
                                                    if random.randint(0,100)==0:
                                                        blocks[-1].ore='Apatite'
                                                        blocks[-1].hardness=600
                                                        blocks[-1].reqPick=6
                                                    elif random.randint(0,100)==0:
                                                        blocks[-1].ore='Forsterite'
                                                        blocks[-1].hardness=600
                                                        blocks[-1].reqPick=7
                                                    elif random.randint(0,100)==0:
                                                        blocks[-1].ore='Fayalite'
                                                        blocks[-1].hardness=800
                                                        blocks[-1].reqPick=7
                                                    elif random.randint(0,80)==0:
                                                        blocks[-1].ore='Spinel'
                                                        blocks[-1].hardness=600
                                                        blocks[-1].reqPick=6
                                                    if depth==294:
                                                        if random.randint(1,2)==1:
                                                            blocks[-1].ore='Anorthite'
                                                            blocks[-1].hardness=120*(round(depth/30)+1)
                                                            blocks[-1].reqPick=4
                                                    if depth==295:
                                                        if random.randint(1,3) in range(1,2):
                                                            blocks[-1].ore='Anorthite'
                                                            blocks[-1].hardness=120*(round(depth/30)+1)
                                                            blocks[-1].reqPick=4
                                                    if depth==296:
                                                        if random.randint(1,4) in range(1,3):
                                                            blocks[-1].ore='Anorthite'
                                                            blocks[-1].hardness=120*(round(depth/30)+1)
                                                            blocks[-1].reqPick=4
                                                    if depth==297:
                                                        if random.randint(1,5) in range(1,4):
                                                            blocks[-1].ore='Anorthite'
                                                            blocks[-1].hardness=120*(round(depth/30)+1)
                                                            blocks[-1].reqPick=4
                                                    if depth==298:
                                                        if random.randint(1,6) in range(1,5):
                                                            blocks[-1].ore='Anorthite'
                                                            blocks[-1].hardness=120*(round(depth/30)+1)
                                                            blocks[-1].reqPick=4
                                                    if depth==299:
                                                        if random.randint(1,7) in range(1,6):
                                                            blocks[-1].ore='Anorthite'
                                                            blocks[-1].hardness=120*(round(depth/30)+1)
                                                            blocks[-1].reqPick=4
                                                        
                                            depth+=1
                                        while depth<500:
                                            for i in range(0,20):
                                                class block:
                                                    x=0
                                                    y=0
                                                    ore='Lavastone'
                                                    rect=pg.Rect(x,y,32,32)
                                                    hardness=60
                                                    mined=False
                                                    reqPick=0
                                                blocks.append(block)
                                                blocks[-1].x=i*32
                                                blocks[-1].y=350+(depth*32)
                                                blocks[-1].rect=pg.Rect(i,350,32,32)
                                                blocks[-1].reqPick=4
                                                blocks[-1].hardness=120*(round(depth/30)+1)
                                                if currentWorld==2:
                                                    blocks[-1].ore='Anorthite'
                                                    blocks[-1].hardness=120*(round(depth/30)+1)
                                                    if random.randint(0,100)==0:
                                                        blocks[-1].ore='Bytownite'
                                                        blocks[-1].hardness=1200
                                                        blocks[-1].reqPick=7
                                                    elif random.randint(0,120)==0:
                                                        blocks[-1].ore='Labradorite'
                                                        blocks[-1].hardness=1800
                                                        blocks[-1].reqPick=8
                                                    elif random.randint(0,120)==0:
                                                        blocks[-1].ore='Pyroxene'
                                                        blocks[-1].hardness=1800
                                                        blocks[-1].reqPick=8
                                                    elif random.randint(0,100)==0:
                                                        blocks[-1].ore='Ulvite'
                                                        blocks[-1].hardness=2400
                                                        blocks[-1].reqPick=9
                                                    elif random.randint(0,100)==0:
                                                        blocks[-1].ore='Plagioclase'
                                                        blocks[-1].hardness=2000
                                                        blocks[-1].reqPick=8
                                            depth+=1
                                        while depth<520:
                                            for i in range(0,20):
                                                class block:
                                                    x=0
                                                    y=0
                                                    ore='Bedrock'
                                                    rect=pg.Rect(x,y,32,32)
                                                    hardness=60
                                                    mined=False
                                                    reqPick=0
                                                blocks.append(block)
                                                blocks[-1].x=i*32
                                                blocks[-1].y=350+(depth*32)
                                                blocks[-1].rect=pg.Rect(i,350,32,32)
                                                blocks[-1].reqPick=0
                                                blocks[-1].hardness=99999999999999999999999999999999999
                                            depth+=1
                                if event.button==4 and shopIndex>0:
                                    shopIndex-=1
                                if event.button==5 and shopIndex<len(pickaxeList)-1:
                                    shopIndex+=1
                            if event.type==pg.MOUSEMOTION:
                                mouserect=pg.Rect(event.pos,(1,1))
                                mousex=event.pos[0]
                                mousey=event.pos[1]
                        for row in range(20):
                            for column in range(20):
                                if row==2 and column==13:
                                    gameDisplay.blit(sapphire,(row*32,column*32))
                                elif row==2 and column==3:
                                    gameDisplay.blit(uranium,(row*32,column*32))
                                elif row==15 and column==17:
                                    gameDisplay.blit(gold,(row*32,column*32))
                                else:
                                    gameDisplay.blit(stone,(row*32,column*32))
                        sellButton=font.render('Back',False,(255,255,255)).get_rect(topleft=(10,10))
                        if mouserect.colliderect(sellButton):
                            gameDisplay.blit(font.render('Back',False,(255,0,0)),(10,10))
                        else:
                            gameDisplay.blit(font.render('Back',False,(255,255,255)),(10,10))
                        if not progMenu:
                            gameDisplay.blit(font.render(pickaxeList[shopIndex],False,(255,255,255)),(320-font.render(pickaxeList[shopIndex],False,(255,255,255)).get_width()/2,100))
                            gameDisplay.blit(pickaxeImgList[shopIndex],(160,160))
                            gameDisplay.blit(font.render(pickaxeDescList[shopIndex],False,(255,255,255)),(320-font.render(pickaxeDescList[shopIndex],False,(255,255,255)).get_width()/2,610))
                            gameDisplay.blit(font.render('Price: $%d'%pickaxePrices[shopIndex],False,(255,255,255)),(320-font.render('Price: %d'%pickaxePrices[shopIndex],False,(255,255,255)).get_width()/2,130))
                            gameDisplay.blit(font.render('Your Money: $%d'%money,False,(255,255,255)),(620-font.render('Your Money: %d'%money,False,(255,255,255)).get_width(),10))
                            blocksminedRect=font.render('Blocks Mined: %d'%blocksMined,False,(255,255,255)).get_rect(topleft=(640-font.render('Blocks Mined: %d'%blocksMined,False,(255,255,255)).get_width(),30))
                            if mouserect.colliderect(blocksminedRect):
                                gameDisplay.blit(font.render('Blocks Mined: %d'%blocksMined,False,(255,0,0)),(640-font.render('Blocks Mined: %d'%blocksMined,False,(255,255,255)).get_width(),30))
                            else:
                                gameDisplay.blit(font.render('Blocks Mined: %d'%blocksMined,False,(255,255,255)),(640-font.render('Blocks Mined: %d'%blocksMined,False,(255,255,255)).get_width(),30))
                            
                            if pickaxeList[shopIndex] in ownedPickaxes:
                                if shopIndex==equippedPickaxe:
                                    shopButton=font.render('Equipped',False,(255,255,255)).get_rect(topleft=(320-font.render('Equipped',False,(255,255,255)).get_width()/2,540))
                                    if mouserect.colliderect(shopButton):
                                        gameDisplay.blit(font.render('Equipped',False,(255,0,0)),(320-font.render('Equipped',False,(255,255,255)).get_width()/2,540))
                                    else:
                                        gameDisplay.blit(font.render('Equipped',False,(255,255,255)),(320-font.render('Equipped',False,(255,255,255)).get_width()/2,540))
                                else:
                                    shopButton=font.render('Equip',False,(255,255,255)).get_rect(topleft=(320-font.render('Equip',False,(255,255,255)).get_width()/2,540))
                                    if mouserect.colliderect(shopButton):
                                        gameDisplay.blit(font.render('Equip',False,(255,0,0)),(320-font.render('Equip',False,(255,255,255)).get_width()/2,540))
                                    else:
                                        gameDisplay.blit(font.render('Equip',False,(255,255,255)),(320-font.render('Equip',False,(255,255,255)).get_width()/2,540))
                            else:
                                shopButton=font.render('Buy',False,(255,255,255)).get_rect(topleft=(320-font.render('Buy',False,(255,255,255)).get_width()/2,540))
                                if mouserect.colliderect(shopButton):
                                    gameDisplay.blit(font.render('Buy',False,(255,0,0)),(320-font.render('Buy',False,(255,255,255)).get_width()/2,540))
                                else:
                                    gameDisplay.blit(font.render('Buy',False,(255,255,255)),(320-font.render('Buy',False,(255,255,255)).get_width()/2,540))
                            
                        else:
                            if blocksMined<=5000:
                                pg.draw.rect(gameDisplay,(255,0,0),pg.Rect(104+48,222,blocksMined/14.8,4))
                            else:
                                pg.draw.rect(gameDisplay,(255,0,0),pg.Rect(104+48,222,5000/14.8,4))
                            gameDisplay.blit(font.render('World Progression',False,(255,255,255)),(320-font.render('World Progression',False,(255,255,255)).get_width()/2,10))
                            gameDisplay.blit(font.render('As you get more experienced with mining,',False,(255,255,255)),(320-font.render('As you get more experienced with mining,',False,(255,255,255)).get_width()/2,500))
                            gameDisplay.blit(font.render('you will unlock new worlds to mine in. ',False,(255,255,255)),(320-font.render('you will unlock new worlds to mine in. ',False,(255,255,255)).get_width()/2,520))
                            gameDisplay.blit(font.render('These new worlds have lots of different minerals,',False,(255,255,255)),(320-font.render('These new worlds have lots of different minerals,',False,(255,255,255)).get_width()/2,540))
                            gameDisplay.blit(font.render('many of which are extremely valuable and will sell',False,(255,255,255)),(320-font.render('many of which are extremely valuable and will sell',False,(255,255,255)).get_width()/2,560))
                            gameDisplay.blit(font.render('for very high prices. ',False,(255,255,255)),(320-font.render('for very high prices. ',False,(255,255,255)).get_width()/2,580))
                            gameDisplay.blit(wpImg,(104,200))
                            gameDisplay.blit(font.render('Blocks Mined: %d'%blocksMined,False,(255,255,255)),(620-font.render('Blocks Mined: %d'%blocksMined,False,(255,255,255)).get_width(),10))
                            if currentWorld==0:
                                gameDisplay.blit(pg.transform.scale(selectionBox,(48,48)),(104,200))
                            if currentWorld==1:
                                gameDisplay.blit(pg.transform.scale(selectionBox,(48,48)),(104+192,200))
                            if currentWorld==2:
                                gameDisplay.blit(pg.transform.scale(selectionBox,(48,48)),(104+384,200))
                            if blocksMined<2500:
                                gameDisplay.blit(locked,(104+192,200))
                                gameDisplay.blit(locked,(104+384,200))
                            if blocksMined in range(2500,4999):
                                gameDisplay.blit(locked,(104+384,200))
                            if mousex in range(104,104+47) and mousey in range(200,247):
                                gameDisplay.blit(font.render('The Earth', False,(255,255,255)),(mousex+12,mousey+12))
                            if mousex in range(104+194,104+239) and mousey in range(200,247):
                                if blocksMined>=2500:
                                    gameDisplay.blit(font.render('Ocean Trench', False,(255,255,255)),(mousex+12,mousey+12))
                                else:
                                    gameDisplay.blit(font.render('Unlock at 2.5k blocks mined', False,(255,255,255)),(mousex+12,mousey+12))
                            if mousex in range(104+384,104+431) and mousey in range(200,247):
                                if blocksMined>=5000:
                                    gameDisplay.blit(font.render('The Moon', False,(255,255,255)),(mousex+12,mousey+12))
                                else:
                                    gameDisplay.blit(font.render('Unlock at 5k blocks mined', False,(255,255,255)),(mousex-130,mousey+10))
                        pg.display.update()
        if event.type==pg.MOUSEBUTTONUP:
            if event.button==1:
                mouseClicked=False
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_a:
                movingLeft=True
                facingLeft=True
            if event.key==pg.K_d:
                movingRight=True
                facingLeft=False
            if event.key==pg.K_SPACE and not playerFalling and jumpable:
                jumping=True
            '''if event.key==pg.K_k:
                kPressed=True''' #admin tool for testing
        if event.type==pg.KEYUP:
            if event.key==pg.K_a:
                movingLeft=False
            if event.key==pg.K_d:
                movingRight=False
            if event.key==pg.K_k:
                kPressed=False
    for i in blocks:
        if i.hardness<=0:
            if stuffInBackpack<backpackCapacity[equippedBackpack] and not i.mined:
                stuffInBackpack+=1
                blocksMined+=1
                if i.ore=='Grass' or i.ore=='Stone' or i.ore=='Deepstone' or i.ore=='Lavastone':
                    moneyInBackpack+=1
                if i.ore=='Coal':
                    moneyInBackpack+=3
                if i.ore=='Iron':
                    moneyInBackpack+=5
                if i.ore=='Gold':
                    moneyInBackpack+=15
                if i.ore=='Ruby':
                    moneyInBackpack+=25
                if i.ore=='Sapphire':
                    moneyInBackpack+=25
                if i.ore=='Emerald':
                    moneyInBackpack+=30
                if i.ore=='Amethyst':
                    moneyInBackpack+=15
                if i.ore=='Diamond':
                    moneyInBackpack+=50
                if i.ore=='Uranium':
                    moneyInBackpack+=30
                if i.ore=='Magnetite':
                    moneyInBackpack+=60
                if i.ore=='Kalite':
                    moneyInBackpack+=70
                if i.ore=='Platinum':
                    moneyInBackpack+=45
                if i.ore=='Malachite':
                    moneyInBackpack+=40
                if i.ore=='Aquamarine':
                    moneyInBackpack+=50
                if i.ore=='Hafnium':
                    moneyInBackpack+=50
                if i.ore=='Mithril':
                    moneyInBackpack+=60
                if i.ore=='Glowstone':
                    moneyInBackpack+=55
                if i.ore=='Illuminite':
                    moneyInBackpack+=75
                if i.ore=='Plutonium':
                    moneyInBackpack+=90
                if i.ore=='Sand':
                    moneyInBackpack+=2
                if i.ore=='Sandstone':
                    moneyInBackpack+=2
                if i.ore=='Quartzite':
                    moneyInBackpack+=2
                if i.ore=='Seashells':
                    moneyInBackpack+=3
                if i.ore=='Coral':
                    moneyInBackpack+=5
                if i.ore=='Fossils':
                    moneyInBackpack+=15
                if i.ore=='Treasure':
                    moneyInBackpack+=25
                if i.ore=='Beryllium':
                    moneyInBackpack+=80
                if i.ore=='Zirconium':
                    moneyInBackpack+=80
                if i.ore=='Topaz':
                    moneyInBackpack+=65
                if i.ore=='Corundum':
                    moneyInBackpack+=60
                if i.ore=='Molybdenum':
                    moneyInBackpack+=70
                if i.ore=='Rubidium':
                    moneyInBackpack+=125
                if i.ore=='Iridium':
                    moneyInBackpack+=130
                if i.ore=='Strontium':
                    moneyInBackpack+=110
                if i.ore=='Yttrium':
                    moneyInBackpack+=135
                if i.ore=='Dravite':
                    moneyInBackpack+=110
                if i.ore=='Regolith':
                    moneyInBackpack+=2
                if i.ore=='Augite':
                    moneyInBackpack+=9
                if i.ore=='Chromite':
                    moneyInBackpack+=15
                if i.ore=='Enstatite':
                    moneyInBackpack+=25
                if i.ore=='Hercynite':
                    moneyInBackpack+=35
                if i.ore=='Troilite':
                    moneyInBackpack+=40
                if i.ore=='Apatite':
                    moneyInBackpack+=25
                if i.ore=='Spinel':
                    moneyInBackpack+=25
                if i.ore=='Forsterite':
                    moneyInBackpack+=30
                if i.ore=='Fayalite':
                    moneyInBackpack+=35
                if i.ore=='Bytownite':
                    moneyInBackpack+=50
                if i.ore=='Labradorite':
                    moneyInBackpack+=75
                if i.ore=='Pyroxene':
                    moneyInBackpack+=120
                if i.ore=='Ulvite':
                    moneyInBackpack+=120
                if i.ore=='Plagioclase':
                    moneyInBackpack+=100
                random.choice([hit1,hit2,hit3,hit4,hit5]).play()
            i.mined=True
        i.rect=pg.Rect(i.x,i.y,32,30)
        if playerFalling and not jumping:
            i.y-=int(downAccel)
            if currentWorld==2:
                downAccel+=0.000025
            else:
                downAccel+=0.00005
        if playerBottomRect2.colliderect(i.rect) and kPressed and i.ore!='Bedrock':
            i.hardness=0
            i.mined=True
        if not i.mined and i.y<640 and i.y>-32:
            if i.ore=='Grass':
                gameDisplay.blit(grass,(i.x,i.y))
            if i.ore=='Stone':
                gameDisplay.blit(stone,(i.x,i.y))
            if i.ore=='Coal':
                gameDisplay.blit(coal,(i.x,i.y))
            if i.ore=='Iron':
                gameDisplay.blit(iron,(i.x,i.y))
            if i.ore=='Gold':
                gameDisplay.blit(gold,(i.x,i.y))
            if i.ore=='Ruby':
                gameDisplay.blit(ruby,(i.x,i.y))
            if i.ore=='Sapphire':
                gameDisplay.blit(sapphire,(i.x,i.y))
            if i.ore=='Amethyst':
                gameDisplay.blit(amethyst,(i.x,i.y))
            if i.ore=='Diamond':
                gameDisplay.blit(diamond,(i.x,i.y))
            if i.ore=='Uranium':
                gameDisplay.blit(uranium,(i.x,i.y))
            if i.ore=='Emerald':
                gameDisplay.blit(emerald,(i.x,i.y))
            if i.ore=='Deepstone':
                gameDisplay.blit(deepstone,(i.x,i.y))
            if i.ore=='Magnetite':
                gameDisplay.blit(magnetite,(i.x,i.y))
            if i.ore=='Kalite':
                gameDisplay.blit(kalite,(i.x,i.y))
            if i.ore=='Platinum':
                gameDisplay.blit(platinum,(i.x,i.y))
            if i.ore=='Malachite':
                gameDisplay.blit(malachite,(i.x,i.y))
            if i.ore=='Lavastone':
                gameDisplay.blit(lavastone,(i.x,i.y))
            if i.ore=='Mithril':
                gameDisplay.blit(mithril,(i.x,i.y))
            if i.ore=='Glowstone':
                gameDisplay.blit(glowstone,(i.x,i.y))
            if i.ore=='Illuminite':
                gameDisplay.blit(illuminite,(i.x,i.y))
            if i.ore=='Hafnium':
                gameDisplay.blit(hafnium,(i.x,i.y))
            if i.ore=='Bedrock':
                gameDisplay.blit(bedrock,(i.x,i.y))
            if i.ore=='Sand':
                gameDisplay.blit(sand,(i.x,i.y))
            if i.ore=='Sandstone':
                gameDisplay.blit(sandstone,(i.x,i.y))
            if i.ore=='Slate':
                gameDisplay.blit(slate,(i.x,i.y))
            if i.ore=='Quartzite':
                gameDisplay.blit(quartzite,(i.x,i.y))
            if i.ore=='Seashells':
                gameDisplay.blit(seashells,(i.x,i.y))
            if i.ore=='Fossils':
                gameDisplay.blit(fossils,(i.x,i.y))
            if i.ore=='Treasure':
                gameDisplay.blit(treasure,(i.x,i.y))
            if i.ore=='Coral':
                gameDisplay.blit(coral,(i.x,i.y))
            if i.ore=='Beryllium':
                gameDisplay.blit(beryllium,(i.x,i.y))
            if i.ore=='Corundum':
                gameDisplay.blit(corundum,(i.x,i.y))
            if i.ore=='Topaz':
                gameDisplay.blit(topaz,(i.x,i.y))
            if i.ore=='Zirconium':
                gameDisplay.blit(zirconium,(i.x,i.y))
            if i.ore=='Rubidium':
                gameDisplay.blit(rubidium,(i.x,i.y))
            if i.ore=='Strontium':
                gameDisplay.blit(strontium,(i.x,i.y))
            if i.ore=='Yttrium':
                gameDisplay.blit(yttrium,(i.x,i.y))
            if i.ore=='Dravite':
                gameDisplay.blit(dravite,(i.x,i.y))
            if i.ore=='Iridium':
                gameDisplay.blit(iridium,(i.x,i.y))
            if i.ore=='Regolith':
                gameDisplay.blit(regolith,(i.x,i.y))
            if i.ore=='Moonstone':
                gameDisplay.blit(moonstone,(i.x,i.y))
            if i.ore=='Anorthite':
                gameDisplay.blit(anorthite,(i.x,i.y))
            if i.ore=='Augite':
                gameDisplay.blit(augite,(i.x,i.y))
            if i.ore=='Chromite':
                gameDisplay.blit(chromite,(i.x,i.y))
            if i.ore=='Enstatite':
                gameDisplay.blit(enstatite,(i.x,i.y))
            if i.ore=='Hercynite':
                gameDisplay.blit(hercynite,(i.x,i.y))
            if i.ore=='Troilite':
                gameDisplay.blit(troilite,(i.x,i.y))
            if i.ore=='Apatite':
                gameDisplay.blit(apatite,(i.x,i.y))
            if i.ore=='Fayalite':
                gameDisplay.blit(fayalite,(i.x,i.y))
            if i.ore=='Spinel':
                gameDisplay.blit(spinel,(i.x,i.y))
            if i.ore=='Forsterite':
                gameDisplay.blit(forsterite,(i.x,i.y))
            if i.ore=='Bytownite':
                gameDisplay.blit(bytownite,(i.x,i.y))
            if i.ore=='Labradorite':
                gameDisplay.blit(labradorite,(i.x,i.y))
            if i.ore=='Pyroxene':
                gameDisplay.blit(pyroxene,(i.x,i.y))
            if i.ore=='Ulvite':
                gameDisplay.blit(ulvite,(i.x,i.y))
            if i.ore=='Plagioclase':
                gameDisplay.blit(plagioclase,(i.x,i.y))
            if i.ore=='Aquamarine':
                gameDisplay.blit(aquamarine,(i.x,i.y))
            if i.ore=='Plutonium':
                gameDisplay.blit(plutonium,(i.x,i.y))
            if i.ore=='Molybdenum':
                gameDisplay.blit(molybdenum,(i.x,i.y))
        elif i.y<640 and i.y>-32:
            if i.ore=='Grass':
                gameDisplay.blit(minedGrass,(i.x,i.y))
            elif i.ore=='Sand':
                gameDisplay.blit(minedSand,(i.x,i.y))
            elif i.ore=='Deepstone' or i.ore=='Kalite' or i.ore=='Magnetite' or i.ore=='Platinum' or i.ore=='Malachite' or i.ore=='Aquamarine':
                gameDisplay.blit(minedDeepstone,(i.x,i.y))
            elif i.ore=='Lavastone' or i.ore=='Hafnium' or i.ore=='Glowstone' or i.ore=='Illuminite' or i.ore=='Mithril' or i.ore=='Plutonium':
                gameDisplay.blit(minedLavastone,(i.x,i.y))
            elif i.ore=='Sandstone' or i.ore=='Coral' or i.ore=='Fossils' or i.ore=='Seashells' or i.ore=='Treasure':
                gameDisplay.blit(minedSandstone,(i.x,i.y))
            elif i.ore=='Slate' or i.ore=='Beryllium' or i.ore=='Corundum' or i.ore=='Topaz' or i.ore=='Zirconium' or i.ore=='Molybdenum':
                gameDisplay.blit(minedSlate,(i.x,i.y))
            elif i.ore=='Quartzite' or i.ore=='Rubidium' or i.ore=='Strontium' or i.ore=='Yttrium' or i.ore=='Dravite' or i.ore=='Iridium':
                gameDisplay.blit(minedQuartzite,(i.x,i.y))
            elif i.ore=='Regolith' or i.ore=='Augite' or i.ore=='Hercynite' or i.ore=='Enstatite' or i.ore=='Chromite' or i.ore=='Troilite':
                gameDisplay.blit(minedRegolith,(i.x,i.y))
            elif i.ore=='Moonstone' or i.ore=='Apatite' or i.ore=='Forsterite' or i.ore=='Spinel' or i.ore=='Fayalite':
                gameDisplay.blit(minedMoonstone,(i.x,i.y))
            elif i.ore=='Anorthite' or i.ore=='Bytownite' or i.ore=='Labradorite' or i.ore=='Pyroxene' or i.ore=='Ulvite' or i.ore=='Plagioclase':
                gameDisplay.blit(minedAnorthite,(i.x,i.y))
            else:
                gameDisplay.blit(minedStone,(i.x,i.y))
        if mouserect.colliderect(i.rect) and not i.mined:
            if rangeTop.colliderect(i.rect) or rangeSide.colliderect(i.rect) or rangeBottom.colliderect(i.rect) :
                gameDisplay.blit(selectionBox,(i.x,i.y))
                if stuffInBackpack<backpackCapacity[equippedBackpack]:
                    if equippedPickaxe<i.reqPick:
                        gameDisplay.blit(sfont.render('You need a %s'%pickaxeList[i.reqPick],False,(255,255,255)),(320-sfont.render('You need a %s'%pickaxeList[i.reqPick],False,(255,255,255)).get_width()/2,10))
                        gameDisplay.blit(sfont.render('or better to mine this ore!',False,(255,255,255)),(320-sfont.render('or better to mine this ore!',False,(255,255,255)).get_width()/2,20))
                    else:
                        gameDisplay.blit(font.render(i.ore,False,(255,255,255)),(320-font.render(i.ore,False,(255,255,255)).get_width()/2,10))
                        gameDisplay.blit(font.render(str(round(i.hardness/60,ndigits=1)),False,(255,255,255)),(320-font.render(str(round(i.hardness/60,ndigits=1)),False,(255,255,255)).get_width()/2,40))
                else:
                    gameDisplay.blit(font.render('Your backpack is full!',False,(255,255,255)),(320-font.render('Your backpack is full!',False,(255,255,255)).get_width()/2,10))
                if mouseClicked and stuffInBackpack<backpackCapacity[equippedBackpack] and not playerFalling and equippedPickaxe>=i.reqPick:
                    i.hardness-=1*pickaxeStrs[equippedPickaxe]
                    if miraculousLadybug%20==0 and mouseClicked:
                        random.choice([hit1,hit2,hit3,hit4,hit5]).play()
    if facingLeft:
        if mouseClicked:
            gameDisplay.blit(minerAnimationLeft[int(miraculousLadybug/5%4)],(x,y))
        else:
            gameDisplay.blit(playerLeft,(x,y))
    else:
        if mouseClicked:
            gameDisplay.blit(minerAnimation[int(miraculousLadybug/5%4)],(x,y))
        else:
            gameDisplay.blit(player,(x,y))
    for i in blocks:
        if playerBottomRect.colliderect(i.rect) and playerBottomRect2.colliderect(i.rect) and not i.mined:
            playerFalling=False
            downAccel=1
            break
        else:
            playerFalling=True
    for i in blocks:
        if playerRectLeft.colliderect(i.rect) and not i.mined:
            canMoveLeft=False
            break
        else:
            canMoveLeft=True
    for i in blocks:
        if playerRectRight.colliderect(i.rect) and not i.mined:
            canMoveRight=False
            break
        else:
            canMoveRight=True
    for i in blocks:
        if playerBottomRect2.colliderect(i.rect) and not i.mined:
            y=i.y-53
            break
    for i in blocks:
        if i.rect.colliderect(playerTopRect) and not i.mined:
            jumpable=False
            break
        else:
            jumpable=True
    if jumping and jumpCounter<8:
        jumpCounter+=1
        y-=5
    if jumpCounter>=8:
        jumpCounter+=1
        if currentWorld==2:
            y+=2
        else:
            y+=5
    if jumpCounter>16:
        jumpCounter=0
        jumping=False
    if movingLeft and x>0 and canMoveLeft:
        x-=3
    if movingRight and x<600 and canMoveRight:
        x+=3
    gameDisplay.blit(font.render('Mochila: %d/%d'%(stuffInBackpack,backpackCapacity[equippedBackpack]),False,(255,255,255)),(640-font.render('Backpack: %d/%d'%(stuffInBackpack,backpackCapacity[equippedBackpack]),False,(255,255,255)).get_width(),10))
    sellButton=font.render('Vender Itens',False,(255,255,255)).get_rect(topleft=(495,30))
    if mouserect.colliderect(sellButton):
        gameDisplay.blit(font.render('Vender Itens',False,(255,0,0)),(495,30))
    else:
        gameDisplay.blit(font.render('Vender Itens',False,(255,255,255)),(495,30))
    surfaceButton=font.render('Voltar',False,(255,255,255)).get_rect(topleft=(535,70))
    if mouserect.colliderect(surfaceButton):
        gameDisplay.blit(font.render('Voltar',False,(255,0,0)),(535,70))
    else:
        gameDisplay.blit(font.render('Voltar',False,(255,255,255)),(535,70))
    shopButton=font.render('Loja',False,(255,255,255)).get_rect(topleft=(545,50))
    if mouserect.colliderect(shopButton):
        gameDisplay.blit(font.render('Loja',False,(255,0,0)),(545,50))
    else:
        gameDisplay.blit(font.render('Loja',False,(255,255,255)),(545,50))
    gameDisplay.blit(font.render('Dinheiro: $%d'%money,False,(255,255,255)),(10,10))
    if y<222:
        for i in blocks:
            i.y+=1
        y+=1
    gameDisplay.blit(font.render('Camada: %d'%playerDepth,False,(255,255,255)),(10,620))
    playerRectLeft=pg.Rect(x-2,y,23,50)
    playerRectRight=pg.Rect(x+21,y,23,50)
    playerBottomRect=pg.Rect(x+5,y+50,32,4)
    playerTopRect=pg.Rect(x+4,y-20,32,20)
    playerBottomRect2=pg.Rect(x+4,y+50,32,8)
    clock.tick(60)
    rangeTop=pg.Rect(x-14,y-20,70,20)
    rangeSide=pg.Rect(x-14,y,70,40)
    rangeBottom=pg.Rect(x+5,y+50,34,10)
    pg.display.update()
