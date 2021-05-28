from tkinter import *
import tkinter as tk
from tkinter import messagebox
import pickle
import numpy as np
import pandas as pd


model_warp = pickle.load(open("XGBoost_model_warp.pkl", "rb"))
model_weft = pickle.load(open("XGBoost_model_weft.pkl","rb"))
cols_when_model_builds = model_weft.get_booster().feature_names


def test():
	# print("Testing.............")
	input_get = np.array([float(tc.get()), float(weave.get()), float(dwp.get()), float(blend.get()),float(warp_count.get()), float(weft_count.get()), float(epi.get()), float(ppi.get()), float(thread_count.get()), float(gsm.get())])
	# print(input_get)
	# print(type(input_get))
	input_get.resize((1,10))

	df = pd.DataFrame(input_get, columns = cols_when_model_builds)

	tear_warp = model_warp.predict(df)
	tear_weft = model_weft.predict(df)
	resultLabel1.config(text="Tear Strength Warp = "+str(tear_warp))
	resultLabel2.config(text="Tear Strength Weft = " +str(tear_weft))
	# lsum["text"] = str(tear_warp)
	print("Warp :", tear_warp)
	print("Weft: ", tear_weft)


win = Tk()
win.configure(background="cyan")
win.title("Tear Strength Prediction")

win.geometry("900x600")
title = Label(win,text="Inputs for Model",bg="gray",width="300",height="2",fg="White",font = ("Calibri 20 bold italic underline")).pack()

tc = Label(win, text="Thread count Expected",bg="cyan",font = ("Verdana 12")).place(x=12,y=100)
gap = Label(win,text="",bg="cyan").pack()

weave = Label(win, text="Weave (Plain 1/1 ->1 , Satin -> 2)",bg="cyan",font = ("Verdana 12")).place(x=12,y=140)
gap = Label(win,text="",bg="cyan").pack()

dwp = Label(win, text="DWP(Dyed-1,PigmentPrint-2,White-3,R.Dyed-4,Dyed over Print-5)",bg="cyan",font = ("Verdana 12")).place(x=12,y=180)
gap = Label(win,text="",bg="cyan").pack()

blend = Label(win, text="Cotton blend %( 100 % Cotton -> 100,62/38 Cotton/Poly -> 62)",bg="cyan",font = ("Verdana 12")).place(x=12,y=220)
gap = Label(win,text="",bg="cyan").pack()

warp_count = Label(win, text="Warp count ",bg="cyan",font = ("Verdana 12")).place(x=12,y=260)
gap = Label(win,text="",bg="cyan").pack()

weft_count = Label(win, text="Weft count ",bg="cyan",font = ("Verdana 12")).place(x=12,y=300)
gap = Label(win,text="",bg="cyan").pack()

epi = Label(win, text="EPI ",bg="cyan",font = ("Verdana 12")).place(x=12,y=340)
gap = Label(win,text="",bg="cyan").pack()

ppi = Label(win, text="PPI ",bg="cyan",font = ("Verdana 12")).place(x=12,y=380)
gap = Label(win,text="",bg="cyan").pack()

thread_count = Label(win, text="Thread count Actual ",bg="cyan",font = ("Verdana 12")).place(x=12,y=420)
gap = Label(win,text="",bg="cyan").pack()

gsm = Label(win, text="GSM: ",bg="cyan",font = ("Verdana 12")).place(x=12,y=460)
gap = Label(win,text="",bg="cyan").pack()

tc = StringVar()
weave = StringVar()
dwp = StringVar()
blend = StringVar()
warp_count  = StringVar()
weft_count = StringVar()
epi  = StringVar()
ppi  = StringVar()
thread_count  = StringVar()
gsm  = StringVar()


entry_tc = Entry(win,textvariable = tc,width=30)
entry_tc.place(x=220,y=100)
entry_weave = Entry(win,textvariable = weave,width=30)
entry_weave.place(x=500,y=140)
entry_dwp = Entry(win,textvariable = dwp,width=30)
entry_dwp.place(x=580,y=180)
entry_blend = Entry(win,textvariable = blend,width=30)
entry_blend.place(x=580,y=220)
entry_warp_count = Entry(win,textvariable = warp_count,width=30)
entry_warp_count.place(x=220,y=260)
entry_weft_count = Entry(win,textvariable = weft_count,width=30)
entry_weft_count.place(x=220,y=300)
entry_epi = Entry(win,textvariable = epi,width=30)
entry_epi.place(x=220,y=340)
entry_ppi = Entry(win,textvariable = ppi,width=30)
entry_ppi.place(x=220,y=380)
entry_thread_count = Entry(win,textvariable = thread_count,width=30)
entry_thread_count.place(x=220,y=420)
entry_gsm = Entry(win,textvariable = gsm,width=30)
entry_gsm.place(x=220,y=460)


submit = Button(win, text="Test", width="18",height="2",activebackground="violet", bg="Pink",command = test,font = ("Calibri 12 ")).place(x=450, y=520)

resultLabel1 = Label(win, text = "Tear Strength Warp")
resultLabel1.place(x = 20,y = 520)

resultLabel2 = Label(win, text="Tear Strength Weft")
resultLabel2.place(x = 20,y = 550)


win.mainloop()