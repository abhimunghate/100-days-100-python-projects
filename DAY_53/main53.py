# This is Day 53 project : Tic-Tac-Toe Game

import tkinter as tk
import random

BOARD_SIZE = 3

BG_COLOR = "#1e1e2f"
CARD_COLOR = "#292943"
X_COLOR = "#00d4ff"
O_COLOR = "#ff4f81"
TEXT_COLOR = "#ffffff"
WIN_COLOR = "#00c853"
BUTTON_COLOR = "#38385a"
HOVER_COLOR = "#4a4a70"

board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

current_player = "X"

game_mode = "Computer"
difficulty = "Hard"

player_symbol = "X"
computer_symbol = "O"

game_over = False
computer_thinking = False

scores = {"X": 0, "O": 0, "Draws": 0}

buttons = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

winning_cells = []

window = tk.Tk()
window.title("Tic-Tac-Toe")
window.geometry("800x800")
window.resizable(False, False)
window.configure(bg=BG_COLOR)

def play_sound(sound_type):
    """
    Uses Windows built-in Beep function.

    If the program is not running on Windows, the function simply does nothing.
    """
    try:
        import winsound
        if sound_type == "move":
            winsound.Beep(700, 80)
        elif sound_type == "win":
            winsound.Beep(800, 100)
            winsound.Beep(1000, 120)
            winsound.Beep(1200, 150)
        elif sound_type == "draw":
            winsound.Beep(500, 120)
            winsound.Beep(400, 150)
        elif sound_type == "error":
            winsound.Beep(300, 100)
    except Exception:
        pass

title_label = tk.Label(window, text="TIC-TAC-TOE", font=("Arial", 30, "bold"), bg=BG_COLOR, fg=TEXT_COLOR)
title_label.pack(pady=(20, 5))

subtitle_label = tk.Label(window, text="Classic Game • Smart AI", font=("Arial", 11), bg=BG_COLOR, fg="#aaaaaa")
subtitle_label.pack()

score_frame = tk.Frame(window, bg=CARD_COLOR, padx=20, pady=12)
score_frame.pack(pady=20)

x_score_label = tk.Label(score_frame, text="X\n0", font=("Arial", 18, "bold"), bg=CARD_COLOR, fg=X_COLOR, width=8)
x_score_label.grid(row=0, column=0)

draw_score_label = tk.Label(score_frame, text="Draws\n0", font=("Arial", 15, "bold"), bg=CARD_COLOR, fg=TEXT_COLOR, width=8)
draw_score_label.grid(row=0, column=1)

o_score_label = tk.Label(score_frame, text="O\n0", font=("Arial", 18, "bold"), bg=CARD_COLOR, fg=O_COLOR, width=8)
o_score_label.grid(row=0, column=2)

result_label = tk.Label(window, text="Player X's Turn", font=("Arial", 17, "bold"), bg=BG_COLOR, fg=TEXT_COLOR)
result_label.pack(pady=5)

def button_enter(button):
    if button["state"] == "normal":
        button.config(bg=HOVER_COLOR)

def button_leave(button):
    if button["state"] == "normal":
        button.config(bg=BUTTON_COLOR)

def create_board():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            button = tk.Button(board_frame, text="", font=("Arial", 32, "bold"), width=5, height=2, bg=BUTTON_COLOR, fg=TEXT_COLOR, activebackground=HOVER_COLOR, activeforeground=TEXT_COLOR, relief="flat", bd=0, command=lambda r=row, c=col: on_click(r, c))
            button.grid(row=row, column=col, padx=5, pady=5)
            button.bind("<Enter>", lambda event, b=button: button_enter(b))
            button.bind("<Leave>", lambda event, b=button: button_leave(b))
            buttons[row][col] = button

def reset_game():
    global board
    global current_player
    global game_over
    global computer_thinking
    global winning_cells

    board = [["", "", ""], ["", "", ""], ["", "", ""]]
    current_player = "X"
    game_over = False
    computer_thinking = False
    winning_cells = []

    result_label.config(text=f"Player {current_player}'s Turn", fg=TEXT_COLOR)
    for row in buttons:
        for button in row:
            button.config(text="", state="normal", bg=BUTTON_COLOR, fg=TEXT_COLOR)

def reset_scores():
    global scores
    scores = {"X": 0, "O": 0, "Draws": 0}
    update_scoreboard()
    reset_game()

def update_scoreboard():
    x_score_label.config(text=f"X\n{scores['X']}")
    o_score_label.config(text=f"O\n{scores['O']}")
    draw_score_label.config(text=f"Draws\n{scores['Draws']}")

def disable_buttons():
    for row in buttons:
        for button in row:
            button.config(state="disabled")

def check_winner(game_board):
    for row in range(3):
        if (game_board[row][0] != "" and game_board[row][0] == game_board[row][1] == game_board[row][2]):
            return game_board[row][0], [(row, 0), (row, 1), (row, 2)]

    for col in range(3):
        if (game_board[0][col] != "" and game_board[0][col] == game_board[1][col] == game_board[2][col]):
            return game_board[0][col], [(0, col), (1, col), (2, col)]

    if (game_board[0][0] != "" and game_board[0][0] == game_board[1][1] == game_board[2][2]):
        return game_board[0][0], [(0, 0), (1, 1), (2, 2)]

    if (game_board[0][2] != "" and game_board[0][2] == game_board[1][1] == game_board[2][0]):
        return game_board[0][2], [(0, 2), (1, 1), (2, 0)]
    return None, []

def is_draw(game_board):
    for row in game_board:
        if "" in row:
            return False
    return True

def animate_winner(cells, step=0):
    if step >= 6:
        return

    for row, col in cells:
        if step % 2 == 0:
            buttons[row][col].config(bg=WIN_COLOR)
        else:
            buttons[row][col].config(bg=BUTTON_COLOR)
    window.after(180, lambda: animate_winner(cells, step + 1))

def handle_result():
    global game_over
    global winning_cells
    winner, cells = check_winner(board)

    if winner:
        game_over = True
        winning_cells = cells
        scores[winner] += 1
        update_scoreboard()

        if game_mode == "Computer":
            if winner == player_symbol:
                result_label.config(text="🎉 You Win!", fg=WIN_COLOR)
            else:
                result_label.config(text="🤖 Computer Wins!", fg=O_COLOR)
        else:
            result_label.config(text=f"Player {winner} Wins!", fg=WIN_COLOR)
        play_sound("win")
        disable_buttons()
        animate_winner(cells)
        return True

    if is_draw(board):
        game_over = True
        scores["Draws"] += 1
        update_scoreboard()
        result_label.config(text="It's a Draw!", fg="#ffd54f")
        play_sound("draw")
        disable_buttons()
        return True
    return False

def on_click(row, col):
    global current_player
    global computer_thinking

    if game_over:
        return
    if computer_thinking:
        return
    if board[row][col] != "":
        play_sound("error")
        return

    if game_mode == "Computer" and current_player != player_symbol:
        return
    board[row][col] = current_player
    buttons[row][col].config(text=current_player, fg=X_COLOR if current_player == "X" else O_COLOR)
    play_sound("move")

    if handle_result():
        return

    if game_mode == "Computer":
        current_player = computer_symbol
        result_label.config(text="🤖 Computer is thinking...")
        computer_thinking = True
        window.after(500, computer_move)
    else:
        current_player = ("O" if current_player == "X" else "X")
        result_label.config(text=f"Player {current_player}'s Turn")

def get_empty_cells(game_board):
    cells = []

    for row in range(3):
        for col in range(3):
            if game_board[row][col] == "":
                cells.append((row, col))
    return cells

def minimax(game_board, maximizing):
    winner, _ = check_winner(game_board)
    if winner == computer_symbol:
        return 10
    if winner == player_symbol:
        return -10
    if is_draw(game_board):
        return 0

    if maximizing:
        best_score = -float("inf")
        for row, col in get_empty_cells(game_board):
            game_board[row][col] = computer_symbol
            score = minimax(game_board, False)
            game_board[row][col] = ""
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for row, col in get_empty_cells(game_board):
            game_board[row][col] = player_symbol
            score = minimax(game_board, True)
            game_board[row][col] = ""
            best_score = min(best_score, score)
        return best_score

def get_best_move():
    best_score = -float("inf")
    best_move = None

    for row, col in get_empty_cells(board):
        board[row][col] = computer_symbol
        score = minimax(board, False)
        board[row][col] = ""

        if score > best_score:
            best_score = score
            best_move = (row, col)
    return best_move

def get_easy_move():
    empty_cells = get_empty_cells(board)
    if not empty_cells:
        return None
    return random.choice(empty_cells)

def computer_move():
    global current_player
    global computer_thinking

    if game_over:
        computer_thinking = False
        return
    
    if difficulty == "Easy":
        move = get_easy_move()
    else:
        move = get_best_move()

    if move is None:
        computer_thinking = False
        return

    row, col = move
    board[row][col] = computer_symbol
    buttons[row][col].config(text=computer_symbol, fg=O_COLOR if computer_symbol == "O" else X_COLOR)
    play_sound("move")
    computer_thinking = False

    if handle_result():
        return
    current_player = player_symbol
    result_label.config(text=f"Your Turn ({player_symbol})")

def change_game_mode():
    global game_mode
    
    game_mode = mode_var.get()
    reset_game()

    if game_mode == "Computer":
        difficulty_menu.config(state="normal")
        result_label.config(text=f"Your Turn ({player_symbol})")
    else:
        difficulty_menu.config(state="disabled")
        result_label.config(text="Player X's Turn")
        
def change_difficulty(value):
    global difficulty
    difficulty = value

def change_symbol():
    global player_symbol
    global computer_symbol
    global current_player
    
    player_symbol = symbol_var.get()

    if player_symbol == "X":
        computer_symbol = "O"
    else:
        computer_symbol = "X"
    reset_game()

    if player_symbol == "X":
        result_label.config(text="Your Turn (X)")
    else:
        result_label.config(text="Computer starts...")
        current_player = "X"
        window.after(500, computer_move)

settings_frame = tk.Frame(window, bg=BG_COLOR)
settings_frame.pack(pady=5)

tk.Label(settings_frame, text="Mode:", font=("Arial", 11, "bold"), bg=BG_COLOR, fg=TEXT_COLOR).grid(row=0, column=0, padx=5)
mode_var = tk.StringVar(value="Computer")
mode_menu = tk.OptionMenu(settings_frame, mode_var, "Computer", "2 Players", command=lambda _: change_game_mode())
mode_menu.config(font=("Arial", 10), bg=BUTTON_COLOR, fg=TEXT_COLOR, activebackground=HOVER_COLOR, activeforeground=TEXT_COLOR, width=10, relief="flat")
mode_menu.grid(row=0, column=1, padx=5)

tk.Label(settings_frame, text="Difficulty:", font=("Arial", 11, "bold"), bg=BG_COLOR, fg=TEXT_COLOR).grid(row=0, column=2, padx=5)
difficulty_var = tk.StringVar(value="Hard")
difficulty_menu = tk.OptionMenu(settings_frame, difficulty_var, "Easy", "Hard", command=change_difficulty)
difficulty_menu.config(font=("Arial", 10), bg=BUTTON_COLOR, fg=TEXT_COLOR, activebackground=HOVER_COLOR, activeforeground=TEXT_COLOR, width=8, relief="flat")
difficulty_menu.grid(row=0, column=3, padx=5)

tk.Label(settings_frame, text="You:", font=("Arial", 11, "bold"), bg=BG_COLOR, fg=TEXT_COLOR).grid(row=1, column=0, padx=5, pady=8)
symbol_var = tk.StringVar(value="X")
symbol_menu = tk.OptionMenu(settings_frame, symbol_var, "X", "O", command=lambda _: change_symbol())
symbol_menu.config(font=("Arial", 10), bg=BUTTON_COLOR, fg=TEXT_COLOR, activebackground=HOVER_COLOR, activeforeground=TEXT_COLOR, width=10, relief="flat")
symbol_menu.grid(row=1, column=1, padx=5, pady=8)

game_area = tk.Frame(window, bg=BG_COLOR)
game_area.pack(pady=15)

board_frame = tk.Frame(game_area, bg=BG_COLOR)
board_frame.grid(row=0, column=0, padx=(10, 25), sticky="n")

control_frame = tk.Frame(game_area, bg=BG_COLOR, padx=15, pady=20)
control_frame.grid(row=0, column=1, padx=10, sticky="n")

new_game_button = tk.Button(control_frame, text="🔄 New Round", font=("Arial", 12, "bold"), bg=BUTTON_COLOR, fg=TEXT_COLOR, activebackground=HOVER_COLOR, activeforeground=TEXT_COLOR, relief="flat", padx=15, pady=10, command=reset_game)
new_game_button.pack(pady=8)

reset_score_button = tk.Button(control_frame, text="🗑 Reset Score", font=("Arial", 12, "bold"), bg=BUTTON_COLOR, fg=TEXT_COLOR, activebackground=HOVER_COLOR, activeforeground=TEXT_COLOR, relief="flat", padx=15, pady=10, width=14, command=reset_scores)
reset_score_button.pack(pady=8)

exit_button = tk.Button(control_frame, text="✖ Exit", font=("Arial", 12, "bold"), bg=BUTTON_COLOR, fg=TEXT_COLOR, activebackground=HOVER_COLOR, activeforeground=TEXT_COLOR, relief="flat", padx=15, pady=10, width=14, command=window.destroy)
exit_button.pack(pady=8)

create_board()
update_scoreboard()

window.mainloop()

# Done