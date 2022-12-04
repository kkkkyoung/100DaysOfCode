<읽기>

file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()  # open하면 close는 세트


with open("my_file.txt") as file:  # with는 close할 필요 없음
    contents = file.read()         # mode = "r" 기본값 읽기모드
    print(contents)

--------------------------------
<쓰기>

with open("my_file.txt", mode = "w") as file: 
    file.write("new text")  # w : 덮어쓰기, 파일이 없으면 새로만듬


with open("my_file.txt", mode = "a") as file: 
    file.write("\nnew text")  # a : 이어쓰기
