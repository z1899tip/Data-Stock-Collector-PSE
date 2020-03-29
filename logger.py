import logging
import datetime

def logger_func(orig_func):
    logging.basicConfig(filename='Test_Info_{}.log'.format(datetime.datetime.now().strftime('%m-%d-%Y')),level = logging.INFO)
    def wrapper_func(*args,**kwargs):
        # logging.basicConfig(level=logging.DEBUG,format=('%(asctime)s - %(levelname)s - %(message)s'))
        logging.info('Stock Name:{} Inputs:{} - Time:{} '.format(args,kwargs,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        # logging.getLogger('chardet.charsetprober').setLevel(logging.INFO)
        return orig_func(*args,**kwargs)
    return wrapper_func
