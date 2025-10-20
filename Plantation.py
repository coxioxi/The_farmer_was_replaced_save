import Reset_position

def getWood():
	if get_pos_y() % 2 != 0:
		plant(Entities.Tree)
	else:
		plant(Entities.Bush)
			
def getHay():
	if get_ground_type() != Grounds.Grassland:
		till()
		
def getCarrot():
	if get_ground_type() != Grounds.Soil:
			till()
	plant(Entities.Carrot)
		
def getPumpkin():
	alive_pump = False
	
	for i in range(2):
		for j in range(get_world_size()):
			for k in range(get_world_size()):
				if get_ground_type() != Grounds.Soil:
					till()
				if i % 2 == 0:
					move(North)
				else:
					move(South)
				if not can_harvest():
					plant(Entities.Pumpkin)
					
			if i == get_world_size()-1:
				Reset_position.main()
			else:
				move(East)
					
def waterAnal():
	if get_water() <= 0.5:
		use_item(Items.Water)
	
	