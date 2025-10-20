def main():
	def reset_pos():
		while get_pos_y() != 0:
			move(South)
		while get_pos_x() != 0:
			move(West)

if __name__ == "__main__":
	main()