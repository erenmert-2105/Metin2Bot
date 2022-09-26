import time
import pyautogui
import datetime
import os
import warnings
import psutil

#
path="C:/Users/erenm/OneDrive/Masaüstü/metin2bot/"
#id of pvp
pvp=("Leran2")

warnings.filterwarnings('ignore')
#out-in mod
mode=1
#location of game icon
inx=460
iny=1060

#location of boss npc
npcx=615
npcy=327
#how many bosses
number=7

#set 1 to starter if bosses ready to kill
#else set 0
starter=1
    






def Boss(npcx,npcy,number):
    os.startfile(path+"tab.exe", 'runas')
    time.sleep(1)
    Click(1005,431)
    time.sleep(10)
    Click(npcx,npcy)#boss ring giriş npc
    Click(776,287)
    Click(769,335)
    time.sleep(10)
    Oto_Av_Boss() 
    time.sleep(2)
    os.startfile(path+"tab.exe", 'runas')
    time.sleep(1)
    Click2(number)#kaç bos kesicek number ı degiştir
    time.sleep(2)


def Metin():   
    Click(796,812,1)
    Click(770,412)
    Click(752,350)#metin bolgesi
    Click(770,329)
    time.sleep(10)
    Oto_Av_Metin()    

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;
    
def Out():
    Click(1426,13)
    
def In(x,y):
    pyautogui.moveTo(x, y,0.5)
    pyautogui.moveTo(x, y,0.5)
    Click(x,y)
    
def Passed(now1):
    
    now2 = datetime.datetime.now()
    passed = (now2-now1)
    sec = passed.total_seconds()/60
    return sec

def Click(x,y,right=0,delay=0.5):
    if right==0:
        
        pyautogui.moveTo(x, y,delay)
        time.sleep(0.5)
        pyautogui.click()
    if right==1:
        
        pyautogui.moveTo(x, y,delay)
        time.sleep(0.5)
        pyautogui.click(button='right')
        
def Click2(number=1,mode=0):
    array=([(701,121),(713,171),(713,225),(713,268),(713,326),(713,385),(713,430)])
    
    if number==1:
        time.sleep(0.5)
        pyautogui.moveTo(array[0][0], array[0][1],0.5)
        time.sleep(0.5)
        pyautogui.click()
        
        time.sleep(0.5)
        pyautogui.moveTo(960, 430,0.5)
        time.sleep(0.5)
        pyautogui.click()
    if number>1 and number<8:
        for i in range(number):
            if i != 100:
                time.sleep(0.5)
                pyautogui.moveTo(array[i][0], array[i][1],0.5)
                time.sleep(0.5)
                pyautogui.click()
                
                time.sleep(0.5)
                pyautogui.moveTo(960, 430,0.5)
                time.sleep(0.5)
                pyautogui.click()
    if number >7:
        for i in range(7):
            if i != 100:
                time.sleep(0.5)
                pyautogui.moveTo(array[i][0], array[i][1],0.5)
                time.sleep(0.5)
                pyautogui.click()
                
                time.sleep(0.5)
                pyautogui.moveTo(960, 430,0.5)
                time.sleep(0.5)
                pyautogui.click()
        
        pyautogui.scroll(-10)
        time.sleep(0.4)
        pyautogui.scroll(-10)
        time.sleep(0.4)
        pyautogui.scroll(-10)
        time.sleep(0.4)
        pyautogui.scroll(-10)
        time.sleep(0.4)
        pyautogui.scroll(-10)
        time.sleep(0.4)
        for i in range(number-7):
            i=i+4
            pyautogui.moveTo(array[i][0], array[i][1],1)
            time.sleep(0.5)
            pyautogui.click()

            time.sleep(0.5)
            pyautogui.moveTo(960, 430,1)
            time.sleep(0.5)
            pyautogui.click()

                
def Oto_Av_Boss():
    os.startfile(path+"u.exe", 'runas')
    time.sleep(1)
    Click(780,560,0,0.2)
    Click(780,640,0,0.2)
    Click(770,667,0,0.2)
    Click(854,172,0,0.2)  

    
def Oto_Av_Metin():
    os.startfile(path+"u.exe", 'runas')
    time.sleep(1)
    Click(780,560)
    Click(825,640)
    Click(769,666)
    Click(854,172)
            
 

    


time.sleep(3)

if mode ==1:
    while True: 
        if checkIfProcessRunning(pvp) == False:
            break
        if starter>0:
            In(inx,iny)
            Boss(npcx,npcy,number)
            time.sleep(90)
        if starter==0:
            In(inx,iny)
        now1 = datetime.datetime.now()
        starter=starter+1
        Metin()
        Out()
        while True:
            if checkIfProcessRunning(pvp) == False:
                break
            time.sleep(2)
            Passed(now1)
            print(Passed(now1))
            if Passed(now1) >= 14:
                break
if mode == 0:
    while True: 
        if checkIfProcessRunning(pvp) == False:
            break
        if starter>0:
            
            Boss(npcx,npcy,number)
            time.sleep(90)
        now1 = datetime.datetime.now()
        starter=starter+1
        Metin()
        while True:
            if checkIfProcessRunning(pvp) == False:
                break
            time.sleep(2)
            Passed(now1)
            print(Passed(now1))
            if Passed(now1) >= 14:
                break
    

        
        