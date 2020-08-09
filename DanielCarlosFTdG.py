import pyrebase
import smbus            #import SMBus module of I2C
import requests
from time import sleep          #import
from datetime import datetime,date
import RPi.GPIO as GPIO
import serial
import time
from firebase import firebase
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np
from numpy import array
from numpy import *
from numpy import convolve

config = {
    "apiKey": "AIzaSyAX_8Ev18N7hymbowlOUQNbRTo5LoGLlYs",
    "authDomain": "iotdatos.firebaseapp.com",
    "databaseURL": "https://iotdatos.firebaseio.com",
    "projectId": "iotdatos",
    "storageBucket": "iotdatos.appspot.com",
    "messagingSenderId": "707459608347",
    "appId": "1:707459608347:web:f7531b2727ac65b38b2dbe",
    "measurementId": "G-ZFECKGYY6N"
  };
   

firebas = pyrebase.initialize_app(config)
storage = firebas.storage()

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Al tener una resistenica pull-app devolvera un high cuando este sin pulsar y false cuando se pulse 
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)



#some MPU6050 Registers and their Address
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47
TEMP = 0x41

def MPU_Init():
    #write to sample rate register
    bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
    
    #Write to power management register
    bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
    
    #Write to Configuration register
    bus.write_byte_data(Device_Address, CONFIG, 0)
    
    #Write to interrupt enable register
    bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
    #Accelero and Gyro value are 16-bit
        high = bus.read_byte_data(Device_Address, addr)
        low = bus.read_byte_data(Device_Address, addr+1)
    
        #concatenate higher and lower value
        value = ((high << 8) | low)
        
        #to get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return value
    
def moving_average(values,window) :
    weights= np.repeat(1.0,window)/window
    sma= np.convolve(values,weights, 'valid')
    return sma

bus = smbus.SMBus(1)    # or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x68   # MPU6050 device address

MPU_Init()
print ("Oprime El boton para iniciar la toma de datos")
bien = 0
i = 3
j= 0
k= 0
gravedad = 9.8
tiempo_muestreo = 0.350
lista_velocidad = []
xma = []
yma = []
zma =[]
Ax_lista = []
Ay_lista = []
Az_lista =[]
xma1 = []
yma1 = []
zma1 =[]
tma1 =[]
xs=[]
tx1=[]
ty1=[]
dq=0
proz = 0
limitez = 0
iniciox = 0
inicioy = 0
finx = 0
fny = 0
transx = 0
transy = 0
bandx = 0
bandy = 0
actx = 0
acty = 0
conpos = 0
conneg = 0
connor = 0
lista_velocidad = []
contador_de_pulsos = 0
velocidad = 0
timeDifference = (1000)*350
analysisFrequency = 60
lastLecture = datetime.now()
lastAnalysis = datetime.now()
contador_riesgo_alto_velocidad = 0
cxm = 0
cxa = 0
cym = 0
cya = 0
czm = 0
cza = 0
txm = 0
txa = 0
tym = 0
tya = 0
tzm = 0
tza = 0
FBcon = firebase.FirebaseApplication('https://iotdatos.firebaseio.com/', None)

while True:
    valor_entrada = GPIO.input(24)
    negativo = GPIO.input(21)
    normal = GPIO.input(20)
    positivo = GPIO.input(16)
    if (valor_entrada == False):
        contador_de_pulsos = contador_de_pulsos +1
        print("Inicia proceso")
        sleep(0.31)
        initialTime = datetime.now()
    if(valor_entrada == True & contador_de_pulsos == 1):
        acc_xn = read_raw_data(ACCEL_XOUT_H)
        acc_yn = read_raw_data(ACCEL_YOUT_H)
        acc_zn = read_raw_data(ACCEL_ZOUT_H)
        Axn = (acc_xn/16384.0)
        Ayn = (acc_yn/16384.0)
        Azn = (acc_zn/16384.0)
        Azn = abs(Azn-0.98)
        contador_de_pulsos = 2
    if (contador_de_pulsos == 2):
    
        nowTime = datetime.now() 
        #print((nowTime- lastLecture).microseconds)
        if (nowTime-lastAnalysis).seconds >= analysisFrequency:
            lastAnalysis = nowTime
            print("Pasó un minuto")
        if (nowTime- lastLecture).microseconds>timeDifference:
            lastLecture = nowTime
            #Reading sensor
            acc_x = read_raw_data(ACCEL_XOUT_H)
            acc_y = read_raw_data(ACCEL_YOUT_H)
            acc_z = read_raw_data(ACCEL_ZOUT_H)
            #Full scale range +/- 250 degree/C as per sensitivity scale factor
            Ax = (acc_x/16384.0)-Axn
            Ay = (acc_y/16384.0)-Ayn
            if(Azn>=0):
                Az = (acc_z/16384.0)-Azn
            if(Azn<0):
                Az = (acc_z/16384.0)+Azn
            Ax_lista.append(Ax)
            Ay_lista.append(Ay)
            Az_lista.append(Az)
            xs.append(dt.datetime.now().strftime('%H%M%S'))
            tiempo = round((nowTime - initialTime ).seconds,0)
            xma=moving_average(Ax_lista,6)
            yma=moving_average(Ay_lista,6)
            zma=moving_average(Az_lista,6)
            xma7=moving_average(Ax_lista,10)
            yma7=moving_average(Ay_lista,10)
            zma7=moving_average(Az_lista,10)
            if(bien<6):
                i=i-1
                if (bien==5):
                    i=0
                bien=bien+1
            if(bien>=6):
                tma1.append(0.35*i)
                xma1.append(xma[i])
                yma1.append(yma[i])
                zma1.append(zma[i])
                proz = proz + zma[i]
                velocidad = velocidad + (yma[i]*gravedad)*tiempo_muestreo
                lista_velocidad.append(velocidad)
                if(yma[i-1] == 0 and yma[i]== 0):
                    lista_velocidad[i] = 0
                if(velocidad < 0):
                    lista_velocidad[i] = 0
                print ("\tAx=%.2f g" %xma[i], "\tAy=%.2f g" %yma[i], "\tAz=%.2f g" %zma[i])
                if(i%172 == 0 and i > 0):
                    fremx = FBcon.put('/MyTestData/','riesm_x',cxm)
                    fremy = FBcon.put('/MyTestData/','riesm_y',cym)
                    fremz = FBcon.put('/MyTestData/','riesm_z',czm)
                    freax = FBcon.put('/MyTestData/','riesa_x',cxa)
                    freay = FBcon.put('/MyTestData/','riesa_y',cya)
                    freaz = FBcon.put('/MyTestData/','riesa_z',cza)
                    fregx = FBcon.put('/MyTestData/','Reg_x4',{"ejex" : xma1[(dq*172):((dq+1)*172)]})
                    fregy = FBcon.put('/MyTestData/','Reg_y4',{"ejey" : yma1[(dq*172):((dq+1)*172)]})
                    fregz = FBcon.put('/MyTestData/','Reg_z4',{"ejez" : zma1[(dq*172):((dq+1)*172)]})
                    print(dq)
                    dq += 1
                    cxm=0
                    cym=0
                    czm=0
                    cxa=0
                    cya=0
                    cza=0
                limitez = 0.98+(0.98*0.075)
                limitez1 = 0.98-(0.98*0.075)
                limitez3 = 0.98+(0.98*0.15)
                limitez4 = 0.98-(0.98*0.15)
                if(limitez3>zma1[i]>=limitez or limitez4<zma1[i]<=limitez1):
                    czm = czm +1
                    tzm = tzm +1
                if(zma1[i] >= limitez3 or zma1[i]<= limitez4):
                    cza = cza +1
                    tza = tza +1
                    print(cza)
                if (abs(yma1[i]) < 0.09):
                    bandy = 0
                if (0.09 < abs(yma1[i]) < 0.15):
                    cym += 1
                    tym += 1
                    bandy = 1
                if (abs(yma1[i]) > 0.15):
                    cya += 1
                    tya += 1
                    bandy = 1
                if (abs(xma1[i])<0.09):
                    bandx = 0
                if (0.09 < abs(xma[i]) < 0.15):
                    cxm += 1
                    txm += 1
                    bandx = 1
                if (0.15 < abs(xma[i])):
                    cxa += 1
                    txa += 1
                    bandx = 1
                if (bandy == 1 and acty == 0):
                    inicioy = i
                    acty = 1
                if (bandy == 0 and acty == 1):
                    finy = i
                    transy = finy-inicioy
                    transy = transy * 0.35
                    ty1.append(transy)
                    acty = 0
                if (bandx == 1 and actx == 0):
                    iniciox = i
                    actx = 1
                if (bandx == 0 and actx == 1):
                    finx = i
                    transx = finx-iniciox
                    transx = transx * 0.35
                    tx1.append(transx)
                    actx = 0    
                i=i+1
                bien=bien+1
                
    if (contador_de_pulsos == 3):
        #for x in range(len(yma1)):
            #velocidad = velocidad + (yma1[x]*gravedad)*tiempo_muestreo
            #lista_velocidad.append(velocidad)
            #if(yma1[x-1] == 0 and yma1[x]== 0):
                #lista_velocidad[x] = 0
            #if(velocidad < 0):
                #lista_velocidad[x] = 0
        tiempo = i*0.35 
        archivo=open('/home/pi/Desktop/fichero.txt','w')  
        archivo.write('Lectura Acelerometro\n')
        archivo.write("eje x: "+str(xma1)+"\n")
        archivo.write("eje y: "+str(yma1)+"\n")
        archivo.write("eje z: "+str(zma1)+"\n")
        archivo.write("riesgo en eje Y medio: "+str(tym)+"\n")
        archivo.write("riesgo en eje Y alto: "+str(tya)+"\n")
        archivo.write("riesgo en eje X medio: "+str(txm)+"\n")
        archivo.write("riesgo en eje X alto: "+str(txa)+"\n")
        archivo.write("riesgo en eje Z medio: "+str(tzm)+"\n")
        archivo.write("riesgo en eje Z alto: "+str(tza)+"\n")
        archivo.close()
        orden = time.time()
        path_on_cloud = "doc/base_de_datos.txt " + time.ctime(orden)
        path_local = "fichero.txt"
        storage.child(path_on_cloud).put(path_local)
        
        total_time = {
        "transcurrido" : tiempo
        }
        data_to_uploadx = {
        "ejex" : xma1
        }
        data_to_uploady = {
        "ejey" : yma1
        }
        data_to_uploadz = {
        "ejez" : zma1
        }
        tottime = FBcon.put('/MyTestData/','tiempo',total_time)
        resultx = FBcon.put('/MyTestData/','Registrodatosx',data_to_uploadx)
        resulty = FBcon.put('/MyTestData/','Registrodatosy' ,data_to_uploady)
        resultz = FBcon.put('/MyTestData/','Registrodatosz',data_to_uploadz)
        riesgodxm = FBcon.put('/MyTestData/','Reg_pel_xm',txm)
        riesgodxa = FBcon.put('/MyTestData/','Reg_pel_xa',txa)
        riesgoaym = FBcon.put('/MyTestData/','Reg_pel_ym',tym)
        riesgoaya = FBcon.put('/MyTestData/','Reg_pel_ya',tya)        
        riesgozm = FBcon.put('/MyTestData/','Reg_pel_zm',tzm)       
        riesgoza = FBcon.put('/MyTestData/','Reg_pel_za',tza)
        
        print("comparar",contador_riesgo_alto_velocidad)
        
        
        print("Finaliza proceso")
        contador_de_pulsos = 0
        plt.figure(1)
        plt.plot(range(len(xma)),xma,lw=2)
        plt.title("Aceleracion eje x (filtro 3)")
        plt.xlabel('Número de muestra')
        plt.ylabel('Aceleración G')
        plt.grid(True)
        plt.savefig("eje x filtro promedio 3.pdf")
        
        plt.figure(2)
        plt.plot(range(len(yma)),yma,lw=2)
        plt.title("Aceleracion eje y (filtro 3)")
        plt.xlabel('Número de muestra')
        plt.ylabel('Aceleración G')
        plt.grid(True)
        plt.savefig("eje y filtro promedio 3.pdf")
        
        plt.figure(3)
        plt.plot(range(len(zma)),zma,lw=2)
        plt.title("Aceleracion eje z (filtro 3)")
        plt.xlabel('Número de muestra')
        plt.ylabel('Aceleración G')
        plt.grid(True)
        plt.savefig("eje z filtro promedio 3.pdf")
        
        plt.figure(4)
        plt.plot(range(len(xma7)),xma7,lw=2)
        plt.title("Aceleracion eje x (filtro 10)")
        plt.xlabel('Número de muestra')
        plt.ylabel('Aceleración G')
        plt.grid(True)
        plt.savefig("eje x filtro promedio 10.pdf")
        
        plt.figure(5)
        plt.plot(range(len(yma7)),yma7,lw=2)
        plt.title("Aceleracion eje y (filtro 10)")
        plt.xlabel('Número de muestra')
        plt.ylabel('Aceleración G')
        plt.grid(True)
        plt.savefig("eje y filtro promedio 10.pdf")
        
        plt.figure(6)
        plt.plot(range(len(zma7)),zma7,lw=2)
        plt.title("Aceleracion eje z (filtro 10)")
        plt.xlabel('Número de muestra')
        plt.ylabel('Aceleración G')
        plt.grid(True)
        plt.savefig("eje z filtro promedio 10.pdf")
        
        plt.figure(7)
        plt.plot(range(len(Ax_lista)),Ax_lista,lw=2)
        plt.title("Aceleracion eje x (sin filtro)")
        plt.xlabel('Número de muestra')
        plt.ylabel('Aceleración G')
        plt.grid(True)
        plt.savefig("eje x sin filtro.pdf")
        
        plt.figure(8)
        plt.plot(range(len(Ay_lista)),Ay_lista,lw=2)
        plt.title("Aceleracion eje y (sin filtro)")
        plt.xlabel('Número de muestra')
        plt.ylabel('Aceleración G')
        plt.grid(True)
        plt.savefig("eje y sin filtro.pdf")
        
        plt.figure(9)
        plt.plot(range(len(Az_lista)),Az_lista,lw=2)
        plt.title("Aceleracion eje z (sin filtro)")
        plt.xlabel('Número de muestra')
        plt.ylabel('Aceleración G')
        plt.grid(True)
        plt.savefig("eje z sin filtro.pdf")
        plt.show ()
        break 




