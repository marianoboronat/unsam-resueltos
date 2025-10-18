# hipoteca.py
# alumno: mariano boronat

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

mes = 0
pago_extra_mes_comienzo = 2
pago_extra_mes_fin = 260
pago_extra = 4000

while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    mes += 1

    #condicional para que incremente el pago total y decremente el saldo

    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        total_pagado += pago_extra
        saldo -= pago_extra

    print('Mes: ', mes," / Total Pagado: ", round(total_pagado, 2), " / saldo: ",saldo)
    

