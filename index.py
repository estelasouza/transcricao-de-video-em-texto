import moviepy.editor as mp
import speech_recognition as sr
import moviepy.editor as mp
from pydub import AudioSegment
from pydub.utils import make_chunks
import sys

# colocar o diretório que está o seu vídeo na variável path 
path = "./exemplo.mp4" 

# convert mp4 paramp3

clip = mp.VideoFileClip(path).subclip()

# essa função irá gerar um arquivo de áudio no diretório que você está rodando o script 
clip.audio.write_audiofile("./audio.mp3")


audio = AudioSegment.from_file("audio.mp3", "mp3")

size = 180000 # o milisegundo para cortar o audio no maximo 3 min

chunks = make_chunks(audio, size) # Corte o arquivo em pedaços de 10s

for i, chunk in enumerate(chunks):
   # Enumeration, i is the index, chunk is the cut file
   # convert mp3 file to wav
   chunk_name = "audio{0}.wav".format(i)
   # save document
   chunk.export(chunk_name, format="wav")
   file_audio = sr.AudioFile("./" + chunk_name)
   
   # use the audio file as the audio source
   r = sr.Recognizer()
   with file_audio as source:
      audio_text = r.record(source)
      text = r.recognize_google(audio_text,language='pt-BR')

   arq = open(chunk_name.replace('.wav', '') + '.txt','w')
   arq.write(text)
   arq.close()
   print(text)
