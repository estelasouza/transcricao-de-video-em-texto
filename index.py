import moviepy.editor as mp
import speech_recognition as sr
import moviepy.editor as mp
from pydub import AudioSegment
import sys

# colocar o diretório que está o seu vídeo na variável path 
path = "./exemplo.mp4" 

# convert mp4 paramp3

clip = mp.VideoFileClip(path).subclip()

# essa função irá gerar um arquivo de áudio no diretório que você está rodando o script 

clip.audio.write_audiofile("./nome_para_audio.mp3")
# r = sr.Recognizer()
src=(r"./nome_para_audio.mp3")

# convert mp3 file to wav
sound = AudioSegment.from_mp3(src)
sound.export("./portugues.wav", format="wav")

file_audio = sr.AudioFile("./portugues.wav")

# use the audio file as the audio source

r = sr.Recognizer()
with file_audio as source:
   audio_text = r.record(source)
   text = r.recognize_google(audio_text,language='pt-BR')
arq = open('transcricao.txt','w')
arq.write(text)
arq.close()
print(text)