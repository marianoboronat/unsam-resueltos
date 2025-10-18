# alumno boronat mariano
from datetime import datetime, date

hoy = date.today()


# Así podés obtener el año, el mes, el día y el día de la semana:
print('Año actual:', hoy.year)
print('Mes actual:', hoy.month)
print('Día actual:', hoy.day)
print('Día de la semana:', hoy.weekday()) # va de 0 a 6 empezando en lunes


# Un objeto timedelta representa una duración, es decir, la diferencia entre dos instantes de tiempo.
t1 = date(year = 2021, month = 4, day = 21)
t2 = date(year = 2020, month = 8, day = 23)
t3 = t1 - t2
print(t3)

t4 = datetime(year = 2020, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2021, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print(t6)
print('tipo de t3 =', type(t3))
print('tipo de t6 =', type(t6))