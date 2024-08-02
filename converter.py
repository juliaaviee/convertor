import moviepy.editor as mp
from tkinter.filedialog import askopenfilename
from tkinter import Tk
import os

# Ocultar a janela raiz do Tkinter
root = Tk()
root.withdraw()

# Abrir o diálogo para selecionar o arquivo de vídeo
video_path = askopenfilename()

# Verificar se um arquivo foi selecionado
if video_path:
    # Carregar o vídeo
    video = mp.VideoFileClip(video_path)
    
    # Extrair o áudio
    audio = video.audio
    
    # CD para salvar o arquivo MP3
    output_path = "euamoroblox.mp3"
    
    # Salvar o áudio como MP3
    audio.write_audiofile(output_path)
    print("Conversão concluída!")
    
    # Exibir o caminho completo do arquivo MP3
    full_path = os.path.abspath(output_path)
    print(f"O arquivo MP3 foi salvo em: {full_path}")
    
    # Fechar os arquivos
    audio.close()
    video.close()
else:
    print("Nenhum arquivo selecionado.")
