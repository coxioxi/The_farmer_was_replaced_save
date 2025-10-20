import Reset_position

def getWood():
	if get_pos_x() % 2 != 0:
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
	
	for i in range(get_world_size()):
		for j in range(get_world_size()-1):
			plant(Entities.Pumpkin)
			if get_ground_type() != Grounds.Soil:
				till()
			if i % 2 == 0:
				move(North)
			else:
				move(South)
			plant(Entities.Pumpkin)
					
		if i == get_world_size()-1:
			Reset_position.reset_pos()
		else:
			move(East)
		plant(Entities.Pumpkin)
					
def waterAnal():
	if get_water() <= 0.5:
		use_item(Items.Water)
	
	