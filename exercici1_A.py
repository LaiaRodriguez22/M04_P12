'''
Una funcio que retorni un XML (crear arxiu .xml i mostrar per consola l’XML). La funció ha de crear l’XML,
crear les etiquetes i inserir text segons les especificacions del document adjuntat.
'''

import xml.etree.ElementTree as ET

def creaXML():

    #ROOT TREE -- STUDENTS
    root = ET.Element('students')

    #CHILDS -- STUDENT 1
    childStudents = ET.SubElement(root, 'student 1')
    #POSEM LA COMUNITAT AUTONOMA DE CADA PERSONA
    element = root[0]
    element.set('Comunitat Autonoma','Islas Canarias')
    #SUBCHILDS -- SUBELEMENT DE CHILDS
        #SUBCHILD 1
    subchildStudent = ET.SubElement(childStudents, 'name')
    subchildStudent.text = "Juan Daniel"
    subchildStudent = ET.SubElement(childStudents, 'surname')
    subchildStudent.text = "Aguilar "
    subchildStudent = ET.SubElement(childStudents, 'email')
    subchildStudent.text = "machokke@gmail.com"
    subchildStudent = ET.SubElement(childStudents, 'DNI')
    subchildStudent.text = "56781234A"

    #CHILDS -- STUDENT 2
    childStudents = ET.SubElement(root, 'student 2')
    # POSEM LA COMUNITAT AUTONOMA DE CADA PERSONA
    element = root[1]
    element.set('Comunitat Autonoma', 'Catalunya')
    #SUBCHILDS -- SUBELEMENT DE CHILDS
        #SUBCHILD 2
    subchildStudent = ET.SubElement(childStudents, 'name')
    subchildStudent.text = "Marina"
    subchildStudent = ET.SubElement(childStudents, 'surname')
    subchildStudent.text = "Rodríguez"
    subchildStudent = ET.SubElement(childStudents, 'email')
    subchildStudent.text = "pekerodri90@gmail.com"
    subchildStudent = ET.SubElement(childStudents, 'DNI')
    subchildStudent.text = "12345678Z"


    #CHILDS -- STUDENT 5
    childStudents = ET.SubElement(root, 'student 3')
    # POSEM LA COMUNITAT AUTONOMA DE CADA PERSONA
    element = root[2]
    element.set('Comunitat Autonoma', 'Extremadura')
    #SUBCHILDS -- SUBELEMENT DE CHILDS
        #SUBCHILD 3
    subchildStudent = ET.SubElement(childStudents, 'name')
    subchildStudent.text = "Laia"
    subchildStudent = ET.SubElement(childStudents, 'surname')
    subchildStudent.text = "Rodríguez"
    subchildStudent = ET.SubElement(childStudents, 'email')
    subchildStudent.text = "lrodrigu22@balmes.net"
    subchildStudent = ET.SubElement(childStudents, 'DNI')
    subchildStudent.text = "42345678W"


    #CHILDS -- STUDENT
    childStudents = ET.SubElement(root, 'student 4')
    # POSEM LA COMUNITAT AUTONOMA DE CADA PERSONA
    element = root[3]
    element.set('Comunitat Autonoma', 'Andalucia')
    #SUBCHILDS -- SUBELEMENT DE CHILDS
        #SUBCHILD 4
    subchildStudent = ET.SubElement(childStudents, 'name')
    subchildStudent.text = "Joaquín Javier"
    subchildStudent = ET.SubElement(childStudents, 'surname')
    subchildStudent.text = "Rodríguez"
    subchildStudent = ET.SubElement(childStudents, 'email')
    subchildStudent.text = "joaquimpintor@gmail.com"
    subchildStudent = ET.SubElement(childStudents, 'DNI')
    subchildStudent.text = "43216249W"


    #CHILDS -- STUDENT 5
    childStudents = ET.SubElement(root, 'student 5')
    # POSEM LA COMUNITAT AUTONOMA DE CADA PERSONA
    element = root[4]
    element.set('Comunitat Autonoma', 'Pixapilandia')
    #SUBCHILDS -- SUBELEMENT DE CHILDS
        #SUBCHILD 5
    subchildStudent = ET.SubElement(childStudents, 'name')
    subchildStudent.text = "Alex"
    subchildStudent = ET.SubElement(childStudents, 'surname')
    subchildStudent.text = "Navarro"
    subchildStudent = ET.SubElement(childStudents, 'email')
    subchildStudent.text = "anavarr22@balmes.net"
    subchildStudent = ET.SubElement(childStudents, 'DNI')
    subchildStudent.text = "63456789B"

    #TABULO AQUEST XML
    ET.indent(root)

    #GUADO AQUEST XML
    tree = ET.ElementTree(root)
    tree.write("exercici1XML_A.xml")

    #MOSTRAR PER CONSOLA
    return ET.dump(root)