fw = open('sample.txt','w')
fw.write('writing in my new text file\n. hey you!\n')
fw.write('I like table tennis! :D\n')
fw.close()

fr  = open('dict.py', 'r')
text = fr.read()
print(text)
fr.close()