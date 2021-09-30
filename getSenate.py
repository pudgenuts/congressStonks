import urllib.request, json 
import pprint
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file')
args = parser.parse_args()

print("filein: %s" % (args.file))
f = open(args.file,"r")
data = json.load(f)
pprint.pprint(data)

symbols = []
# with urllib.request.urlopen("https://senate-stock-watcher-data.s3-us-west-2.amazonaws.com/aggregate/all_ticker_transactions.json") as url:
# data = json.loads(url.read().decode())
for record in data: 
    pprint.pprint(record)
    for transaction in record['transactions']: 
        # Sale (Full)
        # Sale (Partial)
        # Purchase
        print(transaction['type'])
        if transaction['ticker'] != "--" and  transaction['type'] == 'Purchase':
            print("senator: %s[%s] bought between %s (%s) of %s on %s" % ( transaction['senator'], transaction['owner'], transaction['amount'], record['ticker'], transaction['asset_description'],transaction['transaction_date']))
            # pprint.pprint(record['transactions'])
            # print("found new stonk %s" % (record['ticker']))
            symbols.append(record)
        if transaction['ticker'] != "--" and transaction['type'] == 'Sale (Full)':
            print("senator: %s[%s] sold between %s (%s) of %s on %s" % ( transaction['senator'], transaction['owner'], transaction['amount'], record['ticker'], transaction['asset_description'],transaction['transaction_date']))


# print(symbols)
