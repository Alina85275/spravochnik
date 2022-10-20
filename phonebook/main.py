from file_reading import reading_scv, reading_xml, reading_json
from file_creating import writing_scv, writing_xml, writing_json
n = input('Введите тип файла действия(импорт/экспорт):')
k = input('Введите тип файла (csv/xml/json):')
if k == 'csv' and n == 'импорт':
    reading_scv()
elif k == 'xml' and n == 'импорт':
    reading_xml()
elif k == 'json' and n == 'импорт':
    reading_json()
if k == 'csv' and n == 'экспорт':
    writing_scv()
if k == 'xml' and n == 'экспорт':
    writing_xml()
if k == 'json' and n == 'экспорт':
    writing_json()



