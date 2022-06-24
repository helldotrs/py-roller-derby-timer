import time

def time_convert(secs):
    mins    =   secs // 60 # // for int value instead of float
    secs    =   secs %  60 
    hours   =   mins %  60
    mins    =   mins %  60
    
    print("Time lapsed = {0}:{1}:{2}".format(int(hours),int(mins),secs)) 

input("Press [enter] to start")
start_time  = time.time()

input("Press [enter] to stop")
end_time    = time.time()

time_lapsed = end_time - start_time
time_convert(time_lapsed)
