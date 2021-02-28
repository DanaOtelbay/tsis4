import os 
import shutil

#pwd  -до
#/users/askar/documents/pp2/

dir_path = "/users/askar/documents/pp2/test/"
os.makedirs(dir_path) #- сосдаёт новые папки путь указываешь сам

#pwd  -после
#/users/askar/documents/pp2/test/

src =  "/users/askar/documents/pp2/test/"
dst =  "/users/askar/documents/pp2/test_1/"
os.rename(src, dst) #- изменяет имя файла

src =  "/users/askar/documents/pp2/test/"
dst =  "/users/askar/documents/pp2/test_1/"
shutil.move(src, dst) #-передвигает в dst из scr (test_1)
shutil.copythree(src, dst) #-copy это для файлов0 а copythree это для папки

