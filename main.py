"""
main.py — Point d'entrée de l'application Mini-Bibliothèque
Lancer avec : python main.py
"""

from src.app import BiblioApp

if __name__ == "__main__":
    app = BiblioApp()
    app.mainloop()
