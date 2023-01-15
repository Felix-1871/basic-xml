import xml.etree.ElementTree as ET
from lxml import etree

# parse the XML file
tree = etree.parse('data.xml')
root = tree.getroot()

def _create():
    # create new elements
    new_person = etree.Element("person")

    firstName = etree.SubElement(new_person, "firstName")
    firstName.text = input("Value for field Name: ")

    lastName = etree.SubElement(new_person, "lastName")
    lastName.text = input("Value for the field Surname: ")

    age = etree.SubElement(new_person, "age")
    age.text = input("Value for the field Age: ")

    # add new element to the root element
    root.append(new_person)

    # write the modified XML to the file
    tree.write("data.xml")
    print('Correctly created element')

def _read():
    #defining values
   firstName = root.xpath('//firstName')
   lastName = root.xpath('//lastName')
   age = root.xpath('//age')

   blabla = input('What value do you want to read? ')
   number = input('From which position do you want to read value? ')      

   match blabla:
        case 'firstName':
         print(firstName[int(number)].text) 
        case 'lastName':
            print(lastName[int(number)].text) 
        case 'age':
            print(age[int(number)].text) 
        case 'all':
         print(firstName[int(number)].text) 
         print(lastName[int(number)].text) 
         print(age[int(number)].text) 
        case _:
            print('Unknown value')

def _update():
    
        element_name = input('What element do you want to update? ')
        if (element_name == "firstName" or element_name == "lastName" or element_name == "age"):
            number = input('Which position do you want to update? ')
           
           # concatenating every input to create selection for xpath
            xpath_expression = '//person' + '[' + int(number) + ']/' + element_name

            selectedElement = root.xpath(xpath_expression)
            selectedElement[0].text = input('Enter new value: ')
           # writing to file
            tree.write("data.xml")
        else:
            print("Unknown element")

def _delete():
   firstName = root.xpath('//firstName')
   lastName = root.xpath('//lastName')
   age = root.xpath('//age')
   number = input('Which row do you want to delete? ')
   xpath_expression = '//person[' + number +']' 
   person = root.xpath(xpath_expression)
   print( 'You want to delete' + ' ' + firstName[int(number) -1].text + ' ' + lastName[int(number) -1].text + ' ' + 'aged ' + age[int(number) -1].text)
   sure = input('Are you sure? (y/n) ')
   
   if(sure == 'y'):
    person[0].getparent().remove(person[0])
    tree.write("data.xml")
    print('Delete action complete')
   else:
    print('Delete action cancelled')


def start():
    derp = input('What action do you want to take? ')
    match derp:
        case 'update':
            _update()
        case 'create':
            _create()
        case 'read':
            _read()
        case 'delete':
            _delete()
        case _:
            print('Unknown command')

start()