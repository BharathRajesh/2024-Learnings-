#trying matrix using list
col_1=[1,1,1]
col_2=[1,1,1]
col_3=[1,1,1]
matrix=[col_1,col_2,col_3]
print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}")
position=input("enter the position u have to store:")
value=input("enter the value u wana store")
row=int(position[0])
column=int(position[1])
sel_row=matrix[row-1]
sel_row[column-1]=value
print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}")



