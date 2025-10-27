import Choose_Class
import Traverse_Farm
import Plantation
import Polyculture
import Get_Hay
import Get_Wood
import Get_Carrot
import Get_Pumpkin

def main():		

	# Check the item with least amount and plant it	
	while True:
		if get_pos_x() == 0 and get_pos_y() == 0:
			hay_num = num_items(Items.Hay)
			wood_num = num_items(Items.Wood)
			carrot_num = num_items(Items.Carrot)
			pumpkin_num = num_items(Items.Pumpkin)

		Plantation.waterAnal()
		if hay_num <= wood_num and hay_num < pumpkin_num:
			Get_Hay.main()
		elif wood_num <= hay_num and wood_num < pumpkin_num:
			Get_Wood.main()
		else:
			if pumpkin_num > 2 * carrot_num:
				Get_Carrot.main()
			else:
				Get_Pumpkin.main()
		#Choose_Class.main(False)

			
if __name__ == "__main__":
	main()