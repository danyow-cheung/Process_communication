file_path = 'history.txt'
file = open(file_path,'r',encoding='utf-8')

while True:    
    for line in file:
        line = line.strip()  
        print('cur lien',line)

