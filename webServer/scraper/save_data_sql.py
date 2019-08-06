from main.models import *

company = Company(ticker='yyo',name='ANZ',sector='YET')
company.save()
# def save_data(stockDataArray):
#     logger.info("Starting to save data")

#     # Create connection with MongoDB instance
#     mongoURL = 'mongodb://aut12345:aut12345@localhost:27017/'
#     logger.info("Trying connection to DB via: {}".format(mongoURL))
#     client = MongoClient(mongoURL)
#     db = client.test
#     companyData = db.CompanyData
#     currentTimeStamp = "2019/07/30" #datetime.now().strftime('%Y/%m/%d')

#     scrapeInsert = {currentTimeStamp:{'Date':currentTimeStamp}}
#     dividendInsert = {'Data':{}, 'Name': 'HistoricalDividends'}
#     priceInsert = {'Data':{}, 'Name': 'HistoricalPrices'}

#     # Select stock
#     for stock in stockDataArray:
#         currentStockTicker = stock['Summary']['Ticker']
#         logger.info("Saving data for: " + currentStockTicker)
#         stockInsert = {}


#         # Create stock dict from scraped data
#         for sectionKey, sectionData in stock.items():
#             logger.info(sectionKey)
#             sectionInsert = {}
#             if sectionKey == 'HistoricalPrices':
#                 for line in sectionData:
#                     logger.debug(line)
#                     sectionInsert[line.pop('Date')] = line
#                 priceInsert['Data'][currentStockTicker] = sectionInsert
#             elif sectionKey == 'HistoricalDividends':
#                 for line in sectionData:
#                     sectionInsert[line.pop('Date')] = line.pop('Dividend Paid')
#                 dividendInsert['Data'][currentStockTicker] = sectionInsert
#             else:
#                 for elementKey, elementValue in sectionData.items():
#                     sectionInsert[elementKey] = elementValue
#                 stockInsert[sectionKey] = sectionInsert

#         scrapeInsert[currentTimeStamp][stock['Summary']['Ticker']] = stockInsert


#     with open('data.txt', 'w') as outfile:
#         json.dump(scrapeInsert, outfile, indent=4)

#     # Build the DB if not exists
#     if not companyData.count_documents({}):
#         companyData.insert_one({'Name':'StockData'})
#         companyData.insert_one({'Name':'HistoricalDividends'})
#         companyData.insert_one({'Name':'HistoricalPrices'})

#     # Update the appropriate document with the new data
#     companyData.update_one(
#         {'Name':'StockData'},
#         {'$set':scrapeInsert}
#         )
#     companyData.update_one(
#         {'Name':'HistoricalDividends'},
#         {'$set':dividendInsert}
#         )
#     companyData.update_one(
#         {'Name':'HistoricalPrices'},
#         {'$set':priceInsert}
#         )

#     client.close()