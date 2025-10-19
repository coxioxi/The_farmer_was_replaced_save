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
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Pumpkin)
			
	

def waterAnal():
	if get_water() <= 0.5:
		use_item(Items.Water)
	
	