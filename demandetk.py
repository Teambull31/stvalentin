import tkinter as tk
from tkinter import messagebox
import random

class ProposalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("💕 Une question importante 💕")
        self.root.geometry("700x500")
        
        # Gradient de fond (simulé avec un canvas)
        self.canvas = tk.Canvas(root, width=700, height=500, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        
        # Créer un dégradé rose
        self.create_gradient(self.canvas, 700, 500, "#FFB6C1", "#FF69B4")
        
        # Ajouter des coeurs décoratifs
        hearts = ["💕", "💖", "💗", "💓", "💝", "❤️"]
        for i in range(15):
            x = random.randint(30, 670)
            y = random.randint(20, 480)
            heart = random.choice(hearts)
            size = random.randint(14, 24)
            self.canvas.create_text(x, y, text=heart, font=("Arial", size), fill="#FF1493")
        
        # Titre avec ombre
        self.canvas.create_text(352, 102, text="💍 Question importante 💍", 
                               font=("Arial", 28, "bold"), fill="#8B008B")
        self.canvas.create_text(350, 100, text="💍 Question importante 💍", 
                               font=("Arial", 28, "bold"), fill="white")
        
        # Question principale avec ombre
        self.canvas.create_text(352, 202, text="Veux-tu passer ta vie avec moi ?", 
                               font=("Arial", 32, "bold"), fill="#8B008B")
        self.canvas.create_text(350, 200, text="Veux-tu passer ta vie avec moi ?", 
                               font=("Arial", 32, "bold"), fill="white")
        
        # Bouton OUI avec style moderne
        self.yes_button = tk.Button(
            root,
            text="OUI ! 💖",
            font=("Arial", 22, "bold"),
            bg='#FF1493',
            fg='white',
            width=15,
            height=2,
            command=self.yes_clicked,
            cursor="heart",
            relief="raised",
            borderwidth=5,
            activebackground='#FF69B4',
            activeforeground='white'
        )
        self.yes_button.place(x=250, y=300)
        
        # Effet hover sur le bouton OUI
        self.yes_button.bind('<Enter>', lambda e: self.yes_button.config(bg='#FF69B4', font=("Arial", 24, "bold")))
        self.yes_button.bind('<Leave>', lambda e: self.yes_button.config(bg='#FF1493', font=("Arial", 22, "bold")))
        
        # Bouton NON avec style (plus large pour afficher le texte complet)
        self.no_button = tk.Button(
            root,
            text="Non 😢",
            font=("Arial", 16),
            bg='#D3D3D3',
            fg='#696969',
            width=20,
            height=1,
            relief="raised",
            borderwidth=3
        )
        self.no_button.place(x=260, y=400)
        
        # Lier l'événement de survol au bouton NON
        self.no_button.bind('<Enter>', self.move_no_button)
        
        # Compteur de tentatives
        self.attempts = 0
        
    def create_gradient(self, canvas, width, height, color1, color2):
        """Créer un dégradé de couleur"""
        limit = height
        (r1, g1, b1) = self.root.winfo_rgb(color1)
        (r2, g2, b2) = self.root.winfo_rgb(color2)
        r_ratio = (r2 - r1) / limit
        g_ratio = (g2 - g1) / limit
        b_ratio = (b2 - b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = f'#{nr//256:02x}{ng//256:02x}{nb//256:02x}'
            canvas.create_line(0, i, width, i, fill=color)
    
    def move_no_button(self, event):
        """Déplacer le bouton NON de manière aléatoire"""
        self.attempts += 1
        
        # Obtenir les dimensions de la fenêtre
        window_width = 700
        window_height = 500
        
        # Obtenir les dimensions du bouton (plus large maintenant)
        button_width = 200
        button_height = 40
        
        # Générer des positions aléatoires dans toute l'interface
        new_x = random.randint(10, window_width - button_width - 10)
        new_y = random.randint(10, window_height - button_height - 10)
        
        # Déplacer le bouton
        self.no_button.place(x=new_x, y=new_y)
        
        # Messages qui progressent vers "Tu ne m'auras pas !"
        messages = [
            "Non 😢",
            "Attends... 🤔",
            "Tu es sûre ? 😥",
            "Réfléchis bien ! 💭",
            "Allez... 🥺",
            "S'il te plaît ? 🙏",
            "Juste un OUI ! 💕",
            "Tu ne m'auras pas ! 😊"
        ]
        
        # Afficher le message correspondant à la tentative
        if self.attempts < len(messages):
            self.no_button.config(text=messages[self.attempts])
        else:
            # Après avoir affiché tous les messages, rester sur le dernier
            self.no_button.config(text="Tu ne m'auras pas ! 😊")
            
    def yes_clicked(self):
        """Réaction au clic sur OUI"""
        # Cacher la fenêtre principale
        self.root.withdraw()
        
        # Créer une nouvelle fenêtre pour la célébration
        celebration_window = tk.Toplevel(self.root)
        celebration_window.title("🎉 YES ! 🎉")
        celebration_window.geometry("600x400")
        
        # Canvas pour le dégradé
        canvas = tk.Canvas(celebration_window, width=600, height=400, highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        
        # Créer un dégradé doré
        self.create_gradient_celebration(canvas, 600, 400, "#FFE5E5", "#FFD700")
        
        # Ajouter des coeurs et étoiles
        decorations = ["💖", "✨", "🎉", "💕", "⭐", "💫", "🌟", "❤️"]
        for i in range(30):
            x = random.randint(20, 580)
            y = random.randint(20, 380)
            deco = random.choice(decorations)
            size = random.randint(16, 28)
            canvas.create_text(x, y, text=deco, font=("Arial", size))
        
        # Message de célébration avec ombre
        canvas.create_text(302, 152, text="JE T'AIME ! ❤️", 
                          font=("Arial", 36, "bold"), fill="#8B008B")
        canvas.create_text(300, 150, text="JE T'AIME ! ❤️", 
                          font=("Arial", 36, "bold"), fill="white")
        
        canvas.create_text(302, 222, text="Je suis l'homme le plus heureux ! 🎉", 
                          font=("Arial", 22), fill="#8B008B")
        canvas.create_text(300, 220, text="Je suis l'homme le plus heureux ! 🎉", 
                          font=("Arial", 22), fill="white")
        
        # Bouton pour fermer
        close_button = tk.Button(
            celebration_window,
            text="💕 Fermer 💕",
            font=("Arial", 18, "bold"),
            bg='#FF1493',
            fg='white',
            width=15,
            height=2,
            command=self.root.destroy,
            relief="raised",
            borderwidth=5
        )
        canvas.create_window(300, 320, window=close_button)
        
    def create_gradient_celebration(self, canvas, width, height, color1, color2):
        """Créer un dégradé pour la fenêtre de célébration"""
        limit = height
        (r1, g1, b1) = (255, 229, 229)  # FFE5E5
        (r2, g2, b2) = (255, 215, 0)    # FFD700
        r_ratio = (r2 - r1) / limit
        g_ratio = (g2 - g1) / limit
        b_ratio = (b2 - b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = f'#{nr:02x}{ng:02x}{nb:02x}'
            canvas.create_line(0, i, width, i, fill=color)

# Créer et lancer l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = ProposalApp(root)
    root.mainloop()
