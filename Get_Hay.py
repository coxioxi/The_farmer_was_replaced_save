import Traverse_Farm
import Plantation

def main():
	Plantation.harv()
	if get_ground_type() != Grounds.Grassland:
		till()
	Traverse_Farm.main()
	
if __name__ == "__main__":
	main()