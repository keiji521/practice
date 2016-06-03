# coding: utf-8
'''
0==empty
1==queen
2==load of queen move
'''
board=[[0 for i in range(8)] for j in range(8)]
queen=[7,6,5,4,3]
def backtrack(n,m=0):
	for i in range(8):
		pass
		
def put_queen():
	global board
	board=[[0 for i in range(8)] for j in range(8)]
	for i in range(len(queen)):
		board[queen[i]][i]=1
		
def queen_move():
	for i in range(len(board)):
		for j in range(len(board)):
			if board[i][j]==1:
				for k in range(j+1,len(board)):
					if board[i][k]==0:
						board[i][k]=2
				for k in range(min(i,len(board)-j-1)):
					if board[i-(k+1)][j+(k+1)]==0:
						board[i-(k+1)][j+(k+1)]=2
				for k in range(1,min(len(board)-i,len(board)-j)):
					if board[i+k][j+k]==0:
						board[i+k][j+k]=2
					


def print_board():
	for i in range(len(board)):
		print(board[i])
		
put_queen()
queen_move()
print_board()
