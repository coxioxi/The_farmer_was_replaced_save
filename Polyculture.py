import Choose_Class
import Traverse_Farm
import Plantation
import Equilibrium_Function

dict1 = {}

def main():		
	def poly_check(dict):
		if get_companion() != None:
			plant_type, coordinates = get_companion()
			dict[(coordinates)] = plant_type
			x, y = get_pos_x(),get_pos_y()
			if (x, y) in dict:
				if dict[(x,y)] == Entities.Carrot:
					Plantation.getCarrot()
				elif dict[(x,y)] == Entities.Grass:
					Plantation.getHay()
				else:
					plant(dict[(x,y)])
				dict.pop((x,y)) # Remove the value after planting the companion
		else:
			list = [Plantation.getHay, Plantation.getWood, Plantation.getCarrot]
			list[random()*len(list)//1]()
		Plantation.harv()
		Plantation.waterAnal()
				
	while True:	
		poly_check(dict1)
		Traverse_Farm.main()
		Choose_Class.main(True)
	
		
if __name__ == "__main__":
	main()
	