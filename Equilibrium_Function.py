import Choose_Class
import Traverse_Farm
import Plantation
import Polyculture

def main():	
	def evaluate_plant(position):
		hay_num = num_items(Items.Hay)
		wood_num = num_items(Items.Wood)
		carrot_num = num_items(Items.Carrot)
		pumpkin_num = num_items(Items.Pumpkin)

		Plantation.harv()
		Plantation.waterAnal()
		if hay_num <= wood_num and hay_num < pumpkin_num:
			Plantation.getHay()
		elif wood_num <= hay_num and wood_num < pumpkin_num:
			Plantation.getWood(position)
		else:
			if pumpkin_num > 2 * carrot_num:
				Plantation.getCarrot()
			else:
				Plantation.getPumpkin()

	location = 0
	while True:
		evaluate_plant(location)
		Traverse_Farm.main()
		location += 1
		Choose_Class.main(False)

			
if __name__ == "__main__":
	main()