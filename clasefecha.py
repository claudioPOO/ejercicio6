class FechaHora:
    __dia=0
    __mes=0
    __año=0
    __hora=0
    __minutos=0
    __segundos=0
    def __init__(self,d=1,mes=1,año=2020,hora=0,minutos=0,segundos=0):
        self.__dia=int(d)
        self.__mes=int(mes)
        self.__año=int(año)
        self.__hora=int(hora)
        self.__minutos=int(minutos)
        self.__segundos=int(segundos)
    def getSeg(self):
        return self.__segundos
    def getMin(self):
        return self.__minutos
    def getHora(self):
        return self.__hora
    def __add__(self,hora):
       return FechaHora(self.__dia + 0,self.__mes + 0,2020,self.__hora+hora.getHora(),self.__minutos + hora.getMin(),self.__segundos+ hora.getSeg())        
    def __sub__(self,hora):
        return FechaHora(self.__dia + 0,self.__mes + 0,self.__año + 0,self.__hora-hora.getHora(),self.__minutos - hora.getMin(),self.__segundos - hora.getSeg())
    def aSeg(self):
        self.__segundos=self.__segundos + 60
        self.__minutos=self.__minutos - 1
    def aMin(self):
        self.__minutos= self.__minutos + 60
        self=__hora= self.__hora -1
    def __str__(self):
        return ('DIA   MES  AÑO \n' 
                '{}    {}   {} \n'
                '{}hs:{}min:{}seg'.format(self.__dia,self.__mes,self.__año,self.__hora,self.__minutos,self.__segundos))                     
    def __gt__(self,hora):
        if(self.__hora==hora.getHora()):
            if(self.__minutos>hora.getMin()):
                return 1
            else:
                return 0
        if(self.__hora>hora.getHora()):
                return 1
        else:
                return 2
    def acomodar(self):
            if self.__segundos > 60:
                self.__segundos=self.__segundos-60
                self__minutos=self.__minutos+1
            if self.__minutos > 60:
                self.__minutos=self.__minutos-60
                self.__hora=self.__hora+1
            if self.__hora>24:
                
                self.__hora=self.__hora-24
                self.__dia=self.__dia+1
            if(self.__mes==4)or(self.__mes==6)or (self.__mes==9)or (self.__mes==11):
               if(self.__dia>30):
                   self.__dia=self.__dia-30
                   self.__mes=self.__mes+1
            else:
                if(self.__mes==1)or (self.__mes==3)or (self.__mes==5)or (self.__mes==7)or (self.__mes==8)or (self.__mes==10)or (self.__mes==12):
                    if(self.__dia>31):
                        self.__dia=self.__dia - 31
                        self.__mes=self.__mes+1
            
            if(self.__mes==2):
                if(self.__año%100==0):
                    if(self.__añ0%400==0):
                        if(self.__dia>29):
                            self.__mes=self.__mes+1
                            self.__dia=self.__dia - 29
                            
                    else:
                        if(self.__año%4==0):
                            if(self.__dia>29):
                                self.__mes=self.__mes+1
                                self.__dia=self.__dia - 29
                        else:
                            if(self.__dia>28):
                                self.__mes=self.__mes+1
                                self.__dia=self.__dia - 28
            if(self.__mes>12):
                self.__mes=self.__mes-12
                self.__año=self.__año+1
    def acomodaR(self):
        if(self.__mes==1):
               if(self.__dia==1):
                    if(self.__hora<0):
                        self.__año=self.__año - 1
                        self.__dia=31
                        self.__mes=self.__mes + 11
                
        if(self.__hora<0):
            self.__hora=self.__hora + 24
            self.__dia=self.__dia - 1
        if(self.__dia<1):
            self.__mes=self.__mes - 1
            if(self.__mes==4)or(self.__mes==6)or (self.__mes==9)or (self.__mes==11):
                self.__dia=30
            else:
                if(self.__mes==1)or (self.__mes==3)or (self.__mes==5)or (self.__mes==7)or (self.__mes==8)or (self.__mes==10)or (self.__mes==12):
                    self.__dia=31
             
