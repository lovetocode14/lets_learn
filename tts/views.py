from django.shortcuts import render
from django.http import HttpResponse
from TTS.api import TTS
from django.http import FileResponse
import os

# Create your views here.
def index(request):
    return render(request,'tts/index.html')

def tts_view(request):
    if request.method == 'POST':
        text = str(request.POST.get('text'))

        # generate TTS
        model_name = TTS.list_models()[0]

        tts = TTS(model_name)
        print(os.getcwd())
        tts.tts_to_file(text=text, speaker=tts.speakers[3],
                        language=tts.languages[0], file_path="output.wav")


        file = open("output.wav", "rb")


        response = FileResponse(file)
        response["content-Type"] = "audio/wav"
        response['Content-Disposition'] = "attachment; filename=tts.wav"
        return response
    return render(request, 'tts/index.html')


