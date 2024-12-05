# coun_file = open('/home/kali/Desktop/pyBackend/basic/countries.txt','r')
# coun_file = open('/home/kali/Desktop/pyBackend/basic/new.txt','w')
coun_file = open('/home/kali/Desktop/pyBackend/basic/new.txt','a')
# print(coun_file.readable())
coun_file.write("\nThis is a new text")

# print(coun_file.writable())
# coun_file.write('print(\'This is a new file\')')
# for lines in coun_file:
#     print(lines)
# coun_file.close()