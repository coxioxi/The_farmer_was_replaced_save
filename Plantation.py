def getWood():
	location = 0
	if location % 2 != 0:
		plant(Entities.Tree)
	else:
		plant(Entities.Bush)
	location += 1
			
def getHay():
	if get_ground_type() != Grounds.Grassland:
		till()
		
def getCarrot():
	if get_ground_type() != Grounds.Soil:
			till()
	plant(Entities.Carrot)
		
def getPumpkin():
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Pumpkin)

def harv():
	if(can_harvest()):
		harvest()
					
def waterAnal():
	if get_water() <= 0.15:
		use_item(Items.Water)
	
	