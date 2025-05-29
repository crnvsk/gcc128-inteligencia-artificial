import tkinter as tk
from tkinter import messagebox
from eight_puzzle import EightPuzzle, GOAL_STATE, generate_random_state
from search import bfs, astar

INITIAL_STATE = generate_random_state()

class PuzzleGUI:
    def __init__(self, master):
        self.master = master
        master.title("Jogo dos Oito - IA")
        self.state = EightPuzzle([row[:] for row in INITIAL_STATE])
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()
        self.update_board()

    def create_widgets(self):
        frame = tk.Frame(self.master)
        frame.pack()
        for i in range(3):
            for j in range(3):
                btn = tk.Button(frame, text="", width=4, height=2, font=("Arial", 24),
                                command=lambda x=i, y=j: self.try_move(x, y))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn

        self.bfs_btn = tk.Button(self.master, text="Resolver (BFS)", command=self.solve_bfs)
        self.bfs_btn.pack(side=tk.LEFT, padx=10, pady=10)

        self.astar_btn = tk.Button(self.master, text="Resolver (A*)", command=self.solve_astar)
        self.astar_btn.pack(side=tk.LEFT, padx=10, pady=10)

        self.reset_btn = tk.Button(self.master, text="Resetar", command=self.reset)
        self.reset_btn.pack(side=tk.LEFT, padx=10, pady=10)

    def update_board(self):
        for i in range(3):
            for j in range(3):
                val = self.state.state[i][j]
                self.buttons[i][j]['text'] = "" if val == 0 else str(val)

    def try_move(self, x, y):
        zero_i, zero_j = self.state.find_zero()
        if (abs(zero_i - x) == 1 and zero_j == y) or (abs(zero_j - y) == 1 and zero_i == x):
            direction = None
            if x == zero_i - 1: direction = 'Cima'
            elif x == zero_i + 1: direction = 'Baixo'
            elif y == zero_j - 1: direction = 'Esquerda'
            elif y == zero_j + 1: direction = 'Direita'
            if direction:
                self.state = self.state.move(direction)
                self.update_board()
                if self.state.is_goal():
                    messagebox.showinfo("Parabéns!", "Você resolveu o puzzle!")

    def solve_bfs(self):
        path = bfs(self.state)
        if path is None:
            messagebox.showinfo("Sem solução", "Não foi possível encontrar solução.")
            return
        self.animate_solution(path)

    def solve_astar(self):
        path = astar(self.state)
        if path is None:
            messagebox.showinfo("Sem solução", "Não foi possível encontrar solução.")
            return
        self.animate_solution(path)

    def animate_solution(self, path):
        def step(i):
            if i < len(path):
                self.state = self.state.move(path[i])
                self.update_board()
                self.master.after(500, lambda: step(i+1))
            else:
                messagebox.showinfo("Resolvido!", f"Puzzle resolvido em {len(path)} movimentos!")
        step(0)

    def reset(self):
        self.state = EightPuzzle([row[:] for row in INITIAL_STATE])
        self.update_board()

if __name__ == "__main__":
    root = tk.Tk()
    gui = PuzzleGUI(root)
    root.mainloop()