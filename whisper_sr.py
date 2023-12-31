import whisper

def speech_recognition(model='base'):
    speech_model = whisper.load_model(model)
    audio_file = 'swartz.wav'
    result = speech_model.transcribe(audio_file)
    print(result.get('text'))


# models: tiny, base, small, medium, large

if __name__ == '__main__':
    speech_recognition()

