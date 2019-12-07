'''
run me run me 

'''

from DataAcquisition import StockDataAcquire
'''
Get nasdaq 100 index stocks historical data 
'''
def GetNasdaqNDXData(self):
    StockDataAcquire().GetHistoricData1(StockDataAcquire().GetNasdaq100IndexNDX())
    
'''
Get All nasdaq stocks historical data 
'''
def GetAllNasdaqData(self):
    StockDataAcquire().GetHistoricData()
    

'''
Get list of all stocks
'''
def GetStocksInfor(self):
    return StockDataAcquire().GetStockSymbleList()
'''

'''
def GetNasdaqNDXList(self):
    return StockDataAcquire().GetNasdaq100IndexNDX()


'''
GetNasdaq100 historical data
'''