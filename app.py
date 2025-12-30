import tkinter as tk
from tkinter import messagebox
import pygame  # Musiqa uchun

class TicTacToe:
    def __init__(self):
        # Pygame audioni ishga tushirish
        pygame.mixer.init()
        
        self.window = tk.Tk()
        self.window.title("X-0 O'yini")
        self.window.geometry("400x400")
        
        for i in range(3):
            self.window.grid_columnconfigure(i, weight=1)
            self.window.grid_rowconfigure(i, weight=1)

        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        self.create_widgets()

    def play_win_sound(self):
        """G'alaba musiqasini chalish"""
        try:
            # Bu yerga g'alaba musiqasi fayl yo'lini yozing
            # Masalan: pygame.mixer.music.load("win.mp3")
            # Hozircha tizim xabari tovushini ishlatamiz yoki pastdagi izohni ko'ring
            pygame.mixer.music.load("win_sound.mp3") # Fayl nomi
            pygame.mixer.music.play()
        except:
            # Agar fayl topilmasa, xato bermasligi uchun
            print("Musiqa fayli topilmadi! 'win_sound.mp3' faylini loyiha papkasiga joylang.")

    def create_widgets(self):
        for i in range(9):
            btn = tk.Button(self.window, text="", font=("Arial", 20, "bold"), 
                            command=lambda i=i: self.on_click(i))
            btn.grid(row=i//3, column=i%3, sticky="nsew")
            self.buttons.append(btn)

    def on_click(self, index):
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            
            winner_coords = self.check_winner()
            if winner_coords:
                # G'olib qatorini rangli qilish
                for pos in winner_coords:
                    self.buttons[pos].config(bg="lightgreen")
                
                self.play_win_sound() # Musiqa chalish
                messagebox.showinfo("G'alaba!", f"Yutdingiz! O'yinchi {self.current_player} g'alaba qozondi!")
                self.reset_board()
            elif "" not in self.board:
                messagebox.showinfo("Durang", "O'yin durang bilan tugadi!")
                self.reset_board()
            else:
                self.current_player = "0" if self.current_player == "X" else "X"

    def check_winner(self):
        win_coords = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for combo in win_coords:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return combo # G'alaba kombinatsiyasini qaytaradi
        return None

    def reset_board(self):
        self.current_player = "X"
        self.board = [""] * 9
        for btn in self.buttons:
            btn.config(text="", bg="SystemButtonFace") # Tugma rangini qaytarish

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()