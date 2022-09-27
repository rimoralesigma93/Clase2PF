# Import the required libraries
from csv import *
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

window=Tk()
upload= Image.open("sigmalogo.png")
image=ImageTk.PhotoImage(upload)
label= Label(window,image=image,height = 250, width =250)
label.place(x=400,y=0)

window.title("Inputs Diccionarios")
window.geometry("800x600")
main_lst=[]

def Add():
   lst=[proceso.get(),
        prshortdesc.get(),
        original.get(),
        unit.get(),
        lowspec.get(),
        target.get(),
        hspec.get(),
        hlimit.get(),
        aushortdesc.get(),
        value.get()]
   main_lst.append(lst)
   messagebox.showinfo("Informacion","Los datos han sido agredados satisfactoriamente")

def Save():
   with open("diccframes.csv","r+", newline='') as file: 
      file.read()
      Writer=writer(file)
      #Writer.writerow(["Proceso","PR_SHORT_DESC","Original_Data","UNIT","LOW_SPEC", "TARGET", "HIGH_SPEC", "HIGH_LIMIT", "AU_SHORT_DESC", "VALUE"])
      Writer.writerows(main_lst)
      messagebox.showinfo("Informacion","Grabado con Exito")

def Clear():
   proceso.delete(0,END)
   prshortdesc.delete(0,END)
   original.delete(0,END)
   unit.delete(0,END)
   lowspec.delete(0,END)
   target.delete(0,END)
   hspec.delete(0,END)
   hlimit.delete(0,END)
   aushortdesc.delete(0,END)
   value.delete(0,END)
   

# 3 labels, 4 buttons,3 entry fields
label1=Label(window,text="Proceso: ",padx=20,pady=10)
label2=Label(window,text="PR_SHORT_DESC: ",padx=20,pady=10)
label3=Label(window,text="Original_Data: ",padx=20,pady=10)
label4=Label(window,text="UNIT: ",padx=20,pady=10)
label5=Label(window,text="LOW_SPEC: ",padx=20,pady=10)
label6=Label(window,text="TARGET: ",padx=20,pady=10)
label7=Label(window,text="HIGH_SPEC: ",padx=20,pady=10)
label8=Label(window,text="HIGH_LIMIT: ",padx=20,pady=10)
label9=Label(window,text="AU_SHORT_DESC: ",padx=20,pady=10)
label10=Label(window,text="VALUE: ",padx=20,pady=10)

proceso=Entry(window,width=30,borderwidth=3)
prshortdesc=Entry(window,width=30,borderwidth=3)
original=Entry(window,width=30,borderwidth=3)
unit=Entry(window,width=30,borderwidth=3)
lowspec=Entry(window,width=30,borderwidth=3)
target=Entry(window,width=30,borderwidth=3)
hspec=Entry(window,width=30,borderwidth=3)
hlimit=Entry(window,width=30,borderwidth=3)
aushortdesc=Entry(window,width=30,borderwidth=3)
value=Entry(window,width=30,borderwidth=3)


add=Button(window,text="Añadir",padx=20,pady=10,command=Add)
save=Button(window,text="Grabar",padx=20,pady=10,command=Save)
clear=Button(window,text="Limpiar",padx=20,pady=10,command=Clear)
Exit=Button(window,text="Salir",padx=20,pady=10,command=window.quit)

label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
label3.grid(row=2,column=0)
label4.grid(row=3,column=0)
label5.grid(row=4,column=0)
label6.grid(row=5,column=0)
label7.grid(row=6,column=0)
label8.grid(row=7,column=0)
label9.grid(row=8,column=0)
label10.grid(row=9,column=0)


proceso.grid(row=0,column=1)
prshortdesc.grid(row=1,column=1)
original.grid(row=2,column=1)
unit.grid(row=3,column=1)
lowspec.grid(row=4,column=1)
target.grid(row=5,column=1) 
hspec.grid(row=6,column=1)
hlimit.grid(row=7,column=1)
aushortdesc.grid(row=8,column=1)
value.grid(row=9,column=1)

add.grid(row=10,column=0,columnspan=2)
save.grid(row=11,column=0,columnspan=2)
clear.grid(row=12,column=0,columnspan=2)
Exit.grid(row=13,column=0,columnspan=2)


window.mainloop()
print(main_lst)