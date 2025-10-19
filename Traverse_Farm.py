def reset_pos():
	x, y = get_pos_x(), get_pos_y()
	while y != 0:
		move(South)
	while x != 0:
		move(West)

def traverse():
	x, y = get_pos_x(), get_pos_y()
	
	if x % 2 == 0 and y != get_world_size()-1:
		move(North)
	elif y == get_world_size()-1 or y == 0:
		move(East)
	elif x % 2 != 0:
		move(South)
	elif x == get_world_size()-1 and y == 0:
		reset_pos()