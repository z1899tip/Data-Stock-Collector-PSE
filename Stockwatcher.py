from bs4 import BeautifulSoup
import requests
import datetime,time
import random
import subprocess
import platform
##import Smail_sender
from Sms_Sender import sms_sender
 

#https://www.alphavantage.co/  API:  L5LQB4N9GS1RTYVW


class DataStockCollector(object):
    def __init__(self,stock_name,t_value=None,c_value = None,\

        ent= None,mail_name=None,glob_market_con=False,indicator=None):


        if isinstance(stock_name,list):
            if len(stock_name)==2:  #for forex stock name input.
                self.from_stock_name,self.to_stock_name = stock_name
            elif len(stock_name)==1: #for local and global stocks.
                self.stock_name = stock_name
            else:
                raise AssertionError ('Invalid stock name input!')
        else:
            self.stock_name = stock_name

        self.target_price = t_value
        self.cutloss = c_value
        self.entry = ent
        self.mail_name = mail_name
        self.glob_market_con = glob_market_con
        if indicator is not None:
            self.indicator = str.upper(indicator)
        else:
            self.indicator = 'LOCAL_PRICE'

        self.apikey = "L5LQB4N9GS1RTYVW"

        ## Below are the default values, but can modify by user.
        self.glob_stock_price_params = {
            "interval":"5min", #accept: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
            "series_type":"close" #"close","open","high","low"
            }

        self.forex_price_params = {
            "interval":"5min", #accept: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
            "series_type":"close" #"close","open","high","low"
            }

        self.macd_params ={
            "interval":"5min", #accept: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
            "fastperiod":12,  #any integer
            "slowperiod":26,  #any integer
            "signalperiod":9, #any integer
            "series_type":"close" #"close","open","high","low"
            }

        self.rsi_params = {
            "interval":"5min",  #accept: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
            "time_period":14,   #any integer
            "series_type":"close"   #"close","open","high","low"
            }

    def request_connection(self):
        if self.glob_market_con == False:
            for _ in range(10):       
                try:
                    r = requests.get('https://www.investagrams.com/Stock/{}'.format(self.stock_name),timeout=5)
                    self.etime = r.elapsed.total_seconds()
                    break
                except requests.ConnectionError:
                    print("Connection Failed..")
                    print("Please Check your Internet Connection!")
                    print("trying to reconnect in local market....")
                    time.sleep(10)
                    continue
                except KeyboardInterrupt:
                    print('Test Aborted..')
                except:
                    print('Unexpected Error [Local Market]')

            return r
        else:
            for _ in range(10):       
                try:
                    # print("Connecting to global market..")
                    API_URL ="https://www.alphavantage.co/query?"
                    requested_value = requests.get(API_URL,params=self.global_market_indicator,timeout=5)
                    self.etime = requested_value.elapsed.total_seconds()
                    # print(requested_value.json())
                    break
                except requests.ConnectionError:
                    print("Connection Failed..")
                    print("Please Check your Internet Connection!")
                    print("trying to reconnect in local market....")
                    time.sleep(10)
                    continue
                except KeyboardInterrupt:
                    print('Test Aborted..')
                except:
                    print('Unexpected Error [global Market]')

            return requested_value

    @property
    def global_market_indicator(self):
        if self.indicator == "MACD":
            data = {"function":"MACD",
            "symbol":self.stock_name,
            "interval":self.macd_params["interval"],
            "fastperiod":self.macd_params["fastperiod"],
            "slowperiod":self.macd_params["slowperiod"],
            "signalperiod":self.macd_params["signalperiod"],
            "series_type":self.macd_params["series_type"],
            "apikey":self.apikey}


        elif self.indicator == "RSI":
            data = {"function":"RSI",
            "symbol":self.stock_name,
            "interval":self.rsi_params["interval"],
            "time_period":self.rsi_params["time_period"],
            "series_type":self.rsi_params["series_type"],
            "apikey":self.apikey}


        elif self.indicator == "INTRA_GLOB_PRICE":
            data = {"function":"TIME_SERIES_INTRADAY",
            "symbol":self.stock_name,
            "interval":self.glob_stock_price_params["interval"],
            "series_type":self.glob_stock_price_params["series_type"],
            "apikey":self.apikey}

        elif self.indicator == "INTRA_FX_PRICE":
            data = {"function":"FX_INTRADAY",
            "from_symbol":self.from_stock_name,
            "to_symbol":self.to_stock_name,
            "interval":self.forex_price_params["interval"],
            "series_type":self.forex_price_params["series_type"],
            "apikey":self.apikey}
        return data

    @property
    def delays(self):
        ad_val = random.randint(1,10)
        time.sleep(self.etime+ ad_val)

    @property
    def extract_value(self):
        if self.glob_market_con == False:
            #for local stockmarket extraction.
            r = self.request_connection()
            bf = BeautifulSoup(r.content,'lxml')
            self.cur_val = bf.find('span', id='lblStockLatestLastPrice').text
            self.cur_val = float(self.cur_val)
            self.low_val = bf.find('span', id='lblStockLatestLow').text
            self.low_val = float(self.low_val)
            self.high_val = bf.find('span', id='lblStockLatestHigh').text
            self.high_val = float(self.high_val)
            self.update_time = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")

        else:
            # for global and forex stockmarket extraction.
            req_val = self.request_connection()
            json_val = req_val.json()
            # print(json_val.values())

            for k,v in json_val.items():
                if 'Time Series' in k:
                    time_series = k
                if 'Meta Data' in k:
                    meta_data = k
                if 'Technical Analysis' in k:
                    Tech_Analysis = k

            # print(time_series,meta_data)

            if self.indicator in ['MACD','RSI']:
                last_refreshed = json_val[meta_data]['3: Last Refreshed']                        
                last_refreshed = last_refreshed.split(':')
                last_refreshed = ':'.join(last_refreshed[0:2])
                self.cur_val = json_val[Tech_Analysis][last_refreshed][self.indicator]
                self.update_time = last_refreshed
                # print(self.indicator,':',self.cur_val)


            else:
                last_refreshed = json_val[meta_data]['3. Last Refreshed']                
                self.cur_val = json_val[time_series][last_refreshed]['4. close']
                self.low_val = json_val[time_series][last_refreshed]['3. low']
                self.high_val = json_val[time_series][last_refreshed]['2. high']
                self.update_time = last_refreshed
                # print('indicator:',self.indicator)
                # print('close:',self.cur_val)
                # print('low:',self.low_val)                   
                # print('high:',self.high_val)
                # print('Last Update Time:',self.update_time)



    @property
    def result_value(self):
        if self.glob_market_con == False:
            if self.target_price is not None:
                float(self.target_price)

 
                if self.target_price<=self.high_val:
                    result_str = 'Your Target Price was Hit!'
                    status_result = 'Target'
                    # highest_price = "Today's Highest Price"
                    self.alarm(result_str,self.stock_name)
                    # self.send_notification(result_str,status_result,self.target_price,self.high_val,self.update_time)
                    self.send_sms(result_str,status_result,self.target_price,self.high_val,self.update_time)
                    return True

            if self.cutloss not in (None,[]):
                if isinstance(self.cutloss,list) == 0:
                    self.cutloss = [self.cutloss]

                if len(self.cutloss) == 2:
                    if (max(self.cutloss) >=self.cur_val) and (min(self.cutloss) <=self.cur_val):
                        result_str = 'Your Cutloss Price Range was Hit!'
                        status_result = 'Cutloss Range'
                        # current_price = "Current Price"
                        self.alarm(result_str,self.stock_name)
                        # self.send_notification(result_str,ent_price,self.entry,self.cur_val,self.update_time)
                        self.send_sms(result_str,status_result,self.cutloss,self.cur_val,self.update_time)
                        return True
                    else:
                        return False

                #In case of 1 input, cutloss will refer to Today's Lowest Price.
                elif(len(self.cutloss) == 1):
                    if self.cutloss[0] >=self.low_val:
                        result_str = 'Your Cutloss was Hit!'
                        status_result = 'Cutloss'
                        lowest_price = "Today's Lowest Price"
                        self.alarm(result_str,self.stock_name)
                        # self.send_notification(result_str,c_loss,self.cutloss,self.low_val,lowest_price)
                        self.send_sms(result_str,status_result,self.cutloss,self.cur_val,self.update_time)
                        return True

                else:
                    print('[Warning!] Cutloss was not set properly.Input must not exceed 2 digits.')
                    return False


            if self.entry is not None:
                if isinstance(self.entry,list):
                    if len(self.entry) == 2:
                        if (max(self.entry) >=self.cur_val) and (min(self.entry) <=self.cur_val):
                            result_str = 'Your Entry Price was Hit!'
                            status_result = 'Entry Range'
                            current_price = "Current Price"
                            self.alarm(result_str,self.stock_name)
                            # self.send_notification(result_str,status_result,self.entry,self.cur_val,current_price)
                            self.send_sms(result_str,status_result,self.entry,self.cur_val,self.update_time)
                            return True
                        else:
                            return False
                    else:
                        raise AssertionError('Insufficient Entry.. Note: min of 2 inputs')
                        return False
                else:
                    raise AssertionError('Entry Input not valid..')
                    return False
            else:
                return False


    def send_notification(self,result_str,status_result,set_price,current_val,update_time):
        Smail_sender.send_automail(self.mail_name,self.stock_name,result_str,status_result,set_price,self.cur_val,update_time)


    def send_sms(self,result_str,status_result,set_price,current_val,update_time):
        sms_sender(self.stock_name,result_str,status_result,set_price,current_val,update_time)
        print('Message Sent!')


    def alarm(self,sp,my_stock):
        op_system = platform.system()
        if op_system == 'Linux':
            for _ in range(3):
                #text to speech in linux
                subprocess.call(['spd-say', 'Alert! Stock name {}: {}'.format(my_stock,sp)])
                time.sleep(5)

                #text to speech in linux (Not yet tested.)
        elif op_system == 'Windows':
            for _ in range(3):
                subprocess.call(['PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak("Alert! Stock name {}: {}");'.format(my_stock,sp)])
                time.sleep(5)

    def __str__(self):
        return("'{}': Current {} Value: {} - as of:{})".format(self.stock_name,self.indicator,self.cur_val,self.update_time))

    def __repr__(self):
        return("DataStockCollector(stock_name={},target_price={},cutloss={},entry={},mail_name={},glob_market_con={},indicator={}".format(self.stock_name,self.target_price,self.cutloss,self.entry,self.mail_name,self.glob_market_con,self.indicator))

