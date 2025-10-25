import Polyculture
import Equilibrium_Function

def main(poly):
	if (num_items(Items.Hay) + num_items(Items.Wood) + num_items(Items.Carrot) > 3 * num_items(Items.Pumpkin)) and poly:
		Equilibrium_Function.main()
	elif (num_items(Items.Hay) + num_items(Items.Wood) + num_items(Items.Carrot) < 3 * num_items(Items.Pumpkin)) and not poly:
		Polyculture.main()
	else:
		return

if __name__ == "__main":
	main()
	