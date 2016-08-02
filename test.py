import threading

def func1(func):
	for i in range(5):
		print("x" + str(i))
		func.join()
		func2()
def func2():
	for i in range(60):
		print('Y' + str(i))

tfunc2 = threading.Thread(target = func2)
tfunc1 = threading.Thread(target = func1,args=(tfunc2,))
tfunc1.start()
