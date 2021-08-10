def swap () :
    file1= input("Enter the file name : ")
    file2 = input("Name the file to swap the data : ")
    a = open(file1, "r")
    dataA = a.read()
    b = open(file2, 'r')
    dataB = b.read()
    
    a = open(file1, 'w')
    a.write(dataB)
    
    b = open(file2, 'w')
    b.write(dataA)

swap()