import math
class tamgiac():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def chuvi(self):
        return self.a+self.b+self.c
    def dientich(self):
        p=(self.a+self.b+self.c)/2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
from tkinter import *
from tkinter import messagebox
ds=[]
def nhapDL():
  try:
    canha=a.get()
    canhb=b.get()
    canhc=c.get()
    if canha<0 or canhb<0 or canhc<0:
        messagebox.showwarning('Thong bao','canh phai la so duong')
    else:
        obj=tamgiac(canha,canhb,canhc)
        ds.append(obj)
  except:
      messagebox.showwarning('Thong bao','Du lieu sai')
def tinhtoan():
  try:
    t=0
    kq1=' '
    m=1
    mindt=ds[0].dientich()
    for i in range(0,len(ds)):
        kq1= kq1+'chu vi hinh '+ str(i+1)+'la'+ str(ds[i].chuvi()) +'\n'
        t+=ds[i].dientich()
        if mindt>ds[i].dientich():
            mindt=ds[i].dientich()
            m=m+i
    
    kq1=kq1+'tong dien tich la'+str(t)+'\n'+'dien tich nho nhat la'+str(mindt)+'\n'+'hinh so'+str(m)
    Lkq.config(text=kq1)
    Lkq.grid(row=6)
  except:
      messagebox.showwarning('Thong bao','Du lieu sai')
w=Tk()
w.geometry('500x500')
w.title('Bai thi')
L1= Label(w,text='Hay nhap du lieu').grid(row=0)
L2=Label(w,text='canh a: ').grid(column=0,row=1)
a=DoubleVar()
E1=Entry(w,textvariable=a).grid(column=1,row=1)
L3=Label(w,text='canh b: ').grid(column=0,row=2)
b=DoubleVar()
E2=Entry(w,textvariable=b).grid(column=1,row=2)
L4=Label(w,text='canh c: ').grid(column=0,row=3)
c=DoubleVar()
E3=Entry(w,textvariable=c).grid(column=1,row=3)
B1=Button(w,text='nhap DL',command=nhapDL).grid(column=0,row=4)
B2=Button(w,text='tinh toan',command=tinhtoan).grid(column=1,row=4)
Lkq=Label(w)
w.mainloop()
test code 123
