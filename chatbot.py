#coding:utf-8
data_find=(-1)
i=0
while True:
    data=input("question:")
    while data_find==-1:
        with open("data_file.txt", "r")as fic:
            data_file=fic.read()
        data_file1=(data_file+"<split>end")
        data_file1=data_file1.split("<split>")
        try:
            data_file1=(data_file1[i])
            data_find=(data_file1.find(data))
            if(data_find=="end"):
                data_find=0
            if(data_find is not -1):
                c=input(data)
                i=0
                print(data_file[i+1])
        except:
            print("i didn't find")
        finally:
            # i +2 because unpair number it's for the sytem finds and pairs number it's the anser
            i=+2
print("end")
        
    
