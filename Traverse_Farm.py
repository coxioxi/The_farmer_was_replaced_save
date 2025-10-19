def reset_pos():
	x, y = get_pos_x(), get_pos_y()
	while y != 0:
		move(South)
	while x != 0:
		move(West)

def traverse():
	x, y = get_pos_x(), get_pos_y()
	
	for i in range(get_world_size()):
		for j in range(get_world_size()-1):
			if i % 2 == 0:
				move(North)
				break
			else:
				move(South)
				break
		
		if i == get_world_size()-1:
			reset_pos()
			break
		else:
			move(East)
			break