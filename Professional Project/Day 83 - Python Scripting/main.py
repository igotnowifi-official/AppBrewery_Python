############### Tic Tac Toe Game #################
# Objective 1. Make the game board
# Objective 2. Enter your move
# Objective 3. Computer to make random move
# Objective 4. Whomever make a three consecutive line wins.
# Objective 5. Two Player Mode

import random
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy

# Creating the board
global board
board = [[" " for x in range(3)] for y in range(3)]

#with computer
def gameboard_pc(gb, p1, pc):
	global button
	button = []
	for i in range(3):
		m = 3+i
		button.append(i)
		button[i] = []
		for j in range(3):
			n = j
			button[i].append(j)
			messageboard = partial(messageboard_pc, i, j, gb, p1, pc)
			button[i][j] = Button(
				gb, bd=5, command=messageboard, height=4, width=8)
			button[i][j].grid(row=m, column=n)
	gb.mainloop()

#with player
def gameboard_player(gb, p1, p2):
	global button
	button = []
	for i in range(3):
		m = 3+i
		button.append(i)
		button[i] = []
		for j in range(3):
			n = j
			button[i].append(j)
			messageboard = partial(messageboard_player, i, j, gb, p1, p2)
			button[i][j] = Button(
				gb, bd=5, command=messageboard, height=4, width=8)
			button[i][j].grid(row=m, column=n)
	gb.mainloop()

#initializing game
#with computer
def withpc(gb):
	gb.destroy()
	gb = Tk()
	gb.title("Tic Tac Toe Game")
	p1 = Button(gb, text="Player : X", width=10)
	p1.grid(row=1, column=1)
	pc = Button(gb, text="Computer : O",
				width=10, state=DISABLED)

	pc.grid(row=2, column=1)
	gameboard_pc(gb, p1, pc)

#with player

def withplayer(gb):
	gb.destroy()
	gb = Tk()
	gb.title("Tic Tac Toe Game")
	p1 = Button(gb, text="Player 1 : X", width=10)

	p1.grid(row=1, column=1)
	p2 = Button(gb, text="Player 2 : O",
				width=10, state=DISABLED)

	p2.grid(row=2, column=1)
	gameboard_player(gb, p1, p2)



# Game Logic
def winner(b, l):
	return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or #hori1
			(b[1][0] == l and b[1][1] == l and b[1][2] == l) or #hori2
			(b[2][0] == l and b[2][1] == l and b[2][2] == l) or #hori3
			(b[0][0] == l and b[1][0] == l and b[2][0] == l) or #ver1
			(b[0][1] == l and b[1][1] == l and b[2][1] == l) or #ver2
			(b[0][2] == l and b[1][2] == l and b[2][2] == l) or #ver3
			(b[0][0] == l and b[1][1] == l and b[2][2] == l) or #diadown
			(b[0][2] == l and b[1][1] == l and b[2][0] == l)) #diaup

def isfree(i, j):
	return board[i][j] == " "

#Check if board is full - if yes, tie.
def isfull():
	flag = True
	for i in board:
		if(i.count(' ') > 0):
			flag = False
	return flag
  
#with computer
#computer is always p2.
def pc():
	nextmove = []
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == ' ':
				nextmove.append([i, j])
	move = []
	if nextmove == []:
		return
	else:
		for let in ['O', 'X']:
			for i in nextmove:
				boardcopy = deepcopy(board)
				boardcopy[i[0]][i[1]] = let
				if winner(boardcopy, let):
					return i
		corner = []
		for i in nextmove:
			if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
				corner.append(i)
		if len(corner) > 0:
			move = random.randint(0, len(corner)-1)
			return corner[move]
		edge = []
		for i in nextmove:
			if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
				edge.append(i)
		if len(edge) > 0:
			move = random.randint(0, len(edge)-1)
			return edge[move]

#messageboard
sign = 0
def messageboard_pc(i, j, gb, p1, pc):
	global sign
	if board[i][j] == ' ':
		if sign % 2 == 0:
			p1.config(state=DISABLED)
			pc.config(state=ACTIVE)
			board[i][j] = "X"
		else:
			button[i][j].config(state=ACTIVE)
			pc.config(state=DISABLED)
			p1.config(state=ACTIVE)
			board[i][j] = "O"
		sign += 1
		button[i][j].config(text=board[i][j])
	x = True
	if winner(board, "X"):
		gb.destroy()
		x = False
		box = messagebox.showinfo("Winner", "Player won")
	elif winner(board, "O"):
		gb.destroy()
		x = False
		box = messagebox.showinfo("Winner", "Computer won")
	elif(isfull()):
		gb.destroy()
		x = False
		box = messagebox.showinfo("Tie", "Tie")
	if(x):
		if sign % 2 != 0:
			move = pc()
			button[move[0]][move[1]].config(state=DISABLED)
			messageboard_pc(move[0], move[1], gb, p1, pc)

#with player
#messageboard
def messageboard_player(i, j, gb, p1, p2):
	global sign
	if board[i][j] == ' ':
		if sign % 2 == 0:
			p1.config(state=DISABLED)
			p2.config(state=ACTIVE)
			board[i][j] = "X"
		else:
			p2.config(state=DISABLED)
			p1.config(state=ACTIVE)
			board[i][j] = "O"
		sign += 1
		button[i][j].config(text=board[i][j])
	if winner(board, "X"):
		gb.destroy()
		box = messagebox.showinfo("Winner", "Player 1 won")
	elif winner(board, "O"):
		gb.destroy()
		box = messagebox.showinfo("Winner", "Player 2 won")
	elif(isfull()):
		gb.destroy()
		box = messagebox.showinfo("Tie", "Tie")


# GUI Interface and starting game
def play():
	menu = Tk()
	menu.geometry("250x250")
	menu.title("Tic Tac Toe Game")
	w_pc = partial(withpc, menu)
	w_pl = partial(withplayer, menu)


	O1 = Button(menu, text="Single Player", command=w_pc,
				activeforeground='white',
				activebackground="black", bg="blue",
				fg="white", width=500, font='summer', bd=5)

	O2 = Button(menu, text="Multi Player", command=w_pl, activeforeground='white',
				activebackground="black", bg="blue", fg="white",
				width=500, font='summer', bd=5)

	O3 = Button(menu, text="Exit", command=menu.quit, activeforeground='red',
				activebackground="black", bg="red", fg="black",
				width=500, font='summer', bd=5)

	O1.pack(side='top')
	O2.pack(side='top')
	O3.pack(side='top')
	menu.mainloop()


# Call main function
if __name__ == '__main__':
	play()
