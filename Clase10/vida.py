# alumno boronat mariano
from datetime import datetime, date, timedelta

# %%
# 10.1
def vida_en_segundos(fecha_nac):
    """devuelve la cantidad de segundos que viviste 
    (asumiendo que naciste a las 00:00hs de tu fecha de nacimiento),
    La función debe tomar como entrada una cadena en formato 'dd/mm/AAAA'"""

    fecha_nac = datetime.strptime(fecha_nac, "%d/%m/%Y")
    fecha_hoy = datetime.today()
    diferencia = fecha_hoy - fecha_nac

    
    if fecha_nac.month == fecha_hoy.month and fecha_nac.day == fecha_hoy.day:
        print("¡feliz cumple! c:")

    print(f"tenés {round(diferencia.total_seconds(),2)} segundos de vida")



# %%
# 10.2
def dias_para_la_primavera():
    """indica la cantidad de dias que faltan para la proxima primavera"""
    # primicia
    fecha_hoy = datetime.today()
    # fecha_hoy = datetime.strptime("21/09/2025", "%d/%m/%Y")

    # definimos el dia dela primavera
    fecha_primavera = f"21/09/{fecha_hoy.year}"
    fecha_primavera = datetime.strptime(fecha_primavera, "%d/%m/%Y")
    
    # si la fecha es anterior al dia de la primavera del AÑO ACTUAL
    if fecha_primavera > fecha_hoy:
        diferencia = fecha_primavera - fecha_hoy
        print(f"faltan {diferencia.days} dias para la primavera")

    elif fecha_primavera == fecha_hoy:
        print("¡feliz primavera!")

    # en cambio si se sigue en el año actual pero ya paso la primavera
    # se debe calcular los dias para la primavera del año siguiente.
    else:
        fecha_primavera = f"21/09/{fecha_hoy.year + 1}" #se suma el año actual
        fecha_primavera = datetime.strptime(fecha_primavera, "%d/%m/%Y")
        diferencia = fecha_primavera - fecha_hoy
        print(f"faltan {diferencia.days} dias para la primavera")

# %%
# 10.3
def fecha_de_reincorporación(fecha_xaternidad):
    """devuelve una fecha 200 dias despues de la fecha_xaternidad"""
    fecha_xaternidad = datetime.strptime(fecha_xaternidad, "%d/%m/%Y")
    fecha_regreso = fecha_xaternidad + timedelta(days = 200)
    
    print(fecha_regreso)


if __name__ =="__main__":
    # 10.1
    vida_en_segundos("21/06/1995")

    # 10.2
    dias_para_la_primavera()
    
    # 10.3
    fecha_de_reincorporación("03/06/2025")