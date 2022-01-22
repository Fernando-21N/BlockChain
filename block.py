import os

ID_reserva= []
ID_tren= []
origen= []
destino= []
hora_salida= []
min_salida= []
hora_llegada = []
min_llegada= []

os.system ("cls")

def graba_BlockChain(ID_reserva,ID_tren,origen,destino,hora_salida,min_salida,hora_llegada,min_llegada,duracion):
    print("INFORMACIÓN DE RESERVA:")
    print("\nId de Reserva: ", ID_reserva)
    print("Id Tren: ", ID_tren)
    print("Ciudad de Origen: ", origen)
    print("Ciudad de Destino: ", destino)
    print("\nHora de Salida del Tren: ", hora_salida, ":", min_salida)
    print("Hora programada de llegada del tren: ", hora_llegada, ":", min_llegada)


ID_reserva.append(input("Introduzca id de su reserva: "))
ID_tren.append(input("Introduzca id del tren: "))
origen.append(input("Introduzca ciudad de origen: "))
destino.append(input("Introduzca ciudad de destino: "))
hora_salida = int(input("Ingrese hora de salida: "))
min_salida = int(input("Ingrese minuto de salida: "))
duracion = int(input("Duración del trayecto: "))
hora_llegada = int(input("Ingrese hora de llegada programada: "))
min_llegada = int(input("Ingrese minuto de llegada programada: "))



os.system ("cls")
    
graba_BlockChain(ID_reserva,ID_tren,origen,destino,hora_salida,min_salida,hora_llegada,min_llegada,duracion)


def ObtenBlockChain(hora_salida,min_salida,hora_llegada,min_llegada,duracion):
    min = min_salida + duracion
    hora = hora_salida + min // 60
    min = min % 60
    hora = hora % 24
    
    print("Hora de llegada a la estación: ",hora, ":", min)

    if min > min_llegada:
        print("\nTiene acceso a un Reembolso de tu billete")
    elif min_llegada >= min:
        print("\nGracias por su viaje")
    else:
        print("\nPongase en contacto con la compañia.")


ObtenBlockChain(hora_salida,min_salida,hora_llegada,min_llegada,duracion)