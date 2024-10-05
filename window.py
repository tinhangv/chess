import pygame
import sys
from board import Board

# Initialize Pygame
pygame.init()

#initialize board
chessBoard = Board()
chessBoard.newGame()

# Set up the display window
screen_width = 800  # Adjust this based on your image size
screen_height = 800  # Adjust this based on your image size
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Chess')

# Load the chessboard image
chessboard_image = pygame.image.load('board.png')
# Scale the image to fit the window, if necessary
chessboard_image = pygame.transform.scale(chessboard_image, (screen_width, screen_height))

# load chess pieces images (rescaled)
square_size = screen_width // 8
Pb = pygame.transform.scale(pygame.image.load('Pb.png'), (square_size, square_size))
Pw = pygame.transform.scale(pygame.image.load('Pw.png'), (square_size, square_size))
Rb = pygame.transform.scale(pygame.image.load('Rb.png'), (square_size, square_size))
Rw = pygame.transform.scale(pygame.image.load('Rw.png'), (square_size, square_size))
Bb = pygame.transform.scale(pygame.image.load('Bb.png'), (square_size, square_size))
Bw = pygame.transform.scale(pygame.image.load('Bw.png'), (square_size, square_size))
Nb = pygame.transform.scale(pygame.image.load('Nb.png'), (square_size, square_size))
Nw = pygame.transform.scale(pygame.image.load('Nw.png'), (square_size, square_size))
Qb = pygame.transform.scale(pygame.image.load('Qb.png'), (square_size, square_size))
Qw = pygame.transform.scale(pygame.image.load('Qw.png'), (square_size, square_size))
Kb = pygame.transform.scale(pygame.image.load('Kb.png'), (square_size, square_size))
Kw = pygame.transform.scale(pygame.image.load('Kw.png'), (square_size, square_size))

selected_piece = None

def draw_pieces():
    pieces = {"Pb": Pb, "Pw": Pw, "Rb": Rb, "Rw": Rw, "Bb": Bb, "Bw": Bw, "Nb": Nb, "Nw": Nw, "Qb": Qb, "Qw": Qw, "Kb": Kb, "Kw": Kw}
    for i in range(8): 
        for j in range(8):
            try:
                screen.blit(pieces[chessBoard.board[7-i][j]], (j*square_size, i*square_size))
            except KeyError:
                pass

def mouseClickHandler():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    board_x = mouse_x // square_size
    board_y = 7 - (mouse_y // square_size)

    chessBoard.setSelectedPiece(board_y, board_x)
    # if chessBoard.getSelectedPiece() == None:
    #     chessBoard.setSelectedPiece(board_x, board_y)
    # else:

  
# Game loop
while True:
    # Blit (draw) the chessboard image onto the window
    screen.blit(chessboard_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #detect mouse click
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouseClickHandler()

    #highlight selected piece
    selected_piece = chessBoard.getSelectedPiece()
    if selected_piece is not None:
        row, col = selected_piece
        pygame.draw.rect(screen, (255, 0, 0), (col * square_size, (7 - row) * square_size, square_size, square_size), 3)

    # Draw pieces
    draw_pieces()

    # Update the display
    pygame.display.update()
