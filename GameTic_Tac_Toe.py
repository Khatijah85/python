def initialize_board():
    """Inisialisasi papan permainan 3x3 dengan nilai kosong."""
    return [[' ' for _ in range(3)] for _ in range(3)]

def display_board(board):
    """Menampilkan papan permainan."""
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

def get_player_move():
    """Mendapatkan input pemain untuk langkah."""
    row = int(input("Masukkan nombor baris (0-2): "))
    col = int(input("Masukkan nombor kolom (0-2): "))
    return row, col

def is_valid_move(board, row, col):
    """Memeriksa apakah langkah pemain valid."""
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

def make_move(board, player, row, col):
    """Melakukan langkah pemain pada papan permainan."""
    board[row][col] = player

def check_winner(board, player):
    """Memeriksa apakah pemain menang."""
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    return board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player

def is_board_full(board):
    """Memeriksa apakah papan permainan penuh."""
    return all(all(cell != ' ' for cell in row) for row in board)

def play_tic_tac_toe():
    current_player = 'X'
    game_board = initialize_board()
    
    while True:
        display_board(game_board)
        print(f"Langkah pemain {current_player}.")
        move = get_player_move()
        
        if is_valid_move(game_board, *move):
            make_move(game_board, current_player, *move)
            if check_winner(game_board, current_player):
                print(f"Pemain {current_player} menang!")
                break
            elif is_board_full(game_board):
                print("Permainan berakhir seri!")
                break
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Langkah tidak valid. Cuba lagi.")

# Jalankan permainan Tic-Tac-Toe
play_tic_tac_toe()
