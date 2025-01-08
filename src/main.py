##########################################
# Project: Generate and Play Voice with VoicePeak
# Author: jolon
# Usage: python main.py [query] -o [out path] -v [vp path] -n [narrator] -e [emotion parameters]
##########################################

from func import *

if __name__ == "__main__":
  # 引数呼び出し
  args = arg_parser()

  # wavファイル生成&再生
  generate_voice(query=args.query, out_file=args.out, narrator=args.narrator, vp_path=args.vppath, emotion=args.emotion)
  play_voice(input=args.out)
  
