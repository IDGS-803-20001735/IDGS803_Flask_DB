from db import get_connection

try:
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call get_estudents()')
        resulset = cursor.fetchall()
        for row in resulset:
            print(row)
    connection.close()

except Exception as ex:
    print(ex)
print('----------------------------------------------------------------')
try:
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call alumno(%s)',(2,))
        resulset = cursor.fetchall()
        for row in resulset:
            print(row)
    connection.close()

except Exception as ex:
    print(ex)
print('----------------------------------------------------------------')
try:
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call save_estudent(%s,%s,%s)',('Cristian Hassel', 'Almaguer', 'Valdez'))
    
    connection.commit()
    connection.close()

except Exception as ex:
    print(ex)