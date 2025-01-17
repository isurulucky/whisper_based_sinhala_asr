import os.path
speech_data_dir = './sinhala_asr/data/'

if __name__ == '__main__':
    file1 = open(speech_data_dir + 'utt_spk_text.tsv', 'r')
    Lines = file1.readlines()

    file = open(speech_data_dir + 'metadata.csv', 'w')
    file.write('file_name,transcription\n')

    for line in Lines:
        parts = line.split(maxsplit=2)
        audio_file_name = parts[0] + '.flac'
        transcription = parts[2]
        if transcription.endswith(',\n'):
            transcription = transcription.replace(',\n', '\n')
        if ',' in transcription:
            transcription = transcription.replace(',', ' ')
        if '"' in transcription:
            transcription = transcription.replace('"', ' ')
        if "'" in transcription:
            transcription = transcription.replace("'", ' ')
        transcription = transcription.lstrip()
        if os.path.exists(speech_data_dir + audio_file_name):
            file.write(f'{audio_file_name},{transcription}')

    file1.close()
    file.close()
