from tkinter import Tk, Canvas, Entry, Button, Text
from pytube import exceptions
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound

def get_video_id(url):
    if 'youtu.be/' in url:
        return url.split('youtu.be/')[1].split('?')[0]
    elif 'v=' in url:
        return url.split('v=')[1].split('&')[0]
    return url.split('/')[-1]

def transcrever_video():
    url = entry_url.get()
    text_output.delete(1.0, "end")
    
    try:
        video_id = get_video_id(url)
        
        if not video_id or len(video_id) < 5:
            text_output.insert("insert", "URL inválida ou ID não encontrado")
            return
            
        try:
            transcript = YouTubeTranscriptApi.get_transcript(
                video_id, 
                languages=['pt', 'en']
            )
            
            output = "\nTranscrição do vídeo:\n\n"
            for entry in transcript:
                output += f"{entry['text']}\n"
            
            text_output.insert("insert", output)
            
        except NoTranscriptFound:
            text_output.insert("insert", f"Este vídeo não possui transcrição disponível.\nID: {video_id}")
            
    except exceptions.VideoError:
        text_output.insert("insert", "Erro ao acessar o vídeo")
    except Exception as e:
        text_output.insert("insert", f"Erro inesperado: {str(e)}")

def copiar_texto():
    texto = text_output.get("1.0", "end-1c")  
    texto_com_prompt = f"Resuma essa transcrição pra mim:\n\n{texto}" 
    root.clipboard_clear() 
    root.clipboard_append(texto_com_prompt)  


root = Tk()
root.title("Transcrição de Vídeos do YouTube")
root.geometry("600x500")

canvas = Canvas(root, width=600, height=500)
canvas.pack()

entry_url = Entry(root, width=70)
entry_url.place(x=20, y=20)

btn_transcrever = Button(root, text="Obter Transcrição", command=transcrever_video)
btn_transcrever.place(x=20, y=60)

btn_copiar = Button(root, text="Copiar Texto", command=copiar_texto)
btn_copiar.place(x=140, y=60)  

text_output = Text(root, height=25, width=72, wrap="word")
text_output.place(x=20, y=100)

root.mainloop()