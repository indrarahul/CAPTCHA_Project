import tkinter as tk
import os
from PIL import ImageTk, Image
from bs4 import BeautifulSoup
# import pyautogui
dire = input()
UniqNum = 11

a = os.listdir(dire + '/.')
if(not(dire  + '_new' in os.listdir('.'))):
	os.system('mkdir ' + dire  + '_new')
if(not('CAPTCHA_new' in os.listdir('.'))):
	os.system('mkdir CAPTCHA_new')

class tkwindow:
	is_over = False

	def __init__(self,file):
		self.filename = a[file]
		self.root = tk.Tk()
		self.root.title("Editing Box")
		self.root.geometry("400x250")
		name = tk.Label(self.root, text='Current Name: '+ self.filename)
		img = ImageTk.PhotoImage(Image.open(os.path.join(dire + "/" + a[file])).resize((180, 70), Image.ANTIALIAS))
		img2 = ImageTk.PhotoImage(Image.open(os.path.join(dire + "/" + a[file+1])).resize((180, 70), Image.ANTIALIAS))
		img3 = ImageTk.PhotoImage(Image.open(os.path.join(dire + "/" + a[file+2])).resize((180, 70), Image.ANTIALIAS))
		img4 = ImageTk.PhotoImage(Image.open(os.path.join(dire + "/" + a[file+3])).resize((180, 70), Image.ANTIALIAS))
		img5 = ImageTk.PhotoImage(Image.open(os.path.join(dire + "/" + a[file+4])).resize((180, 70), Image.ANTIALIAS))
		img6 = ImageTk.PhotoImage(Image.open(os.path.join(dire + "/" + a[file+5])).resize((180, 70), Image.ANTIALIAS))
		
		panel = tk.Label(self.root, image=img)
		panel2 = tk.Label(self.root, image=img2)
		panel3 = tk.Label(self.root, image=img3)
		panel4 = tk.Label(self.root, image=img4)
		panel5 = tk.Label(self.root, image=img5)
		panel6 = tk.Label(self.root, image=img6)
		
		# editbut = tk.Button(self.root, text='Edit',command= self.naam)
		# nextb = tk.Button(self.root, text='Next',command= self.nextbb)
		exitb = tk.Button(self.root, text = 'Exit', command= self.on_exit)
		# self.rename = tk.Entry(self.root)
		
		
		panel.grid(column=0, row=0)
		panel2.grid(column=1, row=0)
		panel3.grid(column=0, row=1)
		panel4.grid(column=1, row=1)
		panel5.grid(column=0, row=2)
		panel6.grid(column=1, row=2)
		
		# editbut.grid(column=0, row=6)
		# nextb.grid(column=1, row=6)
		# self.rename.grid(column=0,row=2)
		exitb.grid(column=2, row=6)
		b = input().split()
		for j in range(6):
			html= open('WEBPAGE/' + a[i+j].split('.')[0]+'.html').read()
			soup = BeautifulSoup(html, 'html.parser')
			idddd = soup.find(id="ctl00_SPWebPartManager1_g_aa197fec_b38c_41a8_b14e_a11722636b37_ctl00_lblCaptcha")
			os.system('mv ' + dire + "/" + a[i+j] + " " + dire + "_new/" + str(UniqNum) + "_" + a[i+j].split('.')[0] + '_' + idddd.text.replace(' ','-') + "_" + b[j] + "." +a[i+j].split('.')[-1])
			os.system('mv ' + 'CAPTCHA/' + a[i+j].split('.')[0] + '.png' + " " + "CAPTCHA_new/" + str(UniqNum) + "_" + a[i+j].split('.')[0] + '_' + idddd.text.replace(' ','-') + "_" + b[j] + ".png")
			os.system('mv ' + 'CAPTCHA/' + a[i+j].split('.')[0] + '.aspx' + " " + "CAPTCHA_new/" + str(UniqNum) + "_" + a[i+j].split('.')[0] + '_' + idddd.text.replace(' ','-') + "_" + b[j] + ".aspx")
	
		self.nextbb() 
		self.root.mainloop()
		

	def on_exit(self):
		self.is_over = True
		self.root.destroy()

	def naam(self):
		# try:
		os.system('mv ' + dire + "/" + self.filename + " " + dire + "_new/" + self.rename.get() + "." + self.filename.split('.')[-1])
		print("Done")
		self.nextbb()
		# except(e):
		# 	print(e)

	def nextbb(self):
		self.root.destroy()


for i in range(0,len(a),6):
	if i < len(a)-6:
		window = tkwindow(i)
	if window.is_over:
		exit()
