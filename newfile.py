import os  

outF = open("logs/myOutFile.txt", "w")

textList = ["One", "Two", "Three", "Four", "Five"]

try:
	os.remove("logs/myOutFile.txt")
except OSError:
	pass

outF = open("logs/myOutFile.txt", "w")
for line in textList:
  outF.write(line)
  outF.write("\n")
outF.close()
