#here I am create file with different-dirrerent location and inssert data
# """
# import os 
# class File_Handling:

#     #create file in working directory
#     def create_file(self):
#         with open("test1.txt",'w') as f:
#             pass

#     def create_user_location(self):
#         with open("C:\\Users\\kumar\Desktop\Work Space\\Python\\test\\test.txt",'w') as f:
#             pass

#     def file_name_location_input_user(self,location,file_name,file_name2):
#         #this is my approch
#         path=location+"\\"+file_name
#         print(path)
#         with open(path,'w') as f:
#             pass
        
#         #this is onine approch
#         if not os.path.exists(location):
#             os.makedirs(location)
    
#         file_path = os.path.join(location, file_name2)
#         with open(file_path,'w') as f:
#             pass   

#     #Write some data in text file
#     def write_text(self):
#         with open('test1.py','w') as f:
#             f.write("Hello world...!")
#             print("Successfull write some message...!")
 
#     #Read the file 
#     def read_file(self):
#         with open('test1.py','r') as f:
#             res=f.read()
#             print(res)

# fh=File_Handling()
# #fh.create_file()
# #fh.write_text()
# #fh.read_file()


# #fh.create_file()
# #fh.create_user_location("kundan")
# #f="C:\Users\kumar\Desktop\Work Space\Python\test"
# #location = input("Enter the directory path where you want to create the file: ")
# #file_name = input("Enter the file name (with .txt extension): ")
# #p='C:\\Users\\kumar\\Desktop\\Work Space\\Python\\ram'
# #fh.file_name_location_input_user(p,'chandan.txt','kundan.txt')
# #fh.display_name("kundan")
# # 
# # 



#Create a file and perform some operation
# 1. Insert some data 
# 2. Insert data from user input 
# 3. Read which type of data
# 4. Check how many char data in file 
# 5. find the total number of upper,lower case char, digit and sysmbole



# class Operation:
#     # create file & insert record
#     def create_file(self):
#         with open('operation.py','w') as f:
#             pass

#     def add_text(self,data):
#         with open('operation.py','a') as file:
#             file.write(data + "\n")

#         with open('operation.py','r') as f:
#             global res 
#             res=f.read()
#             print("\n\n","show all character present in file")
#             print(res)
#             print("\n\nshow the type of data ")
#             print(type(res))
    


#     #Here is problem is going on ------------------------------------------------>
#     #show how many char in data in file
#     def count_char_file(self):
#         with open('C:\\Users\\kumar\\Desktop\\Work Space\\WorkSpace\\PythonTestCode3.py','r') as f:
#             res=f.read()
#         print(len(res))

#     def seperate_val(self):
#         uchar=""
#         lchar=""
#         num=""
#         sp=""
#         c1,c2,c3,c4=0,0,0,0
#         with open("C:\\Users\\kumar\\Desktop\\Work Space\\WorkSpace\\PythonTestCode3.py",'r') as file:
#             res=file.read()

#             for val in res:
#                 if val.isupper():
#                     c1=c1+1
#                     uchar=uchar+val 
#                 elif val.islower():
#                     c2=c2+1
#                     lchar=lchar+val 
#                 elif val.isnumeric():
#                     c3=c3+1
#                     num=num+val
#                 elif val.isspace():
#                     c4=c4+1
#                     sp=sp+val 
#         print("\nShow total number of upper letter:",c1,"\nTotal upper clase latter: \n",uchar,)
#         print("\nTowal number of lower letter: ",c2,"\nlower case character: \n",lchar)
#         print("\nTotal number of number : ",c3,"\nTotal number: \n",num)
#         print("\nTotal number of space: \n",c4)
        
# ops=Operation()
# #ops.create_file()

# # data=input("Enter text data: ")
# #ops.add_text(data)

# #ops.count_char_file()
# ops.seperate_val()  


# #Phase2
# class Phase3:
#     def readfile(self,name,n):
#           f=open(name,'r')
#           l=f.readlines()
#           count=0
#           for a in l:
#               count=count+1
#               if n==count:
#                   print(a)

#           f.close()
# p=Phase3()
# name="C:\\Users\\kumar\\Desktop\\Work Space\\WorkSpace\\PythonTestCode3.py"
# p.readfile(name,5)