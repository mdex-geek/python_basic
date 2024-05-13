file = open('youtube_manager.txt','w')

try:
    file.write('chai aur code')
finally:
    file.close()

with open('youtube_manager.txt','w') as file :
    file.write('chai aur python')