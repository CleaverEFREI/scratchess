import chess
import sys
import time

class ChessEngine:
    def __init__(self):
        self.board = chess.Board()
        self.name = "EnCroissant"
        self.author = "YourName"

    def handle_uci(self):
        """Initialize UCI protocol with Stockfish-like output."""
        print(f"id name {self.name}")
        print(f"id author {self.author}")
        
        print("uciok")
        sys.stdout.flush()

    def handle_position(self, command):
        """Handle position command like Stockfish."""
        if "startpos" in command:
            self.board.reset()
            if "moves" in command:
                moves = command.split("moves ")[1].split()
                for move in moves:
                    self.board.push_uci(move)
        elif "fen" in command:
            fen = command.split("fen ")[1].split(" moves ")[0]
            self.board.set_fen(fen)
            if "moves" in command:
                moves = command.split("moves ")[1].split()
                for move in moves:
                    self.board.push_uci(move)

    def handle_go(self, command):
        """Handle go command with Stockfish-like output."""
        
        # Get first legal move as a basic implementation
        legal_moves = list(self.board.legal_moves)
        if legal_moves:
            chosen_move = legal_moves[0]
            # Final output with bestmove
            print(legal_moves)
            print(f"bestmove {chosen_move.uci()}")
        else:
            Exception("No legal moves found.")
        sys.stdout.flush()

    def handle_setoption(self, command):
        """Handle setoption command."""
        try:
            name = command.split("name ")[1].split(" value ")[0]
            value = command.split("value ")[1]
            self.options[name] = value
        except:
            pass

    def main_loop(self):
        """Main loop handling UCI protocol."""
        while True:
            try:
                command = input()
                
                if command == "uci":
                    self.handle_uci()
                elif command == "isready":
                    print("readyok")
                    sys.stdout.flush()
                elif command.startswith("setoption"):
                    self.handle_setoption(command)
                elif command.startswith("position"):
                    self.handle_position(command)
                elif command.startswith("go"):
                    self.handle_go(command)
                elif command == "ucinewgame":
                    self.board.reset()
                elif command == "quit":
                    break
                
            except EOFError:
                break

if __name__ == "__main__":
    engine = ChessEngine()
    engine.main_loop()