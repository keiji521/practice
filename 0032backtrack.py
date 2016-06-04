# coding: utf-8
'''
0==empty
1==queen
2==load of queen move
'''
board=[[0 for i in range(8)] for j in range(8)]
bl=len(board)
queen=[]
answer=[]
def backtrack(n):
	global board
	global queen
	global answer
	global bl

	for i in range(bl):
		if board[i][n]==0:
			put_queen()
			queen_move()
			#print(n,i)
			queen.append(i)
			print(queen)
			put_queen()
			queen_move()
			print_board()
			if n == bl-1:
				answer.append(queen)
				#print(answer)
				queen.pop()
				break
			else:
				backtrack(n+1)
	if queen:
		queen.pop()
	put_queen()
	queen_move()
				
			
		
def put_queen():
	global board
	global bl
	board=[[0 for i in range(bl)] for j in range(bl)]
	for i in range(len(queen)):
		board[queen[i]][i]=1
		
def queen_move():
	global board
	global bl
	for i in range(bl):
		for j in range(bl):
			if board[i][j]==1:
				for k in range(j+1,bl):
					if board[i][k]==0:
						board[i][k]=2
				for k in range(min(i,bl-j-1)):
					if board[i-(k+1)][j+(k+1)]==0:
						board[i-(k+1)][j+(k+1)]=2
				for k in range(1,min(bl-i,bl-j)):
					if board[i+k][j+k]==0:
						board[i+k][j+k]=2
					


def print_board():
	print("-----------------")
	for i in range(bl):
		print(board[i])
	print("-----------------")

'''
put_queen()
queen_move()
print_board()
'''
backtrack(0)
print(answer)