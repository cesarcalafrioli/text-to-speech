from gtts import gTTS
import os

def conv_txt_audio(entrada):
    # Texto que queremos converter para audio
    text = entrada[0]

    # Idioma desejado para conversão
    language = entrada[1]

    # Caminho no qual queremos que o audio seja salvo
    path  = entrada[2]

    # Analisando o texto e o idioma para a conversão
    # slow = False significa que o audio convertido
    # deve estar em velocidade alta de reprodução
    myobj = gTTS(text = text , lang = language , slow = False)

    # Salvando o audio convertido em um arquivo wav
    myobj.save("{}/audio.wav".format(path))

def main():
    # Recebendo as informações digitadas pelo usuário. As informações serão recebidas em forma de parâmetros e, portanto,
    # divididas e colocadas em um vetor.
    entrada = input().split()

    # Convertendo o texto em audio
    conv_txt_audio(entrada)

if __name__ == "__main__":
    main()