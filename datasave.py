#Apenas para codificação mais simples, salva dados
class load:

    def load_int(filepath):         #retorna um int de um arquivo
        file=open(filepath,'r+')
        file_data=file.read()
        file.close()
        return int(file_data)


    def load_str(filepath):         #retorna um int de um arquivo
        file=open(filepath,'r+')
        file_data=file.read()
        file.close()
        return str(file_data)
    def load_list(filepath):         #retorna um int de um arquivo
        file=open(filepath,'r+')
        file_data=file.read()
        file.close()
        
        i=0
        newList=[]
        newString=''
        
        while i<len(file_data):
            if file_data[i]!='~':
                newString+=str((file_data[i]))
            else:
                newList.append(newString)
                newString=''
            i+=1

        
        return newList
class save:

    def save_str(filepath,var):         #Salva um STR em um arquivo
        file=open(filepath,'w')
        file.write(str(var))
        file.close()

    def save_list(filepath,var):         #Salva um STR em um arquivo
        file=open(filepath,'w')
        for i in var:
            file.write(str(i))
            file.write('~')
        file.close()





