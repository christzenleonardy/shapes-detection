import sys
from PIL import Image, ImageTk, ImageOps
import tkinter as tk
from tkinter import ttk

from tkinter import filedialog

import subprocess
import kbs
import clips

initial_facts = []
src_image1 = ""
src_image2 = ""
file_path = ""
file_path2 = ""

class TopLevel (tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.showElements()

    def showElements(self):
        #frame images
        self.ImagesFrame = tk.Frame(self)
        self.ImagesFrame.grid(row=0, column=0)

        #source image
        self.Label1 = tk.Label(self.ImagesFrame)
        self.Label1.configure(text='''Source Image''')
        self.Label1.grid(row=0, column=0, pady=10)

        self.CanvasSourceImage = tk.Canvas(self.ImagesFrame, width=400, height=400, background="#FFFFFF")
        self.CanvasSourceImage.grid(row=1, column=0, padx=10)

        self.SourceImg = self.CanvasSourceImage.create_image(0, 0, anchor= 'nw')

        #detected image
        self.Label2 = tk.Label(self.ImagesFrame)
        self.Label2.configure(text='''Detection Image''')
        self.Label2.grid(row=0, column=1, pady=10)

        self.CanvasDetectionImage = tk.Canvas(self.ImagesFrame, width=400, height=400, background="#FFFFFF")
        self.CanvasDetectionImage.grid(row=1, column=1, padx=10)

        self.DetectionImg = self.CanvasDetectionImage.create_image(0, 0, anchor= 'nw')

        #buttons

        self.ButtonsFrame = tk.Frame(self)
        self.ButtonsFrame.grid(row=0, column=2, pady=(0, 10))

        self.OpenImgButton = tk.Button(self.ButtonsFrame)
        self.OpenImgButton.configure(text='''Open Image''')
        self.OpenImgButton.configure(command= self.openImageButton)
        self.OpenImgButton.grid(row=0, column=0, pady=10)
        self.OpenImgButton.config(height=1, width=30)

        self.OpenRuleButton = tk.Button(self.ButtonsFrame)
        self.OpenRuleButton.configure(text='''Open Rule Editor''')
        self.OpenRuleButton.configure(command= self.openrule)
        self.OpenRuleButton.grid(row=1, column=0, pady=10)
        self.OpenRuleButton.config(height=1, width=30)

        self.ShowRulesButton = tk.Button(self.ButtonsFrame)
        self.ShowRulesButton.configure(text='''Show Rules''')
        self.ShowRulesButton.configure(command= self.showrule)
        self.ShowRulesButton.grid(row=2, column=0, pady=10)
        self.ShowRulesButton.config(height=1, width=30)

        self.ShowFactsButton = tk.Button(self.ButtonsFrame)
        self.ShowFactsButton.configure(text='''Show Facts''')
        self.ShowFactsButton.configure(command= self.showfact)
        self.ShowFactsButton.grid(row=3, column=0, pady=10)
        self.ShowFactsButton.config(height=1, width=30)

        #treeview
        self.TreeViewShape = ttk.Treeview(self.ButtonsFrame)
        self.TreeViewShape.grid(row=4, column=0, pady=10, padx=(10,20))
        self.TreeViewShape.heading("#0",text = "What shape do you want",anchor=tk.W)
        self.TreeViewShape.column("#0", width=270, minwidth=270, stretch=tk.NO)
        

        #treeviewcontent
        main = self.TreeViewShape.insert("",0, text="All Shapes")

        tri= self.TreeViewShape.insert(main,0, text="Triangle")
        quad = self.TreeViewShape.insert(main,1, text="Quadrilateral")
        penta = self.TreeViewShape.insert(main,2, text="Pentagon")
        hexa = self.TreeViewShape.insert(main,3, text="Hexagon")

        trilancip= self.TreeViewShape.insert(tri,0, text="Segitiga-Lancip")
        tritumpul= self.TreeViewShape.insert(tri,1, text="Segitiga-Tumpul")
        trisiku= self.TreeViewShape.insert(tri,2, text="Segitiga-Siku-siku")
        trisamakaki= self.TreeViewShape.insert(tri,3, text="Segitiga-Sama-Kaki")
        trisama= self.TreeViewShape.insert(tri,4, text="Segitiga-Sama-Sisi")
        jajargenjang= self.TreeViewShape.insert(quad,0, text="Jajaran-Genjang")
        trapesium= self.TreeViewShape.insert(quad,1, text="Trapesium")
        pentasama= self.TreeViewShape.insert(penta,0, text="Segi-Lima-Sama-Sisi")
        hexasama= self.TreeViewShape.insert(hexa,0, text="Segi-Enam-Sama-Sisi")

        kakisiku= self.TreeViewShape.insert(trisamakaki,0, text="Segitiga-sama-kaki-dan-siku-siku")
        kakitumpul= self.TreeViewShape.insert(trisamakaki,1, text="Segitiga-sama-kaki-dan-tumpul")
        kakilancip= self.TreeViewShape.insert(trisamakaki,2, text="Segitiga-sama-kaki-dan-lancip")
        beraturan= self.TreeViewShape.insert(jajargenjang,0, text="Segiempat-beraturan")
        layang= self.TreeViewShape.insert(jajargenjang,1, text="Layang-layang")
        samakaki= self.TreeViewShape.insert(trapesium,0, text="Trapesium-sama-kaki")
        ratakanan= self.TreeViewShape.insert(trapesium,1, text="Trapesium-rata-kanan")
        ratakiri= self.TreeViewShape.insert(trapesium,2, text="Trapesium-rata-kiri")
        self.TreeViewShape.bind("<Double-1>", self.sendString)

        #framebottom
        self.ResultFrame = tk.Frame(self)
        self.ResultFrame.grid(row=1, column=0, columnspan = 3)

        self.Label4 = tk.Label(self.ResultFrame)
        self.Label4.configure(text='''Detection Result''')
        self.Label4.grid(row=0, column=0, pady=10)
        self.DetectionRes = tk.Text(self.ResultFrame, width=45, height=20, background="#FFFFFF")
        self.DetectionRes.grid(row=1, column=0, padx=10, pady=10)

        self.Label5 = tk.Label(self.ResultFrame)
        self.Label5.configure(text='''Matched Facts''')
        self.Label5.grid(row=0, column=1, pady=10)
        self.MatchedFacts = tk.Text(self.ResultFrame, width=45, height=20, background="#FFFFFF")
        self.MatchedFacts.grid(row=1, column=1, padx=10, pady=10)

        self.Label6 = tk.Label(self.ResultFrame)
        self.Label6.configure(text='''Hit Rules''')
        self.Label6.grid(row=0, column=2, pady=10)
        self.HitRules = tk.Text(self.ResultFrame, width=45, height=20, background="#FFFFFF")
        self.HitRules.grid(row=1, column=2, padx=10, pady=10)

    def openImageButton(self):
        global file_path, src_image1
        file_path = filedialog.askopenfilename()
        src_image1 = ImageTk.PhotoImage(Image.open(file_path))
        print(src_image1)
        self.CanvasSourceImage.itemconfigure(self.SourceImg, image=src_image1)

    def openDetectionImg(self, event):
        global file_path2
        file_path2 = "./shape/result.jpg"
        global src_image2
        src_image2 = ImageTk.PhotoImage(Image.open(file_path2))
        self.CanvasDetectionImage.itemconfigure(self.DetectionImg, image=src_image2)
        # getAllResult(self, res) #CHANGE THIS SHITTTTTTT LATER

    def sendString(self,event):
        global initial_facts, src_image1, src_image2, file_path, file_path2
        item = self.TreeViewShape.identify('item',event.x,event.y)
        item = self.TreeViewShape.item(item)['text']
        # print (self.src_image1)
        print('haha', file_path, item)
        hasil, matched_facts, fired_rules, result_list, initial_facts = kbs.run_kbs(file_path, 'segitiga-sama-sisi')
        self.openDetectionImg(event)
        self.showDetRes(hasil, result_list)
        self.showMatchedFacts(matched_facts)
        self.showHitRules(fired_rules)


    def showrule(self):
        newwin = tk.Toplevel(master=root)
        newwin.title('All Rules')
        display2 = tk.Text(newwin, width=45, height=20, background="#FFFFFF")

        env = clips.Environment()
        env.load('kbs.clp')
        for rule in env.rules():
            display2.insert(tk.END, rule)
            display2.insert(tk.END, "\n")
        
        display2.insert(tk.END, "Just a text Widget\nin two lines\n")
        display2.pack()

    def showfact(self):
        newwin = tk.Toplevel(master=root)
        newwin.title('All Facts')
        # display = tk.Label(newwin, text="Humm, see a new window !")
        display2 = tk.Text(newwin, width=45, height=20, background="#FFFFFF")
        for fact in initial_facts:
            display2.insert(tk.END, fact + "\n")
        display2.pack()

    def openrule(self):
        subprocess.call(["notepad.exe", 'kbs.clp'])

    def showDetRes(self, hasil, result_list):
        self.DetectionRes.insert(tk.END, hasil + "\n")
        for x in result_list :
            self.DetectionRes.insert(tk.END, x + "\n")

    def showMatchedFacts(self, res):
        for x in res:
            self.MatchedFacts.insert(tk.END, x + "\n")

    def showHitRules(self, res):
        for x in res:
            self.HitRules.insert(tk.END, x + "\n")

root = tk.Tk()

app = TopLevel(master=root)
app.mainloop()