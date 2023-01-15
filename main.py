import xml.etree.ElementTree as ET
from lxml import etree

# parse the XML file
tree = etree.parse('data.xml')
root = tree.getroot()



def _create():
    # create new elements
    new_person = etree.Element("person")
    firstName = etree.SubElement(new_person, "firstName")
    firstName.text = input("Podaj imie: ")
    lastName = etree.SubElement(new_person, "lastName")
    lastName.text = input("Podaj nazwisko: ")
    age = etree.SubElement(new_person, "age")
    age.text = input("Podaj wiek: ")

    # add new element to the root element
    root.append(new_person)

    # write the modified XML to the file
    tree.write("data.xml")
    print('poprawnie stworzono element :)')

def _read():
    blabla = input('Co chcesz odczytać? ')
    match blabla:
        case 'firstName':
         number = input('Z ktorej pozycji chcesz odczytac dane? ')
         firstName = root.xpath('//firstName')
         print(firstName[number].text) 
        case 'lastName':
            number = input('Z ktorej pozycji chcesz odczytac dane? ')
            lastName = root.xpath('//lastName')
            print(lastName[number].text) 
        case 'age':
            number = input('Z ktorej pozycji chcesz odczytac dane? ')
            age = root.xpath('//age')
            print(age[number].text) 

def _update():
    #update element
    print('tu bedzie update')
def _delete():
    #delete element

    print('tu bedzie delete')

derp = input('Co chcesz zrobić? ')
match derp:
    case 'update':
        _update
    case 'create':
        _create
    case 'read':
        _read
    case 'delete':
        _delete
    case _:
        print('Nieznana komenda, spróbuj jeszcze raz')