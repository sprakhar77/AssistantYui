import random
import single_input


class Board(object):
	def __init__(self, size):
		self.size = size
		self.board = [[0] * self.size for i in range (self.size)]
		self.empty_cell = []

	def update_empty_cell(self):
		self.empty_cell[:] = []
		for i in range (self.size):
			for j in range (self.size):
				if self.board[i][j] == 0:
					self.empty_cell.append((i, j))
		return len(self.empty_cell)

	def generate_random(self):
		if self.update_empty_cell():
			random.seed(None)
			index = random.randrange(len(self.empty_cell))
			value = random.randrange(1, 3) * 2
			x, y = self.empty_cell[index]
			self.board[x][y] = value
			return True
		return False

	def print_board(self):
		for row in range (self.size):
			for col in range(self.size):
				print self.board[row][col], 
			print
		print


class Game(object):
	def __init__(self, name, board):
		self.score = 0
		self.name = name
		self.board = board
		self.size = self.board.size

	def handle_up_util(self):
		for col in range (self.size):
			for row in range(self.size):
				temp = row
				while (self.board.board[temp][col] != 0) and \
					  (temp - 1 >= 0) and (self.board.board[temp - 1][col] == 0):
					self.board.board[temp - 1][col] = self.board.board[temp][col]
					self.board.board[temp][col] = 0
					temp -= 1

	def handle_up(self):
		self.handle_up_util()
		for col in range (self.size):
			for row in range(self.size):
				if (self.board.board[row][col] != 0) and \
				   (row - 1 >= 0) and (self.board.board[row][col] ==\
									   self.board.board[row - 1][col]):
					self.board.board[row - 1][col] *= 2
					self.board.board[row][col] = 0
		self.handle_up_util()

	def handle_left_util(self):
		for row in range (self.size):
			for col in range(self.size):
				temp = col
				while (self.board.board[row][temp] != 0) and \
					  (temp - 1 >= 0) and (self.board.board[row][temp - 1] == 0):
					self.board.board[row][temp - 1] = self.board.board[row][temp]
					self.board.board[row][temp] = 0
					temp -= 1

	def handle_left(self):
		self.handle_left_util()
		for row in range (self.size):
			for col in range(self.size):
				if (self.board.board[row][col] != 0) and \
				   (col - 1 >= 0) and (self.board.board[row][col] ==\
									   self.board.board[row][col - 1]):
					self.board.board[row][col - 1] *= 2
					self.board.board[row][col] = 0
		self.handle_left_util()

	def handle_down_util(self):
		for col in range (self.size):
			for row in xrange(self.size - 1, -1, -1):
				temp = row
				while (self.board.board[temp][col] != 0) and \
					  (temp + 1 < self.size) and (self.board.board[temp + 1][col] == 0):
					self.board.board[temp + 1][col] = self.board.board[temp][col]
					self.board.board[temp][col] = 0
					temp += 1

	def handle_down(self):
		self.handle_down_util()
		for col in range (self.size):
			for row in xrange(self.size - 1, -1, -1):
				if (self.board.board[row][col] != 0) and \
				   (row + 1 < self.size) and (self.board.board[row][col] ==\
									   self.board.board[row + 1][col]):
					self.board.board[row + 1][col] *= 2
					self.board.board[row][col] = 0
		self.handle_down_util()

	def handle_right_util(self):
		for row in range (self.size):
			for col in xrange(self.size - 1, -1, -1):
				temp = col
				while (self.board.board[row][temp] != 0) and \
					  (temp + 1 < self.size) and (self.board.board[row][temp + 1] == 0):
					self.board.board[row][temp + 1] = self.board.board[row][temp]
					self.board.board[row][temp] = 0
					temp += 1


	def handle_right(self):
		self.handle_right_util()
		for row in range (self.size):
			for col in xrange(self.size - 1, -1, -1):
				if (self.board.board[row][col] != 0) and \
				   (col + 1 < self.size) and (self.board.board[row][col] ==\
									   self.board.board[row][col + 1]):
					self.board.board[row][col + 1] *= 2
					self.board.board[row][col] = 0
		self.handle_right_util()

	def handle_move(self, move):
		if move == 'w':
			self.handle_up()
		elif move == 'a':
			self.handle_left()
		elif move == 's':
			self.handle_down()
		elif move == 'd':
			self.handle_right()
		elif move == 'q':
			exit(0)
		else:
			print "Invalid move! Try again"
	def play(self):
		while self.board.generate_random():
			self.board.print_board()
			self.handle_move(single_input.getch())
		print "Game Over"

board = Board(4)
game = Game("Prakhar", board)
game.play()