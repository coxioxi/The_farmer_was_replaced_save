import Traverse_Farm
import Plantation

def main():
	Plantation.harv()
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Carrot)
	Traverse_Farm.main()
	
if __name__ == "__main__":
	main()