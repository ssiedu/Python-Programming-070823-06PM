import pickle
file=open("Binary1.dat","wb")
list1=[11,22,33,44,55]
pickle.dump(list1,file)
file.close()

file=open("Binary1.dat","rb")
data=pickle.load(file)
file.close()
print(data)
