import tkinter as tk
import main
import re

keyWord = "hi"

def startSingleplayer():
	frmMenu.pack_forget()
	frmSingleplayer.pack(fill='both')
	return


def startMultiplayer():
	return


def sendWordSolo(entry, frame):
        word = entry.get().lower()
        entry.delete(0, 'end')
        global keyWord
        if word == keyWord:
                frame.pack_forget()
                frmWinFrame.pack(fill="both")
        else:
        	bulls, cows = main.getBullsAndCows(keyWord, word)
        	tk.Label(frame, text=f"{word}\nBulls:{bulls} Cows:{cows}").pack()
        return


def backToMenu():
	frmWinFrame.pack_forget()
	frmMenu.pack(fill="both")


def singleplayerFrame():
        frmSingleplayer = tk.Frame(root)
        
        tk.Label(frmSingleplayer, text="Guess 5-letter word:", font=gameLabelFont).pack(side='top', pady=(50, 20))
        wordEntrySolo = tk.Entry(frmSingleplayer, width=14, font=gameEntryFont, justify='center')
        wordEntrySolo.pack(side='top', ipadx=2, ipady=7)
        wordEntrySolo.bind('<Return>', lambda event: sendWordSolo(wordEntrySolo, frmSingleplayer) )

        frmSingleplayer.pack(fill='both')


def multiplayerFrame():
        frmMultiplayer = tk.Frame(root)

        frmMultiplayer.pack(fill='both')


def main():
        root = tk.Tk()
        root.title("Bulls and Cows")
        root.geometry("330x400+550+150")
        root.resizable(0, 0)

        tk.Label(root, text="Bulls and Cows", font=("Noto Sans Mro",14)).pack(side='top', pady=(30,0))

        frmMenu = tk.Frame(root)
        menuFont = ("Roboto Light",12)
        tk.Label(frmMenu, text="Choose game mode:",font=menuFont).pack(side='top', pady=(50, 10))

        btnMenuFont = ("Roboto Light",10)
        tk.Button(frmMenu, text="Singleplayer", width=20, height=1, font=btnMenuFont, command=startSingleplayer).pack(side='top', ipadx=4, ipady=5, pady=(50, 7))
        tk.Button(frmMenu, text="Multiplayer", width=20, height=1, font=btnMenuFont, command=startMultiplayer).pack(side='top', ipadx=4, ipady=5, pady=4)

        frmMenu.pack(fill="both")


        gameLabelFont = ("Roboto Light", 12)
        gameEntryFont = ("Noto Sans Lao UI", 10)

        frmWinFrame = tk.Frame(root)
        winText = tk.Label(frmWinFrame, text="You win!", font=gameLabelFont)
        winText.pack(side='top', pady=(50, 20))
        tk.Entry(frmWinFrame, width=14, font=gameEntryFont, justify='center', state='disabled').pack(side='top', ipadx=2, ipady=7)
        goToMenuButton = tk.Button(frmWinFrame, text="Back to menu", font=gameEntryFont, command=backToMenu)
        goToMenuButton.pack(side='top', ipadx=2, ipady=7, pady=(50, 0))


        root.mainloop()


if __name__ == "__main__":
        main()
