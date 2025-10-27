import Traverse_Farm
import Plantation

def main():
	Plantation.harv()
	if get_pos_x() % 2 == 0 and get_pos_y() % 2 == 0:
		plant(Entities.Tree)
	elif get_pos_x() % 2 != 0 and (get_pos_y()+1) % 2 == 0:
		plant(Entities.Tree)
	else:
		plant(Entities.Bush)
	Traverse_Farm.main()
	
if __name__ == "__main__":
	main()