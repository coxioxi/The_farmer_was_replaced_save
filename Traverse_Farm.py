def reset_pos():
	x, y = get_pos_x(), get_pos_y()
	while y != 0:
		move(South)
	while x != 0:
		move(West)

def traverse():
	moved = False

	if get_pos_x() % 2 == 0 and get_pos_y() != get_world_size()-1:
		move(North)
		if get_pos_y() + 1 != get_world_size()-1:
			moved = True
	elif get_pos_x() % 2 != 0 and get_pos_y() != 0:
		move(South)
		if get_pos_y() - 1 != 0:
			moved = True

	if (not moved and (get_pos_y() == get_world_size()-1 or get_pos_y() == 0)):
		move(East)
		