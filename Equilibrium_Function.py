import Plantation
import Polyculture

def main():
	def reset_pos():
		while get_pos_y() != 0:
			move(South)
		while get_pos_x() != 0:
			move(West)
	
	def harv():
		if(can_harvest()):
			harvest()
			
	def evaluate_plant(hay_num, wood_num, carrot_num, pumpkin_num):
		if hay_num <= wood_num and hay_num < pumpkin_num:
			Plantation.getHay()
		elif wood_num <= hay_num and wood_num < pumpkin_num:
			Plantation.getWood(location)
		else:
			Plantation.getPumpkin()

	while True:
		hay_num = num_items(Items.Hay)
		wood_num = num_items(Items.Wood)
		carrot_num = num_items(Items.Carrot)
		pumpkin_num = num_items(Items.Pumpkin)
		
		for i in range(get_world_size()):
			for j in range(get_world_size()-1):
				harv()
				Plantation.waterAnal()
				evaluate_plant(hay_num, wood_num, carrot_num, pumpkin_num)
				if i % 2 == 0:
					move(North)
				else:
					move(South)
			
			harv()
			Plantation.waterAnal()
			evaluate_plant(hay_num, wood_num, carrot_num, pumpkin_num)
			if i == get_world_size()-1:
				reset_pos()
			else:
				move(East)
			#Polyculture.main()

			
if __name__ == "__main__":
	main()