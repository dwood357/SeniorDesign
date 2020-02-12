import os

data = []

i  = 0
d = 0

import sys
import threading
import time
import queue

def add_input(input_queue):
    while True:
        input_queue.put(sys.stdin.read(1))

def foobar():
    input_queue = queue.Queue()

    input_thread = threading.Thread(target=add_input, args=(input_queue,))
    input_thread.daemon = True
    input_thread.start()

    last_update = time.time()
    i = 0
    d=0
    datal = []
    datar = []
    data = []
    while i<10:

        if time.time()-last_update>0.5:
            # sys.stdout.write(".")
            last_update = time.time()
            d=d+1
        if not input_queue.empty():
            
            print ("Left,Right:")#, input_queue.get())
            
            a = input_queue.get()
            
            
            if a != '\n':
            	
            	# a.strip()
            	# a = ''.join(a)
            	a=float(a)
            	if a == 1:
            		print("Thats the one")
            	print(type(a))
            	print(a)
            # right.strip('\n')
            # a.split(",")
            # a.strip(",")
            # left = a[:0]
            # right = a[:1]
            
            # datal.append(left)
            # datar.append(right)
            	i = i+1
    # print(datal)
    # print(datar)
    print(data)
    print(a)
    print(d)
foobar()


# while i < 10:

# 	new_data = foobar()
# 	if new_data == '':
# 		i = i 
# 	elif new_data != '':
# 		data.append(new_data)
# 		i = i + 1
# 	else:
# 		continue
# 	d= d+1
# 	print(d)
# print(data) 