# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'

import os

caminho = os.path.join(
    os.getcwd(), 
    "section 6 - python modules - os, datetime, sys, json, csv, selenium, pillow  and more", 
    "EXEMPLO",
)
print(caminho)

for item in os.listdir(caminho):
    print(item)
    
    if not os.path.isdir(os.path.join(caminho, item)):
        continue

    for subitem in os.listdir(os.path.join(caminho, item)):
        print("->", subitem)
