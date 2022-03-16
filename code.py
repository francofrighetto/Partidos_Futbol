from gc import disable
import re
import tkinter 
from datetime import date, datetime
#import subprocess
import sys
from os import path
#import os
import socket
from turtle import pen
import requests
import os

"""hacer q avise el torneo"""
#game-fin si termino
# game time si todavia no
# game play si se esta jugando
# id=r1 o r2 son los resultados
# id=t1 o t2 son los equipos

# voy a tener <id t1>equipo<algo>
# lo q tengo q hacer es split con > y si encuentra un t1o2 le siguiente campo es el equipo y le vuelvo a hacer un split


# esto de aca nose si lo uso
def CamposParaFinal(campo, nombre):
    campos_si = campo.split("<tr")
    return Final(campos_si,nombre)

def verGoles():
    root_goles = tkinter.Tk()
    root_goles.title("Goles")
    #800x260+100+40"
    root_goles.geometry("800x260+100+350")
    #root_goles.iconbitmap(file_absolute+'river.ico')
    root_goles.maxsize(800, 260)
    root_goles.minsize(800,260)

    f_goles = open("goles.txt","r")
    goles = f_goles.readlines()
    label_goles = tkinter.Label(root_goles,text="".join(goles),font=("Arial",11),anchor="nw")
    label_goles.place(x=30,y=30)
    f_goles.close()
    root_goles.mainloop()

def Partido(vec, nombre):
    mensaje=""
    for i in range(len(vec)):
        if nombre in vec[i]:
            campos = vec[i].split("copa=")
            for f in range(len(campos)):
                if nombre in campos[f]:
                    campos_si=""
                    if nombre == "River Plate":
                        if "(URUGUAY)" not in campos[f] and "(U)" not in campos[f] and "FEMENINO" not in campos[f]:
                            print(campos[f])
                            campos_si = campos[f].split("tr")
                            mensaje = Final(campos_si, nombre)

                            if "RESERVA PRIMERA" in campos[f]:
                                separado = mensaje.split(" ")
                                separado = separado[2:len(separado)]
                                mensaje = "River Plate (R) "+ (" ").join(separado)
                            
                    elif nombre =="Argentina" and "div" in campos[f]:
                        campos_si = campos[f].split("tr")
                        validar=False
                        for t in range(len(campos_si)):
                            if nombre in campos_si[t]:
                                if "datoequipo" in campos_si[t]:
                                    validar=True
                        if validar:
                            mensaje = Final(campos_si, nombre)
                    elif nombre =="Chelsea":
                        campos_si = campos[f].split("tr")
                        mensaje = Final(campos_si, nombre)
                                       

    return mensaje

def Final(campos, nombre):
    equipo1=""
    equipo2=""
    tipo_partido = ""
    campodetallado =""
    mensaje=""
    copa=""
    for j in range(len(campos)):
        if "tituloin" in campos[j]:
            """print(campos[j])
            print(nombre)
            print("------------")"""
            copa = campos[j].split("/> ")
            copa = copa[1].split(" <")
            copa = copa[0].title()
        
        if nombre in campos[j]:
            campodetallado = campos[j].split(">")
            for k in range(len(campodetallado)):
                if "game-time" in campodetallado[k]:
                    tipo_partido = "por jugar"
                if "game-fin" in campodetallado[k]:
                    tipo_partido = "terminado"
                if "game-play" in campodetallado[k]:
                    tipo_partido = "jugando"
                                
            hora = campodetallado[2].split("<")
            hora = hora[0]

            for k in range(len(campodetallado)):
                if "t1_" in campodetallado[k]:
                    equipo1 = campodetallado[k+1]
                    equipo1 = equipo1.split("<")
                    equipo1 = equipo1[0]
                if "t2_" in campodetallado[k]:
                    equipo2 = campodetallado[k+1]
                    equipo2 = equipo2.split("<")
                    equipo2 = equipo2[0]
                if "r1_" in campodetallado[k]:
                    resultado1 = campodetallado[k+1]
                    resultado1 = resultado1.split("<")
                    resultado1 = resultado1[0]
                            
                if "r2_" in campodetallado[k]:
                    resultado2 = campodetallado[k+1]
                    resultado2 = resultado2.split("<")
                    resultado2 = resultado2[0]
                if equipo1 == nombre:
                    equipo = "equipo1"
                    otroequipo="equipo2"
                else:
                    equipo = "equipo2"
                    otroequipo ="equipo1"
                        
            
            if tipo_partido == "por jugar":
                if equipo == "equipo1":
                    mensaje = nombre+ " juega contra "+equipo2+" a las "+hora+"hs de local"
                else:
                    mensaje = nombre+" juega contra "+equipo1+" a las "+hora+ "hs de visitante"
            elif tipo_partido =="jugando":
                if equipo == "equipo1":
                    if resultado1 > resultado2:
                        mensaje = nombre +" esta juegando contra "+equipo2+" de local, van "+hora+"minutos y va ganando: "+str(resultado1)+" a "+str(resultado2)
                    elif resultado1 == resultado2:
                        mensaje = nombre +" esta juegando contra "+equipo2+" de local, van "+hora+"minutos y va empatando: "+str(resultado1)+" a "+str(resultado2)
                    elif resultado1 < resultado2:
                        mensaje = nombre +" esta juegando contra "+equipo2+" de local, van "+hora+"minutos y va perdiendo: "+str(resultado1)+" a "+str(resultado2)
                else:
                    if resultado1 > resultado2:
                        mensaje = nombre +" esta juegando contra "+equipo1+" de visitante, van "+hora+"minutos y va perdiendo: "+str(resultado1)+" a "+str(resultado2)
                    elif resultado1 == resultado2:
                        mensaje = nombre +" esta juegando contra "+equipo1+" de visitante, van "+hora+"minutos y va empatando: "+str(resultado1)+" a "+str(resultado2)
                    elif resultado1 < resultado2:
                        mensaje = nombre +" esta juegando contra "+equipo1+" de visitante, van "+hora+"minutos y va ganando: "+str(resultado1)+" a "+str(resultado2)
            elif tipo_partido == "terminado":
                if equipo == "equipo1":
                    if resultado1 > resultado2:
                        mensaje = nombre+" jugo contra "+equipo2+" de local y gano: "+str(resultado1)+" a "+str(resultado2)
                    elif resultado1 == resultado2:
                        mensaje = nombre+" jugo contra "+equipo2+" de local y empato: "+str(resultado1)+" a "+str(resultado2)
                    elif resultado1 < resultado2:
                        mensaje = nombre+" jugo contra "+equipo2+" de local y perdio: "+str(resultado1)+" a "+str(resultado2)
                else:
                    if resultado1 > resultado2:
                        mensaje = nombre+" jugo contra "+equipo1+" de visitante y perdio: "+str(resultado1)+" a "+str(resultado2)
                    elif resultado1 == resultado2:
                        mensaje = nombre+" jugo contra "+equipo1+" de visitante y empato: "+str(resultado1)+" a "+str(resultado2)
                    elif resultado1 < resultado2:
                        mensaje = nombre+" jugo contra "+equipo1+" de local y gano: "+str(resultado1)+" a "+str(resultado2)
        if "goles" in campos[j] and nombre in campos[j-1]:
            
            #print(campos[j].split("<i>"))   
            #print(equipo)     
            goles_ambos= campos[j].split('id="g')
            goles_quipo1=goles_ambos[2].split(";")
            goles_quipo1=goles_quipo1[0:len(goles_quipo1)-1]
            goles_quipo2=goles_ambos[3].split(";")
            goles_quipo2=goles_quipo2[0:len(goles_quipo2)-1]
            f_goles = open("goles.txt","a")

            f_goles.write(equipo1+": ")
            gol=""
            for h in range(len(goles_quipo1)):
                gol=goles_quipo1[h].split("<i>")
                gol=gol[1].split("</i>")
                f_goles.write((str(gol[0])+" -"+str(gol[1]))+" ; ")
            f_goles.write("\n")

            f_goles.write(equipo2+": ")
            for h in range(len(goles_quipo2)):
                gol=goles_quipo2[h].split("<i>")
                gol=gol[1].split("</i>")
                f_goles.write((str(gol[0])+" de"+str(gol[1]))+" ; ")
            f_goles.write("\n\n")
            f_goles.close()

            #return mensaje + " ("+copa+")"
    return mensaje + " ("+copa+")"

def terminar():
    sys.exit()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)
wifi=False
try:
    s.connect(("www.google.com", 80))
except (socket.gaierror, socket.timeout):
    print("Sin wifi")
else:
    wifi=True
    s.close()

file_absolute="D:/Franco/algoritmos o programacion extra/Proyectos/Partidos_Futbol/"
fd = open(file_absolute+"dia.txt","r")
dia = fd.read()
fd.close()

now = datetime.now()
dias_ingles = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
#CAMBIA ESTA VARIABLE PAJERO
dia_str=datetime.today().strftime('%A')
verificador_dia=True
try:
    if dias_ingles.index(dia_str) < 5 and now.hour>12 and now.hour<20:
        verificador_dia=False
except ValueError:
    pass

f_goles=open("goles.txt","w")
f_goles.close()

if dia != str(date.today()) and wifi and verificador_dia:
    fd = open(file_absolute+"dia.txt","w")
    dia = str(date.today())
    fd.write(dia)
    fd.close()
    cont=0
    

    r = requests.get("https://www.promiedos.com.ar")
    with open(file_absolute+"index.html", "wb") as f:
        f.write(r.content)
    r.close()
    
    f =  open(file_absolute+"index.html","r")
    lectura = f.readlines()
    vec = []
    vec_mensajes = []
    for i in range(len(lectura)):
        new_string = re.sub(r'\x00', '', lectura[i])
        vec.append(new_string)
    junto =""

    

    vec_mensajes.append(Partido(vec, "River Plate"))
    vec_mensajes.append(Partido(vec, "Chelsea"))
    vec_mensajes.append(Partido(vec, "Argentina"))
    for i in range(len(vec_mensajes)):
        if vec_mensajes[i] != "":
            junto += vec_mensajes[i] +"\n\n"
    
    if junto != "":
        root = tkinter.Tk()
        root.title("Es de mi placer informar que hoy rueda el esferico")
        root.geometry("800x260+100+40")
        root.iconbitmap(file_absolute+'river.ico')
        root.maxsize(800, 260)
        root.minsize(800,260)
        root.protocol("WM_DELETE_WINDOW",terminar)

        img = tkinter.PhotoImage(file=file_absolute+'pelotita.png')
        imgl = tkinter.Label(root,image=img)
        imgl.place(x=30,y=30)

        label_info = tkinter.Label(root,text=junto,font=("Arial",11))
        label_info.place(x=260,y=80)

        f_goles=open("goles.txt","r")
        goles=f_goles.readlines()
        f_goles.close()

        btn_goles = tkinter.Button(root,text="Ver goles",font=("Arial",11),command=verGoles)
        btn_goles.place(x=400,y=220)

        if len(goles)==0:
            btn_goles.configure(state="disabled")

        
        

        root.mainloop()


