code="""
main: plus.android.runtimeMainActivity(),
	Environment: plus.android.importClass('android.os.Environment'),
	BufferedWriter: plus.android.importClass('java.io.BufferedWriter'),
	File: plus.android.importClass('java.io.File'),
	FileOutputStream: plus.android.importClass('java.io.FileOutputStream'),
	OutputStreamWriter: plus.android.importClass('java.io.OutputStreamWriter'),"""

fields_code=""

lines=code.split("\n")

for line in lines:
    if ":" not in line:
        continue
    parts=line.split(": ")
    print(f"this.{parts[0]} = {parts[1][:-1]};")
    fields_code+=f"{parts[0]} :null,\n"

print()
print(fields_code)