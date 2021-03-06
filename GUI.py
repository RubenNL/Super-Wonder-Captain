def Window():
	'stuurt het window object terug, zodat de game kan worden gestart'
	return window

def getName():
	'geeft de naam van de speler terug'
	return nameEntry.get()

def showFrame(frameName):
	'zet het correcte frame op de voorgrond'
	mainMenu.pack_forget()
	introFrame.pack_forget()
	gameFrame.pack_forget()
	endFrame.pack_forget()
	leaderFrame.pack_forget()
	eval(frameName).pack(expand=True, fill='both')

def setText(label,text):
	'veranderd de text van een label/knop'
	eval(label).config(text=text)

def setDisabled(button,value):
	'disables/enables een knop'
	if(value):
		state=DISABLED
	else:
		state='normal'
	eval(button).config(state=state)

def setBg(button,value):
	'veranderd de achtergrond van een knop'
	eval(button).config(bg=value)

def setImage(label, image):
	'veranderd de afbeelding van een label'
	eval(label).config(image=image)
	eval(label).image=image

from quiz import *
try:
	from tkinter.messagebox import showinfo
except:
	print("tkinter is niet (correct) geinstalleerd.")
	exit()
try:
	from tkinter import *
except:
	showinfo("ERROR","Tkinter is niet (correct) geinstalleerd.")
	exit()
try:
	import pyglet
except:
	showinfo("ERROR","pyglet is niet (correct) geinstalleerd.")
	exit()

alltimeScoreBoardLabels=[]
dailyScoreBoardLabels=[]


window = Tk()
#window.iconbitmap(r'marvelicon.bmp')
logo = PhotoImage(file='marvelicon.gif')
window.call('wm', 'iconphoto', window._w, logo)
pyglet.font.add_file('changa.ttf')
action_man = pyglet.font.load('Changa')

window.title("Marvel Quiz")
mainMenu = Frame(window, height=800, width=1280)
# mainMenu = Frame(window, height=768, width=1280)

# Main frame settings
window.resizable(width=False, height=False)
window.geometry('1280x800')
background_image = PhotoImage(file="marvel-login-screen.png")
background_label = Label(mainMenu, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

startFrame = Frame(mainMenu, bg="#fff")
startFrame.pack(side=LEFT, anchor=W, padx=(45, 0))

nameLabel = Label(startFrame, text="Naam:", bg="#fff")
nameLabel.config(font=("Changa", 12))

nameEntryText = StringVar()
nameEntry = Entry(startFrame, bg="#fafafa", relief="groove", bd="2", textvariable=nameEntryText)
nameEntry.bind('<Return>', (lambda event: switchToIntro()))
nameEntry.config(font=("Changa", 12))

def character_limit(entry_text):
	if len(entry_text.get()) > 0:
		entry_text.set(entry_text.get()[:15])

nameEntryText.trace("w", lambda *args: character_limit(nameEntryText))

startButton = Button(startFrame, text="START", width=15, command=switchToIntro)
startButton.config(font=("Changa", 10, "bold"), bg="#4c4c4c", fg="#fff", bd="0")

leaderBoardButton = Button(startFrame, text="LEADERBOARD", width=15, command=switchToScoreboard)
leaderBoardButton.config(font=("Changa", 10, "bold"), bg="#4c4c4c", fg="#fff", bd="0")

# Grid config / layout
nameLabel.grid(row=1, column=0, sticky=W)
nameEntry.grid(row=1, column=1, sticky=W, padx=(5, 0))
startButton.grid(row=2, column=0, sticky=W, pady=(60, 8), columnspan=2, ipadx=10, ipady=2)
leaderBoardButton.grid(row=3, column=0, sticky=W, pady=(5, 8), columnspan=2, ipadx=10, ipady=2)

introFrame = Frame(window, height=800, width=1280, bg="#fff")
introFrame_background = PhotoImage(file="marvel-login-screen.png")
introFrame_background_label = Label(introFrame, image=introFrame_background)
introFrame_background_label.place(x=0, y=0, relwidth=1, relheight=1)
introLabel = Label(master=introFrame, bg='white', height=5,font="Changa")
introLabel.place(relx=0.21, rely=0.65, anchor=CENTER)

endFrame = Frame(window, height=800, width=1280, bg="#fff")
endFrame_background = PhotoImage(file="stan-lee-positieve-score.png")
endFrame_background_label = Label(endFrame, image=endFrame_background)
endFrame_background_label.place(x=0, y=0, relwidth=1, relheight=1)
endLabel = Label(master=endFrame, bg='white', height=5,font="Changa")
endLabel.place(relx=0.21, rely=0.55, anchor=CENTER)

menuButton2 = Button(introFrame, text="TERUG NAAR MENU", command=switchToMenu)
menuButton2.config(font=("Changa", 10, "bold"), bg="#4c4c4c", fg="#fff", bd="0")
menuButton2.place(relx=0.25, rely=0.45)

menuButton3 = Button(endFrame, text="TERUG NAAR MENU", command=switchToMenu)
menuButton3.config(font=("Changa", 10, "bold"), bg="#ED1D24", fg="#fff", bd="0")
menuButton3.place(relx=0.15, rely=0.60)

startButton2 = Button(introFrame, text="START SPEL", width=15, command=newGame)
startButton2.config(font=("Changa", 10, "bold"), bg="#ED1D24", fg="#fff", bd="0")
startButton2.place(relx=0.13, rely=0.45)

gameFrame = Frame(window, height=800, width=1280, bg="#fff")
gameFrame_background = PhotoImage(file="marvel-quiz-background.png")
gameFrame_background_label = Label(gameFrame, image=gameFrame_background)
gameFrame_background_label.place(x=0, y=0, relwidth=1, relheight=1)

menuButton = Button(gameFrame, text="MENU", command=switchToMenu)
menuButton.config(font=("Changa", 10, "bold"), bg="#f4f4f4", fg="#6c6c6c", bd="0")
menuButton.place(relx=0.04, rely=0.04,anchor=CENTER)

questionContainer = Label(gameFrame, bg="#f4f4f4")
questionContainer.place(relx=0.20, rely=0.5,anchor=CENTER)

buttons = []
for i in range(10):
	actionButton = Button(questionContainer, text=str(i), command=lambda x=i: buttonClicked(x), anchor=CENTER)
	actionButton.config(font=("Changa", 10, "bold"), bg="#f4f4f4", fg="#fff", bd="0")
	actionButton.grid(row=i, pady=(5, 5))
	buttons.append(actionButton)

description = Label(gameFrame, text="<DESC>", wraplength=500)
description.place(relx=0.26, rely=0.15, anchor=CENTER)
description.config(font=("Changa", 10, "bold"), bg="#f4f4f4", fg="#6c6c6c", bd="0")
hintButton = Button(gameFrame, text="Hint (-3 Punten)",command=displayDescription)
hintButton.place(relx=0.6, rely=0.04,anchor=CENTER)
hintButton.config(font=("Changa", 10, "bold"), bg="#f4f4f4", fg="#6c6c6c", bd="0", borderwidth=2, relief="groove")
aantalvragen = Label(gameFrame, text="<VRAGEN>")
aantalvragen.place(relx=0.5, rely=0.9, anchor=CENTER)
aantalvragen.config(font=("Changa", 10, "bold"), bg="#f4f4f4", fg="#6c6c6c", bd="0")
scoreLabel = Label(gameFrame, text="<SCORE>")
scoreLabel.place(relx=0.02, rely=0.9, anchor=W)
scoreLabel.config(font=("Changa", 10, "bold"), bg="#f4f4f4", fg="#6c6c6c", bd="0")

characterImage = Label(gameFrame, image=PhotoImage(file="marvel-login-screen.png"))
characterImage.place(rely=0.25, relx=0.55)

leaderFrame = Frame(window, height=800, width=1280, bg="#fff")
leaderFrameBackgroundImage = PhotoImage(file="marvel-quiz-background.png")
leaderFrameBackgroundLabel = Label(leaderFrame, image=leaderFrameBackgroundImage)
leaderFrameBackgroundLabel.place(x=0, y=0, relwidth=1, relheight=1)
leaderFrameBackButton = Button(leaderFrame, text="MENU", command=switchToMenu)
leaderFrameBackButton.config(font=("Changa", 10, "bold"), bg="#f4f4f4", fg="#6c6c6c", bd="0")
leaderFrameBackButton.place(relx=0.02, rely=0.02)
dailyleaderFrameGrid=Frame(leaderFrame, bg="#f4f4f4", borderwidth=2, relief="groove")
dailyleaderFrameGrid.place(relx=0.05,rely=0.2)
dailyleaderBoardName=Label(dailyleaderFrameGrid,text="Naam", bg="#f4f4f4", fg="#6c6c6c")
dailyleaderBoardName.grid(row=0,column=1)
dailyleaderBoardDate=Label(dailyleaderFrameGrid,text="Tijd", bg="#f4f4f4", fg="#6c6c6c")
dailyleaderBoardDate.grid(row=0,column=2)
dailyleaderBoardScore=Label(dailyleaderFrameGrid,text="Score", bg="#f4f4f4", fg="#6c6c6c")
dailyleaderBoardScore.grid(row=0,column=3)
alltimeleaderFrameGrid=Frame(leaderFrame, bg="#f4f4f4", borderwidth=2, relief="groove")
alltimeleaderFrameGrid.place(relx=0.3,rely=0.2)
alltimeleaderBoardName=Label(alltimeleaderFrameGrid,text="Naam", bg="#f4f4f4", fg="#6c6c6c")
alltimeleaderBoardName.grid(row=0,column=1)
alltimeleaderBoardDate=Label(alltimeleaderFrameGrid,text="Datum", bg="#f4f4f4", fg="#6c6c6c")
alltimeleaderBoardDate.grid(row=0,column=2)
alltimeleaderBoardScore=Label(alltimeleaderFrameGrid,text="Score", bg="#f4f4f4", fg="#6c6c6c")
alltimeleaderBoardScore.grid(row=0,column=3)
dailyLabel = Label(leaderFrame, text="Dagelijks:", bg="#fff")
dailyLabel.config(font=("Changa", 12), bg="#f4f4f4", fg="#6c6c6c")
dailyLabel.place(relx=0.05, rely=0.15)
alltimeLabel = Label(leaderFrame, text="Top Highscores:")
alltimeLabel.config(font=("Changa", 12), bg="#f4f4f4", fg="#6c6c6c")
alltimeLabel.place(relx=0.3, rely=0.15)


for i in range(1,11):
	leaderBoardName=Label(dailyleaderFrameGrid,text="", bg="#f4f4f4", fg="#6c6c6c")
	leaderBoardName.grid(row=i,column=1,padx=(10,10))
	leaderBoardDate=Label(dailyleaderFrameGrid,text="", bg="#f4f4f4", fg="#6c6c6c")
	leaderBoardDate.grid(row=i,column=2,padx=(10,10))
	leaderBoardScore=Label(dailyleaderFrameGrid,text="", bg="#f4f4f4", fg="#6c6c6c")
	leaderBoardScore.grid(row=i,column=3,padx=(10,10))
	dailyScoreBoardLabels.append({"name":leaderBoardName,"date":leaderBoardDate,"score":leaderBoardScore})
	leaderBoardName=Label(alltimeleaderFrameGrid,text="", bg="#f4f4f4", fg="#6c6c6c")
	leaderBoardName.grid(row=i,column=1,padx=(10,10))
	leaderBoardDate=Label(alltimeleaderFrameGrid,text="", bg="#f4f4f4", fg="#6c6c6c")
	leaderBoardDate.grid(row=i,column=2,padx=(10,10))
	leaderBoardScore=Label(alltimeleaderFrameGrid,text="", bg="#f4f4f4", fg="#6c6c6c")
	leaderBoardScore.grid(row=i,column=3,padx=(10,10))
	alltimeScoreBoardLabels.append({"name":leaderBoardName,"date":leaderBoardDate,"score":leaderBoardScore})
