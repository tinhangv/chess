"""
Text Based Chess
credits: Victor Kwok, Russel Reid
"""

class Board:
  def __init__(self):
    self.blank = '  '
    self.board = [[self.blank for _ in range(8)] for _ in range(8)]
    self.CurrentPlayer = 'w'
    self.gameOver = False
    self.moveHistory = []
    self.selectedPiece = None

    #self.checkMate = False
    self.inCheck = {"w":False, "b":False}
    self.castled = {"w":False, "b":False}

  def __str__(self):
    #convert code representation of pieces into unicode chess pieces
    pieces=['♔','♕','♖','♗','♘','♙','♚','♛','♜','♝','♞','♟︎',' ']
    piecesCode = ['Kw','Qw','Rw','Bw','Nw','Pw','Kb','Qb','Rb','Bb','Nb','Pb',self.blank]
    printBoard = []
    for i in range(8):
      row = []
      for j in range(8):
        row.append(pieces[piecesCode.index(self.board[i][j])])
      printBoard.append(row)
    #print the board
    files = 'ABCDEFGH'
    s = ""
    for i in range(7,-1, -1):
      s += str(i+1) + str(printBoard[i]) + "\n"
    s+= '   A    B    C    D    E    F    G    H'
    return s
     
  def newGame(self):
    #reset the board to starting postion
    self.board[7] = ['Rb','Nb','Bb','Qb','Kb','Bb','Nb','Rb']
    self.board[6] = ['Pb']*8
    for i in range(3,6): self.board[i] = [self.blank]*8
    self.board[1] = ['Pw']*8
    self.board[0] = ['Rw','Nw','Bw','Qw','Kw','Bw','Nw','Rw']

    #for i in range(2,7): self.board[i] = [self.blank]*8

  def history(self, s=''):
    if len(s) == 0:
      return "Moves Made: " + str(self.moveHistory)
    else:
      self.moveHistory.append(s)

  def setSelectedPiece(self, a,b):
    if (a,b) == (-1,-1):
      self.selectedPiece = None
    self.selectedPiece = (a,b)

  def getSelectedPiece(self):
    return self.selectedPiece

  def inputToCoordinates(self,move):
    b=(ord(move[0].lower())-97) 
    a=int(move[1])-1
    d=(ord(move[3].lower())-97) 
    c=int(move[4])-1
    return a,b,c,d
  
  def validateMove(self, move):
    #move should be in format: A1 B2
    #check input format and convert to coordinates
    if not(len(move) == 5): return False
    if not (move[0].isalpha() and move[1].isnumeric() and move[3].isalpha() and move[4].isnumeric()): return False
    a,b,c,d = self.inputToCoordinates(move)
    if any([ (x not in range(8)) for x in [a,b,c,d]]): return False
    
    #check if selected square is empty
    if self.board[a][b] == self.blank: return False
    #check piece colour
    color = self.board[a][b][1]
    if color != self.CurrentPlayer: return False

    selectedPiece = self.board[a][b][0]
    #check if the move is a possible move for the piece selected
    if selectedPiece == 'Q':
      if [c,d] not in self.RookMoves(a,b,color)+self.BishopMoves(a,b,color): return False
    if selectedPiece == 'R':
      if [c,d] not in self.RookMoves(a,b,color): return False
    if selectedPiece == 'B':
      if [c,d] not in self.BishopMoves(a,b,color): return False
    if selectedPiece == 'P':
      if [c,d] not in self.PawnMoves(a,b,color): return False
    if selectedPiece == 'K':
      if [c,d] not in self.KingMoves(a,b,color): return False

    #check if move results in check

    return True
  
  def checkSquare(self,c,d,color):
    append, stop = False,True
    if self.board[c][d] == self.blank:
      append = True
      stop = False
    elif self.board[c][d][1] != color:
      append = True
    return append, stop
  
  def PawnMoves(self,a,b,color):
    movesList = []
    if color == 'w':
      if a==1: #starting position
        append, stop = self.checkSquare(3,b,color)
        if append: movesList.append([3,b])
      if a<7:
        append, stop = self.checkSquare(a+1,b,color)
        if append: movesList.append([a+1,b])
  
    if color == 'b':
      if a==6: #starting position
        append, stop = self.checkSquare(4,b,color)
        if append: movesList.append([4,b])
      if a>0:
        append, stop = self.checkSquare(a-1,b,color)
        if append: movesList.append([a-1,b])

    #captures
    #promotion
        
    return movesList
  
  def KingMoves(self,a,b,color):
    movesList = []
    #check all 8 adjacent squares
    #castle
    return movesList
  
  def BishopMoves(self,a,b,color):
    movesList = []
    #check the 4 sightlines (a:rows,b:columns)
    #north east
    for i in range(1,8-a):
      if a+i<8 and b+i<8:
        append, stop = self.checkSquare(a+i,b+i,color)
        if append: movesList.append([a+i,b+i])
        if stop: break
    #north west
    for i in range(1,8-a):
      if a+i<8 and b-i>=0:
        append, stop = self.checkSquare(a+i,b-i,color)
        if append: movesList.append([a+i,b-i])
        if stop: break
    #south east
    for i in range(1,a+1):
      if a-i>=0 and b+i<8:
        append, stop = self.checkSquare(a-i,b+i,color)
        if append: movesList.append([a-i,b+i])
        if stop: break
    #south west
    for i in range(1,a+1):
      if a-i>=0 and b-i>=0:
        append, stop = self.checkSquare(a-i,b-i,color)
        if append: movesList.append([a-i,b-i])
        if stop: break

    return movesList
    
  def RookMoves(self,a,b,color):
    movesList = []
    #check the 4 sightlines (a:rows,b:columns)
    #up
    if a<7:
      for i in range(a+1,8):
        append, stop = self.checkSquare(i,b,color)
        if append: movesList.append([i,b])
        if stop: break
    #down
    if a>0:
      for i in range(a-1,-1,-1):
        append, stop = self.checkSquare(i,b,color)
        if append: movesList.append([i,b])
        if stop: break
    #right
    if b<7:
      for i in range(b+1,8):
        append, stop = self.checkSquare(a,i,color)
        if append: movesList.append([a,i])
        if stop: break
    #left
    if b>0:
      for i in range(b-1,-1,-1):
        append, stop = self.checkSquare(a,i,color)
        if append: movesList.append([a,i])
        if stop: break
    return movesList
    
  
  def move(self, move):
    #move piece on (a,b) to (c,d)
    a,b,c,d = self.inputToCoordinates(move)
    self.board[c][d] = self.board[a][b]
    self.board[a][b] = self.blank
    if self.CurrentPlayer == 'w':
      self.CurrentPlayer = 'b'
    else: self.CurrentPlayer = 'w'
      
def main():
  board = Board()
  board.newGame()
  print(board)
  while(not board.gameOver):
    #get a valid move from user input
    move = input("Enter Next Move: ")
    valid = board.validateMove(move)
    while not valid:
      print("invalid move")
      move = input("Enter Next Move: ")
      valid = board.validateMove(move)
    board.move(move)
    board.history(move)
    print(board.history())
    print(board)
    
if __name__ == "__main__":
  main()