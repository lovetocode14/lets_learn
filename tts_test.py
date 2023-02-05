from TTS.api import TTS

model_name = TTS.list_models()[0]

tts = TTS(model_name)


tts.tts_to_file(text="Hello World thank you for joining our lecture on text to speech", speaker=tts.speakers[0], language=tts.languages[0], file_path="tts/static/output.wav")



