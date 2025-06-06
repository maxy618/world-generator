import numpy as np
from matplotlib.colors import to_rgb


name_to_rgb = lambda name: (np.array(to_rgb(name)) * 255).astype('uint8')


WATER = name_to_rgb('blue')
GROUND = name_to_rgb('saddlebrown')
MOUNTAIN = name_to_rgb('grey')
SAND = name_to_rgb('navajowhite')
SNOW = name_to_rgb('white')
SWAMP = name_to_rgb('seagreen')
VOLCANO = name_to_rgb('dimgray')
ASH = name_to_rgb('lightgray')
FLOWER_FIELD = name_to_rgb('mediumspringgreen')


FORESTS = {
    'taiga': name_to_rgb('darkgreen'),
    'oak': name_to_rgb('green'),
    'acacia': name_to_rgb('lightgreen'),
    'jungle': name_to_rgb('limegreen'),
    'sakura': name_to_rgb('lightpink')
}


BIOMES = {
    'mountain': (MOUNTAIN),
    'taiga_forest': (FORESTS['taiga'], GROUND, SAND),
    'oak_forest': (FORESTS['oak'], GROUND, SAND),
    'acacia_forest': (FORESTS['acacia'], GROUND, SAND),
    'sakura_forest': (FORESTS['sakura'], GROUND, SAND),
    'jungle': (FORESTS['jungle'], GROUND, SAND),
    'desert': (SAND),
    'swamp': (SWAMP, GROUND, SAND),
    'volcano': (VOLCANO, ASH, GROUND),
    'snowy_mountain': (SNOW, MOUNTAIN, GROUND),
}