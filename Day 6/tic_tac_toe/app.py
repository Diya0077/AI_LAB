from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Game state (reset on server restart)
board = [""] * 9
current_player = "X"
game_over = False

def check_winner():
    win_patterns = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for pattern in win_patterns:
        if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] != "":
            return True
    return False

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/move", methods=["POST"])
def move():
    global board, current_player, game_over
    data = request.get_json()
    index = data["index"]

    if board[index] == "" and not game_over:
        board[index] = current_player
        if check_winner():
            game_over = True
            return jsonify({"status": f"🎉 Player {current_player} wins!", "board": board})
        elif all(cell != "" for cell in board):
            game_over = True
            return jsonify({"status": "It's a draw!", "board": board})
        else:
            current_player = "O" if current_player == "X" else "X"
            return jsonify({"status": f"Player {current_player}'s turn", "board": board})
    return jsonify({"status": "Invalid move", "board": board})

@app.route("/reset", methods=["POST"])
def reset():
    global board, current_player, game_over
    board = [""] * 9
    current_player = "X"
    game_over = False
    return jsonify({"status": "Player X's turn", "board": board})

if __name__ == "__main__":
    app.run(debug=True)
