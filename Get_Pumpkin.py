import Traverse_Farm
import Plantation

def main():
	Plantation.harv()
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Pumpkin)
	Traverse_Farm.main()
	
if __name__ == "__main__":
	main()