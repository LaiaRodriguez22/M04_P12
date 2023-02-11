import json

"Función que guarda el contenido en un archivo .json"
def creaJSON():
    book = """
    {
        "book":[
            {"title": "Geronimo Stilton 1",
            "cover": "hard cover",
            "year":"2008",
            "pages":"220"
            }
            {"title": "Geronimo Stilton y el reino de fantasía",
            "cover": "soft cover",
            "year":"2009",
            "pages":"150"
            }
            {"title": "Geronimo Stilton y los cielos de chuches",
            "cover": "hard cover",
            "year":"2012",
            "pages":"190"
            }
            {"title": "Geronimo Stilton en los reinos de fantasía - Precuela",
            "cover": "soft cover",
            "year":"2014",
            "pages":"208"
            }
           ]
    }
    
    """
    """
    Con open() indicamos el archivo que queremos abrir (en este caso crear porque no existe)
    y indicamos 'w' para que sea apto de escritura.
    Y con json.dump() le indicamos qué información (book), queremos pasarle al archivo creado (file).
    """
    with open("book.json",'w') as file:
        json.dump(book,file)
    
"""
En este caso, esta función nos permite leer el archivo .json, con (open) indicamos que abra el archivo en formato read 'r', y con el método load(),
se puede imprimir TODA la información del archivo creado anteriormente.
"""
def leeJSON():
    with open("book.json",'r') as file:
        result = json.load(file)
        print (result)