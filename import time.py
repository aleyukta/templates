import time
from pandas.tseries.offsets import BDay
import matplotlib.pyplot as plt
import psutil
import argparse
 
def process_memory_use():
    """
    Return system memory (RAM) used by the process in GB.
    """
    pid = os.getpid()
    py = psutil.Process(pid)
    return py.memory_info()[0]/2.**30
 
def showmem():
    print(__name__ + f""".load_csv_file: Process RAM usage: {process_memory_use():0.2f} GB
        [total RAM in use {psutil.virtual_memory()[2]} %]""")
   
 
if __name__ == '__main__':
 
    parser = argparse.ArgumentParser()
 
    parser.add_argument('--input_directory', dest='input_directory', action='store',default='C:/Users/Julia.Dancu/Documents/Avala project/avala_sentiment')
    parser.add_argument('--input_sentiment_score_file', dest='input_sentiment_score_file', action='store',default='df_sentiment_all.csv')
    parser.add_argument('--input_universe_us_file', dest='input_universe_us_file', action='store',default='TMunivus.csv')
    parser.add_argument('--input_universe_eu_file', dest='input_universe_eu_file', action='store',default='TMuniver.csv')
    parser.add_argument('--input_returns_file', dest='input_returns_file', action='store',default='TMretusd.csv')
    parser.add_argument('--output_directory', dest='output_directory', action='store',default='C:/Users/Julia.Dancu/Documents/Avala project/avala_sentiment')
 
    args = parser.parse_args()
 
    time_start = time.perf_counter()
 
    #### Code here ####
 
    time_elapsed = (time.perf_counter() - time_start)
    print ("%5.1f secs" % (time_elapsed))
    showmem()
    