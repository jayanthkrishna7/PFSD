f1 = open("dnaruto.jpg", "rb")
data = f1.read()
f2 = open("s45.jpg", "wb")
f2.write(data)
f1.close()
f2.close()
print('file copied successfully')
