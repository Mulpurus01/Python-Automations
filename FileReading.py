with open(r"\path\where\the\file\exist\name.txt\",'r',encoding='ISO-8859-1') as readFile:
          for linein in readFile:
            #Perform the logic you want, after that copying that line to new file
            with open(r"\path\where\the\file\exist\new\name.txt\",'a',encoding='ISO-8859-1') as writeFile:
                      writeFile.write(line)
print('All the operations are completed')
