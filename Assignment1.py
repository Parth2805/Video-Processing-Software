# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 15:45:55 2019

@author: parth's alienware
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 23:35:38 2019

@author: parth
"""

import sys

import cv2          #Install OpenCV
import numpy as np  #Install NumPy
from PIL import Image     #Install PILLOW (PIL)
from PyQt5.QtCore import QTimer  #Install PyQt5
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

class mainwindow(QMainWindow):
    
    vid1 = []
    vid2 = []
    vid3 = []
    x0 = 0
    x1 = 0
    x2 = 0
    l2 = 0
    
    def __init__(self):
        super(mainwindow, self).__init__()
        loadUi('main.ui', self)   #Load the GUI
        
        
        self.cap = cv2.VideoCapture('1.mp4')
        self.cap1 = cv2.VideoCapture('2.mp4')
        self.capture2 = cv2.VideoCapture('3.avi')
        self.success, self.i0 = self.cap.read()
        self.a, self.i1 = self.cap1.read()
        self.ret, self.image2 = self.capture2.read()
        print (self.ret)
        
        while self.success:
            self.success, self.i0 = self.cap.read()
            self.vid1.append(self.i0)
        while self.a:
            self.a, self.i1 = self.cap1.read()
            self.vid2.append(self.i1)
        while self.ret:
            self.ret, self.image2 = self.capture2.read()
            self.vid3.append(self.image2) 
            
        self.l2=len(self.vid3)         
        self.l0=len(self.vid1)
        self.l1=len(self.vid2)
        print(self.l2)
        #Read your files here...
        
        self.display(self.vid1[0], 1)        
        self.display1(self.vid2[0], 1) 
        self.display2(self.vid1[0], 1)
        self.stop1 = True
        self.stop2 = True
        self.stopc = True
        self.play1.clicked.connect(self.getVideo1)
        self.pause1.clicked.connect(self.pauseVideo1)
        self.play2.clicked.connect(self.getVideo2)
        self.pause2.clicked.connect(self.pauseVideo2)
        self.playc.clicked.connect(self.getVideo3)
        self.pausec.clicked.connect(self.pauseVideoC)
        self.convert.clicked.connect(self.convert1)
        self.fade.setChecked(True)
                
        
        
    def convert1(self):
        #
        #
        #
        #
        #
        #
        #   Your code goes here...
        #
        #
        #   Your output should be stored as "3.avi" for each transition
        #
        #
        #
        
        if(self.fade.isChecked()):
            print("Fade")
            i=0;
            i2=0;
            cap = cv2.VideoCapture('1.mp4')
            cap2=cv2.VideoCapture('2.mp4')
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter('3.avi',fourcc, 30.0, (640,480))
            frames=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            ret, frame = cap.read()
            i=i+1
            while(ret):
                if(i<=frames-33):
                    out.write(frame)
                    ret, frame= cap.read()
                    i=i+1
                else:
                    break
            
            ret2, frame2 = cap2.read()
            i2=i2+1
            
            fadein=1
           
            done=-1
            while(ret2):
                
                if (done<0):
                    for i3 in range(32):
                        
                        dst= cv2.addWeighted( frame, fadein, frame2, 1-fadein, 0)
                        out.write(dst)
                        fadein= fadein - 1/32
                        ret, frame= cap.read()
                        ret2, frame2 = cap2.read()
                        i2=i2+1
                        done=1
                out.write(frame2)
                ret2, frame2 = cap2.read()
       
          
           
            
        if(self.cut.isChecked()):
            print("CUT")
            cap = cv2.VideoCapture('1.mp4')
            cap2=cv2.VideoCapture('2.mp4')
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter('3.avi',fourcc, 30.0, (640,480))
            i=0;
            i2=0;
            ret, frame = cap.read()
            i=i+1
            while(ret):
                out.write(frame)
                ret, frame= cap.read()
                i=i+1
        
            ret2, frame2 = cap2.read()
            i2=i2+1
            while(ret2):
                out.write(frame2)
                ret2, frame2 = cap2.read()
                i2=i2+1
                
              
           
            
        
        if(self.wipe.isChecked()):
            print("Wipe")
            cap = cv2.VideoCapture('1.mp4')
            cap2=cv2.VideoCapture('2.mp4')
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter('3.avi',fourcc, 30.0, (640,480))#576,432#38,28
            ret, frame= cap.read()
            i=0
            i=i+1
            frames=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            print(frames)
            fp=frame
            while(ret):
                
                if(i<=frames-30):
        
                    out.write(frame)
                    ret, frame= cap.read()
                    i=i+1
        
                else:
                    break

            ret2, frame2= cap2.read()
            fp2=frame2
            i2=0
            i2=i2+1
            move=21
            while(ret2):
    

                while(ret):
        
                    fp[0:480,0:640]=[0,0,0]
                    fp2[0:480,0:640]=[0,0,0]
                    
                    cv2.imwrite("Frame1.jpg",frame)
                    cv2.imwrite("Frame2.jpg",frame2)
                    fp=cv2.imread("Frame1.jpg")
                    fp2=cv2.imread("Frame2.jpg")
    
                    fp2[0:480,0:move]=fp2[0:480,640-move:640]
                    fp2[0:480,move:640]=fp[0:480,0:640-move]

                    out.write(fp2)
                    ret, frame= cap.read()
                    ret2, frame2= cap2.read()         
                    move=move+21
                    
                out.write(frame2)
                ret2, frame2 = cap2.read()    
        
        if(self.scale.isChecked()):
            print("Scale")
            i=0;
            i2=0;
            cap = cv2.VideoCapture('1.mp4')
            cap2=cv2.VideoCapture('2.mp4')
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter('3.avi',fourcc, 30.0, (640,480))#576,432#38,28
        
       

            ret, frame = cap.read()
            black=frame
            i=i+1
            y=640
            x=480
            y_reduce=38
            x_reduce=28
            y_start=19
            x_start=14
            frames=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
                
            while(ret):
                    
                
                if(i<=frames-15):
                    out.write(frame)
                    ret, frame=cap.read()
                    i=i+1
                    
                else:
                        
                    black[0:480,0:640]=[0,0,0]
                    cv2.imwrite("Black.jpg",black)
                    black=cv2.imread("Black.jpg")
                    x=x-x_reduce
                    y=y-y_reduce
                    black[x_start:480-x_start,y_start:640-y_start]=cv2.resize(frame,(y,x))
                    
                    x_start=x_start+14
                    y_start=y_start+19
                    out.write(black)
                    ret, frame=cap.read()
                    i=i+1
                        
                        
                      
            ret2, frame2 = cap2.read()
            i2=i2+1
                    
            x_start=x_start-14
            y_start=y_start-19
                        
            while(ret2):
                            
                if(i2<=15):
                    
                    black[0:480,0:640]=[0,0,0]
                    cv2.imwrite("Black.jpg",black)
                    black=cv2.imread("Black.jpg")
                    
                    black[x_start:480-x_start,y_start:640-y_start]=cv2.resize(frame2,(y,x))
                    x=x+x_reduce
                    y=y+y_reduce                 
                    x_start=x_start-14
                    y_start=y_start-19
                    out.write(black)
                    ret2, frame2=cap2.read()
                    i2=i2+1
                    
                else:    
                    out.write(frame2)
                    ret2, frame2 = cap2.read()
                    i2=i2+1
                        
            
                
            
            
        if(self.picInPic.isChecked()):
            print("PIP")
            cap = cv2.VideoCapture('1.mp4')
            cap2=cv2.VideoCapture('2.mp4')
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter('3.avi',fourcc, 30.0, (640,480))#576,432#38,28
            i=0
            ret, frame = cap.read()
            fp=frame
            i=i+1
            y=640
            x=480
            x_start=64
            y_start=48
            y_reduce=19
            x_reduce=14
            frames=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

            while(ret):
    
    
                if(i<=frames-30):
                    out.write(frame)
                    ret, frame=cap.read()
                    i=i+1
                else:
                    break

            ret2, frame2= cap2.read()
            fp2=frame2
            while(ret2):
                
                while(ret):
                    fp[0:480,0:640]=[0,0,0]
                    fp2[0:480,0:640]=[0,0,0]
                    cv2.imwrite("Frame1.jpg",frame)
                    cv2.imwrite("Frame2.jpg",frame2)
                    fp=cv2.imread("Frame1.jpg")
                    fp2=cv2.imread("Frame2.jpg")        
                    
        
       
                    fp[0:x_start,y-y_start:640]=cv2.resize(frame2,(y_start,x_start))
        
                    x_start=x_start+14
                    y_start=y_start+19
                    out.write(fp)
                    ret, frame=cap.read()
                    ret2,frame2=cap2.read()
                out.write(frame2)
                ret2, frame2=cap2.read()    
        
        
        
            
               
        out.release()
        cap.release()
        cap2.release()
        cv2.destroyAllWindows()
        self.vid3 = []
        self.x2=0
        self.capture2 = cv2.VideoCapture('3.avi')
        self.ret, self.image2 = self.capture2.read()
        print (self.ret)
        
        while self.ret:
            self.ret, self.image2 = self.capture2.read()
            self.vid3.append(self.image2)
        self.l2=len(self.vid3)    
        self.display2(self.vid3[0], 1)    
        self.stopc = True
       
        
       # print("Add your code...")
     
        
        
    def getVideo1(self):                #Playing Video 1
        if self.stop1:
            self.timer0 = QTimer(self)       
            self.timer0.timeout.connect(self.update_frame)
            self.timer0.start(33.34)
            self.stop1 = False
    def getVideo2(self):                #Playing Video 2
        if self.stop2:
            self.timer1 = QTimer(self)
            self.timer1.timeout.connect(self.update_frame1)
            self.timer1.start(33.34)
            self.stop2 = False
    def getVideo3(self):                #Playing Converted Video  
       # print ('No file named "3.avi". Please add your code and generate the file.')
        if self.stopc:  
            self.timer2 = QTimer(self)
            self.timer2.timeout.connect(self.update_frame2)
            self.timer2.start(33.34)
            self.stopc = False
    def pauseVideo1(self):
        self.timer0.stop()
        self.stop1 = True
    def pauseVideo2(self):
        self.timer1.stop()
        self.stop2 = True
    def pauseVideoC(self):
        self.timer2.stop()
        self.stopc = True
    
    
    def update_frame(self):
        if self.x0 < self.l0:
            self.display(self.vid1[self.x0], 1)   
            self.x0 += 1
        else:
            self.x0 = 0
    def update_frame1(self):
        if self.x1 < self.l1:
            self.display1(self.vid2[self.x1], 1)        
            self.x1 += 1
        else:
            self.x1 = 0
    def update_frame2(self):
        if self.x2 < self.l2:
            self.display2(self.vid3[self.x2], 1)
            self.x2 += 1
        else:
            self.x2 = 0
        
    def display(self, img, window = 1):
        qformat = QImage.Format_Indexed8
        qformat=QImage.Format_RGB888
        outImage=QImage(img, 640, 480, qformat)
        outImage = outImage.rgbSwapped()
        if window == 1:
            self.video1.setPixmap(QPixmap.fromImage(outImage))
            self.video1.setScaledContents(True)
    def display1(self, img, window = 1):
        qformat = QImage.Format_Indexed8
        qformat=QImage.Format_RGB888
        outImage=QImage(img, 640, 480, qformat)
        outImage = outImage.rgbSwapped()
        if window == 1:
            self.video2.setPixmap(QPixmap.fromImage(outImage))
            self.video2.setScaledContents(True)
    def display2(self, img, window = 1):
        qformat = QImage.Format_Indexed8
        qformat=QImage.Format_RGB888
        outImage=QImage(img, 640, 480, qformat)
        outImage = outImage.rgbSwapped()
        if window == 1:
            self.convertedVideo.setPixmap(QPixmap.fromImage(outImage))
            self.convertedVideo.setScaledContents(True)
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mainwindow()
    window.setWindowTitle('Assignment1 SOEN6761')
    window.show()
    sys.exit(app.exec_())
