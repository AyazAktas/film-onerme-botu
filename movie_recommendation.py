import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import messagebox

df = pd.read_csv("movies_metadata.csv")

class MovieRecommendationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Film Öneri Uygulaması")
        self.root.geometry("600x400")  #pencere boyutunu ayarla 

        self.title_label = tk.Label(root, text="Rastgele Film Öneri Uygulaması", font=("Helvetica", 24))
        self.title_label.pack(pady=20)

        self.movie_info_label = tk.Label(root, text="", font=("Helvetica", 18))
        self.movie_info_label.pack()

        self.watch_button = tk.Button(root, text="İzledim", font=("Helvetica", 14), command=self.watched_movie)
        self.watch_button.pack(pady=10)

        self.not_watch_button = tk.Button(root, text="İzlemedim", font=("Helvetica", 14), command=self.not_watched_movie)
        self.not_watch_button.pack(pady=10)

        self.get_movie_button = tk.Button(root, text="Yeni Film Önerisi", font=("Helvetica", 16), command=self.get_new_movie)
        self.get_movie_button.pack(pady=20)

        self.quit_button = tk.Button(root, text="Çıkış", font=("Helvetica", 14), command=root.quit)
        self.quit_button.pack()

        self.movie_pool = []  
        self.get_new_movie()

    def show_message(self, message):
        messagebox.showinfo("Bilgi", message)

    def get_random_movie(self):
        filtered_df = df[(~df["title"].isin(self.movie_pool))]  
        if filtered_df.empty:
            self.movie_pool = []  
        random_row = filtered_df.sample()
        selected_title = random_row["title"].values[0]
        selected_year = random_row["year"].values[0]
        return selected_title, selected_year

    def update_movie_info(self):
        self.selected_title, self.selected_year = self.get_random_movie()
        self.movie_info_label.config(text=f"Film: {self.selected_title} ({self.selected_year})")

    def watched_movie(self):
        self.movie_pool.append(self.selected_title)  
        message = f"{self.selected_title} filmini izlediniz. Umarım beğenmişsinizdir.\n\nYeni bir film öneriyorum:"
        self.show_message(message)
        self.update_movie_info()

    def not_watched_movie(self):
        message = f"{self.selected_title} bu geceki filminiz olsun. İyi Seyirler !\n\nYeni bir film önereyim mi?"
        choice = messagebox.askquestion("Film Botu", message, icon='question')
        
        if choice == 'yes':
            self.update_movie_info()
        else:
            self.root.quit()

    def get_new_movie(self):
        self.update_movie_info()

if __name__ == "__main__":
    root = tk.Tk()
    app = MovieRecommendationApp(root)
    root.mainloop()