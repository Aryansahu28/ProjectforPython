from gtts import gTTS
import os
myText = 'Shoutout to Rahul,Shoutout to Ravi ,Shoutout to Aaryan'

language = "en"
myobj = gTTS(text=myText, lang=language, slow=False)
myobj.save("shoutout.mp3")
os.system("shoutout.mp3")