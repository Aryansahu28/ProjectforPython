from gtts import gTTS
import os
myText = ['Shoutout to Rahul','Shoutout to Ravi','Shoutout to Aryan']

language = "en"

myobj = gTTS(text=myText, lang=language, slow=False)

myobj.save("shoutout1.mp3")

os.system("shoutout1 .mp3")