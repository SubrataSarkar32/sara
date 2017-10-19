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
root.minsize(800,450)

#Here the main parent program strats


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

text1.config(state='normal')
text1.insert(Tkinter.INSERT,'''Welcome Sir! Sara is here at your service.\n''')
text1.config(state='disabled')
label=Tkinter.Label(root,relief=FLAT,background="#2c8da9",foreground="white",width=10,text='image to be supplied')
label.place(x=510,y=0)
button1=Tkinter.Button(root,relief=FLAT,background="#2c8da9",foreground="white",width=10,text='HELP')
button1.place(x=510,y=380)
button2=Tkinter.Button(root,relief=FLAT,background="#2c8da9",foreground="white",width=10,text='CREDIT')
button2.place(x=580,y=380)

def send_to_ai(event=None):
        usrsay=entrye.get()
        if usrsay=='':
                import speech_recognition as sr

                # obtain audio from the microphone
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Say something!")
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
        if usrsay!='':
                global text1
                print usrsay
                text1.config(state='normal')
                text1.insert(Tkinter.INSERT,str(usrsay)+'\n')
                text1.config(state='disabled')
                usrsaylst=usrsay.split(' ')
                strvar.set('')
                if usrsaylst[0]=='search':
                        try:
                               print usrsaylst[2]
                               if usrsaylst[1]=='for' :
                                       link='+'.join(usrsaylst[2:])
                                       engine = pyttsx.init()
                                       try:
                                               engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
                                       except:
                                               pass
                                       engine.say('Searching for '+' '.join(usrsaylst[2:]))
                                       engine.runAndWait()
                                       text1.config(state='normal')
                                       text1.insert(Tkinter.INSERT,'Searching for '+' '.join(usrsaylst[2:])+'\n')
                                       text1.config(state='disabled')
                                       webbrowser.open('https://www.google.co.in/search?q=' + link)
                               else:
                                       link='+'.join(usrsaylst[1:])
                                       engine = pyttsx.init()
                                       try:
                                               engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
                                       except:
                                               pass
                                       engine.say('Searching for '+' '.join(usrsaylst[2:]))
                                       engine.runAndWait()
                                       text1.config(state='normal')
                                       text1.insert(Tkinter.INSERT,'Searching for '+' '.join(usrsaylst[2:])+'\n')
                                       text1.config(state='disabled')
                                       webbrowser.open('https://www.google.co.in/search?q=' + link)    
                        except Exception as e:
                              link='+'.join(usrsaylst[1:])
                              engine = pyttsx.init()
                              try:
                                      engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
                              except:
                                      pass
                              engine.say('Seaching for '+' '.join(usrsaylst[1:]))
                              engine.runAndWait()
                              text1.config(state='normal')
                              text1.insert(Tkinter.INSERT,'Searching for '+' '.join(usrsaylst[1:])+'\n')
                              text1.config(state='disabled')
                              webbrowser.open('https://www.google.co.in/search?q=' + link)
                elif usrsaylst[0]=='write':
                        file1=open(str(usrsaylst[1])+'.txt','w+')
                        file1.write(' '.join(usrsaylst[1:]))
                        file1.close()
                        engine = pyttsx.init()
                        try:
                                engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
                        except:
                                pass
                        engine.say('''Completed writing speech to text file.''' )
                        engine.runAndWait()
                        text1.config(state='normal')
                        text1.insert(Tkinter.INSERT,'''Completed writing speech to text file.\n''')
                        text1.config(state='disabled')
                        os.startfile(str(usrsaylst[1])+'.txt')
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
                        engine = pyttsx.init()
                        try:
                                engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
                        except:
                                pass
                        engine.say('Searching for '+search_query)
                        engine.runAndWait()
                        text1.config(state='normal')
                        text1.insert(Tkinter.INSERT,'Searching for '+' '.join(link)+'\n')
                        text1.config(state='disabled')
                        webbrowser.open("https://www.youtube.com/watch?v=" + search_results[0])
                        
                else:
                        engine = pyttsx.init()
                        try:
                                engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
                        except:
                                pass
                        engine.say('''Sir you didn't program me for this.''' )
                        engine.runAndWait()
        else:
                pass

entrye.bind("<Down>",send_to_ai)
import pyttsx
engine = pyttsx.init()
try:
     engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
except:
        pass
engine.say('Welcome Sir! Sara is here at your service.')
engine.runAndWait()
print 'Start'
send_to_ai()
root.mainloop()
