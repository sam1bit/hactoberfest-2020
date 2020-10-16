import os
path=os.getcwd()
def find_os(num):
    if os.name=="posix":
        print("creating directory")
        os.mkdir("py_dir")
        print("creating files")
        list_dir=os.listdir(path)
        if "py_dir" in list_dir:
            pat=os.path.join(path,"py_dir")
            for i in range(1,num+1):
                file_create=pat+"/"+"file"+str(i)
                a=os.popen("touch "+file_create)
                a.close()
                
        b=os.popen("ls -lish")
        for i in b:
            
    elif os.name=="nt":
        print("creating folder")
        os.mkdir("py_folder")
        list_folder=os.listdir(path)
        if "py_folder" in list_folder:
            print("creating files")
            pat=os.path.join(path,"py_folder")
            for i in range(1,num+1):
                file_create=pat+"/"+"file"+str(i)+".txt"
                with open(file_create,"w") as f:
                    f.write("omg")
            
                
                    
find_os(5)
                
        
