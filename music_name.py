

# D:\music>

import os
root_dir = r"D:\music"


lst_files = os.listdir(root_dir)

# file_map = {
#     "abs_path": "1",
#     "id": "2"
# }

id_list = []

#  file_map={
net_url_out_str=""
for file in lst_files:
    
    abs_path = os.path.join(root_dir, file)
    id = file.split("-")[0]
    if id.endswith(".js") or id.endswith(".json"):
        continue
    if file.endswith("idx!"):
        continue
    net_url = f"https://music.163.com/#/song?id={id}"
    net_url_out_str+=net_url+"\n"
    id_list.append({
        "abs_path": abs_path,
        "id": id,
        "net_url": net_url
    })
    # print(id)
print(id_list)
import json
# json.dump(id_list)

def json_to_file(json_obj,filename):
    with open(filename, "w") as fp:
        json.dump(json_obj, fp)

# json_to_file(id_list,"id_list.json")

with open("net_url_list.txt","w") as f:
    f.write(net_url_out_str)