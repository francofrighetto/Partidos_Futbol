import re
import tkinter 
from datetime import date, datetime
import subprocess
import sys
from os import path
import os
"""hacer q avise el torneo"""
#game-fin si termino
# game time si todavia no
# game play si se esta jugando
# id=r1 o r2 son los resultados
# id=t1 o t2 son los equipos

# voy a tener <id t1>equipo<algo>
# lo q tengo q hacer es split con > y si encuentra un t1o2 le siguiente campo es el equipo y le vuelvo a hacer un split

def CamposParaFinal(campo, nombre):
    campos_si = campo.split("tr")
    return Final(campos_si,nombre)

def Partido(vec, nombre):
    mensaje=""
    for i in range(len(vec)):
        if nombre in vec[i]:
            campos = vec[i].split("copa=")
            for f in range(len(campos)):
                if nombre in campos[f]:
                    if nombre == "River Plate":
                        if "URUGUAY" not in campos[f] and "FEMENINO" not in campos[f]:
                            campos_si = campos[f].split("tr")
                            mensaje = Final(campos_si, nombre)
                    elif nombre =="Argentina" and "div" in campos[f]:
                        campos_si = campos[f].split("tr")
                        mensaje = Final(campos_si, nombre)
                    elif nombre =="Chelsea":
                        campos_si = campos[f].split("tr")
                        mensaje = Final(campos_si,nombre)

    return mensaje

def Final(campos, nombre):
    equipo1=""
    equipo2=""
    tipo_partido = ""
    campodetallado =""
    mensaje=""
    for j in range(len(campos)):
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
                
            return mensaje


file_absolute="D:/Franco/algoritmos o programacion extra/Proyectos/Partidos_Futbol/"
fd = open(file_absolute+"dia.txt","r")
dia = fd.read()
fd.close()

if dia != str(date.today()):
    fd = open(file_absolute+"dia.txt","w")
    dia = str(date.today())
    fd.write(dia)
    fd.close()
    cont=0
    while True:
        subprocess.Popen('powershell.exe -ExecutionPolicy RemoteSigned -file "D:\\Franco\\algoritmos o programacion extra\\Proyectos\\Partidos_Futbol\\script.ps1"', stdout=sys.stdout)
        modificado = str(datetime.fromtimestamp(os.path.getmtime(file_absolute+"archivo.txt")))
        modificado = modificado.split(" ")
        modificado = modificado[0]
        cont+=1
        if modificado == dia:
            break
        if cont >10:
            break
    

    f =  open(file_absolute+"archivo.txt","r")
    lectura = f.readlines()
    vec = []
    vec_mensajes = []
    for i in range(len(lectura)):
        new_string = re.sub(r'\x00', '', lectura[i])
        vec.append(new_string)
    junto =""

    vec_mensajes.append(Partido(vec, "Chelsea"))
    vec_mensajes.append(Partido(vec, "River Plate"))
    vec_mensajes.append(Partido(vec, "Argentina"))
    for i in range(len(vec_mensajes)):
        if vec_mensajes[i] != "":
            junto += vec_mensajes[i] +"\n\n"
    if junto != "":
        root = tkinter.Tk()
        root.title("Es de mi placer informar que hoy rueda el esferico")
        root.geometry("700x260")
        root.iconbitmap(file_absolute+'river.ico')
        root.maxsize(700, 260)
        root.minsize(700,260)

        img = tkinter.PhotoImage(file=file_absolute+'pelotita.png')
        imgl = tkinter.Label(root,image=img).place(x=30,y=30)
        label_info = tkinter.Label(root,text=junto,font=("Arial",11)).place(x=260,y=80)
        root.mainloop()
