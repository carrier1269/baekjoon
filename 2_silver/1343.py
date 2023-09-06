board = input()

poly = ['AAAA', 'BB']

board = board.replace('XXXX', poly[0])
board = board.replace('XX', poly[1])

if 'X' in board: print(-1)
else: print(board)

# p = input().replace('XXXX', 'AAAA').replace('XX','BB')
# print( -1 if 'X' in p else p)