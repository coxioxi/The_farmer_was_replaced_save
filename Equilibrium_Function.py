import Traverse_Farm
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
			
	def evaluate_plant(position):
		hay_num = num_items(Items.Hay)
		wood_num = num_items(Items.Wood)
		carrot_num = num_items(Items.Carrot)
		pumpkin_num = num_items(Items.Pumpkin)
		
		if hay_num <= wood_num and hay_num < pumpkin_num:
			Plantation.getHay()
		elif wood_num <= hay_num and wood_num < pumpkin_num:
			Plantation.getWood(position)
		else:
			if carrot_num < 10000:
				Plantation.getCarrot()
			else:
				Plantation.getPumpkin()

	location = 0
	while True:
		
		harv()
		Plantation.waterAnal()
		evaluate_plant(location)
		Traverse_Farm.traverse()
		location += 1

			
if __name__ == "__main__":
	main()