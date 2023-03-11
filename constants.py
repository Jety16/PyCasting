import math

WIN_HEIGHT = 1080
WIN_WIDTH = 2 * WIN_HEIGHT
WIN_TITLE = 'RayCasting'

FOV = math.pi / 3
HALF_FOV = int(FOV / 2)

RAYS = 120
STEP_ANGLE = FOV / RAYS

SCALE = int(WIN_WIDTH / RAYS)