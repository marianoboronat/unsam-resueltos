
# 11.5
class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        raise NotImplementedError()

    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        raise NotImplementedError()

# 11.6
class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()

class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))

class FormatoTablaHTML(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        # <tr>
        #   <th>Nombre</th>
        #   <th>Cajones</th>
        #   ...
        # </tr>
        
        element = "<tr>"
        for head in headers:
            text = f"<th>{head}</th>"
            element += text
        element += "</tr>"
        print(element)
        return element

    def fila(self, data_fila):
        # <tr>
        #   <td>data 1</td>
        #   <td>data 2</td>
        #   ...
        # </tr>
        element = "<tr>"
        for data in data_fila:
            text = f"<td>{data}</td>"
            element += text
        element += "</tr>"
        print(element)
        return element

# 11.7
def crear_formateador(fmt):
    """ """
    # Elige formato
    if fmt == 'txt':
        formateador = FormatoTablaTXT()
    elif fmt == 'csv':
        formateador = FormatoTablaCSV()
    elif fmt == 'html':
        formateador = FormatoTablaHTML()
    else:
        raise RuntimeError(f'Unknown format {fmt}')
    return formateador