from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_file("test.wav", format="wav")

print("再生します")
play(sound)
print("再生終了")
