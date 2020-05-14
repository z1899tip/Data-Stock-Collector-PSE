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



try:
    from Credential import mail_list
    mailing_list = mail_list()
except ImportError as Ie:

    #Need user replacement {1:youremail@gmail.com}

    mailing_list = {
    1:None,
    2:None,
    3:None}

mail_list = [mailing_list[i] for i in mailing_list.keys()]





t = datetime.datetime.now().strftime('%H:%M')
trigger = [0,0,0,0,0,0,0,0]  #length of trigger must greater than declared test objects. (or below stock name)
epoch = 0
object_cnt = 1  #change the value depends on below test object

#### -----------------------Input Condition----------------------------------------

####    Input --> (stock_name,target price, cutloss price, entry price (in list, maxmin), mailing list)
# start_function('BDO',TP=160,CL=150,EP=[155,156],mail_name=mail_list)



# ##---------------------------Test Object--------------------------------------------
# while(t != '12:00' and t!='15:30'):
while(t != '01:30'): #new schedule


    if (trigger[0] == False):
        trigger[0] = start_function('TECH',EP=[7.96,8.2],mail_name=mail_list)


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
