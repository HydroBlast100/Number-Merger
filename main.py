Code
# # Create a list of integers from File_1.txt
# myFile = open("File_1.txt", "r")
# dataList1 = myFile.readlines()
# dataList1 = [data.strip() for data in dataList1]
# numList = [eval(i) for i in dataList1]

# #Create a list of integers from File_2.txt
# myFile2 = open("File_2.txt", "r")
# dataList2 = myFile2.readlines()
# dataList2 = [data.strip() for data in dataList2]
# numList2 = [eval(i) for i in dataList2]

# #Combine two lists and sort
# combinedList = numList + numList2
# combinedList.sort()
# print(combinedList)


#Method 2
file = open("File_1.txt", "r")
file2 = open("File_2.txt", "r")
line = file.readline()
line2 = file2.readline()

while file and file2:
  if line<line2:
    print(line)
    line = file.readline()
  elif line>line2:
    print(line2)
    line2 = file2.readline()
  elif line or line2 == "":
    break
file.close()
