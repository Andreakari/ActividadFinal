lista1=[]
nombre=(input("ingrese el nombre del alumno:     "))
lista1.append(nombre)
lista2=[]
print("        ingresaremos 4 notas de cada alumno       ")
nota1=float(input("ingrese primera nota del alumno:     "))
nota2=float(input("ingrese segunda nota de alumnos:     "))
nota3=float(input("ingrese terecer nota del alumno:     "))
nota4=float(input("ingrese la cuarta nota edl alumno:    "))
lista2.append(nota1)
ingreso=(input("desea ingresar nuevo alumno? s/n: "))
menu=0
contador=(nota1,nota2,nota3,nota4)

promedionotas=(nota1+nota2+nota3+nota4)
while ingreso == "s" or ingreso== "S":
        nombre=(input("ingrese un nombre:  "))  
        lista1.append(nombre)
        nota1=float(input("ingrese las notas del alumno:     "))
        nota2=float(input("ingrese segunda nota de alumnos:     "))
        nota3=float(input("ingrese terecer nota del alumno:     "))
        nota4=float(input("ingrese la cuarta nota edl alumno:    "))

        
        ingreso=(input("desea ingresar nuevo alumno? s/n: "))
        
                            
else:
                    
                   
 menu=int(input(" 1 ordenar alfabeticamente\n 2 nota alfabetica por nota\n 3 promedio de notas\n 4 nota media de alumnos\n 5 media de alumnos aprobados\n 6 media alumnos desaprobados \n 7 salir  :   " ))
if menu==1:
                lista1.sort()
                print(lista1)
                
elif menu == 2:
        lista2.append(contador)
        for i in [lista1]:
                for j in [lista2]:
        ##lista1.sort()
                        print (lista1,lista2)
elif menu ==3:
        promedio=promedionotas/4
        print("su proemedio es de :   ", promedio)

        
##promedio de todos los alumno
elif menu==4:
                for i in [lista1]:
                        for j in [lista2]:
                                                               
                                promedio=sum(lista2)/len(lista2)
                                print(lista1, "EL PROMEDIO DE LOS ALUMNOS ES :   ",promedio)
elif menu==5:
         for i in [lista1]:
                        for j in [lista2]:
                                promedio=sum(lista2)/len(lista2)
                                if promedio >=7 :
                                        print("aprobados con promedio de:" ,  promedio)
elif menu==6:
                 promedio1=sum(lista2)/len(lista2)
                 print( "promedio de notas es :   ", promedio1)
elif menu==7:
        
        exit
        print("salir del programa")
        


        
        


                
        
                        


        
       
