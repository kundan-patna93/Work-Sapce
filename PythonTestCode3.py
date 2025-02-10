#here I am create file with different-dirrerent location and inssert data

import os 
class File_Handling:

    #create file in working directory
    def create_file(self):
        with open("test.txt",'w') as f:
            pass

    def create_user_location(self):
        with open("C:\\Users\\kumar\Desktop\Work Space\\Python\\test\\test.txt",'w') as f:
            pass

    def file_name_location_input_user(self,location,file_name,file_name2):
        #this is my approch
        path=location+"\\"+file_name
        print(path)
        with open(path,'w') as f:
            pass
        
        #this is onine approch
        if not os.path.exists(location):
            os.makedirs(location)
    
        file_path = os.path.join(location, file_name2)
        with open(file_path,'w') as f:
            pass   

fh=File_Handling()
#fh.create_file()
#fh.create_user_location("kundan")
#f="C:\Users\kumar\Desktop\Work Space\Python\test"
#location = input("Enter the directory path where you want to create the file: ")
#file_name = input("Enter the file name (with .txt extension): ")
p='C:\\Users\\kumar\\Desktop\\Work Space\\Python\\ram'
fh.file_name_location_input_user(p,'chandan.txt','kundan.txt')
#fh.display_name("kundan")
# 
# 



