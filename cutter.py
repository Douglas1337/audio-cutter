
'''
 Douglas Alves
 08/04/2021
 
 This program extract a fragment of a many audio files located in the same directory.
 
 This program works was only teste in Linux Operational Systems, but I think this works fine in Linux.
 
 PROBABLY YOU NEED TO INSTALL ffmpeg in our system: "pip install ffmpeg" to this program works fine!
 
'''

import os, time
from pydub import AudioSegment

def main():
    startTime=''
    endTime=''
    
    
    
    while True:
        file_type = input("Digite 1 para arquivos .mp3 e 2 para arquivos .wav \n")
        if file_type =="1" or file_type=="2":
            break
        
    directory = input("Digite o caminho do diretório aonde estão os arquivos\n")
    
    while not startTime.isnumeric():
        startTime = input("Digite o tempo de início do corte, em segundos\n") # in sec
    
    while not endTime.isnumeric():
        endTime = input("Digite o tempo de fim do corte, em segundos\n") # in sec
    
    #to milissec
    startTime = int(startTime) * 1000
    endTime = int(endTime) * 1000
    
    try:
        filetype = ".mp3" if file_type == 1 else ".wav"
        print("Tipo de arquivo:".format(filetype))
        print("Diretório especificado:{}\n".format(directory))
        
    except:
        print("Houve algum erro na busca das configurações especificadas\n")
    
    print("Iniciando....")
    time.sleep(3)
    try:    
        if file_type == "1":
            for filename in os.listdir(directory):
                # Open and extract a audio Segment
                print( directory+filename )
        
                song = AudioSegment.from_mp3( directory+filename )
                extract = song[startTime:endTime]
                #Save the song segment
                extract.export( filename, format="mp3")
                
        elif file_type == "2":
            for filename in os.listdir(directory):
                # Open and extract a audio Segment
                print( directory+filename )
        
                song = AudioSegment.from_wav( directory+filename )
                extract = song[startTime:endTime]
                #Save the song segment
                extract.export( filename, format="wav")
    except:
        print("Erro ao extrair parte do áudio")
        
if __name__ == "__main__":
    main()