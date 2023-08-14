import cProfile
import palingrams
import time
start_time = time.time()
cProfile.run('palingrams.find_palingrams()')
end_time = time.time()















print("runtime for this program was {} seconds.".format(end_time - start_time))