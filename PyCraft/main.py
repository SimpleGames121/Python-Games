from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina(title='PyCraft', development_mode=False)
player = FirstPersonController()
Sky()
#EditorCamera()
f = open("assets/worldgen/data", "r")

worldgendata = f.read().split()
width = int(worldgendata[2])
levelzero = -6
buildingblock = worldgendata[1]
blockholding = worldgendata[0]



boxes = []
l1 = PointLight(y=20)
l2 = PointLight(y=20,z=width)
l3 = PointLight(x=width,y=20)
l4 = PointLight(x=width,y=20,z=width)
text = Text(text=buildingblock, origin=(0,0), world_scale=20)
for i in range(width):
  for j in range(width):
    box = Button(color=color.white, model='cube', position=(j, 0, i), texture=f'assets/textures/blocks/{blockholding}.png',parent=scene, origin_y=0.5)
    boxes.append(box)

def Quit():
  print('ESC')
  sys.exit()

def input(key):
  global buildingblock
  if key == 'escape':
    Quit()
  for box in boxes:
    if box.hovered:
      if key == 'right mouse down':
        new = Button(color=color.white, model='cube', position=box.position + mouse.normal, texture=f'assets/textures/blocks/{buildingblock}.png', parent=scene, origin_y=0.5)
        boxes.append(new)
      if key == 'left mouse down':
        boxes.remove(box)
        destroy(box)

  match key:
    case '1':
      buildingblock = 'dirt'
    case '2':
      buildingblock = 'diamond_block'
    case '3':
      buildingblock = 'acacia_planks'
    case '4':
      buildingblock = 'bamboo_mosaic'
    case '5':
      buildingblock = 'birch_planks'
    case '6':
      buildingblock = 'emerald_block'
    case '7':
      buildingblock = 'glass'
    case '8':
      buildingblock = 'jungle_planks'
    case '9':
      buildingblock = 'obsidian'
    case '0':
      buildingblock = 'stone_block'

def respawn():
  spawnPlayer()

def update():
  if player.y < -10:
    print('You Felt')
    respawn()

  text.text = buildingblock

#UI

#End UI

def spawnPlayer():
  x = random.randint(1,width-1)
  z = random.randint(1,width-1)
  player.position = (x,3,z)

spawnPlayer()
app.run()
