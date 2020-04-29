from clasefecha import FechaHora

def  opcion1 (f1):
   h2=int(input('Hora para sumar '))
   m2=int(input('Minutos '))
   s2=int(input('segundos '))   
   f2=FechaHora(0,0,0,h2,m2,s2)
   suma=f1+f2
   suma.acomodar()#Acomoda dia,mes y año en caso q supere las 24 hs#
   print('{}'.format(suma))
   
def  opcion2 (f1):
   h2=int(input('Hora para restar '))
   m2=int(input('Minutos '))
   s2=int(input('segundos '))   
   f2=FechaHora(0,0,0,h2,m2,s2)
   if(f2.getSeg()>f1.getSeg()):
       f1.aSeg()#le suma 60 a los segundos y le resta 1 a los minutos#
   if(f2.getMin()>f1.getMin()):#le suma 60 a los minutos y le resta 1 a la hora#
       f1.aMin()
   resta=f1-f2
   resta.acomodaR()
   print(resta)
def opcion3(f1):
   h2=int(input('Hora para comparar '))
   m2=int(input('Minutos '))
   s2=int(input('segundos '))   
   f2=FechaHora(0,0,0,h2,m2,s2)
   comp=f1>f2
   if(comp==1):
       print('La hora ingresada es menor')
   else:
       print('La hora ingresada es mayor a la primera')
switcher = {
    1 : opcion1,
    2 : opcion2,
    3 : opcion3,
}

def switch (argumento,f1):
    func  =  switcher.get ( argumento , lambda : print ( "Opción incorrecta" ))
    func (f1)
if __name__ == '__main__':
    d=int(input("Ingrese Dia: "))
    mes=int(input("Ingrese Mes: "))
    a=int(input("Ingrese Año: "))
    h=int(input("Ingrese Hora: "))
    m=int(input("Ingrese Minutos: "))
    s=int(input("Ingrese Segundos: "))
    f1=FechaHora(d,mes,a,h,m,s)
    bandera='falso'
    while bandera=='falso':
        print( '')
        print ( "      Menu" )
        print ( " 1 Sumar Hora" )
        print ( " 2 Restar Hora" )
        print ('  3 Mayor hora ')
        opcion =  int ( input ( "Ingrese una opción:" ))
        switch ( opcion,f1)
        op=(input('Desea Continuar? '))
        if(op=='no'):
            bandera='verdadero'
            print( "Adiós" )
    
    
