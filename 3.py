import whisper

def speech_recognition(model='base'):
    speech_model = whisper.load_model(model)
    audio_file = 'audio/WIKITONGUES： Karen speaking Cantonese.mp3'
    result = speech_model.transcribe(audio_file)
    print(result.get('text'))


# models: tiny, base, small, medium, large

if __name__ == '__main__':
    speech_recognition()

