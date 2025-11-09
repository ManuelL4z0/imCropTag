# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:27:32 2020

@author: ManuelL
"""


import tkinter as tk
from tkinter import filedialog,ttk
import numpy as np
import PIL
from PIL import Image, ImageTk
import os
from math import sqrt
import sys
print(sys.version)
# from cv2 import multiply, imshow, waitKey,destroyWindow
# from matplotlib import cm
import cv2

class imageCropper(tk.Frame):
    patrones2= ['','PigmentNetwork','Ulceration','Large_B_G_OvoidNests','Multi_B_G_Globules','MapleLeaflike','SpokeWheel','ArborizingTelangiectasia']

    # def draw(self,event):
    #     x, y = event.x, event.y
    #     if self.cv1.old_coords:
    #         x1, y1 = self.cv1.old_coords
    #         linea=self.cv1.create_line(x, y, x1, y1,width=1)
    #         self.figuraBruto.append(linea)
        
    #     self.cv1.old_coords = x,y
        
    #     #print(self.cv1.old_coords)
    #     self.figura.append((y,x))
    #     #asi se podria seguir un recorrido, almacenarlo en una variable o un fichero
    #                             #para completar la figura que se dibuje y segmentarla de la imagen
    def selector2(self):
        self.cadenaNombrePatrones = str('')
        for j in range(len(self.lista_selectores)):
            # print('ese no era 0',self.lista_selectores[j].get())
            self.cadenaNombrePatrones += self.patrones2[self.lista_selectores[j].get()]        
            print(self.cadenaNombrePatrones)
            if(self.lista_selectores[j].get() is not 0 and self.patrones2[self.lista_selectores[j].get()] in self.cadenaNombrePatrones):
                self.cadenaNombrePatrones += str('_')
                
                
    def redimensionaAbrir(self,input_image):
        print("Tamaño de entrada",self.coordenadasOriginales)
        self.alto1=self.ancho1=0
        if(self.coordenadasOriginales[0]>self.alto or self.coordenadasOriginales[1]>self.ancho):
            for a in np.arange(1,15,0.05): 
                # print(input_image.shape,a,self.alto1,self.ancho1)
                if(self.ancho >= input_image.shape[1] / a):
                    self.alto1 = int(round(input_image.shape[0] /a))
                    self.ancho1= int(round(input_image.shape[1] /a))
                    self.relacion = a
                    self.mayor = True
                    break            
        else:
            for a in np.arange(1,15,0.05): 
                # print(input_image.shape,a,self.alto1,self.ancho1,self.alto,self.ancho)
                if(self.ancho >= int(round(input_image.shape[1] *a)) and self.alto>=int(round(input_image.shape[0] *a))):
                    self.alto1 = int(round(input_image.shape[0] *a))
                    self.ancho1= int(round(input_image.shape[1] *a))
                    self.relacion = a
                    self.mayor= False

            print("Tamaño de visualización(alto,ancho) ",self.alto1,self.ancho1)
            
            
    # def redimensionaAbrir(self,input_image,hIma,wIma):
    #     # print(self.coordenadasOriginales)
    #     self.alto1=self.ancho1=0
    #     self.hVisor = self.alto
    #     self.wVisor = self.ancho
    #     print(input_image.shape)
    #     wIma,hIma,_ = input_image.shape
    #     if(hIma>self.hVisor or wIma>self.wVisor):
    #         for a in np.arange(1,15,0.05): 
    #             # print(input_image.shape,a,self.alto1,self.ancho1)
    #             if(self.wVisor >= input_image.shape[1] / a):
    #                 self.alto1 = int(round(input_image.shape[0] /a))
    #                 self.ancho1= int(round(input_image.shape[1] /a))
    #                 self.relacion = a
    #                 break            
    #     else:
    #         for a in np.arange(1,15,0.05): 
    #             # print(input_image.shape,a,self.alto1,self.ancho1,self.alto,self.ancho)
    #             if(self.wVisor >= int(round(input_image.shape[1] *a)) and self.hVisor>=int(round(input_image.shape[0] *a))):
    #                 self.alto1 = int(round(input_image.shape[0] *a))
    #                 self.ancho1= int(round(input_image.shape[1] *a))
    #                 self.relacion = a
        
        
        
        
    def procesosAlVisualizar(self,input_image):
            self.ampliado=0
            self.creaMascara = False
            self.coordenadasOriginales = input_image.shape  
            self.redimensionaAbrir(input_image)
            self.k = 0
            # input_image=input_image.reshape((self.ancho1,self.alto1))
            # input_image = cv2.resize(input_image, (self.ancho1,self.alto1))
            self.imagen = input_image
            self.cv1.delete('all')
            # self.imagen_resize = input_image.resize((self.ancho1,self.alto1))
            self.cv_img = Image.fromarray(input_image).resize((self.ancho1,self.alto1))
            # print(self.cv_img)
            self.root.photo=ImageTk.PhotoImage(self.cv_img)
            self.cv1.create_image(0,0, anchor = 'nw' , image=self.root.photo)
            self.T2.delete('1.0',tk.END)                                                        #se vacia el cuadro de texto y se rellena con la siguiente info.
            self.T2.insert(tk.END,str(self.listaImagenes[self.indice]))
            self.T3.delete('1.0',tk.END)                                                        #se vacia el cuadro de texto y se rellena con la siguiente info.
            self.T3.insert(tk.END,str(self.indice+1)+'/'+str(self.totalImagenes))
            self.lista_selectores[0].set(False)
            self.lista_selectores[1].set(False)
            self.lista_selectores[2].set(False)
            self.lista_selectores[3].set(False)
            self.lista_selectores[4].set(False)
            self.lista_selectores[5].set(False)
            self.lista_selectores[6].set(False)
            self.selector2()
    
    
    
    def Abrir(self):
        fichero=filedialog.askopenfilename(title='Abrir',filetypes=(('Todos los ficheros','*'),
                                                      ('Ficheros .png','*.png'),
                                                      ('Ficheros .jpg','*.jpg')))
        # input_image = np.asarray(Image.open(os.path.join(self.data_path,'image1.jpg')).convert('RGB'))
        # print(os.path.dirname(fichero))
        if(self.input_path != ''):
            self.limpiaLienzo()
        if(fichero!=''):
            self.input_path=os.path.dirname(fichero)
            self.listaImagenes=os.listdir(self.input_path)
            self.totalImagenes=len(self.listaImagenes)
            # print(os.path.split())
            self.indice=self.listaImagenes.index(os.path.split(fichero)[1])
            
            input_image=np.asarray(Image.open(fichero).convert('RGB'))
            self.procesosAlVisualizar(input_image)
            
        else:
            print("No se ha elegido un fichero correcto")


    def damePath(self):
        filename = filedialog.askdirectory()
        if(self.input_path != ''):
            self.limpiaLienzo()
        if(filename!=''):
            self.input_path=filename
            # print(self.input_path)
            self.listaImagenes=os.listdir(self.input_path)
            self.totalImagenes=len(self.listaImagenes)
            # print(self.listaImagenes)
            input_image=np.asarray(Image.open(os.path.join(self.input_path,self.listaImagenes[self.indice])).convert('RGB')) 
            self.procesosAlVisualizar(input_image)
            # self.coordenadasOriginales = input_image.shape
            # self.redimensionaAbrir(input_image)
            # # input_image = cv2.resize(input_image, (self.ancho1,self.alto1))
            # # input_image=input_image.resize(self.ancho1,self.alto1)
            # self.imagen = input_image
            # self.cv_img = Image.fromarray(input_image).resize((self.ancho1,self.alto1))
            # # print(self.cv_img)
            # self.root.photo=ImageTk.PhotoImage(self.cv_img)
            # self.cv1.create_image(0,0, anchor = 'nw' , image=self.root.photo)     
            # self.T2.delete('1.0',tk.END)                                                        #se vacia el cuadro de texto y se rellena con la siguiente info.
            # self.T2.insert(tk.END,str(self.listaImagenes[self.indice]))
            # self.T3.delete('1.0',tk.END)                                                        #se vacia el cuadro de texto y se rellena con la siguiente info.
            # self.T3.insert(tk.END,str(self.indice+1)+'/'+str(self.totalImagenes))
        else:
            print("No se ha elegido una ruta de entrada correcta")


    def damePath2(self):
        filename = filedialog.askdirectory()
        self.output_path=filename
        # print(self.output_path)



    def siguienteImagen(self):
        if(self.indice+1<self.totalImagenes):
            self.indice+=1
            self.limpiaLienzo()
            input_image=np.asarray(Image.open(os.path.join(self.input_path,self.listaImagenes[self.indice])).convert('RGB')) 
            self.procesosAlVisualizar(input_image)
            # self.coordenadasOriginales = input_image.shape            
            # self.redimensionaAbrir(input_image)
            # # input_image = cv2.resize(input_image, (self.ancho1,self.alto1))
            # self.imagen = input_image
            # self.cv_img = Image.fromarray(input_image).resize((self.ancho1,self.alto1))
            # # print(self.cv_img)
            # self.root.photo=ImageTk.PhotoImage(self.cv_img)
            # self.cv1.create_image(0,0, anchor = 'nw' , image=self.root.photo)    
            #     #un else con una ventana de dialogo que informe de que no quedan mas imagenes
            # self.T3.delete('1.0',tk.END)                                                        #se vacia el cuadro de texto y se rellena con la siguiente info.
            # self.T3.insert(tk.END,str(self.indice+1)+'/'+str(self.totalImagenes))
            # self.T2.delete('1.0',tk.END)                                                        #se vacia el cuadro de texto y se rellena con la siguiente info.
            # self.T2.insert(tk.END,str(self.listaImagenes[self.indice]))


    def anteriorImagen(self):
        if(self.indice>0):
            self.limpiaLienzo()
            self.indice-=1
            input_image=np.asarray(Image.open(os.path.join(self.input_path,self.listaImagenes[self.indice])).convert('RGB')) 
            self.procesosAlVisualizar(input_image)
            # self.coordenadasOriginales = input_image.shape
            # self.redimensionaAbrir(input_image)
            # self.imagen = input_image
            # self.cv_img = Image.fromarray(input_image).resize((self.ancho1,self.alto1))
            # # print(self.cv_img)
            # self.root.photo=ImageTk.PhotoImage(self.cv_img)
            # self.cv1.create_image(0,0, anchor = 'nw' , image=self.root.photo)    
            # self.T3.delete('1.0',tk.END)                                                        #se vacia el cuadro de texto y se rellena con la siguiente info.
            # self.T3.insert(tk.END,str(self.indice+1)+'/'+str(self.totalImagenes))
            # self.T2.delete('1.0',tk.END)                                                        #se vacia el cuadro de texto y se rellena con la siguiente info.
            # self.T2.insert(tk.END,str(self.listaImagenes[self.indice]))



    def guardaImagen(self):
        # nombreImagen = str(self.listaImagenes[self.indice][0:-4])+str('_mask.jpg')
        if self.cadenaNombrePatrones != []:
            nombreImagen=str(self.listaImagenes[self.indice][0:-4])+ \
                    str(self.cadenaNombrePatrones)+str('_mask_')+str(self.k)+str('.jpg')
        elif self.creaMascara == True:
            nombreImagen=str(self.listaImagenes[self.indice][0:-4])+ \
                    str('_mask_')+str(self.k)+str('.jpg')
        else:
            nombreImagen=str(self.listaImagenes[self.indice][0:-4])+ \
                    '_crop_'+str(self.k)+str('.jpg')            
        #lista imagenes en outpath
        listaOutpath=os.listdir(self.output_path)
        print("lista de items en la carpeta output")
        for j in range(len(listaOutpath)):
            print(listaOutpath[j])
            if(listaOutpath[j]==nombreImagen):
                print("pillao")
                print(listaOutpath[j])
                self.k+=1                
                nombreImagen=str(self.listaImagenes[self.indice][0:-4])+ \
                    str(self.cadenaNombrePatrones)+str(self.k)+str('.jpg')

        
        print(nombreImagen,self.output_path)

        if self.ampliado == 1 and self.creaMascara == False:
            self.output_image = np.asarray(self.cv_img2)
            print("Output image es el recorte cv_img2")
        if self.creaMascara == True:
            self.cierraFiguraPoli()
            print("Retorna de cierraFigura y guarda la imagen")


        try:            
            Image.fromarray(self.output_image).convert('RGB').save(os.path.join(self.output_path,nombreImagen))
            self.k=0
            if self.creaMascara == True:
                nombreImagen = nombreImagen[:-4] +'_mask.jpg'
                Image.fromarray(self.output_image2).convert('RGB').save(os.path.join(self.output_path,nombreImagen))
                
            self.lista_selectores[0].set(False)
            self.lista_selectores[1].set(False)
            self.lista_selectores[2].set(False)
            self.lista_selectores[3].set(False)
            self.lista_selectores[4].set(False)
            self.lista_selectores[5].set(False)
            self.lista_selectores[6].set(False)
            self.selector2()
            # cv2.imwrite(os.path.join(self.output_path,nombreImagen).encode('UTF-16LE'),self.output_image)
            # cv2.imwrite(os.path.join(self.output_path,"prueba.jpg"),self.im3)   

        except:
            print("No pudo guardarse esa imagen")





    # def bresenham(self,x0, y0, x1, y1):
    #     """Yield integer coordinates on the line from (x0, y0) to (x1, y1).
    #     Input coordinates should be integers.
    #     The result will contain both the start and the end point.
    #     """
    #     dx = x1 - x0
    #     dy = y1 - y0
    
    #     xsign = 1 if dx > 0 else -1
    #     ysign = 1 if dy > 0 else -1
    
    #     dx = abs(dx)
    #     dy = abs(dy)
    
    #     if dx > dy:
    #         xx, xy, yx, yy = xsign, 0, 0, ysign
    #     else:
    #         dx, dy = dy, dx
    #         xx, xy, yx, yy = 0, ysign, xsign, 0
    
    #     D = 2*dy - dx
    #     y = 0
    
    #     for x in range(dx + 1):
    #         yield x0 + x*xx + y*yx, y0 + x*xy + y*yy
    #         if D >= 0:
    #             y += 1
    #             D -= 2*dx
    #         D += 2*dy
    
    
    def radiales(self):
        self.creaMascara = True
        # print(self.v)
        if(self.v.get()==1): #poligonal
            # print("llega")
            self.cv1.unbind("<B1-Motion>")
            self.cv1.bind('<Button-1>',self.draw)
        if(self.v.get()==2): #mano alzada
            self.cv1.bind('<B1-Motion>', self.draw1)
            # self.cv1.unbind("<Button-1>")
            # self.cv1.bind('<ButtonRelease-1>', self.reset_coords)
    
    # def motion(self,event):          #mostrar la posicion en el lienzo (las coordenadas)
    #     self.T4.delete('1.0',tk.END)                                                        #se vacia el cuadro de texto y se rellena con la siguiente info.
    #     self.T4.insert(tk.END,str(event.x)+str('||')+str(event.y))
        

    def actualizaCuenta(self,event):
        if(int(self.dato_entrada.get()-2)>=0):
            self.indice=int(self.dato_entrada.get()-2)
            self.siguienteImagen()
        if(int(self.dato_entrada.get()-2)<0):
            # print("llega")
            self.indice=-1
            self.siguienteImagen()
            # print("Entrada.get :"+str(self.cuenta))


    def draw1(self,event):
        x, y = event.x, event.y
        if self.cv1.old_coords:
            x1, y1 = self.cv1.old_coords
            linea=self.cv1.create_line(x, y, x1, y1,width=1)
            # self.figuraBruto.append(linea)
        else:
            self.primerasCoorde=x,y
        self.cv1.old_coords = x, y
        #print(self.cv1.old_coords)
        self.figura.append(self.cv1.old_coords)
        self.figura99.append(self.cv1.old_coords)
        #asi se podria seguir un recorrido, almacenarlo en una variable o un fichero
                                #para completar la figura que se dibuje y segmentarla de la imagen

    def draw2(self,event):
        # print(self.iniR)
        if(self.iniR):
            self.cv1.delete(self.rectangulo)
            self.rectangulo=self.cv1.create_rectangle(self.iniR[0],self.iniR[1],event.x,event.y)
            # print("hola",self.rectangulo)
            self.finR=event.x,event.y
        else:
            self.iniR= event.x, event.y

    # def draw3(self,event):
    #     self.finRectangulo= event.x, event.y
    #     linea1=self.cv1.create_line(x, y, x1, y1,width=1)
    
    
    def draw(self,event):
        x,y=event.x,event.y
        if self.cv1.old_coords is None:
            # print("primera")
            self.cv1.old_coords=x,y
            self.primerasCoorde=self.cv1.old_coords
            # print(self.cv1.old_coords)
            self.figura.append((y,x))
            self.figura99.append((x,y))
            #lo que toca
        else:
            x1,y1 = self.cv1.old_coords
            self.cv1.old_coords= x,y
            linea=self.cv1.create_line(x1,y1,x,y)
            self.figura.append((y,x))
            self.figura99.append((x,y))
            # print(self.cv1.old_coords)


    def cropCrea(self): 
        print(self.iniR,self.finR,self.imagen.shape)
        # return np.asarray(self.cv_img)[self.iniR[1]:self.finR[1],self.iniR[0]:self.finR[0]]
            # print(self.iniR,self.finR,self.img)
        print(self.ampliado)
        if self.ampliado == 0:
            crop =  np.asarray(self.cv_img)[min(self.iniR[1],self.finR[1]):max(self.finR[1],self.iniR[1]),
                                              min(self.iniR[0],self.finR[0]):max(self.iniR[0],self.finR[0])]
        else:
            crop = np.asarray(self.cv_img2)[min(self.iniR[1],self.finR[1]):max(self.finR[1],self.iniR[1]),
                                              min(self.iniR[0],self.finR[0]):max(self.iniR[0],self.finR[0])]
        
        return crop
            
            

    def Zoom(self):
        self.cv1.unbind("<Button-1>")
        self.cv1.bind('<B1-Motion>', self.draw2)
        self.cv1.bind('<ButtonRelease-1>', self.ampliaImagen)
        # self.ampliaImagen()
        #bandera que indique que se ha hecho zoom para recortar bien al extraer
        

    def ampliaImagen(self,event):
        self.cv1.delete(self.rectangulo)
        self.cv1.unbind('<B1-Motion>')
        self.cv1.unbind('<ButtonRelease-1>')
        print("Al hacer zoom el recorte tiene el tamaño(incio,fin): ",self.iniR,self.finR)
        print(self.ampliado)
        recorte=self.cropCrea()
        print(recorte.shape)
        alto2=recorte.shape[0]
        ancho2=recorte.shape[1]
        print("Size recorte: ",recorte.shape)

        for a in np.arange(1,10,0.25): 
            print(a,alto2,ancho2)
            if(self.ancho >= int(round(recorte.shape[0] *a)) and self.alto>=int(round(recorte.shape[1] *a))):
                alto2 = int(round(recorte.shape[0] *a))
                ancho2= int(round(recorte.shape[1] *a))
                self.relacion = a
            else:
                break
        self.ancho3=int(round(ancho2/self.relacion))
        self.alto3=int(round(alto2/self.relacion))
        self.ancho4=ancho2
        self.alto4=alto2
        print("Tamaño de visualizacion del recorte: ",self.ancho4,self.alto4)
        # print(alto2,ancho2,self.alto3,self.ancho3)
        self.cv_img2 = Image.fromarray(cv2.resize(recorte,(ancho2,alto2)))
        # print(self.cv_img)
        self.root.photo=ImageTk.PhotoImage(self.cv_img2)
        self.cv1.create_image(0,0, anchor = 'nw' , image=self.root.photo) 
        self.ampliado=1
    
    
    
    def reset_coords(self,event):
        self.cv1.old_coords = None
        
        
        
    def limpiaLienzo(self):
        #print(self.figura)
        self.rectangulo=[]
        self.iniR=[]
        self.finR=[]
        self.ampliado=0
        self.figura=[]
        self.cierra=[]
        self.casiCierra=[]
        self.figura2=[]
        self.figura3=[]
        self.figura99=[]
        self.cv1.old_coords=None
        self.cv1.delete("all")
        self.root.photo=ImageTk.PhotoImage(self.cv_img)
        self.cv1.create_image(0,0, anchor = 'nw' , image=self.root.photo)
    
    def limpiaEstructura(self):
        #print(self.figura)
        self.vaciado = 1
        self.figura99=[]
        self.cv1.old_coords=None


    def cierraCamino(self):
        #cuantos puntos sera necesario agregar:
        self.figura2=self.figura
        alto=int(self.figura2[0][0])
        ancho=int(self.figura2[0][1])     #estos seran las coordenadas objetivo
        #ultima posicion de la lista que no se cerró
        alto2=int(self.figura2[-1][0])
        ancho2=int(self.figura2[-1][1])   #estas seran las coordenadas de partida
        self.figura3.append(self.figura2[0])
        i=0
        #print("antes del while",self.figura3)
        self.figura2.append(self.figura3[-1])
        # print(self.figura2)
        # print("long figura2=",len(self.figura2))
        # print(self.figura2[0],self.figura3[-1])
        for i in range(len(self.figura2)):  
            alto=int(self.figura3[-1][0])
            ancho=int(self.figura3[-1][1])     #estos seran las coordenadas que iremos variando
            #print("por aqui",i,self.figura2[i][0])
            alto2=int(self.figura2[i][0])
            ancho2=int(self.figura2[i][1])     #estos seran las coordenadas objetivo en cada iteracion            
            # print(self.figura)
            # print(self.figura3)
            # self.figura3 = self.figura3 + list(self.bresenham(alto,ancho,alto2,ancho2))         # self.figura3.append()            
            # # print(self.figura3)
            distancias = []
            while(ancho!=ancho2 or alto!=alto2):
                # distancias.append(sqrt((alto-alto2)**2+(ancho-ancho2)**2))        
                print(i,len(self.figura2))
                print(ancho,ancho2,alto,alto2)
                distancias.append(sqrt((alto-alto2)**2+(ancho-1-ancho2)**2))
                distancias.append(sqrt((alto-alto2)**2+(ancho+1-ancho2)**2))
                distancias.append(sqrt((alto-1-alto2)**2+(ancho-ancho2)**2))
                distancias.append(sqrt((alto+1-alto2)**2+(ancho-ancho2)**2))
                distancias.append(sqrt((alto+1-alto2)**2+(ancho+1-ancho2)**2))
                distancias.append(sqrt((alto-1-alto2)**2+(ancho+1-ancho2)**2))                
                distancias.append(sqrt((alto+1-alto2)**2+(ancho-1-ancho2)**2))
                distancias.append(sqrt((alto-1-alto2)**2+(ancho-1-ancho2)**2))
                if(ancho > ancho2 and min(distancias)==distancias[0]):
                    self.figura3.append((alto,ancho-1))
                elif(ancho < ancho2 and min(distancias)==distancias[1]):
                    self.figura3.append((alto,ancho+1))
                elif(alto > alto2 and min(distancias)==distancias[2]):
                    self.figura3.append((alto-1,ancho))
                elif(alto < alto2 and min(distancias)==distancias[3]):
                    self.figura3.append((alto+1,ancho))
                elif(min(distancias)==distancias[4]):
                    self.figura3.append((alto+1,ancho+1))
                elif(min(distancias)==distancias[5]):
                    self.figura3.append((alto-1,ancho+1))
                elif(min(distancias)==distancias[6]):
                    self.figura3.append((alto+1,ancho-1))
                elif(min(distancias)==distancias[7]):
                    self.figura3.append((alto-1,ancho-1))
                alto=int(self.figura3[-1][0])
                ancho=int(self.figura3[-1][1])     #estos seran las coordenadas que iremos variando    
                distancias=[]
        #print("sale",self.figura3)
        # while(i==0 or self.figura3[0]!=self.figura3[i]):
        #     alto=int(self.figura3[i][0])
        #     ancho=int(self.figura3[i][1])     #estos seran las coordenadas objetivo
        #     if(alto==alto2 and ancho==ancho2 and j+1<len(self.figura2)):
        #         j=j+1
        #     print(self.figura3,i)
        #     alto2=int(self.figura2[j][0])
        #     ancho2=int(self.figura2[j][1])   #estas seran las coordenadas de partida
        #     if(ancho > ancho2):
        #         self.figura3.append((alto,ancho+1))
        #         i=i+1
        #     elif(ancho < ancho2):
        #         self.figura3.append((alto,ancho-1))
        #         i=i+1
        #     elif(alto > alto2):
        #         self.figura3.append((alto+1,ancho))
        #         i=i+1
        #     elif(alto < alto2):
        #         self.figura3.append((alto-1,ancho))
        #         i=i+1
        #     print("sale del bucle")
        
    def extraeFigura(self):
        #print("extraefigura")
        #print(self.figura3[0])
        self.figura3=self.figura99
        # self.figura3=self.figura
        maxVertical = max(elemento[0] for elemento in self.figura3)
        minVertical = min(elemento[0] for elemento in self.figura3)
        maxHorizont = max(elemento[1] for elemento in self.figura3)
        minHorizont = min(elemento[1] for elemento in self.figura3)
        print(maxVertical,minVertical,maxHorizont,minHorizont)
        bbox=(minVertical,minHorizont,maxVertical,maxHorizont)
        #print(bbox)
        # self.cv1.create_line(minHorizont,minVertical,minHorizont,maxVertical) #pinta bbox
        # self.cv1.create_line(minHorizont,minVertical,maxHorizont,minVertical)
        
        #mascara  = np.zeros((bbox[2]-bbox[0],bbox[3]-bbox[1]),dtype='int')
        # mascara2 = np.zeros((bbox[2]-bbox[0],bbox[3]-bbox[1]),dtype='int')
        # mascara3 = np.zeros((bbox[2]-bbox[0],bbox[3]-bbox[1]),dtype='int')
        # mascara4 = np.zeros((bbox[2]-bbox[0],bbox[3]-bbox[1]),dtype='int')        
        # print("Forma de la mascara",mascara2.shape)
        # frontera=0
        # inicio=0
        # np.savetxt('figura.txt',self.figura3,fmt='%s')
        # for i in range(minVertical,maxVertical):
        #     for j in range(minHorizont,maxHorizont):
        #         n = i-minVertical
        #         m = j-minHorizont
        #         if(self.figura3.count((i,j))==1):
        #             # mascara3[n,m]=1
        #             mascara2[n,m]=1
                #     if(frontera==1 and self.figura3.count((i,j+1))!=1):
                #         frontera=0
                #         mascara3[n,inicio:m]=1
                #     if(frontera==0 and self.figura3.count((i,j+1))!=1):
                #         mascara3[n,m]=1
                #         frontera=1
                #         inicio=m        
                # # print(mascara3.shape,i,j,n,m)
                # if(frontera==1 and j==maxHorizont-1 and mascara3[n,0:inicio-6].all()!=1):   #fuera del primer if del bucle o no ocurrira
                #     frontera=0
                #     # print("borde sin figura",inicio,n,m)
                #     mascara3[n,inicio:m]=1             
        # mascara2 = cv2.dilate(np.float32(mascara2),None)    
        if self.ampliado==1:
            mascara4 = np.zeros((self.alto4,self.ancho4))
        else:
            mascara4 = np.zeros((self.alto1,self.ancho1))
            
        # np.savetxt('figura2.txt',mascara2.astype(int),fmt='%s')
        # for i in range(maxVertical-minVertical-1):
        #     inicio=0
        #     lOcupa=0
        #     for j in range(maxHorizont-minHorizont-1):
        #         if(inicio == 0 and mascara2[i,j]==1 and mascara2[i,j+1]==0):
        #             # lOcupa=0
        #             inicio = j
        #             if(lOcupa>0 and mascara2[i,lOcupa:j].all()==1 and mascara2[i,j:-1].all()==0):
        #                 inicio = 0
        #             # print(j)
        #         if(inicio != 0 and mascara2[i,j-1]==0 and mascara2[i,j]==1):
        #             mascara4[i,inicio:j]=1
        #             lOcupa = j
        #             inicio = 0
        #         if(inicio != 0 and j==maxHorizont-minHorizont-2 and 0<i<maxVertical-minVertical-1):
        #             mascara4[i,inicio:j]=1
                    # inicio = 0    
        # numcruces=0
        # cruces = np.zeros((maxHorizont-minHorizont-1),dtype=int)
        # puntos = np.asarray(self.figura99)
        # print(puntos[:])        
        # mascara4=np.zeros((self.alto1,self.ancho1),dtype=np.uint8)
        # mascara5=np.zeros(mascara4.shape)
        cv2.fillPoly(mascara4, [np.asarray(self.figura99).astype('int32')], color=(255,255,255))
        np.savetxt('mascara.txt',(mascara4/255).astype(int),fmt='%s')
        np.savetxt('figura.txt',self.figura99,fmt='%s')
        # cv2.fillPoly(mascara5, [np.asarray(self.figura99).astype('int32')], color=(255,255,255))
        # cv2.imshow("",mascara4)
        # cv2.waitkey(0)
        
        # cv2.imwrite('outttttt.jpg',mascara4)
        # print(self.coordenadasOriginales)
        if(self.ampliado==0):
            self.output_image2 = np.asarray(cv2.resize(mascara4,(self.coordenadasOriginales[1],self.coordenadasOriginales[0])),dtype = np.uint8)
            print("Tamaño de guardado(sin zoom): ",self.coordenadasOriginales)
            # Image.fromarray(self.output_image).convert('RGB').save(os.path.join(self.output_path,'outt.jpeg'))
            # self.im3=cv2.resize(cv2.bitwise_and(np.asarray(self.cv_img),np.asarray(self.cv_img),mask=mascara4),(self.coordenadasOriginales[1],self.coordenadasOriginales[0]))
            # self.im3=cv2.resize(cv2.bitwise_and(self.imagen,self.imagen,mask=self.output_image2),(self.coordenadasOriginales[1],self.coordenadasOriginales[0]))
            print(self.output_image2.shape,self.imagen.shape,mascara4.shape)
            self.im3=cv2.bitwise_and(np.asarray(self.imagen),np.asarray(self.imagen),mask=self.output_image2)
            self.output_image = self.im3
        else:
            # if(self.mayor):
            #     rela = self.relacion
            # else:
            #     rela = 1/self.relacion
            # print("Tamaños maximo y minimo: ",max(self.figura99),min(self.figura99))
            self.creaMascara = True
            imagenDownSize = cv2.resize(mascara4,(self.ancho3,self.alto3))                                     
            imagenMascara = np.zeros((self.alto1,self.ancho1),dtype=np.uint8)
            print(self.ancho3,self.alto3)
            print(self.iniR,self.finR,imagenMascara.shape,imagenDownSize.shape)
            print(self.iniR[1],self.finR[1])
            # imagenMascara[int(round(self.iniR[1]*rela)):int(round(self.finR[1]*rela)),
            #               int(round(self.iniR[0]*rela)):int(round(self.finR[0]*rela))]=imagenDownSize
            imagenMascara[self.iniR[1]:self.finR[1],self.iniR[0]:self.finR[0]]=imagenDownSize
            # print(imagenMascara.shape,self.imagen.shape)
            
            self.im3=cv2.resize(cv2.bitwise_and(np.asarray(self.cv_img),np.asarray(self.cv_img),mask=imagenMascara),(self.coordenadasOriginales[1],self.coordenadasOriginales[0]))
            self.output_image = self.im3
            # self.guardaImagen()
            self.output_image2 = cv2.resize(imagenMascara,(self.coordenadasOriginales[1],self.coordenadasOriginales[0]))
            # self.guardaImagen()
            
        # if(self.vaciado):
            


        # self.imagen_previa=output_image
        # cv2.imwrite('out2.jpg',output_image)       


       # for i in range(maxVertical-minVertical-1):
        #     numcruces=0
        #     bordeFuera=0
        #     entra=0
        #     for j in range(maxHorizont-minHorizont-1):
        #         if(mascara2[i,j]==0 and mascara2[i,j+1]==1 and entra==0): #antes del borde
        #             bordeFuera=1
        #         if(bordeFuera==1 and mascara2[i,j]==1 and mascara2[i,j+1]==0): #despues del borde
        #         #en j+1 empieza el interior del poliedro
        #             bordeDentro=1
        #             entra=j+1
        #             bordeFuera=0
        #             numcruces=+1
        #             #condicion esquinas interiores no convexo
                    
        #         print(numcruces,i)    
        #         if(numcruces%2!=0 and entra!=0 and mascara2[i,j]==0 and mascara2[i,j+1]):
        #             #rellenar
        #             mascara4[i,entra:j]==1
        #             entra=0
        
        # for i in range(maxVertical-minVertical-1):
        #     entra=sale=0
        #     rellenado=0
        #     numcruces=0
        #     for j in range(maxHorizont-minHorizont-1):
        #         if(mascara4[i,j]==0 and mascara4[i,j+1]==1):
        #             entra=j
        #             cruces[j]=1
        #             # if(rellenado > 0 and mascara2[i,j-rellenado:j].all()==0):
        #             #     print("No rellena desde i=",i," j=",j)
        #             #     entra=0
        #         # if(mascara4[i,j]==0 and mascara4[i,j-1]==1 and
        #         #     mascara4[i,j-rellenado:j].all()==1 and mascara2[i-1,j-rellenado:j].all()==0):
        #         #     entra=j
        #         #     print("cree que es un borde en i=",i," j=",j," entra=", entra," sale=",sale," rellenado=",rellenado)
                
        #         if(mascara4[i,j]==1 and mascara4[i,j+1]==0 and entra>0):
        #             sale=j
        #             numcruces+=1
        #             cruces[j]=-1
        #         if(mascara2[i,sale+1:j].all()==0 and mascara4[i,j+1]==1 and sale>0 and numcruces%2!=0):
        #             # print("rellena")
        #             if(mascara2[i+1,sale:j].all()==0 or mascara2[i-1,sale:j].all()==0):
        #                 mascara4[i,sale:j+1]=1
        #                 rellenado=j-sale
        #                 sale=0
        #                 entra=0
                # if(mascara2[i,sale+1:j].all()==0 and mascara4[i,j+1]==1 and mascara4[i-1,sale:j].all()==1 and sale>0):
                #     mascara4[i,sale:j+1]=1
                #     rellenado=j-sale
                #     sale=0
                #     entra=0
                # if(j==(maxHorizont-minHorizont-2)):
                #     print(cruces)
                    
        # for i in range(maxVertical-minVertical-1):
        #     entra=sale=0
        #     rellenado=0
        #     anchoBorde=0
        #     # cruces = np.zeros((maxHorizont-minHorizont-1),dtype=int)  
        #     for j in range(maxHorizont-minHorizont-1):
        #         if(mascara2[i,j]==0 and mascara2[i,j-1]==1):   #cara interior de un borde
        #             entra=j
        #             # print("ha entrado en i=",i," j=",j)
        #             # if(mascara4[i,j-rellenado:j].all()==1 and rellenado > 0):
        #             #     entra=0
        #             #     rellenado=0
        #             # if(mascara4[i-1,int((j-rellenado)*0.9):int(j*1.1)].all()==0):
        #             #     print("ha evitado entrar en i=",i," j=",j, "longitud =",int(j*1.1)-int((j-rellenado)*0.9))
        #             #     entra=j
        #         if(mascara2[i,j]==1 and mascara2[i,j-1]==0 and mascara4[i,entra:j-1].all()==0):   #cara interior de otro borde
        #             # print("ha salido en i=",i," j=",j)
        #             sale=j
        #             # if(mascara4[i-1,int(entra*1.1):int(sale*0.9)].all()==0):
        #             #     entra=0
        #             #     sale=0
        #         if(entra!=0 and sale!=0 and sale>entra):                             #entonces hay que rellenar
        #             # print("ha rellenado desde i=",i," j=",j) 
        #             mascara4[i,entra:sale]=1
        #             rellenado=sale-entra
        #             entra=sale=0
        #         if(entra!=0 and sale==0 and j==maxHorizont-minHorizont-1):
        #             mascara4[i,entra:j]=1
        # #         if(j==0 and mascara2[i,j]==1):                #primera columna y es un borde
        # #             cruces[j]=1
        # #             entra=j
        # #         if(mascara2[i,j]==0 and mascara2[i,j-1]==1):  #va a entrar
        # #             cruces[j]=1
        # #             entra=j
        # #         if(mascara2[i,j]==1 and mascara2[i,j-1]==0 and mascara2[i,entra:j].all()==0):  #sale de un borde
        # #             cruces[j]=-1
        # #             sale=j     
        # # for i in range(maxHorizont-minHorizont-1):
        # #     entra=sale=0
        # #     rellenado=0
        # #     for j in range(maxVertical-minVertical-1):
                
                    
                    
        
        
                    
        # kernel = np.ones((5,5),np.uint8)
        # kernel2 = np.ones((8,8),np.uint8)
        # # mascara3 = cv2.dilate(np.float32(mascara3),None)
        # mascara4 = cv2.erode(np.float32(mascara4),kernel)         
        # mascara4 = cv2.dilate(np.float32(mascara4),kernel2)         
        # mascara4 = cv2.morphologyEx(mascara4, cv2.MORPH_CLOSE, kernel)

        # inicio=frontera=0
        
        # np.savetxt('figura2.txt',mascara2.astype(int),fmt='%s')
        # np.savetxt('figura3.txt',mascara3.astype(int),fmt='%s')
        # np.savetxt('figura4.txt',mascara4.astype(int),fmt='%s')
        # mascara = np.zeros((bbox[2]-bbox[0],bbox[3]-bbox[1],3))
        # print(mascara.shape)
        # mascara[:,:,0] = mascara[:,:,1] = mascara[:,:,2] = mascara4
        # print("forma imagen",self.imagen.shape)
        # recorte = self.imagen[bbox[0]:bbox[2],bbox[1]:bbox[3]]
        # print(recorte.shape)
        # recorteSilueta = np.zeros((bbox[2]-bbox[0],bbox[3]-bbox[1],3))
        # #multiply(recorte,mascara,recorteSilueta)
        # recorteSilueta[:,:,0] = recorte[:,:,0]*mascara[:,:,0]
        # recorteSilueta[:,:,1] = recorte[:,:,1]*mascara[:,:,1]
        # recorteSilueta[:,:,2] = recorte[:,:,2]*mascara[:,:,2]

        
        # recorteSilueta = Image.fromarray(np.uint8(recorteSilueta))
        # recorteSilueta.show()       
        # recorteSilueta.save('out.jpg','JPEG')
        # cv2.imwrite('outttttt.jpg',recorteSilueta)

        # imshow("Pulsar 'Espacio' para cerrar",recorteSilueta)
        # waitKey(0)
        # destroyWindow("Pulsar 'Espacio' para cerrar")
        
        # np.savetxt('recorte.jpg',recorteSilueta,fmt='%s')
        
        # for i in range(minVertical,maxVertical):
        #     for j in range(minHorizont,maxHorizont):
        #         n = i-minVertical
        #         m = j-minHorizont
        #         mascara[n,m]=0
        #         #print(bbox,i,j,n,m,mascara.shape,self.figura3.count((i,j)))
        #         #print((maxVertical-minVertical),(maxHorizont-minHorizont),(i,j),(i,j) in self.figura2)
        #         if(frontera==0 and self.figura3.count((i,j))==1):
        #             frontera=1
        #             inicio=n
        #             mascara[n,m]=1
        #             #print(inicio,frontera)
        #             break
        #         if(frontera==1 and self.figura3.count((i,j))==1):
        #             #print("algo hace")
        #             frontera=0
        #             #print(n,inicio,m)
        #             mascara[inicio:m,m]=1
        #             #print(mascara)
                
        #print(mascara)
    def cierraFiguraPoli(self):
        
        x,y = self.cv1.old_coords
        x1,y1 = self.primerasCoorde
        # print("Coordenadas iniciales: x=",x1," y=",y1)
        # print("Coordenadas finales: x=",x," y=",y)
        self.cv1.create_line(x1,y1,x,y)
        # self.cierraCamino()
        self.extraeFigura()

        
        
    def cierraFigura(self):
        #print((self.figura[5][0]))
        if(len(self.figura)>1):
            for i in range(len(self.figura)):
                alto=int(self.figura[i][0])
                ancho=int(self.figura[i][1])
                # print(alto,ancho)
                for j in range(len(self.figura)-1,-1,-1):
                    #print(i,j)
                    if(i!=j and (j>i*1.5 or j< i*0.5)):
                        alto2=int(self.figura[j][0])
                        ancho2=int(self.figura[j][1])
                        #print(len(self.figura),i,j)
                        if((alto<alto2+3 and alto>alto2-3) and (ancho<ancho2+3 and ancho>ancho2-3) or (alto==alto2 and ancho==ancho2)):
                            #la figura se cierra en algun punto
                            #print(alto,ancho,alto2,ancho2)
                            #print("se cierra")
                            #i=len(self.figura)
                            #self.figura2 = self.figura[i:j]
                            self.cierra.append((i,j,alto,ancho,alto2,ancho2))
                            
                        elif((alto*0.9<alto2 and alto*1.1>alto2)and (ancho*0.9<ancho2 and ancho*1.1>ancho2)):
                            #casi se cierra
                            #print(alto,ancho,alto2,ancho2)
                            #print("casi se cierra")
                            #i=len(self.figura)
                            #self.figura2 = self.figura[i:j]
                            self.casiCierra.append((i,j,alto,ancho,alto2,ancho2))
                            
                            #llamada a funcion cierra camino
                            
                        #agregar a la lista figura los puntos necesarios para volver a unir la figura?
                        #otra posibilidad es contar con esos puntos para luego tener en cuenta que esa
                        #linea no se ha pintado pero existe (a la hora de recorrer el interior de la figura)
                        #algoritmo livewire https://en.wikipedia.org/wiki/Livewire_Segmentation_Technique
            #print("cierra", len(self.cierra))
            #print("casi cierra", len(self.casiCierra))
            if(len(self.cierra)>1):
                self.cierra=self.casiCierra
            puntoCierra=(int(self.cierra[0][2]),int(self.cierra[0][3]),int(self.cierra[0][4]),int(self.cierra[0][5]))   #momento en el que dos coordenadas son casi la misma             
            distancia  = sqrt((puntoCierra[0]-puntoCierra[2])**2+(puntoCierra[1]-puntoCierra[3])**2)     #distancia entre los limites
            #print(distancia)                                                                            #llegado a este punto, necesitamos saber el indice dentro de la figura
            for i in range(len(self.cierra)):
                puntoCierra=(int(self.cierra[i][2]),int(self.cierra[i][3]),int(self.cierra[i][4]),int(self.cierra[i][5]))                
                nuevaDistancia = sqrt((puntoCierra[0]-puntoCierra[2])**2+(puntoCierra[1]-puntoCierra[3])**2)
                if(nuevaDistancia < distancia):
                    distancia = nuevaDistancia
                    puntoCierra2 = self.cierra[i]
                else:
                    puntoCierra2 = puntoCierra
             
            #print(puntoCierra2)    
            #print("casi cierra")
            #print(self.casiCierra)
            for i in range(len(self.cierra)):
                if(self.cierra[i][2]==puntoCierra2[0] and self.cierra[i][3]==puntoCierra2[1]):
                        print()
                if(self.cierra[i][4]==puntoCierra2[2] and self.cierra[i][5]==puntoCierra2[3]):
                        #print(i,self.cierra[i])
                        indice = i
            #entonces la figura cerrada debe de tener la siguiente forma:
            indicePrimero = int(self.cierra[indice][0])
            indiceSegundo = int(self.cierra[indice][1])
            if(indicePrimero>indiceSegundo):
                self.figura2 = self.figura[indiceSegundo:indicePrimero]
            else:
                self.figura2 = self.figura[indicePrimero:indiceSegundo]
            #print(len(self.figura))
            self.cv1.delete("all")
            self.root.photo=ImageTk.PhotoImage(self.cv_img)
            self.cv1.create_image(0,0, anchor = 'nw' , image=self.root.photo)            
            #print("hasta aqui")
            for i in range(len(self.figura2)-3):
                #print("llega")
                self.cv1.create_line(self.figura2[i][1], self.figura2[i][0], self.figura2[i+1][1], self.figura2[i+1][0],width=1)
            self.cv1.create_line(self.figura2[0][0],self.figura2[0][1],self.figura2[-1][0],self.figura2[-1][1],width=1)
            self.cv1.old_coords = None
            self.cierraCamino()
            self.extraeFigura()
            
                        
            
            
            

            
    
    def __init__(self,parent,*args,**kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.parent=parent
        self.root.wm_title("imageCropper Derma")
        path_icono = 'archivos_programa/logoImageCropperDerma.ico'
        icono = os.path.join(os.path.dirname(__file__),path_icono)
        parent.iconbitmap(icono)
        # self.root.geometry('1200x800')
        # self.alto = 600
        # self.ancho= 
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()

        self.root.geometry("%dx%d+0+0" % (w, h))
        self.alto = int(round(0.85*h))
        self.ancho= int(round(0.75*w))
        
        
        nombre = 'archivos_programa/4 logos.png'
        nombre = os.path.join(os.path.dirname(__file__),nombre)
        # pathTDD = 'iconos_programa/angosturaTDD.png'
        # imagenTDD = Image.open(os.path.join(os.path.dirname(__file__),pathTDD))
        # imagenTDD = imagenTDD.resize((int(0.10*self.wMain),int(0.06*self.hMain)))
        
        
        self.frame1 = tk.Frame(self.root, width=self.ancho, height=self.alto)
        self.frame1.grid(row=0, column=0,rowspan=8,columnspan=4,sticky='w')
        self.cv1 = tk.Canvas(self.frame1, height=self.alto, width=self.ancho, background="white", relief=tk.RAISED)
        self.cv1.grid(row=0,column=0)
        

        self.imagenIN = Image.open(os.path.join(os.path.dirname(__file__),nombre))
        hIma,wIma,dims = np.asarray(self.imagenIN).shape
        self.coordenadasOriginales = hIma,wIma
        self.redimensionaAbrir(np.asarray(self.imagenIN))
        self.imagenIN = self.imagenIN.resize((self.ancho,self.alto))
        self.img = ImageTk.PhotoImage(self.imagenIN,master=parent)        
        # self.cv1 = tk.Canvas(parent, height=self.hVisor, width=self.wVisor, bd=1)
        # self.cv1.grid(row=2,column=1,padx=2,pady=2,columnspan = 5, rowspan = 12)
        self.cv1.create_image(0,0, anchor = 'nw' , image=self.img)         
        #path inicializacion
        
        # self.data_path="C:\\Users\\ManuelL\\Documents\\Proyecto TIR\\"
        
        #botones
        
        limpiaButton = tk.Button(self.root, text='Limpiar', height=2, width=8, command = self.limpiaLienzo)
        limpiaButton.grid(row=0, column=4, padx=2, pady=2)
        # cierraButton = tk.Button(self.root, text='Extraer', height=2, width=8, command = self.cierraFigura)
        cierraButton = tk.Button(self.root, text='Extraer', height=2, width=8, command = self.guardaImagen)
        cierraButton.grid(row=0, column=5, padx=2, pady=2)
        
        # vaciaButton = tk.Button(self.root, text='Vaciar', height=2, width=8, command = self.limpiaEstructura)
        # vaciaButton.grid(row=0, column=6, padx=2, pady=2)
        
        ZoomButton = tk.Button(self.root, text='Zoom', height=2, width=8, command = self.Zoom)
        ZoomButton.grid(row=0, column=6, padx=2, pady=2)     
                
        
        AbreButton = tk.Button(self.root, text='Abrir', height=2, width=8, command = self.Abrir)
        AbreButton.grid(row=8, column=0, padx=2, pady=2)
        PathButton = tk.Button(self.root, text='Directorio Entrada', height=2, width=16, command = self.damePath)
        PathButton.grid(row=8, column=1, padx=2, pady=2)        
        Path2Button = tk.Button(self.root, text='Directorio Salida', height=2, width=16, command = self.damePath2)
        Path2Button.grid(row=8, column=2, padx=2, pady=2)     
        

        
        siguienteButton = tk.Button(self.root, text='Siguiente', height=2, width=16, command = self.siguienteImagen)
        siguienteButton.grid(row=5, column=4, padx=2, pady=2)        
        anteriorButton = tk.Button(self.root, text='Anterior', height=2, width=16, command = self.anteriorImagen)
        anteriorButton.grid(row=6, column=4, padx=2, pady=2)        


        self.v = tk.IntVar()
        modoPoliButton=tk.Radiobutton(self.root, text="Poligonal", variable=self.v, value=1,command = self.radiales)
        modoPoliButton.grid(row=1,column=4,padx=2,pady=2)
        modoAlzaButton=tk.Radiobutton(self.root, text="Mano Alzada", variable=self.v, value=2,command=self.radiales)
        modoAlzaButton.grid(row=1,column=5,padx=2,pady=2)
        

        # cuadros de texto: T3, imagen actual/ imagen total
        self.T3 = tk.Text(root,height=1,width=10)
        self.T3.grid(row=3,column=4,sticky='n')
        #  T2: nombre imagen actual
        self.T2 = tk.Text(root,height=1,width=40)
        self.T2.grid(row=5,column=4,columnspan=3,sticky='n')
        #  T4: posicion/coordenadas del raton
        # self.T4 = tk.Text(root,height=1,width=12)
        # self.T4.grid(row=2,column=5,columnspan=3)
        
        
        # etiquetas de texto fijas
        
        texto1 = tk.Label(self.root, text="Imagen Actual/Imágenes Totales", font=("Helvetica", 10))
        texto1.grid(row=2,column=4,sticky='s')
        texto2 = tk.Label(self.root, text="Introducir Nº de Imagen", font=("Helvetica", 10))
        texto2.grid(row=2,column=5,sticky='s')
        texto3 = tk.Label(self.root, text="Nombre del fichero actual", font=("Helvetica", 10))
        texto3.grid(row=4,column=4)

        #input para saltar a una imagen en concreto de la lista
        self.dato_entrada  = tk.IntVar()
        # etiqueta1     = tk.Label(root, textvariable = self.dato_entrada)
        # etiqueta1.grid(row=3,column=5,sticky='n')
        entrada_texto = tk.Entry(root,textvariable=self.dato_entrada)
        entrada_texto.grid(row=3,column=5,sticky='nw')
#        dato_entrada.trace("w",self.actualizaCuenta(dato_entrada.get()))
        entrada_texto.bind("<Return>",self.actualizaCuenta)

        
        #variables
        self.indice=0
        self.vaciado=0
        self.figura=[]
        self.figura3=[]
        self.ampliado=0
        self.figuraBruto=[]
        self.figura99=[]
        self.cierra=[]
        self.casiCierra=[]
        self.eps = 2.220446049250313e-16
        self.iniR=[]
        self.finR=[]
        self.rectangulo=[]
        self.cadenaNombrePatrones = []
        self.input_path=''
        self.k = 0
        self.creaMascara = False
        
        self.var0 = tk.IntVar()
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.var5 = tk.IntVar()
        self.var6 = tk.IntVar()
        self.var7 = tk.IntVar()
        self.lista_selectores = [self.var0 , self.var1, self.var2, self.var3,
                                self.var4, self.var5, self.var6, self.var7] 
        
        
        

        # self.cv1.bind('<Motion>',self.motion)

        r1=ttk.Checkbutton(self.root,text=self.patrones2[1],variable=self.var0, command=self.selector2, onvalue=1)
        r1.grid(row=7,column=4,padx=2,pady=2,sticky='w')
        r2=ttk.Checkbutton(self.root,text=self.patrones2[3],variable=self.var2, command=self.selector2, onvalue=3)
        r2.grid(row=7,column=5,padx=2,pady=2,sticky='w')
        r3=ttk.Checkbutton(self.root,text=self.patrones2[2],variable=self.var1, command=self.selector2, onvalue=2)
        r3.grid(row=7,column=6,padx=2,pady=2,sticky='w')        
        r4=ttk.Checkbutton(self.root,text=self.patrones2[4],variable=self.var3, command=self.selector2, onvalue=4)
        r4.grid(row=8,column=4,padx=2,pady=2,sticky='nw')            
        r5=ttk.Checkbutton(self.root,text=self.patrones2[5],variable=self.var4, command=self.selector2, onvalue=5)
        r5.grid(row=8,column=5,padx=2,pady=2,sticky='nw')    
        r6=ttk.Checkbutton(self.root,text=self.patrones2[6],variable=self.var5, command=self.selector2, onvalue=6)
        r6.grid(row=8,column=6,padx=2,pady=2,sticky='nw')    
        r7=ttk.Checkbutton(self.root,text=self.patrones2[7], variable=self.var6,command=self.selector2, onvalue=7)
        r7.grid(row=9,column=5,padx=2,pady=2,sticky='w')    

        self.listaChecks = [r1,r2,r3,r4,r5,r6,r7]

        self.cv1.old_coords = None
        # input_image = np.asarray(Image.open(os.path.join(self.data_path,'image1.jpg')).convert('RGB'))
        # self.coordenadasOriginales = input_image.shape
        # input_image = cv2.resize(input_image, (self.ancho,self.alto), interpolation = cv2.INTER_AREA)
        # self.imagen = input_image
        # self.cv_img = Image.fromarray(input_image)
        # # print(self.cv_img)
        # self.root.photo=ImageTk.PhotoImage(self.cv_img)
        # self.cv1.create_image(0,0, anchor = 'nw' , image=self.root.photo)



if __name__ == "__main__":
    root = tk.Tk()
    app=imageCropper(root)
    tk.mainloop()