import os
import subprocess
from scipy.io import wavfile

# Path to the WAV file
wav_file = 'swartz.wav'

# Convert WAV to raw 16-bit PCM format
raw_file = 'temp.raw'
subprocess.call(['ffmpeg', '-i', wav_file, '-f', 's16le', '-ac', '1', '-ar', '16000', '-y', raw_file])

# Perform speech recognition using pocketsphinx
hmm = 'en-us'
dict_file = 'cmudict-en-us.dict'
lm = 'en-us.lm.bin'
config = 'pocketsphinx.conf'
output_file = 'output.txt'

subprocess.call(['pocketsphinx_continuous', '-hmm', hmm, '-dict', dict_file, '-lm', lm, '-infile', raw_file, '-logfn', '/dev/null', '-config', config, '-outfn', output_file])

# Read the recognized text from the output file
with open(output_file, 'r') as file:
    recognized_text = file.read()

# Print the recognized text
print("Recognized Text:")
print(recognized_text)

# Clean up temporary files
os.remove(raw_file)
os.remove(output_file)
