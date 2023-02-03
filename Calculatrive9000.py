import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os

win = tk.Tk()
win.title(' Calculatrice-9000 ')
win.configure(bg="#4f4f4f", width=480, height=480)
win.iconbitmap('./ico/calculatrice.ico')

#utilisation d'une zone pour afficher l'entrée de l'utilisateur
Entree_var = StringVar()
Entree_var.set("0")
entree = ttk.Entry(win, width=55, textvariable=Entree_var)
entree.grid(row=0, column=0, padx=10, pady=10)
label = LabelFrame(win)

caneva = Canvas(label)
caneva.configure(bg="#b5b5b5")
caneva.pack(side=RIGHT, fill=BOTH, expand=1)

label.grid(column=0, row=2, padx= 10, pady=10)

labelH = LabelFrame(win)

canevaH = Canvas(labelH)
canevaH.configure(bg="#b5b5b5")
canevaH.pack(side=RIGHT, fill=BOTH, expand=1)

labelH.grid(column=0, row=1)

#code des boutons
def inserNomb(nombr):
	if Entree_var.get() == "0" or Entree_var.get() == "Erreur":
		effacer()
		entree.insert(END, nombr)
	else:
		entree.insert(END, nombr)

def effacer():
	entree.delete(0,END)

def inserDecimale():
	txt = entree.get()
	if txt[-1] == ".":
		messagebox.showwarning(title="Attention", message="Une décimale a déjà été ajoutée.")
		effacer()
		entree.insert(END, ".")
	else:
		entree.insert(END, ".")

def inserOpera(op):
	txt = entree.get()
	if txt == "Erreur":
		messagebox.showerror(title="ERREUR", message="Opération invalide. Veuillez entrer une valeur avant d'utiliser un opérateur.")
		entree.delete(0,op)
	if txt == "":
		messagebox.showerror(title="ERREUR", message="Veuillez entrer une valeur avant d'utiliser un opérateur.")
		entree.delete(0,op)
	if txt[-1] == "+" or txt[-1] == "-" or txt[-1] == "*" or txt[-1] == "/":
		messagebox.showerror(title="ERREUR", message="Ces opérateurs ne sont pas compatibles l'un à la suite de l'autre.")
	else:
		entree.insert(END, op)

def posiNega():
	txt = Entree_var.get()
	if txt != "0":
		if txt[0] != "-":
			entree.insert(0, "-")
		else:
			entree.delete(0,1)

def pourCent():
	txt = float(entree.get())
	total = txt / 100
	Entree_var.set(total)

def carre():
	total = float(Entree_var.get())
	Entree_var.set(total * total)

def racine():
	total = float(Entree_var.get())
	Entree_var.set(pow(total, 0.5))

def pi():
	p = 3.14159
	Entree_var.set(p)

def efface():
	entree.delete(len(entree.get()) - 1)

def nettoyer():
	entree.delete(0, END)

def egale():
	try:
		txt = entree.get()
		total = str(eval(txt))
		fichier = open("Historique.txt", "a")
		fichier.write(txt)
		fichier.write("\n")
		fichier.write("=" + total)
		fichier.write("\n")
		fichier.close()
		Entree_var.set(total)
	except:
		effacer()
		Entree_var.set("Erreur")

def ouvrirHistorique():
	historique = Toplevel()
	historique.title("Historique")
	global historique_label
	historique_label = Label(historique, text="Pas d'historique.", font=("arial", 15))
	historique_label.grid(row=1)
	historique.geometry("300x300")
	nettoyer_historique_btn = ttk.Button(historique, text="Effacer", command=viderHistorique)
	nettoyer_historique_btn.grid(row=0, column=0, pady=5)
	fermer_btn = ttk.Button(historique, text="Fermer", command=historique.destroy)
	fermer_btn.grid(row=0, column=1)
	file = open("Historique.txt", 'r')
	txt = file.read()
	historique_label.config(text=txt, font=("arial", 15))
	file.close()
	historique.mainloop()

def viderHistorique():
	f = open("historique.txt", "w")
	f.close()
	historique_label.config(text="", font=("arial", 15))

def supprimerHistorique():
	os.remove("historique.txt")

#def touchesNumerique(chiffre):

# Clavier numérique

nombre_0 = ttk.Button(caneva,text="0", command=lambda: inserNomb(0))
nombre_0.grid(row=5, column=1, padx=5, pady=5)

nombre_1 = ttk.Button(caneva,text="1", command=lambda: inserNomb(1))
nombre_1.grid(row=4, column=0, padx=5, pady=5)

nombre_2 = ttk.Button(caneva,text="2", command=lambda: inserNomb(2))
nombre_2.grid(row=4, column=1, padx=5, pady=5)

nombre_3 = ttk.Button(caneva,text="3", command=lambda: inserNomb(3))
nombre_3.grid(row=4, column=2, padx=5, pady=5)

nombre_4 = ttk.Button(caneva,text="4", command=lambda: inserNomb(4))
nombre_4.grid(row=3, column=0, padx=5, pady=5)

nombre_5 = ttk.Button(caneva,text="5", command=lambda: inserNomb(5))
nombre_5.grid(row=3, column=1, padx=5, pady=5)

nombre_6 = ttk.Button(caneva,text="6", command=lambda: inserNomb(6))
nombre_6.grid(row=3, column=2, padx=5, pady=5)

nombre_7 = ttk.Button(caneva,text="7", command=lambda: inserNomb(7))
nombre_7.grid(row=2, column=0, padx=5, pady=5)

nombre_8 = ttk.Button(caneva,text="8", command=lambda: inserNomb(8))
nombre_8.grid(row=2, column=1, padx=5, pady=5)

nombre_9 = ttk.Button(caneva,text="9", command=lambda: inserNomb(9))
nombre_9.grid(row=2, column=2, padx=5, pady=5)

# Egal

outilEgale = ttk.Button(caneva,text="=", command=egale)
outilEgale.grid(row=5, column=3, padx=5, pady=5)

# Opérateurs simple

outilPlus = ttk.Button(caneva,text="+", command=lambda: inserOpera("+"))
outilPlus.grid(row=4, column=3, padx=5, pady=5)

outilMoins = ttk.Button(caneva,text="-", command=lambda: inserOpera("-"))
outilMoins.grid(row=3, column=3, padx=5, pady=5)

outilDivise = ttk.Button(caneva,text="/", command=lambda: inserOpera("/"))
outilDivise.grid(row=1, column=2, padx=5, pady=5)

outilMultiple = ttk.Button(caneva,text="x", command=lambda: inserOpera("*"))
outilMultiple.grid(row=2, column=3, padx=5, pady=5)

# Valeur +/-

outilSigne = ttk.Button(caneva,text="+/-", command=posiNega)
outilSigne.grid(row=5, column=0, padx=5, pady=5)

# Décimales

outilVirgule = ttk.Button(caneva,text=",", command=inserDecimale)
outilVirgule.grid(row=5, column=2, padx=5, pady=5)

# Parenthèse

outilParentheseO = ttk.Button(caneva,text="(", command=lambda: inserNomb("("))
outilParentheseO.grid(row=1, column=0, padx=5, pady=5)

outilParentheseF = ttk.Button(caneva,text=")", command=lambda: inserNomb(")"))
outilParentheseF.grid(row=1, column=1, padx=5, pady=5)

# Opérateurs scientifique

outilPourCent = ttk.Button(caneva,text="%", command=pourCent)
outilPourCent.grid(row=5, column=4, padx=5, pady=5)

outilRacine = ttk.Button(caneva,text="√", command=racine)
outilRacine.grid(row=2, column=4, padx=5, pady=5)

outilCarre = ttk.Button(caneva,text="X²", command=carre)
outilCarre.grid(row=3, column=4, padx=5, pady=5)

outilPi = ttk.Button(caneva,text="π", command=pi)
outilPi.grid(row=4, column=4, padx=5, pady=5)

# Fonction effacer
outilEfface = ttk.Button(caneva,text="⇐", command=efface)
outilEfface.grid(row=1, column=4, padx=5, pady=5)

outilNettoyer = ttk.Button(caneva,text="C", command=nettoyer)
outilNettoyer.grid(row=1, column=3, padx=5, pady=5)

# Historique
Historique = ttk.Button(canevaH, text="Historique", command=ouvrirHistorique)
Historique.grid(row=0,column=0, padx=5, pady=5)
Historiqueeffacer = ttk.Button(canevaH, text="Supprimer l'Historique", command=supprimerHistorique)
Historiqueeffacer.grid(row=0,column=1, padx=5, pady=5)

win.mainloop()
