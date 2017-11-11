#Sara virtual Assistant.Licensed under GPLv2 by Subrata Sarkar(subrotosarkar32@gmail.com)
import Tkinter,os,time
from PIL import ImageTk,Image
from Tkconstants import *
import _tkinter # If this fails your Python may not be configured for Tk
tkinter = _tkinter # b/w compat for export
TclError = _tkinter.TclError
import webbrowser
import urllib2
import urllib
import re
import psutil
import tkMessageBox
import speech_recognition as sr
def load_image(file):# function to load images
        '''This function returns original image if PIL is present else runs not avaible image'''
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        file = os.path.join(main_dir, file)        
        try:
             from PIL import ImageTk,Image
             q = ImageTk.PhotoImage(Image.open(file))
             return q
        except ImportError:
             print 'PIL not found.Please install and run'
             q=Tkinter.PhotoImage(file=str(file))
             return q

root=Tkinter.Tk()
root.minsize(840,430)
root.title('Sara')
#Here the main parent program strats
img0=load_image('aiback.jpg')
#making text box and scrollbar
strvar=Tkinter.StringVar()
text_frame=Tkinter.Frame(root,borderwidth=1, relief="sunken")
text1 =Tkinter.Text(root,wrap="word",background="#2c8da9",foreground="white",undo=True,font=("siyam rupali",10),state='disabled')
scroll=Tkinter.Scrollbar(root,orient="vertical",background="#146b85",troughcolor="#2c8da9",width=20,command=text1.yview)
entrye=Tkinter.Entry(root,relief=FLAT,background="#2c8da9",foreground="white",width=10,textvariable=strvar)
text1.config(yscrollcommand=scroll.set)
scroll.pack(in_=text_frame,side="right", fill="y", expand=False)
entrye.pack(in_=text_frame,side="bottom", fill="x", expand=False)
text1.pack(in_=text_frame, side="left", fill="both", expand=True)
text1.focus()
text_frame.place(bordermode=OUTSIDE,height=400,width=500 )
text1.imglist=[]


label=Tkinter.Label(root,relief=FLAT,background="#2c8da9",foreground="white",text='image to be supplied',image=img0)
label.place(x=510,y=0)
def helpart():
        tkMessageBox.showinfo('Help','''1.Click on  start to start button to start.\n2.Say 'search...'. to search for something.\n\
3.Say 'play...'. to youtube for something.\n4.Say 'write....' to write to text file.\n5.Say 'find ...' to search for a file in your pc.''')
def credit():
        tkMessageBox.showinfo('Credit','Made by Subrata Sarkar(subrotosarkar32@gmail.com) and creditsto the makers of the packages used.')
button2=Tkinter.Button(root,relief=FLAT,background="#2c8da9",foreground="white",width=15,text='HELP',command=helpart)
button2.place(x=600,y=380)
button3=Tkinter.Button(root,relief=FLAT,background="#2c8da9",foreground="white",width=23,text='CREDIT',command=credit)
button3.place(x=710,y=380)
def system_say(event=None,say1='Nothing passed into function'):
        engine = pyttsx.init()
        try:
                engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
        except:
                pass
        engine.say(say1)
        engine.runAndWait()
        text1.config(state='normal')
        text1.insert(Tkinter.INSERT,say1+'\n')
        text1.config(state='disabled')
#Main function
def send_to_ai(event=None):
        usrsay=entrye.get()
        if usrsay=='':
                

                # obtain audio from the microphone
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Say something!")
                    audio = r.listen(source)

                # recognize speech using Google.Note one can also try sphinx for offline sppech recognition.
                var=''
                try:
                        usrsay=str(r.recognize_google(audio,language='en-IN'))
                        print usrsay
                        strvar.set(usrsay)
                except sr.UnknownValueError:
                    print("Google could not understand audio")
                except sr.RequestError as e:
                    print("Google error; {0}".format(e))
        if usrsay!='':
                global text1
                print usrsay
                text1.config(state='normal')
                text1.insert(Tkinter.INSERT,str(usrsay)+'\n')
                text1.config(state='disabled')
                usrsaylst=usrsay.split(' ')
                strvar.set('')
                #work to be done when search keyword is used
                if usrsaylst[0]=='search':
                        try:
                               print usrsaylst[2]
                               if usrsaylst[1]=='for' :
                                       link='+'.join(usrsaylst[2:])
                                       system_say(say1='Searching for '+' '.join(usrsaylst[2:]))
                                       webbrowser.open('https://www.google.co.in/search?q=' + link)
                               else:
                                       link='+'.join(usrsaylst[1:])
                                       system_say(say1='Searching for '+' '.join(usrsaylst[1:]))
                                       webbrowser.open('https://www.google.co.in/search?q=' + link)    
                        except Exception as e:
                              link='+'.join(usrsaylst[1:])
                              system_say(say1='Searching for '+' '.join(usrsaylst[1:]))
                              webbrowser.open('https://www.google.co.in/search?q=' + link)
                #work to be done when write keyword is used
                elif usrsaylst[0]=='write':
                        file1=open(str(usrsaylst[1])+'.txt','w+')
                        file1.write(' '.join(usrsaylst[1:]))
                        file1.close()
                        system_say(say1='Completed writing speech to text file.')
                        os.startfile(str(usrsaylst[1])+'.txt')
                #work to be done when play or youtube keyword is used
                elif usrsaylst[0]=='play' or usrsaylst[0]=='youtube':
                        link=' '.join(usrsaylst[1:])
                        url = 'https://www.youtube.com/results?'
                        search_query=link
                        args = urllib.urlencode({'search_query':search_query})
                        conn = urllib2.urlopen(url,args)
                        html_content = conn.read()
                        conn.close()
                        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content)
                        print search_results
                        system_say(say1='Searching for '+search_query)
                        webbrowser.open("https://www.youtube.com/watch?v=" + search_results[0])
                #work to be done when find keyword is used
                elif usrsaylst[0]=='find':
                        try:
                                if 'in drive' in usrsay:
                                      finddirfile=list(usrsay.partition(' in drive '))
                                      finddirfile.pop(1)
                                      findfile=' '.join(finddirfile[0].split()[1:])
                                      finddir=finddirfile[1]
                                      print finddirfile,findfile,finddir
                                      dps = psutil.disk_partitions()
                                      for dp1 in dps:
                                          if dp1.device[0]==finddir.capitalize():
                                              dp=dp1
                                              break
                                      filelst=[]
                                      number=0
                                      print dp.device, dp.fstype, dp.opts
                                      for root, dirs, files in os.walk(dp.device):
                                          for name in files:
                                             if findfile in name:
                                                 filepath=os.path.abspath(os.path.join(root, name))
                                                 filelst+=[filepath]
                                                 number+=1
                                                 text1.config(state='normal')
                                                 text1.insert(Tkinter.INSERT,str(number)+':'+filepath+'\n')
                                                 text1.config(state='disabled')
                                                 print number,filepath

                                else:
                                    file45=' '.join(usrsaylst[1:])
                                    dps = psutil.disk_partitions()
                                    # Only show a couple of different types of devices, for brevity
                                    filelst=[]
                                    number=0
                                    dps = psutil.disk_partitions()
                                    for dp in dps:
                                        print(dp.device, dp.fstype, dp.opts)
                                        for root, dirs, files in os.walk(dp.device):
                                          for name in files:
                                              if findfile in name:
                                                  filepath=os.path.abspath(os.path.join(root, name))
                                                  filelst+=[filepath]
                                                  number+=1
                                                  text1.config(state='normal')
                                                  text1.insert(Tkinter.INSERT,str(number)+':'+filepath+'\n')
                                                  text1.config(state='disabled')
                                                  print number,filepath
                                
                                if len(filelst)>=1:
                                        system_say(sayl='These are the results I found. Please say file number to open file.')
                                        if len(filelst)!=1:
                                                while not(usrsay.isdigit()):
                                                        # obtain audio from the microphone
                                                        r = sr.Recognizer()
                                                        with sr.Microphone() as source:
                                                            print("Say file number!")
                                                            audio = r.listen(source)

                                                        # recognize speech using Sphinx
                                                        var=''
                                                        try:
                                                                usrsay=str(r.recognize_google(audio,language='en-IN'))
                                                                print usrsay
                                                                strvar.set(usrsay)
                                                        except sr.UnknownValueError:
                                                            print("Google could not understand audio")
                                                        except sr.RequestError as e:
                                                            print("Google error; {0}".format(e))
                                                        os.startfile(filelst[int(usrsay)-1])
                                        else:
                                                os.startfile(filelst[int(usrsay)-1][0])
                                        system_say(say1='The file has been opened.')
                                        strvar.set('')
                                else:
                                        system_say(say1='I found no files containing these file name.')
                        except Exception as e:
                                print e
   
                        
                        
                #work to be done for unkown keyword
                else:
                        system_say(say1='''Sir you didn't program me for this.''')
        else:
                pass

entrye.bind("<Down>",send_to_ai)
import pyttsx
system_say(say1='Welcome Sir! Sara is here at your service.')
print 'Start'
button1=Tkinter.Button(root,relief=FLAT,background="#2c8da9",foreground="white",width=15,text='SART',command=send_to_ai)
button1.place(x=510,y=380)

root.mainloop()
