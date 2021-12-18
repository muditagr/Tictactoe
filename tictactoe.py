# -*- coding: utf-8 -*-

class TicTacToe(object):
	def __init__(self):
		self.board = {}
		self.player = None


	def createBoard(self):
		for i in range(1,10):
			self.board[str(i)] = " "
		self.printBoard()

	def choosePlayer(self):
		while True:
			try:
				player = str.upper(str(input("Player one, please choose symbol to start with:").strip()))
			except ValueError:
				print("Sorry, I didn't understand that.")
				continue

			if player not in ("O", "X"):
				print("Wrong Input, Please try Again from X or O")
				continue
			else:
				break
		return player


	def markPosition(self, position, player):
		self.board[position] = player


	def isWinner(self, player):
		win = None
		for position_set in [("1","2","3"), ("4","5","6"), ("7","8","9"), # rows
					("1","4","7"), ("2","5" ,"8"), ("3", "6", "9"), # columns
					("1","5","9"), ("7","5" ,"3")]: # diagonals
			win = True
			for i in position_set:
				if self.board[i] != player:
					win = False
					break
			if win:
				return win
		return False

		
	def IsFilled(self):
		for val in self.board.values():
			if val == " ":
				return False
		return True
	

	def printBoard(self):
		brd = self.board
		print(brd['1'] + '|' + brd['2'] + '|' + brd['3'])
		print("-+-+-")
		print(brd['4'] + '|' + brd['5'] + '|' + brd['6'])
		print('-+-+-')
		print(brd['7'] + '|' + brd['8'] + '|' + brd['9'])


	def swapTurn(self, player):
		return 'X' if player == 'O' else 'O'


	def play(self):
		self.createBoard()
		player = self.choosePlayer()
		while True:
			print(f"Player \"{player}\" turn")
			# user input
			try:
				position = input("Please enter position between (1-9) to mark:\n").strip()
			except ValueError:
				print("Sorry, I didn't understand that.")
				continue

			print(position)
			
			if not position.isnumeric() or not (1 <= int(position) <= 9)  or self.board[position] != " ":
				print("Position marked or invalid input, please try again.\n")
				continue

			print("-"*50)
			self.markPosition(position, player)
			# checking whether current player has won or not
			if self.isWinner(player):
				print(f"Player {player} wins the game!")
				break

			# checking whether the game is draw or not
			if self.IsFilled():
				print("Match Draw!")
				break

			self.printBoard()
			# swapping the turn
			player = self.swapTurn(player)

		self.printBoard()


		
if __name__ == "__main__":
		
	game = TicTacToe()
	game.play()
	
