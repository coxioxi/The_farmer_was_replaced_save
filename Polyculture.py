import Choose_Class
import Traverse_Farm
import Plantation
import Equilibrium_Function
import Get_Hay
import Get_Wood
import Get_Carrot
import Get_Pumpkin

dict1 = {}

def main():		
	def poly_check(dict):
		if get_companion() != None:
			plant_type, coordinates = get_companion()
			dict[(coordinates)] = plant_type
			x, y = get_pos_x(),get_pos_y()
			if (x, y) in dict:
				if dict[(x,y)] == Entities.Carrot:
					Get_Carrot.main()
				elif dict[(x,y)] == Entities.Grass:
					Get_Hay.main()
				else:
					plant(dict[(x,y)])
				dict.pop((x,y)) # Remove the value after planting the companion
			else:
				Plantation.harv()
				Traverse_Farm.main()
		else:
			list = [Get_Hay.main, Get_Wood.main, Get_Carrot.main]
			list[random()*len(list)//1]()
		Plantation.waterAnal()
				
	while True:	
		poly_check(dict1)
		#Choose_Class.main(True)
	
		
if __name__ == "__main__":
	main()
	