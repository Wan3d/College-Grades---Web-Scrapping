nuevaMateria = [' AEC1034  Fundamentos de Telecomunicaciones  JESUS DE LEON MARTINEZ ', '6A ', '81', '85', '100', 'None', 'None', 'None', 'None', 'None', 'None', '20', '81', 
                ' SCC1010  Graficación  MIGUEL ANGEL GUZMAN RIVERA ', '6V ', '72', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 
                ' SCD1016  Lenguajes y Automatas II  GUILLERMO FERNANDEZ ROMERO ', '6A ', '100', '85', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 
                ' SCD1022  Simulación  MARIBEL OCAMPO CASADOS ', '6A ', '86', '70', '75', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 
                ' AEC1061  Sistemas Operativos  JULIO CESAR MENDOZA CONTRERAS ', '6A ', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', ' SCC1023  Sistemas Programables  JOSE LUIS CAMARGO RICO ', '6V ', '97', '80', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']

viejaMateria = [' AEC1034  Fundamentos de Telecomunicaciones  JESUS DE LEON MARTINEZ ', '6A ', '81', '85', 'None', 'None', 'None', 'None', 'None', 'None', 'None', '20', '81', 
                ' SCC1010  Graficación  MIGUEL ANGEL GUZMAN RIVERA ', '6V ', '72', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 
                ' SCD1016  Lenguajes y Automatas II  GUILLERMO FERNANDEZ ROMERO ', '6A ', '100', '85', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 
                ' SCD1022  Simulación  MARIBEL OCAMPO CASADOS ', '6A ', '86', '70', '75', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 
                ' AEC1061  Sistemas Operativos  JULIO CESAR MENDOZA CONTRERAS ', '6A ', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', ' SCC1023  Sistemas Programables  JOSE LUIS CAMARGO RICO ', '6V ', '97', '80', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']

idSubject = {
        "AEC1034": "Fundamentos de Telecomunicaciones",
        "SCC1010": "Graficación",
        "SCD1016": "Lenguajes y Automátas 2",
        "SCD1022": "Simulación",
        "AEC1061": "Sistemas Operativos",
        "SCC1023": "Sistemas Programables",
        "ACD0908": "Desarrollo Sustentable",
        "AEF1031": "Fundamentos de Bases de Datos",
        "LED1904": "Lengua Extranjera IV",
        "SCC1019": "Programación Lógica y Funcional",
        "SCD1021": "Redes de Computadoras",
        "ACA0909": "Taller de Investigación I",
        "SCA1026": "Taller de Sistemas Operativos"
    }

for i in range(0, len(nuevaMateria), 13):
    word = nuevaMateria[i]
    nuevaMateria[i] = idSubject[word[1:8]]

for i in range(0, len(viejaMateria), 13):
    word = viejaMateria[i]
    viejaMateria[i] = idSubject[word[1:8]]

# Creamos los datos que usaremos para nuestro diccionario
plainList = nuevaMateria
dictionaryGrades = {}
gradesBlock = 13

# Iteramos de 13 en 13, ya que principalmente buscaremos los nombres de la materia
# que se repiten cada 13 índices
for i in range(0, len(plainList), gradesBlock):
    # Del bloque de la materia, se extraen 13 columnas de esa materia en específico
    subjectBlock = plainList[i : i + 13]

    # Se identifica el nombre de la materia
    subjectKey = subjectBlock[0]

    # Agarramos el bloque de calificaciones dentro de la materia
    gradesBlock = subjectBlock[2:]

    # En un diccionario, guardamos las calificaciones asociadas al nombre de la materia
    dictionaryGrades[subjectKey] = gradesBlock

plainList2 = viejaMateria
dictionaryGrades2 = {}
gradesBlock2 = 13

for i in range(0, len(plainList2), gradesBlock2):
    subjectBlock2 = plainList2[i : i + 13]
    subjectKey2 = subjectBlock2[0]
    gradesBlock2 = subjectBlock2[2:]
    dictionaryGrades2[subjectKey2] = gradesBlock2
    
for subject, newGrade in dictionaryGrades.items():
    if subject in dictionaryGrades2:
        oldGrade = dictionaryGrades2[subject]

        for j, (old, new) in enumerate(zip(oldGrade, newGrade)):
            if old != new:
                print(f"{subject} (Unidad {j}): {new}")
    
