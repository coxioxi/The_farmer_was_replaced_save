import Traverse_FArm
import Plantation
import Polyculture

def main():
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
		
		harv()
		Plantation.waterAnal()
		evaluate_plant(hay_num, wood_num, carrot_num, pumpkin_num)
		Traverse_FArm.traverse()
		#Polyculture.main()
			
						
if __name__ == "__main__":
	main()