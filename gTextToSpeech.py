from gtts import gTTS

fileName = input("what file name to be saved as mp3")

def createMP3(someText):
    language = 'en'
    mp3 = gTTS(text = f" { someText } ", lang = language)
    mp3.save("micTest.mp3")

createMP3("Hello World This is a test recording")