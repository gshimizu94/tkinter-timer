# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 16:02:12 2020

@author: gshim94
"""

import tkinter as Tk
import time
import sys
 
class Timer(Tk.Frame):
    """
    Class for simple tkinter-based timer application

    Attributes:
        self.time int:
            seconds to count
        self.finish float:
            UNIX end time
        self.timer Tk.Label:
            Label to display the remaining time
        self.b2 Tk.Button:
            Button to finish immediately
    """
    def __init__(self,master=None): 
        Tk.Frame.__init__(self,master)
 
        self.master.title('timer')
        self.master.geometry("300x120")
 
        self.time = 5
        self.timer = Tk.Label(self,text=u'00:00',font='Arial, 25')        
         
        b2 = Tk.Button(self,text='Stop',command=self.stop)
 
        b2.grid(row=2, column=0,columnspan=4, padx=5, pady=2,sticky=Tk.W+Tk.E)
        self.timer.grid(row=1, column=0,columnspan=4, padx=5, pady=2,sticky=Tk.W+Tk.E)
        
 
    def start(self):
        '''
        calculate finish time and start count
        '''       
        self.finish = time.time() + self.time
        self.count()
 
    def count(self):
        '''
        count time and update Label every seconds.
        '''
        t = self.finish - time.time()
        if t < 0:
            self.quit()
            exit()
 
        else:
            self.timer.config(text='%02d:%02d'%(t/60,t%60))
            self.after(100, self.count)
 
 
    def settime(self, t1):
        '''
        set the time from command-line argument
        '''
        self.time = t1
        
    def stop(self): 
        '''
        exit application immediately by pusshing the button
        '''
        self.quit()
        exit() 
 
if __name__ == '__main__':
    args = sys.argv
    f = Timer()
    f.pack()
    if len(args) > 0:
        f.settime(int(args[1]))
    f.start()
    f.mainloop()
