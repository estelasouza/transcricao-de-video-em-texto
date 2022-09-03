## Transcrição de vídeos 
Esse é um script para converter arquivos de video em txt.
Tutorial 1: [Python para transcrição de audio e vídeo](https://mecls.medium.com/usando-python-para-transcri%C3%A7%C3%A3o-de-%C3%A1udio-e-v%C3%ADdeos-em-portugu%C3%AAs-4f40a12aaf93 ) 

Tutorial 2: [Python para cortar audio](https://blog.karatos.in/a?ID=01550-00e4160f-9685-4857-a21e-28e4fdca6dad)


Usando Python para transcrição de áudio e vídeos em português
Eu acredito muito que temos que dar acesso a todos na internet, um dos meios de se fazer isso é pela transcrição de nossos áudios e vídeos. Todos os conteúdos que faço que tenham imagem, áudio e vídeo eu procuro torná-lo acessível, existem diversas ferramentas que nos ajudam nisso!

Só que esses dias decidi aprender a fazer isso com Python! E deu super certo, a maioria dos videos vieram sem erros no reconhecimento das palavras (sempre tenho problemas com isso ) e o melhor, foi bem fácil de fazer isso com as bibliotecas que existem em Python!

Por isso, decidi compartilhar aqui ! Então vamos de passo a passo para criação desse script !

Instale as libs : SpeechRecognition, moviepy, pydub
```
pip install SpeechRecognition
pip install moviepy
pip install pydub
```
obs. caso você esteja rodando na sua maquina, pode dar erro e você precise instalar esse pacote ffmpef, basta instalar:

`sudo apt install ffmpeg`


2. Crie um arquivo index.py e importe as bibliotecas :
```
import moviepy.editor as mp
import speech_recognition as sr
import moviepy.editor as mp
import sys
from pydub import AudioSegment
```

Após isso o que você precisará fazer é transformar seu vídeo (ele deve estar no formato .mp4) em áudio (.mp3)

3. Transformar o vídeo em áudio :

Eu recomendo que você coloque o vídeo que você vai transcrever na pasta que está localizado o seu arquivo index.py

#a variável path contem o nome do arquivo do seu vídeo
`path = “nome_do_arquivo.mp4”`

#converter de mp4 para mp3
```
clip = mp.VideoFileClip(path).subclip()
clip.audio.write_audiofile("./nome_para_audio.mp3")
```
Após criarmos o arquivo .mp3 devemos transforma-lo em um arquivo .wav, que é nesse formato que iremos gerar a transcrição

`src=(r"./nome_para_audio.mp3")`
# converter de mp3 para wav
```
sound = AudioSegment.from_mp3(src)
sound.export("./nome_arquivo.wav", format="wav")
file_audio = sr.AudioFile(r"./nome_arquivo.wav")
```

3. Hora de fazer a transcrição

Importando a classe Recognizer() poderemos fazer essa transcrição!

Ps. Não esquece de colocar o “language = ‘pt-BR’ ”

# use the audio file as the audio source
```
r = sr.Recognizer()
with file_audio as source:
   audio_text = r.record(source)
   text = r.recognize_google(audio_text,language='pt-BR')
4. E agora vamos salvar esse texto em um arquivo .txt :

arq = open(‘transcricao.txt’,’w’)
arq.write(text)
arq.close()
print(text)
```

Prontinho!!!

ps. se você quiser olhar o código no git é só clicar aqui, lá tá com um exemplo :D

ps. é super importante que vocês confiram se o texto está igual ao áudio, a transcrição dessa lib é muito boa, contudo, podem ocorrer falhas :D