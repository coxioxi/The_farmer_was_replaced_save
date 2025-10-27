def harv():
	if(can_harvest()):
		harvest()
					
def waterAnal():
	if get_water() <= 0.15:
		use_item(Items.Water)
	
	