from gtts import gTTS

file = open('sample_data/kim.txt','r',encoding = 'utf-8')

txt_lines = file.readlines()
txt_lines = [txt.replace('\n','') for num, txt in enumerate(txt_lines) if num%2 != 0]

text = ' '.join(txt_lines)

tts = gTTS(text=text, lang='en', slow=False)
tts.save("sample_data/kim.wav")