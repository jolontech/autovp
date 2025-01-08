##########################################
# Project: Methods for generating and playing voice with VoicePeak
# Author: jolon
# Description: methods called from main
##########################################

# Import moudules
import argparse
import subprocess
from pydub import AudioSegment
from pydub.playback import play
import warnings
warnings.simplefilter('ignore')  # デバッグ時は表示させる

# 引数処理
def arg_parser():
    parser = argparse.ArgumentParser(description='Generate and Play Voice with VoicePeak')
    parser.add_argument('query', help='Text to talk')
    parser.add_argument('-o', '--out',
                        help='Output file path',
                        default='test.wav')
    parser.add_argument('-v' ,'--vppath',
                        help='voicepeak command path',
                        default='/Applications/voicepeak.app/Contents/MacOS/voicepeak')
    parser.add_argument('-n', '--narrator',
                        help='select narrator in --list-narrator of voicepeak command',
                        default="Koharu Rikka")
    parser.add_argument('-e', '--emotion',
                        help='set emotion parameters in --list-emotion of voicepeak command',
                        default=False)

    args = parser.parse_args()
    return args

# VoicePeakでボイスのwavデータを生成
def generate_voice(query, out_file, narrator, vp_path, emotion):
  # Generate voice
  # print('Processing: ' + command + ' -s ' + query + ' -n ' + narrator + ' -o ' + out_file)
  input = [vp_path, '-s', query, '-n', narrator, '-o', out_file]
  if emotion is not False:
    input = input + ['-e', emotion]
  subprocess.run(input)

# wavファイルを再生
def play_voice(input, format="wav"):
  # Play voice
  sound = AudioSegment.from_file(input, format=format)
  print("再生中")
  play(sound)
  print("再生終了")
  
