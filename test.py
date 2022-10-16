import tkinter as tk
from main import getBullsAndCows


class Game:
    
    def __init__(self, root=tk.Tk()):
        self.root = root
        self.menu = Menu(self)
        self.singleplayer = Singleplayer(self)
        self.multiplayer = Multiplayer(self)
        self.victory = Victory(self)

    def startApplication(self):
        self.root.title("Bulls and Cows")
        wx = self.root.winfo_screenwidth()
        wh = self.root.winfo_screenheight()
        self.root.geometry(f"330x450+{(wx-330)//2}+{int(0.91*wh-400)//2}")
        self.root.resizable(0, 0)
        self.startMenu()
        self.root.mainloop()

    def startMenu(self):
        self.killOthers()
        self.menu.createMenu()

    def startSingleplayer(self):
        self.killOthers()
        self.singleplayer.createSingleplayer()

    def startMultiplayer(self):
        self.killOthers()
        self.multiplayer.createMultiplayer()

    def killOthers(self):
        self.menu.destroy()
        self.singleplayer.destroy()
        self.multiplayer.destroy()

    def __del__(self):
        self.root.quit()


class Menu:

    def __init__(self, game):
        self.root = game.root
        self.game = game
        self.frmMenu = None

    def createMenu(self):
        menuFont = ("Roboto Light", 12)
        btnMenuFont = ("Roboto Light", 10)
        self.frmMenu = tk.Frame(self.root)
        tk.Label(self.frmMenu, text="Bulls and Cows", \
                 font=("Noto Sans Mro",14)).pack(side='top', pady=(30,0))
        tk.Label(self.frmMenu, text="Choose game mode:",\
                 font=menuFont).pack(side='top', pady=(50, 10))
        tk.Button(self.frmMenu, text="Singleplayer", width=20, height=1, \
                  font=btnMenuFont, command=self.game.startSingleplayer).pack(side='top', ipadx=4, ipady=5, pady=(50, 7))
        tk.Button(self.frmMenu, text="Multiplayer", width=20, height=1, \
                  font=btnMenuFont, command=self.game.startMultiplayer).pack(side='top', ipadx=4, ipady=5, pady=4)
        self.frmMenu.pack(fill="both")

    def destroy(self):
        if self.frmMenu != None:
            self.frmMenu.destroy()


class Singleplayer:

    def __init__(self, game):
        self.root = game.root
        self.game = game
        self.frmSingleplayer = None

    def createSingleplayer(self):
        self.keyWord = ''
        self.generateWord()
        gameLabelFont = ("Roboto Light", 12)
        gameEntryFont = ("Noto Sans Lao UI", 10)
        self.frmSingleplayer = tk.Frame(self.root)
        tk.Label(self.frmSingleplayer, text="Bulls and Cows", \
                 font=("Noto Sans Mro",14)).pack(side='top', pady=(30,0))
        tk.Label(self.frmSingleplayer, text="Guess 5-letter word:", \
                 font=gameLabelFont).pack(side='top', pady=(50, 20))
        self.wordEntry = tk.Entry(self.frmSingleplayer, width=14, \
                                 font=gameEntryFont, justify='center')
        self.wordEntry.pack(side='top', ipadx=2, ipady=7)
        self.wordEntry.bind('<Return>', lambda e: self.checkWord())
        self.frmSingleplayer.pack(fill='both')

    def checkWord(self):
        word = self.wordEntry.get().lower()
        self.wordEntry.delete(0, 'end')
        if word == self.keyWord:
            
            return
        else:
            bulls, cows = getBullsAndCows(self.keyWord, word)
            tk.Label(self.frmSingleplayer, text=f"{word}\nBulls:{bulls} Cows:{cows}").pack()

    def generateWord(self):
        self.keyWord = 'hello'

    def destroy(self):
        if self.frmSingleplayer != None:
            self.frmSingleplayer.destroy()


class Multiplayer:

    def __init__(self, game):
        self.root = game.root
        self.game = game
        self.frmMultiplayer = None

    def createMultiplayer(self):
        self.frmMultiplayer = tk.Frame(self.root)

        self.frmMultiplayer.pack(fill='both')

    def checkWord(self):
        word = self.wordEntry.get().lower()
        self.wordEntry.delete(0, 'end')
        if word == self.keyWord:
            return
        else:
            bulls, cows = getBullsAndCows(self.keyWord, word)
            tk.Label(self.frmMultiplayer, text=f"{word}\nBulls:{bulls} Cows:{cows}").pack()

    def generateWord(self):
        self.keyWord = 'hello'

    def destroy(self):
        if self.frmMultiplayer != None:
            self.frmMultiplayer.destroy()

class Victory:

    def __init__(self, game):
        self.root = game.root
        self.game = game
        self.frmVictory = None

    def createVictoryScreen(self):
        self.frmVictory = Frame(self.root)
        
        self.frmVictory.pack()

    def destroy(self):
        if self.frmVictory != None:
            self.frmVictory.destroy()


def main():
    game = Game()
    game.startApplication()
    
if __name__ == "__main__":
    main()






