from iqoptionapi.stable_api import IQ_Option
import time
import yfinance as yf
import os

#bienvenida

def bienvenida():
    print("")
    print("Bienvenido a AutoTrading sys")
    print("Pedro Soler 23-EIEN-1-027")
    print("")
    print("-----------------------------")

#obtencion del precio de mercado
def getdata(): 
    data=yf.download(tickers = 'EURUSD=X',period='20',interval='1m')	
    v1= data.iloc[0,1]
    v2= data.iloc[1,1]
    v3= data.iloc[2,1]
    v4= data.iloc[3,1]
    v5= data.iloc[4,1]
          
    v6= data.iloc[5,1]
    v7= data.iloc[6,1]
    v8= data.iloc[7,1]
    v9= data.iloc[8,1]
    v10= data.iloc[9,1]
           
    v11= data.iloc[10,1]
    v12= data.iloc[11,1]
    v13= data.iloc[12,1]
    v14= data.iloc[13,1]
    v15= data.iloc[14,1]
            
    v16= data.iloc[15,1]
    v17= data.iloc[16,1]
    v18= data.iloc[17,1]
    v19= data.iloc[18,1]
    v20= data.iloc[19,1]
    SMA= ((v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12+v13+v14+v15+v16+v17+v18+v19+v20)/20)
    return (SMA,v20)


#loguin
while True:
    os.system ("cls")
    bienvenida()
    print("")
    usuario = str(input("Ingreses su usuario, press enter:"))
    print("")
    contraseña = str(input("Ingreses su contraseña, press enter:"))
    print("")
    time.sleep(1) 

        
    API = IQ_Option(usuario,contraseña)
    API.connect()
    API.change_balance('PRACTICE')  #PRACTICE / REAL
    time.sleep(1)
    if API.check_connect() == False:
        print('Error al conectar')
    else:
        print('conectado con exito')
        print("cargando...")
        time.sleep(10)
        os.system ("cls")
        break 

#obtencion del precio
(SMA,v20) = getdata()
 
 
#estrategia de trading
while True:
    bienvenida()
    print("")
    print("Seleccione su estrategia de trading")
    print("TYPE '1' para SMA a 1 MIN")
    print("TYPE '2' para SMA a 2 MIN")
    print("TYPE '3' para SMA a 3 MIN")
    print("")
    tiempo = input()

    if tiempo == "1":
        timeframe = 1
        os.system ("cls")
        break
    if tiempo == "2":
        timeframe = 2
        os.system ("cls")
        break
    if tiempo == "3":
        timeframe = 3
        os.system ("cls")
        break
    else:
        os.system ("cls")
        print("Valor invalido")
        continue
   
time.sleep(2)
bienvenida()
print("")
entrada = int(input("Ingrese un monto entre 10 USD y 10,000 USD,   press enter:"))
print("")
os.system ("cls")

#direccion de compra
while True:
    bienvenida()
    print("Ingrese la direccion de su compra")
    print("1- Call")
    print("2- Put")
    print("")
    value = input()
    if value == "1":
        direccion = 'call'
        os.system ("cls")
        break
    if value == "2":
        direccion = 'put'
        os.system ("cls")
        break
    else:
        os.system ("cls")
        print("valor incorrecto")
        continue



#trading...
bienvenida()
print ("")
print("Iniciando...     Las entradas se realizan en el par EUR/USD")
print("Press ctrl+c para cerrar.")
time.sleep(10)
par = 'EURUSD'
print("Usuario:",usuario)
print("par:", par)
print("Direccion:",direccion)
print("timeframe:",timeframe)
print("entrada:", entrada)
print("")
print("----------------------")
while True:
    time.sleep(2)
    status,id = API.buy(entrada,par,direccion,timeframe)
    print("MEDIA MOVIL:",SMA)
    print("valor del precio:", v20)
    print("Nueva compra")
    time.sleep(timeframe*60)