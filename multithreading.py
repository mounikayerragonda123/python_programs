from threading import*
import  time
def Display():
    print(current_thread().name,'started..')
    time.sleep(3)
    print(current_thread().name,'ended..')
print("the number of active threads:",active_count())
t1=Thread(target='display',name='child thread 1')
t2=Thread(target='display',name='child thread 2')
t3=Thread(target='display',name='child thread 3')
t1.start()
t2.start()
t3.start()
print("the number of active threads:",active_count())
time.sleep(10)
print("the number of active threads:",active_count())
    
    