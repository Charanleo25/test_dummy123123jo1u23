from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
import tkinter as tk
import os
import shutil
from ATS import *
import ATS

class homeui:

   def __init__(self,root):

      self.root=root

      self.root.title("Applicants tracking system")

      self.root.geometry("1366x700+0+0")
      frame_input=Frame(self.root,bg="lightblue")
      frame_input.place(x=0,y=0,height=700,width=1366)
      label1=Label(text="Applicants tracking system",font=('times new roman',32,),fg="royalblue",bg='lightgray')               
      label1.place(x=475,y=20)

      btn1=Button(text="Student",command=self.stulog,cursor="hand2",font=("times new roman",15),width=20,height=2)                 
      btn1.place(x=350,y=340)

      btn2=Button(text="Recruiter",command=self.reclog,cursor="hand2",font=("times new roman",15),width=20,height=2)                 
      btn2.place(x=800,y=340)



   def stulog(self):
      #Frame_login=Frame(self.root,bg="lightgray")

      #Frame_login.place(x=0,y=0,height=700,width=1366)

      frame_input=Frame(self.root,bg='lightblue')

      frame_input.place(x=0,y=0,height=700,width=1366)

      label2=Label(text="Student",font=('times new roman',32,),fg="royalblue",bg='lightgray')               
      label2.place(x=650,y=20)

      btn5=Button(text="Recruiter",command=self.reclog,cursor="hand2",font=("times new roman",15),width=10,height=1)                 
      btn5.place(x=10,y=10)


      btn1=Button(text="Login",command=self.stulogin,cursor="hand2",font=("times new roman",15),width=20,height=2)                 
      btn1.place(x=350,y=340)

      btn2=Button(text="Register",command=self.stureg,cursor="hand2",font=("times new roman",15),width=20,height=2)                 
      btn2.place(x=850,y=340)


   def reclog(self):
      #Frame_login1=Frame(self.root,bg="blue")

      #Frame_login1.place(x=0,y=0,height=700,width=1366)

      frame_input=Frame(self.root,bg='lightblue')

      frame_input.place(x=0,y=0,height=700,width=1366)

      label2=Label(text="Recruiter",font=('times new roman',32,),fg="royalblue",bg='lightgray')               
      label2.place(x=650,y=20)

      btn6=Button(text="Student",command=self.stulog,cursor="hand2",font=("times new roman",15),width=10,height=1)                 
      btn6.place(x=10,y=10)



      btn3=Button(text="Login",command=self.reclogin,cursor="hand2",font=("times new roman",15),width=20,height=2)                 
      btn3.place(x=350,y=340)

      btn4=Button(text="Register",command=self.recreg,cursor="hand2",font=("times new roman",15),width=20,height=2)                 
      btn4.place(x=850,y=340)



   def dash(self):


      #if self.email_txt.get()=="" or self.password.get()=="":messagebox.showerror("Error","All fields are required",parent=self.root)

      #else:
           self.root.title("Applicants tracking system")
           self.root.geometry("1366x700+0+0")
           frame_input=Frame(self.root,bg="lightblue")
           frame_input.place(x=0,y=0,height=700,width=1366)

           btn8=Button(text="logout",command=self.reclog,cursor="hand2",font=("times new roman",15),width=10,height=1)                 
           btn8.place(x=1200,y=0)
        
           btn1=Button(text="Dashboard",cursor="hand2",font=("times new roman",15),width=20,height=2)                 
           btn1.place(x=0,y=0)
   
           btn2=Button(text="Result",command=self.result,cursor="hand2",font=("times new roman",15),width=20,height=2)                 
           btn2.place(x=230,y=0)

           btn3=Button(text="Activity",command=self.act,cursor="hand2",font=("times new roman",15),width=20,height=2)                 
           btn3.place(x=460,y=0)

           btn4=Button(text="Upload job description",cursor="hand2",font=("times new roman",15),width=50,height=10)                 
           btn4.place(x=100,y=100)

           btn5=Button(text="Resume upload",cursor="hand2",font=("times new roman",15),width=50,height=10)                 
           btn5.place(x=700,y=100)




   def shome(self):


      #if self.email_txt.get()=="" or self.password.get()=="":messagebox.showerror("Error","All fields are required",parent=self.root)

      #else:
           self.root.title("Applicants tracking system")
           self.root.geometry("1366x700+0+0")
           frame_input=Frame(self.root,bg="lightblue")
           frame_input.place(x=0,y=0,height=700,width=1366)

           btn8=Button(text="logout",command=self.stulog,cursor="hand2",font=("times new roman",15),width=10,height=1)                 
           btn8.place(x=1200,y=0)
        
           btn1=Button(text="Home",cursor="hand2",font=("times new roman",15),width=20,height=2)                 
           btn1.place(x=0,y=0)
   

           btn4=Button(text="Technology",command=self.tech,cursor="hand2",font=("times new roman",15),width=50,height=10)                 
           btn4.place(x=100,y=100)

           btn5=Button(text="Sales and services",cursor="hand2",font=("times new roman",15),width=50,height=10)                 
           btn5.place(x=700,y=100)

           btn6=Button(text="Teaching",cursor="hand2",font=("times new roman",15),width=50,height=10)                 
           btn6.place(x=100,y=400)

           btn7=Button(text="Others",cursor="hand2",font=("times new roman",15),width=50,height=10)                 
           btn7.place(x=700,y=400)
   


   def tech(self):


      #if self.email_txt.get()=="" or self.password.get()=="":messagebox.showerror("Error","All fields are required",parent=self.root)

      #else:

        
        self.root.title("Applicants tracking system")
        self.root.geometry("1366x700+0+0")
        frame_input=Frame(self.root,bg="lightblue")
        frame_input.place(x=0,y=0,height=700,width=1366)

        label2=Label(text="Resume upload",font=('times new roman',20,),fg="royalblue",bg="lightblue")               
        label2.place(x=600,y=20)

        btn1=Button(text="Home",command=self.shome,cursor="hand2",font=("times new roman",15),width=20,height=2)                 
        btn1.place(x=0,y=0)

        btn8=Button(text="logout",command=self.stulog,cursor="hand2",font=("times new roman",15),width=10,height=1)                 
        btn8.place(x=1200,y=0)

        btn4=Button(text="Web developer",command=self.webd,cursor="hand2",font=("times new roman",15),width=40,height=4)                 
        btn4.place(x=475,y=100)

        btn5=Button(text="Software testing",command=self.st,cursor="hand2",font=("times new roman",15),width=40,height=4)                 
        btn5.place(x=475,y=250)

        btn6=Button(text="Software developer",command=self.sd,cursor="hand2",font=("times new roman",15),width=40,height=4)                 
        btn6.place(x=475,y=400)

        btn7=Button(text="Others",command=self.ot,cursor="hand2",font=("times new roman",15),width=40,height=4)                 
        btn7.place(x=475,y=550)


   def upload(self):
     filename=fd.askopenfile()
     #print('Selected:',filename)
     #datapath = os.path.dirname(filename.name)
     filetype = os.path.realpath(filename.name)
     #print(filetype)
     # print(datapath.name)
     shutil.copy(filetype,"E:/")
     job_score=resume_scan(filetype)
     #print(job_score)
     




      
    
     self.root.title("Applicants tracking system")
     self.root.geometry("1366x700+0+0")
     frame_input=Frame(self.root,bg="lightblue")
     frame_input.place(x=0,y=0,height=700,width=1366)

     label2=Label(text="Result",font=('times new roman',20,),fg="royalblue",bg="lightblue")               
     label2.place(x=600,y=20)

     label3=Label(text=ATS.match,font=('times new roman',20,),fg="royalblue",bg="lightblue")
     label3.place(x=600,y=100)


     btn1=Button(text="Home",command=self.shome,cursor="hand2",font=("times new roman",15),width=20,height=2)                 
     btn1.place(x=0,y=0)

     btn2=Button(text="Ok",command=self.tech,cursor="hand2",font=("times new roman",15),width=10,height=1)
     btn2.place(x=600,y=550)

        
  
   def webd(self):


      #if self.email_txt.get()=="" or self.password.get()=="":messagebox.showerror("Error","All fields are required",parent=self.root)

      #else:
        self.root.title("Applicants tracking system")
        self.root.geometry("1366x700+0+0")
        frame_input=Frame(self.root,bg="lightblue")
        frame_input.place(x=0,y=0,height=700,width=1366)

        btn1=Button(text="home",command=self.shome,cursor="hand2",font=("times new roman",15),width=20,height=2)                 
        btn1.place(x=0,y=0)

     

        btn4=Button(text="Upload",command=self.upload,cursor="hand2",font=("times new roman",15),width=20,height=2)                 
        btn4.place(x=475,y=200)

       # root=tk.Tk()


   def st(self):


      #if self.email_txt.get()=="" or self.password.get()=="":messagebox.showerror("Error","All fields are required",parent=self.root)

      #else:
        self.root.title("Applicants tracking system")
        self.root.geometry("1366x700+0+0")
        frame_input=Frame(self.root,bg="lightblue")
        frame_input.place(x=0,y=0,height=700,width=1366)

        btn1=Button(text="home",command=self.shome,cursor="hand2",font=("times new roman",15),width=20,height=2)                 
        btn1.place(x=0,y=0)

        btn4=Button(text="Upload",cursor="hand2",font=("times new roman",15),width=20,height=2)                 
        btn4.place(x=475,y=200)



   def sd(self):


      #if self.email_txt.get()=="" or self.password.get()=="":messagebox.showerror("Error","All fields are required",parent=self.root)

      #else:
        self.root.title("Applicants tracking system")
        self.root.geometry("1366x700+0+0")
        frame_input=Frame(self.root,bg="lightblue")
        frame_input.place(x=0,y=0,height=700,width=1366)

        btn1=Button(text="home",command=self.shome,cursor="hand2",font=("times new roman",15),width=20,height=2)                 
        btn1.place(x=0,y=0)

        btn4=Button(text="Upload",cursor="hand2",font=("times new roman",15),width=20,height=2)                 
        btn4.place(x=475,y=200)




   def ot(self):


      #if self.email_txt.get()=="" or self.password.get()=="":messagebox.showerror("Error","All fields are required",parent=self.root)

      #else:
        self.root.title("Applicants tracking system")
        self.root.geometry("1366x700+0+0")
        frame_input=Frame(self.root,bg="lightblue")
        frame_input.place(x=0,y=0,height=700,width=1366)

        btn1=Button(text="home",command=self.shome,cursor="hand2",font=("times new roman",15),width=20,height=2)                 
        btn1.place(x=0,y=0)

        btn4=Button(text="Upload",cursor="hand2",font=("times new roman",15),width=20,height=2)                 
        btn4.place(x=475,y=200)




   def recreg(self):
      self.root.title("Applicants tracking system")
      self.root.geometry("1366x700+0+0")
      frame_input=Frame(self.root,bg="lightblue")
      frame_input.place(x=0,y=0,height=700,width=1366)

      frame_input2=Frame(self.root,bg='white')
      frame_input2.place(x=320,y=130,height=450,width=630)
      label1=Label(frame_input2,text="Register Here",font=('impact',32,'bold'),fg="black",bg='white')               
      label1.place(x=45,y=20)
      label2=Label(frame_input2,text="Username",font=(15),bg='white')                  
      label2.place(x=30,y=95)
      self.entry=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')                 
      self.entry.place(x=30,y=145,width=270,height=30)
      label3=Label(frame_input2,text="Password",font=(15),bg='white')                
      label3.place(x=30,y=195)
      self.entry2=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')
      self.entry2.place(x=30,y=245,width=270,height=30)
      label4=Label(frame_input2,text="Email-id",font=(15),bg='white')
      label4.place(x=330,y=95)
      self.entry3=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')
      self.entry3.place(x=330,y=145,width=270,height=30)
      label5=Label(frame_input2,text="Confirm Password",font=(15),bg='white')
      label5.place(x=330,y=195)
      self.entry4=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')
      self.entry4.place(x=330,y=245,width=270,height=30)


      btn2=Button(frame_input2,command=self.reclogin,text="Register",cursor="hand2",font=("times new roman",15),fg="black",width=15,height=1)
             
      btn2.place(x=90,y=340)

      btn3=Button(frame_input2,command=self.reclogin,text="Already Registered?Login",cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)

      btn3.place(x=110,y=390)



   def reclogin(self):


      #if self.entry.get()==""or self.entry2.get()==""or self.entry3.get()==""or self.entry4.get()=="":
      #   messagebox.showerror("Error","All Fields Are Required",parent=self.root)
      #elif self.entry2.get()!=self.entry4.get():
      #   messagebox.showerror("Error","Password and Confirm Password Should Be Same",parent=self.root)                

      #else:

         Frame_login=Frame(self.root,bg="lightgray")

         Frame_login.place(x=0,y=0,height=700,width=1366)

      

      #self.img=ImageTk.PhotoImage(file="background-2.jpg")

      #img=Label(Frame_login,image=self.img).place(x=0,y=0,width=2067,height=700)

      

         frame_input=Frame(self.root,bg='white')

         frame_input.place(x=320,y=130,height=450,width=350)



         label1=Label(frame_input,text="Login Here",font=('impact',32,'bold'),

                   fg="black",bg='white')

         label1.place(x=75,y=20)



         label2=Label(frame_input,text="Email",font=(15),bg='white')
         label2.place(x=30,y=95)
         self.email_txt=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray')
         self.email_txt.place(x=30,y=145,width=270,height=30)    
         label3=Label(frame_input,text="Password",font=(15),bg='white')                  
         label3.place(x=30,y=195)
         self.password=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray')                   
         self.password.place(x=30,y=245,width=270,height=30)
         #btn1=Button(frame_input,text="forgot password?",cursor='hand2',font=('calibri',10),bg='white',fg='black',bd=0)
         #btn1.place(x=125,y=305)
         btn2=Button(frame_input,text="Login",command=self.dash,cursor="hand2",font=("times new roman",15),width=10,height=1)                 
         btn2.place(x=90,y=340)
         btn3=Button(frame_input,command=self.recreg,text="Not Registered?register",cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)
         btn3.place(x=110,y=390)







   def stureg(self):
      self.root.title("Applicants tracking system")
      self.root.geometry("1366x700+0+0")
      frame_input=Frame(self.root,bg="lightblue")
      frame_input.place(x=0,y=0,height=700,width=1366)

      frame_input2=Frame(self.root,bg='white')
      frame_input2.place(x=320,y=130,height=450,width=630)
      label1=Label(frame_input2,text="Register Here",font=('impact',32,'bold'),fg="black",bg='white')               
      label1.place(x=45,y=20)
      label2=Label(frame_input2,text="Username",font=(15),bg='white')                  
      label2.place(x=30,y=95)
      self.entry5=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')                 
      self.entry5.place(x=30,y=145,width=270,height=30)
      label3=Label(frame_input2,text="Password",font=(15),bg='white')                
      label3.place(x=30,y=195)
      self.entry6=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')
      self.entry6.place(x=30,y=245,width=270,height=30)
      label4=Label(frame_input2,text="Email-id",font=(15),bg='white')
      label4.place(x=330,y=95)
      self.entry7=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')
      self.entry7.place(x=330,y=145,width=270,height=30)
      label5=Label(frame_input2,text="Confirm Password",font=(15),bg='white')
      label5.place(x=330,y=195)
      self.entry8=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')
      self.entry8.place(x=330,y=245,width=270,height=30)


      btn2=Button(frame_input2,command=self.stulogin,text="Register",cursor="hand2",font=("times new roman",15),fg="black",width=15,height=1)
             
      btn2.place(x=90,y=340)

      btn3=Button(frame_input2,command=self.stulogin,text="Already Registered?Login",cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)

      btn3.place(x=110,y=390)



   def stulogin(self):


      #if self.entry.get()==""or self.entry2.get()==""or self.entry3.get()==""or self.entry4.get()=="":
      #   messagebox.showerror("Error","All Fields Are Required",parent=self.root)
      #elif self.entry2.get()!=self.entry4.get():
      #   messagebox.showerror("Error","Password and Confirm Password Should Be Same",parent=self.root)                

      #else:

         Frame_login=Frame(self.root,bg="lightgray")

         Frame_login.place(x=0,y=0,height=700,width=1366)

      

      #self.img=ImageTk.PhotoImage(file="background-2.jpg")

      #img=Label(Frame_login,image=self.img).place(x=0,y=0,width=2067,height=700)

      

         frame_input=Frame(self.root,bg='white')

         frame_input.place(x=320,y=130,height=450,width=350)



         label1=Label(frame_input,text="Login Here",font=('impact',32,'bold'),

                   fg="black",bg='white')

         label1.place(x=75,y=20)



         label2=Label(frame_input,text="Email",font=(15),bg='white')
         label2.place(x=30,y=95)
         self.semail_txt=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray')
         self.semail_txt.place(x=30,y=145,width=270,height=30)    
         label3=Label(frame_input,text="Password",font=(15),bg='white')                  
         label3.place(x=30,y=195)
         self.spassword=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray')                   
         self.spassword.place(x=30,y=245,width=270,height=30)
         #btn1=Button(frame_input,text="forgot password?",cursor='hand2',font=('calibri',10),bg='white',fg='black',bd=0)
         #btn1.place(x=125,y=305)
         btn2=Button(frame_input,text="Login",command=self.shome,cursor="hand2",font=("times new roman",15),width=10,height=1)                 
         btn2.place(x=90,y=340)
         btn3=Button(frame_input,command=self.stureg,text="Not Registered?register",cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)
         btn3.place(x=110,y=390)
   
        


   def result(self):
       
        self.root.title("Applicants tracking system")
        self.root.geometry("1366x700+0+0")
        frame_input=Frame(self.root,bg="lightblue")
        frame_input.place(x=0,y=0,height=700,width=1366)

        btn1=Button(text="Dashboard",command=self.dash,cursor="hand2",font=("times new roman",15),width=20,height=2)                 
        btn1.place(x=0,y=0)

        btn8=Button(text="logout",command=self.reclog,cursor="hand2",font=("times new roman",15),width=10,height=1)                 
        btn8.place(x=1200,y=0)

        btn2=Button(text="Result",cursor="hand2",font=("times new roman",15),width=20,height=2)                 
        btn2.place(x=230,y=0)

        btn3=Button(text="Activity",command=self.act,cursor="hand2",font=("times new roman",15),width=20,height=2)                 
        btn3.place(x=460,y=0)





   def act(self):

        self.root.title("Applicants tracking system")
        self.root.geometry("1366x700+0+0")
        frame_input=Frame(self.root,bg="lightblue")
        frame_input.place(x=0,y=0,height=700,width=1366)

        btn8=Button(text="logout",command=self.reclog,cursor="hand2",font=("times new roman",15),width=10,height=1)                 
        btn8.place(x=1200,y=0)

        btn1=Button(text="Dashboard",command=self.dash,cursor="hand2",font=("times new roman",15),width=20,height=2)                 
        btn1.place(x=0,y=0)

        btn2=Button(text="Result",command=self.result,cursor="hand2",font=("times new roman",15),width=20,height=2)                 
        btn2.place(x=230,y=0)

        btn3=Button(text="Activity",cursor="hand2",font=("times new roman",15),width=20,height=2)                 
        btn3.place(x=460,y=0)

        btn4=Button(text="Log",cursor="hand2",font=("times new roman",15),width=40,height=5)                 
        btn4.place(x=475,y=100)

        btn5=Button(text="Task",cursor="hand2",font=("times new roman",15),width=40,height=5)                 
        btn5.place(x=475,y=300)

        btn6=Button(text="Log",cursor="hand2",font=("times new roman",15),width=40,height=5)                 
        btn6.place(x=475,y=500)



  


  
root=Tk()
obj=homeui(root)
root.mainloop()
