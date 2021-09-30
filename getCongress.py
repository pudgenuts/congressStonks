import urllib.request, json 
import pprint
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file')
args = parser.parse_args()

print("filein: %s" % (args.file))
f = open(args.file,"r")
data = json.load(f)
# pprint.pprint(data)

symbols = []
# with urllib.request.urlopen("https://senate-stock-watcher-data.s3-us-west-2.amazonaws.com/aggregate/all_ticker_transactions.json") as url:
# data = json.loads(url.read().decode())
# {'amount': '$1,001 - $15,000',
  # 'asset_description': 'Bausch Health Companies Inc.',
  # 'cap_gains_over_200_usd': False,
  # 'disclosure_date': '04/28/2020',
  # 'disclosure_year': 2020,
  # 'district': 'NV03',
  # 'owner': 'joint',
  # 'ptr_link': 'https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/2020/20016193.pdf',
  # 'representative': 'Hon. Susie Lee',
  # 'ticker': 'BHC',
  # 'transaction_date': '2020-02-24',
  # 'type': 'purchase'},

for record in data: 
    print("%s[%s] of %s  %s between %s of %s(%s) on %s" % ( record['representative'], record['owner'], record['district'], record['type'], record['amount'], record['ticker'], record['asset_description'], record['transaction_date']))
    
# print(symbols)
