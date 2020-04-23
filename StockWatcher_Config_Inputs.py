from Stockwatcher import DataStockCollector
import datetime
from logger import logger_func


@logger_func
def start_function(stock_name,TP=None,CL=None,EP = None,mail_name = None,glob_market_con=False,indicator=None):

    obj = DataStockCollector(stock_name,TP,CL,EP,mail_name,glob_market_con,indicator)
    obj.extract_value
    print(obj)
    res = obj.result_value
    # obj.delays
    return res

#Declared variables

mailing_list ={
    '1':'stephenangelo.villanueva@toshiba.co.jp',
    '2':'dennis.quiambao@toshiba.co.jp',
    '3':'markharold.silva@toshiba.co.jp',
    '4':'markangelo.antonio@toshiba.co.jp',
    }

t = datetime.datetime.now().strftime('%H:%M')
trigger = [0,0,0,0,0,0,0,0]  #length of trigger must greater than declared test objects. (or below stock name)
epoch = 0
object_cnt = 1  #change the value depends on below test object

#### -----------------------Input Condition----------------------------------------

####    Input --> (stock_name,target price, cutloss price, entry price (in list, maxmin), mailing list)
start_function('BDO',TP=160,CL=150,EP=[155,156],mail_name=mailing_list['1'])





# start_function('BCOR',CL=[3.30,3.31],EP=[3.25,3.26],mail_name=mailing_list['1'])
# logging.info('1st')
# start_function('TSLA',glob_market_con=1,indicator='INTRA_GLOB_PRICE')
# logging.debug('2nd')

# start_function('FRUIT',EP=[1.40,1.45],mail_name=mailing_list['1'])

# start_function('BCOR',EP=[3.94,3.98])

# while(t != '12:00' and t!='15:30'):
while(t != '01:30'): #new schedule
# ##---------------------------Test Object--------------------------------------------

    if (trigger[0] == False):
        trigger[0] = start_function('SMPH',CL=28.5,mail_name=mailing_list['1'])



    # if (trigger[1] == False):
    #     trigger[1] = start_function('BDO',CL=[91.5,91.99],mail_name=mailing_list['1'])


    # if (trigger[1] == False):
    #     trigger[1] = start_function('TSLA',glob_market_con=1,indicator='INTRA_GLOB_PRICE')

    # if (trigger[2] == False):
    #     trigger[2] = start_function('TSLA',glob_market_con=1,indicator="MACD")

    # if (trigger[3] == False):
    #     trigger[3] = start_function('FRUIT',EP=[1.27,1.30],mail_name=mailing_list['1'])

    # if (trigger[4] == False):
    #     trigger[4] = start_function('AXLM',CL=2.78,mail_name=mailing_list['1'])
# ####---------------------------------------------------------------------------------

    if (sum(trigger)== object_cnt):
        break

    epoch +=1
    print('Cycle:',epoch)

print('Now Closing....')
