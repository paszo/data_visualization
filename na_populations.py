from pygal.maps.world import World

wm = World()
wm.title = 'Populations of Countries in North America.'
wm.add('North America', {'ca': 34125000, 'us': 300940303, 'mx': 111134343})

wm.render_to_file('na_populaions.svg')
