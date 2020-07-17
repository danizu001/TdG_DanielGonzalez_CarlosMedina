import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def moving_average(values, window):
    weights= np.repeat(1.0,window)/window
    sma= np.convolve(values,weights, 'valid')
    return sma

i=3
large=[]
conteo=globals()
x=range(3,73,1)
y=range(3,20,1)
z=range(20,50,1)
w=range(50,55,1)
#Se lee la base de datos
for i in x:
    if(i<10):
        conteo["datos"+str(i)] = pd.read_csv(r"C:\Users\Daniel Gonzalez\Documents\Base de Datos\Base de Datos\g00"+str(i)+".csv",";",header=None)
    if(i>=10 and i<20):
        conteo["datos"+str(i)] = pd.read_csv(r"C:\Users\Daniel Gonzalez\Documents\Base de Datos\Base de Datos\g0"+str(i)+".csv",";",header=None)
    if(i>=20 and i<=54):
        conteo["datos"+str(i)] = pd.read_excel(r"C:\Users\Daniel Gonzalez\Documents\Base de Datos\Base de Datos\g0"+str(i)+".xlsx",header=None)
k=3
j=0
h=0
i=0
acty=0
actx=0
bandx=0
bandy=0
correlax=0
correlay=0
conttx=0
contty=0
contmx=0
contmy=0
contax=0
contay=0
porctx=0
porcmx=0
porcax=0
porcty=0
porcmy=0
porcay=0
conttz=0
contmz=0
contaz=0
porctz=0
porcmz=0
porcaz=0
lim1=[]
lim2=[]
corrx=[]
corry=[]
contx=[]
conmx=[]
conax=[]
portx=[]
pormx=[]
porax=[]
conty=[]
conmy=[]
conay=[]
porty=[]
pormy=[]
poray=[]
contz=[]
conmz=[]
conaz=[]
portz=[]
pormz=[]
poraz=[]
maxx=[]
maxy=[]
maxz=[]
minx=[]
miny=[]
minz=[]
con=[]
con2=[]
con3=[]

z1=0.98+(0.98*0.07)
z2=0.98-(0.98*0.07)
z3=0.98+(0.98*0.15)
z4=0.98-(0.98*0.15)

#Se coloca en un arreglo los eje x,y y z
for k in y:
    abb=len(globals()["datos"+str(k)])
    for j in range(0,abb,1):
        cond=float(globals()["datos"+str(k)][1][j].replace(",","."))
        cond2=float(globals()["datos"+str(k)][2][j].replace(",","."))
        cond3=float(globals()["datos"+str(k)][3][j].replace(",","."))
        cond3=abs(cond3)
        con.append(cond)
        con2.append(cond2)
        if(cond3 != 0.0):
            con3.append(cond3)
        #Se clasifican las muestras como riesgo alto y medio
        #La variable cont es para contar las muestras que estan en el riesgo
        #La variable band es una bandera para contar el número de veces 
        #que se entra en riesgo (correla)
        if(abs(cond)<0.09):
            bandx = 0
        if(abs(cond2)<0.09):
            bandy = 0
        if(cond < -0.09 or cond > 0.09):
            conttx=conttx+1
            bandx = 1
        if(cond2 < -0.09 or cond2 > 0.09):
            contty=contty+1
            bandy = 1
        if(cond3 < z2 or cond3 > z1):
            conttz=conttz+1               
        if(-0.15<cond < -0.09 or 0.15>cond > 0.09):
            contmx=contmx+1
        if(-0.15<cond2 < -0.09 or 0.15>cond2 > 0.09):
            contmy=contmy+1
        if(cond < -0.15 or cond > 0.15):
            contax=contax+1
        if(cond2 < -0.15 or cond2 > 0.15):
            contay=contay+1
        if( z4 < cond3 < z2 or z3 >cond3 > z1):
            contmz=contmz+1
        if(cond3 < z4 or cond3 > z3):
            contaz=contaz+1
        if(bandy == 1 and acty == 0):
            acty = 1
        if(bandy == 0 and acty == 1):
            acty = 0
            correlay=correlay+1
        if(bandx == 1 and actx == 0):
            actx = 1
        if(bandx == 0 and actx == 1):
            actx = 0
            correlax=correlax+1
        #Se escoge el porcentaje de muestras que estan en riesgo
        if (j==(abb - 1)):
            porctx=(conttx/(abb -1))*100
            porcmx=(contmx/(abb -1))*100
            porcax=(contax/(abb -1))*100
            porcty=(contty/(abb -1))*100
            porcmy=(contmy/(abb -1))*100
            porcay=(contay/(abb -1))*100
            porctz=(conttz/(abb -1))*100
            porcmz=(contmz/(abb -1))*100
            porcaz=(contaz/(abb -1))*100
    conf=moving_average(con, 3)
    conf2=moving_average(con2, 3)
    conf3=moving_average(con3, 3)
    maxx.append(max(con)-max(conf))
    maxy.append(max(con2)-max(conf2))
    maxz.append(max(con3)-max(conf3))    
    minx.append(min(con)-min(conf))
    miny.append(min(con2)-min(conf2))
    minz.append(min(con3)-min(conf3))
    #Todos los porcentajes y cantidad de riesgos se almacenan en un arreglo
    corrx.append(correlax)
    corry.append(correlay)
    contx.append(conttx)
    conmx.append(contmx)
    conax.append(contax)
    portx.append(porctx)
    pormx.append(porcmx)
    porax.append(porcax)
    conty.append(contty)
    conmy.append(contmy)
    conay.append(contay)
    porty.append(porcty)
    pormy.append(porcmy)
    poray.append(porcay)
    contz.append(conttz)
    conmz.append(contmz)
    conaz.append(contaz)
    portz.append(porctz)
    pormz.append(porcmz)
    poraz.append(porcaz)
    #Se igualan a 0 todas las variables para poder leer una nueva base de datos
    correlax=0
    correlay=0
    conttx=0
    contmx=0
    contax=0
    porctx=0
    porcmx=0
    porcax=0
    contty=0
    contmy=0
    contay=0
    porcty=0
    porcmy=0
    porcay=0
    conttz=0
    contmz=0
    contaz=0
    porctz=0
    porcmz=0
    porcaz=0
    con=[]
    con2=[]
    con3=[]
    conf=[]
    conf2=[]
    conf3=[]
    #Se vuelven a repetir los pasos ya que la base de datos contiene diferentes
    #archivos que deben ser leidos de diferente forma para que funcione
for k in z:
    abb=len(globals()["datos"+str(k)])
    for j in range(0,abb,1):
        cond=float(globals()["datos"+str(k)][1][j])
        cond2=float(globals()["datos"+str(k)][2][j])
        cond3=float(globals()["datos"+str(k)][3][j])
        cond3=abs(cond3)
        con.append(cond)
        con2.append(cond2)
        if(cond3 != 0.0):
            con3.append(cond3)
        if(abs(cond)<0.09):
            bandx = 0
        if(abs(cond2)<0.09):
            bandy = 0
        if(cond < -0.09 or cond > 0.09):
            conttx=conttx+1
            bandx = 1
        if(cond2 < -0.09 or cond2 > 0.09):
            contty=contty+1
            bandy = 1
        if(cond3 < z2 or cond3 > z1):
            conttz=conttz+1               
        if(-0.15<cond < -0.09 or 0.15>cond > 0.09):
            contmx=contmx+1
        if(-0.15<cond2 < -0.09 or 0.15>cond2 > 0.09):
            contmy=contmy+1
        if(cond < -0.15 or cond > 0.15):
            contax=contax+1
        if(cond2 < -0.15 or cond2 > 0.15):
            contay=contay+1
        if( z4 < cond3 < z2 or z3 >cond3 > z1):
            contmz=contmz+1
        if(cond3 < z4 or cond3 > z3):
            contaz=contaz+1
        if(bandy == 1 and acty == 0):
            acty = 1
        if(bandy == 0 and acty == 1):
            acty = 0
            correlay=correlay+1
        if(bandx == 1 and actx == 0):
            actx = 1
        if(bandx == 0 and actx == 1):
            actx = 0
            correlax=correlax+1
        if (j==(abb - 1)):
            porctx=(conttx/(abb -1))*100
            porcmx=(contmx/(abb -1))*100
            porcax=(contax/(abb -1))*100
            porcty=(contty/(abb -1))*100
            porcmy=(contmy/(abb -1))*100
            porcay=(contay/(abb -1))*100
            porctz=(conttz/(abb -1))*100
            porcmz=(contmz/(abb -1))*100
            porcaz=(contaz/(abb -1))*100        
    conf=moving_average(con, 3)
    conf2=moving_average(con2, 3)
    conf3=moving_average(con3, 3)
    maxx.append(max(con)-max(conf))
    maxy.append(max(con2)-max(conf2))
    maxz.append(max(con3)-max(conf3))    
    minx.append(min(con)-min(conf))
    miny.append(min(con2)-min(conf2))
    minz.append(min(con3)-min(conf3))
    corrx.append(correlax)
    corry.append(correlay)
    contx.append(conttx)
    conmx.append(contmx)
    conax.append(contax)
    portx.append(porctx)
    pormx.append(porcmx)
    porax.append(porcax)
    conty.append(contty)
    conmy.append(contmy)
    conay.append(contay)
    porty.append(porcty)
    pormy.append(porcmy)
    poray.append(porcay)
    contz.append(conttz)
    conmz.append(contmz)
    conaz.append(contaz)
    portz.append(porctz)
    pormz.append(porcmz)
    poraz.append(porcaz)
    correlax=0
    correlay=0
    conttx=0
    contmx=0
    contax=0
    porctx=0
    porcmx=0
    porcax=0
    contty=0
    contmy=0
    contay=0
    porcty=0
    porcmy=0
    porcay=0
    conttz=0
    contmz=0
    contaz=0
    porctz=0
    porcmz=0
    porcaz=0
    con=[]
    con2=[]
    con3=[]
    conf=[]
    conf2=[]
    conf3=[]
for k in w:
    abb=len(globals()["datos"+str(k)])
    for j in range(1,abb,1):
        cond=float(globals()["datos"+str(k)][1][j])
        cond2=float(globals()["datos"+str(k)][2][j])
        cond3=float(globals()["datos"+str(k)][3][j])
        cond3=abs(cond3)
        con.append(cond)
        con2.append(cond2)
        if(cond3 != 0.0):
            con3.append(cond3)
        if(abs(cond)<0.09):
            bandx = 0
        if(abs(cond2)<0.09):
            bandy = 0
        if(cond < -0.09 or cond > 0.09):
            conttx=conttx+1
            bandx = 1
        if(cond2 < -0.09 or cond2 > 0.09):
            contty=contty+1
            bandy = 1
        if(cond3 < z2 or cond3 > z1):
            conttz=conttz+1               
        if(-0.15<cond < -0.09 or 0.15>cond > 0.09):
            contmx=contmx+1
        if(-0.15<cond2 < -0.09 or 0.15>cond2 > 0.09):
            contmy=contmy+1
        if(cond < -0.15 or cond > 0.15):
            contax=contax+1
        if(cond2 < -0.15 or cond2 > 0.15):
            contay=contay+1
        if( z4 < cond3 < z2 or z3 >cond3 > z1):
            contmz=contmz+1
        if(cond3 < z4 or cond3 > z3):
            contaz=contaz+1
        if(bandy == 1 and acty == 0):
            acty = 1
        if(bandy == 0 and acty == 1):
            acty = 0
            correlay=correlay+1
        if(bandx == 1 and actx == 0):
            actx = 1
        if(bandx == 0 and actx == 1):
            actx = 0
            correlax=correlax+1
        if (j==(abb - 1)):
            porctx=(conttx/(abb -1))*100
            porcmx=(contmx/(abb -1))*100
            porcax=(contax/(abb -1))*100
            porcty=(contty/(abb -1))*100
            porcmy=(contmy/(abb -1))*100
            porcay=(contay/(abb -1))*100
            porctz=(conttz/(abb -1))*100
            porcmz=(contmz/(abb -1))*100
            porcaz=(contaz/(abb -1))*100
    conf=moving_average(con, 3)
    conf2=moving_average(con2, 3)
    conf3=moving_average(con3, 3)
    maxx.append(max(con)-max(conf))
    maxy.append(max(con2)-max(conf2))
    maxz.append(max(con3)-max(conf3))    
    minx.append(min(con)-min(conf))
    miny.append(min(con2)-min(conf2))
    minz.append(min(con3)-min(conf3))
    corrx.append(correlax)
    corry.append(correlay)
    contx.append(conttx)
    conmx.append(contmx)
    conax.append(contax)
    portx.append(porctx)
    pormx.append(porcmx)
    porax.append(porcax)
    conty.append(contty)
    conmy.append(contmy)
    conay.append(contay)
    porty.append(porcty)
    pormy.append(porcmy)
    poray.append(porcay)
    contz.append(conttz)
    conmz.append(contmz)
    conaz.append(contaz)
    portz.append(porctz)
    pormz.append(porcmz)
    poraz.append(porcaz)
    correlax=0
    correlay=0
    conttx=0
    contmx=0
    contax=0
    porctx=0
    porcmx=0
    porcax=0
    contty=0
    contmy=0
    contay=0
    porcty=0
    porcmy=0
    porcay=0
    conttz=0
    contmz=0
    contaz=0
    porctz=0
    porcmz=0
    porcaz=0
    con=[]
    con2=[]
    con3=[]
    conf=[]
    conf2=[]
    conf3=[]
#Promedio de riesgos de la base de datos
antx=np.mean(portx)
anmx=np.mean(pormx)
anax=np.mean(porax)
anty=np.mean(porty)
anmy=np.mean(pormy)
anay=np.mean(poray)
antz=np.mean(portz)
anmz=np.mean(pormz)
anaz=np.mean(poraz)
#Se establece un indice para porder hacer comparación
ind=int(len(portx)*0.5)
ind1=int(len(portx)*0.75)
#Se ordenan los arreglos para establecer la comparación
ordtx=sorted(portx)
ordmx=sorted(pormx)
ordax=sorted(porax)
ordty=sorted(porty)
ordmy=sorted(pormy)
orday=sorted(poray)
ordtz=sorted(portz)
ordmz=sorted(pormz)
ordaz=sorted(poraz)
#Se coloca en un arreglo los limites para hacer la comparación 
#de cada riesgo
lim1.append(ordtx[ind])
lim1.append(ordmx[ind])
lim1.append(ordax[ind])
lim1.append(ordty[ind])
lim1.append(ordmy[ind])
lim1.append(orday[ind])
lim1.append(ordtz[ind])
lim1.append(ordmz[ind])
lim1.append(ordaz[ind])
#Se coloca en un arreglo los limites para hacer la comparación 
#de cada riesgo
lim2.append(ordtx[ind1])
lim2.append(ordmx[ind1])
lim2.append(ordax[ind1])
lim2.append(ordty[ind1])
lim2.append(ordmy[ind1])
lim2.append(orday[ind1])
lim2.append(ordtz[ind1])
lim2.append(ordmz[ind1])
lim2.append(ordaz[ind1])

#En esta parte se grafican los histogramas, si se quiere cambiar de riesgo
#simplemente hay que cambio la variable que esta dentro del plt.hist().
plt.figure(1)
plt.hist(porax)
plt.axvline(x=2.94, color="black")
plt.axvline(x=4.28, color="black")
plt.title("Histograma de porcentajes riesgo alto eje x")
plt.xlabel("Porcentajes %")
plt.ylabel("Veces")
plt.figure(2)
plt.hist(poray)
plt.axvline(x=5.3, color="black")
plt.axvline(x=6.74, color="black")
plt.title("Histograma de porcentajes riesgo alto eje y")
plt.xlabel("Porcentajes %")
plt.ylabel("Veces")
plt.figure(3)
plt.hist(poraz)
plt.axvline(x=6.8, color="black")
plt.axvline(x=9.88, color="black")
plt.title("Histograma de porcentajes riesgo alto eje z")
plt.xlabel("Porcentajes %")
plt.ylabel("Veces")
plt.figure(4)
plt.plot(corrx,contx,'o')
plt.title("Correlación Muestras VS Veces")
plt.xlabel("# de veces")
plt.ylabel("# de muestras")
