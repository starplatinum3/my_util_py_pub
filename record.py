# D:\software\ffmpeg-2022-08-25-git-9bf9d42d01-essentials_build\bin\ffmpeg.exe -list_devices true -f dshow -i dummy 

# now_time

from time_util import get_now_time_str
import os

now_time_str=get_now_time_str()

out_dir=r"D:\recordDir"
out_file_name=os.path.join(out_dir,now_time_str+".mp3")
# 麦克风阵列 (适用于数字麦克风的英特尔® 智音技术)
# os.system(f'D:\software/ffmpeg-2022-08-25-git-9bf9d42d01-essentials_build/bin/ffmpeg.exe  -f dshow -i audio="Microphone (Realtek High Definition Audio)" {out_file_name}')
# os.system(f'D:\software/ffmpeg-2022-08-25-git-9bf9d42d01-essentials_build/bin/ffmpeg.exe  -f dshow -i audio="麦克风阵列 (适用于数字麦克风的英特尔® 智音技术)" {out_file_name}')
# 听到了 录制
# 外部麦克风 (Realtek(R) Audio)" (audio)
# 声音还是挺响的 好像是有杂音的,这个不是耳机吗
os.system(f'D:\software/ffmpeg-2022-08-25-git-9bf9d42d01-essentials_build/bin/ffmpeg.exe  -f dshow -i audio="外部麦克风 (Realtek(R) Audio)" {out_file_name}')
