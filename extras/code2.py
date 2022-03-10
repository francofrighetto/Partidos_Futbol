import re
import tkinter 
from datetime import date, datetime, time
import subprocess
import sys
from os import path
import os
import time
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
                            return CamposParaFinal(campos[f],nombre)
                    elif nombre =="Argentina" and "div" in campos[f]:
                        return CamposParaFinal(campos[f],nombre)
                    elif nombre =="Chelsea":
                        return CamposParaFinal(campos[f],nombre)


def Datos(condicion, campo,k,var):
    if var == "":
        if condicion in campo[k]:
            var = campo[k+1]
            var = var.split("<")
            var = var[0]
    return var

def Final(campos, nombre):
    equipo1=""
    equipo2=""
    resultado1=""
    resultado2=""
    tipo_partido = ""
    campodetallado =""
    mensaje=""
    liga=""
    for j in range(len(campos)):
        if "tituloin" in campos[j]:
            campos_liga = campos[j].split(">")
            for t in range(len(campos_liga)):
                if "img" in campos_liga[t]:
                    liga = campos_liga[t].split("<")
                    liga=liga[0]

                    if liga != "":
                        liga =liga[1:len(liga)-1]
                        liga=liga.lower().title()
                        break
                    
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
                equipo1= Datos("t1_",campodetallado,k,equipo1)
                equipo2= Datos("t2_",campodetallado,k,equipo2)
                resultado1= Datos("r1_",campodetallado,k,resultado1)
                resultado2= Datos("r2_",campodetallado,k,resultado2)

            if equipo1 == nombre:
                equipo = "equipo1"
            else:
                equipo = "equipo2"
            
            if tipo_partido == "por jugar":
                if equipo == "equipo1":
                    mensaje = nombre+ " juega contra "+equipo2+" a las "+hora+"hs de local ("+liga+")"
                else:
                    mensaje = nombre+" juega contra "+equipo1+" a las "+hora+ "hs de visitante ("+liga+")"
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
            print(liga)
            return mensaje


file_absolute="D:/Franco/algoritmos o programacion extra/Proyectos/Partidos_Futbol/"
fd = open(file_absolute+"dia.txt","r")
dia = fd.read()
fd.close()

if dia != str(date.today()):
    fd = open(file_absolute+"dia.txt","w")
    dia = str(date.today())
    #fd.write(dia)
    fd.write("a")
    fd.close()
    subprocess.Popen('powershell.exe -ExecutionPolicy RemoteSigned -file "D:\\Franco\\algoritmos o programacion extra\\Proyectos\\Partidos_Futbol\\script.ps1"', stdout=sys.stdout)
    #    modificado = str(datetime.fromtimestamp(os.path.getmtime(file_absolute+"archivo.txt")))
    #    modificado = modificado.split(" ")
        #modificado = modificado[0]
    #time.sleep(5)
    f =  open(file_absolute+"archivo.txt","r")
    lectura = f.readlines()
    f.close()

    vec = []
    for i in range(len(lectura)):
        new_string = re.sub(r'\x00', '', lectura[i])
        vec.append(new_string)
    junto =""
    vec_mensajes = []
    vec_mensajes.append(Partido(vec, "Chelsea"))
    vec_mensajes.append(Partido(vec, "River Plate"))
    vec_mensajes.append(Partido(vec, "Argentina"))
    for i in range(len(vec_mensajes)):
        if str(vec_mensajes[i]) != "None":
            junto += vec_mensajes[i] +"\n\n"
    if junto != "":
        root = tkinter.Tk()
        root.title("Es de mi placer informar que hoy rueda el esferico")
        root.geometry("800x260")
        root.iconbitmap(file_absolute+'river.ico')
        root.maxsize(800, 260)
        root.minsize(800,260)

        img = tkinter.PhotoImage(file=file_absolute+'pelotita.png')
        imgl = tkinter.Label(root,image=img).place(x=30,y=30)
        label_info = tkinter.Label(root,text=junto,font=("Arial",11)).place(x=260,y=80)
        root.mainloop()
