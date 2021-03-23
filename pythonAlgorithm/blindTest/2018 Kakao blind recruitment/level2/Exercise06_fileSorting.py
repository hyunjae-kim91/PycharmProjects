import re
def solution(files):
    temp = [re.split(r"([0-9]+)",s) for s in files]
    print(temp)
    sort = sorted(temp, key = lambda x : (x[0].lower(), int(x[1])))
    return ["".join(s) for s in sort]

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
#files = ["0000","fo--"]
print(solution(files))


"""
class file_divide:
    def __init__(self):
        self.head = None
        self.number = None
        self.tail = None

    def divide(self, file):
        index_number, index_alpha = len(file), len(file)
        for i in file:
            if i.isnumeric():
                index_number = file.index(i)
                break
        self.head = file[:index_number].upper()
        for i in file[index_number:]:
            if not i.isnumeric():
                index_alpha = file.index(i)
                break
        self.number = file[index_number:index_alpha]
        if self.number != '':
            self.number = int(self.number)
        self.tail = file[index_alpha:]
        return self.head, self.number, self.tail, file

def solution(files):
    file_list = []
    for file in files:
    #divide head / number / tail / file
        a = file_divide()
        head, number, tail, file = a.divide(file)
        file_list.append([head,number,tail,file])
    print(file_list)
    # sorting
    file_list = sorted(file_list, key = lambda x: (x[0],x[1]))
    return [i[3] for i in file_list]



files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
files = ["0000","fo--"]
print(solution(files))
#Result = [img1.png, IMG01.GIF, img02.png, img2.JPG, img10.png, img12.png]
"""