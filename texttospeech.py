from gtts import gTTS
import os
myText = ['Shoutout to Rahul','Shoutout to Ravi','Shoutout to Aaryan']

language = "en"
for i in range(0,3):
    myobj = gTTS(text=myText[f"{i}"], lang=language, slow=False)
    myobj.save(f"shoutout[{i}].mp3")
    os.system(f"shoutout.mp3")