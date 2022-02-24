
import argparse
# import imp

# port_what_pid.py
import os

netstat="netstat -antup |grep  "
port ="13693"
pid="13693"

#  netstat -antup |grep  13693

parser = argparse.ArgumentParser()
parser.add_argument(
    "--pid", required=False, type=str,
    help="Absolute path to video path.", default=pid)
# "G:\FFOutput\手指肌腱断裂康复训练记录Day1&2 00_00_10-00_01_22.flv"
FLAGS, unparsed = parser.parse_known_args()
# hand_detect(FLAGS)
# print("emotion_detect start")
# 训练 dlib
# emotion_detect(log, FLAGS.video_file_path)
# emotion_detect(None, FLAGS.video_file_path)


os.system(f"{netstat} {FLAGS.pid}")

