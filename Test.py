#this is my logic
# def specific_location(location,file_name):
#     path=location+"\\"+file_name
#     with open(path,'w') as f:
#         pass


# location=input("Enter location")
# file_name=input("Enter file name: ")
# specific_location(location,file_name)

# #this is online conde help
# import os
# def specific_location(loc,file_name):
#     if not os.path.exists(loc):
#         path=os.makedirs(loc)
#     path=os.path.join(loc,file_name)

#     with open(path,'w') as f:
#         pass

# loc=input("Enter file location: ")
# file_name=input("Enter file name: ")
# specific_location(loc,file_name)


#Test case-2

class Demo:
    def add(self):
        self.a=10
        b=20
        print(self.a+b)

    def dis(self):
        print(self.a)

demo=Demo()
demo.add()
demo.dis()

