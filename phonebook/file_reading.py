from user_interface import get_info 

def reading_scv():
    with open('Spravochnik.csv', 'r') as fp:
        print(fp.read())
        

def reading_xml():
    with open('Spravochnik.xml', 'r') as fp:
        print(fp.read())

def reading_json():
    with open('Spravochnik.json', 'r') as fp:
        print(fp.read())