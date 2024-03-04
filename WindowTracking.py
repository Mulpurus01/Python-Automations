#! This code geneartes two files within the project folder
#! 1. sessionUssage: Gives the log-in and log-out time
#! 2. sessionTracker: Gives the windows the user is in during the usage

#! evidenceGenerator\Scripts\activate
#! python EvidenceGenerator.py
#! Loads the current focus window to file in the project folder
#! Give the Session IDE_TIME at line 22 in minutes, currently it's 11 minutes
#! File Name chagnes required at line 21, 22, 23
#! Create virtual environment for this file to run, use below commands
#! 1. python -m venv <Environment Name> #--> To create environment with given Name
#! 2. <Environment Name>\Scripts\activate #--> To start the environment
#! 3. deactivate #--> To stop  the environment

#! Eternal libraries needed for this code are below
#!python -m pip install psutil
#!python -m pip install pywin32

from sys import exit
from math import ceil
from time import sleep
from psutil import Process
from datetime import datetime
from traceback import format_exc
from tkinter import Tk, Label, Button
from win32process import GetWindowThreadProcessId
from win32api import GetTickCount, GetLastInputInfo
from win32gui import GetWindowText, GetForegroundWindow

startTime=datetime.now()

entryMode='CloudPC'
sessionUsage='VS-CODE-APP'+startTime.strftime('%b')+'SessionStartEnd.log'
sessionLogger='DAY-Log'+startTime.strftime('%d-%b-%Y')+'.log'

def checkActiveStatus():
    GRACE_IDEL_TIME=11
    return True if ((GetTickCount() - GetLastInputInfo())/(1000*60))<=GRACE_IDEL_TIME else False

def showPopUp(message):
    root=Tk()
    root.title('Session Halt Warning')
    root.attributes('-topmost',True)
    popUpBody="Hello Master!!!\n\n Projet Hail Hydra Begins.\nReason for POPuP is "+message+"\n\nsession started at "+startTime.strftime('%d-%b-%Y %H:%M:%S')+"\nSession halted at"+datetime.now().strftime('%d-%b-%Y %H:%M:%S')+"Total usage is "+str(ceil(((datetime.now()-startTime).total_seconds()/60)*100)/100)
    label=Label(root,text=popUpBody,justify='left',padx=10,pady=10)
    label.pack()
    def on_ok():
        root.destroy()
        if 'MULPURUS: You\'re inactive' not in message:
            exit(message)
    button=Button(root,text='OK',command=on_ok)
    button.pack()
    root.mainloop()

def getWindowName(window):
    try:
        if 'OUTLOOK'.upper() in window.upper():
            return 'In Microsoft Outlook'
        elif 'Microsoft Teams'.upper() in window.upper():
            return 'Microsoft Teams'
        elif 'Google Chrome'.upper() in window.upper():
            return 'Google Chrome'
        else:
            return window
    except Exception as e:
        return window

def sessionTracker():
    with open(sessionLogger,mode='a',encoding='utf-8') as fw:
        fw.write('----------------------------------------\n')
        fw.write('Session started at '+startTime.strftime('%d-%b-%Y %H:%M:%S')+'\n')
        fw.write('-----------------------------------------\n')
        fw.write('Time of note, ApplicationName,TrimmedName,WindowName\n')
        fw.write('-----------------------------------------\n')
        fw.flush()
        
        currentWindow=None
        while True:
            if not checkActiveStatus():
                exit('MULPURUS: You\'re inactive')
            elif currentWindow!=GetWindowText(GetForegroundWindow()):
                sleep(0.11)
                try:
                    process=Process(GetWindowThreadProcessId(GetForegroundWindow())[-1])
                except Exception as e:
                    sleep(1)
                finally:
                    currentWindow=GetWindowText(GetForegroundWindow())
                try:
                    fw.write(datetime.now().strftime('%d-%b-%Y %H:%M:%S')+';'+process.name()+';'+getWindowName(currentWindow)+';'+currentWindow+'\n')
                    fw.flush()
                except OSError as e:
                    sleep(1)
                    showPopUp('Writing into file flush error')
                except Exception as e:
                    sleep(1)
                    print('MULPURUS: EXCEPTION OCCURED WHILE WRITING INTO FILE')
                    print(e)
                    print(format_exc())
                else:#Eexcute when above try block des not encount with any exception
                    currentWindow=GetWindowText(GetForegroundWindow())
                    
def main():
    sessionTracker()

if __name__=='__main__':
    message=''
    try:
        main()
    except KeyboardInterrupt:
        print('Manually Terminated by ctrl+c')
        print("session started at "+startTime.strftime('%d-%b-%Y %H:%M:%S')+"\nSession Manually ended at"+datetime.now().strftime('%d-%b-%Y %H:%M:%S')+"Total usage is "+str(ceil(((datetime.now()-startTime).total_seconds()/60)*100)/100))
    except SystemExit as e: ###Ended the tracker as user in Active from exit()
        message=str(e)
        print(e)
        print("session started at "+startTime.strftime('%d-%b-%Y %H:%M:%S')+"\nSession ended due to inactivity at"+datetime.now().strftime('%d-%b-%Y %H:%M:%S')+"Total usage is "+str(ceil(((datetime.now()-startTime).total_seconds()/60)*100)/100))
    except OSError:
        print('MULPURUS: writing into file flush error')
        print("session started at "+startTime.strftime('%d-%b-%Y %H:%M:%S')+"\nSession ended due to flush error at"+datetime.now().strftime('%d-%b-%Y %H:%M:%S')+"Total usage is "+str(ceil(((datetime.now()-startTime).total_seconds()/60)*100)/100))
    except Exception as e:
        print('mulpuru exception occured while closing the main')
        print(e)
        print(format_exc())
    finally:
        with open(sessionUsage,mode='a',encoding='UTF-8') as wf:
            wf.write(entryMode+' session started at '+startTime.strftime('%d-%b-%Y %H:%M:%S')+"\nSession ended at"+datetime.now().strftime('%d-%b-%Y %H:%M:%S')+"Total usage is "+str(ceil(((datetime.now()-startTime).total_seconds()/60)*100)/100)+'\n')
        with open(sessionLogger,mode='a',encoding='utf-8') as fw:
            fw.write('----------------------------------------\n')
            fw.write('Session ended at '+datetime.now().strftime('%d-%b-%Y %H:%M:%S')+"Total usage is "+str(ceil(((datetime.now()-startTime).total_seconds()/60)*100)/100)+'\n')
            fw.write('-----------------------------------------\n')
        if 'MULPURUS: You\'re inactive' in message:
            showPopUp(message)

