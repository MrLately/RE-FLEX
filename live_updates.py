import time
from datetime import date
import filters
import userdata.serviceAreaIds as serviceAreaIds



def live_mode(block):
    block_length = (block['endTime'] - block['startTime']) / 3600
    block_price = block['rateInfo']['priceAmount']
    block_headstart = block['startTime'] - int(time.time())
    block_rate = block_price / block_length
    block_start = date.fromtimestamp(block['startTime']).strftime('%A'), time.strftime('%m/%d/%Y %I:%M %p', time.localtime(block['startTime']))
    block_station = serviceAreaIds.stationlist[block['serviceAreaId']]
    try:
        if filters.advanced_filter(block):
            print('----------------------------------')
            print('Scanned at', time.strftime('%m/%d/%Y %I:%M:%S %p'))
            print('----------------------------------')
            if block['offerType'] == 'EXCLUSIVE': print('* * R E S E R V E D * *')
            print(block_start)
            print('Starts in:')
            if round((block_headstart) / 60, 2) < 60: print(round((block_headstart) / 60, 2), 'minutes')
            if 1 < round((block_headstart) / 3600, 2) < 24: print(round((block_headstart) / 3600, 2), 'hours')
            if 1 < round(((block_headstart) / 3600) / 24, 2): print(round(((block_headstart) / 3600) / 24, 2), 'days')
            print(block_station)
            print(round(block_length, 1), 'Hours')
            print(round(block_price, 2), 'Dollars')
            print(round(block_rate, 2), '/hr')
            if block['offerType'] == 'EXCLUSIVE': print('* * R E S E R V E D * *')
            print('----------------------------------')
    except KeyError:
        print('live mode glitch')

def print_history(block):
    block_length = (block['endTime'] - block['startTime']) / 3600
    block_price = block['rateInfo']['priceAmount']
    block_rate = block_price / block_length
    block_start = date.fromtimestamp(block['startTime']).strftime('%A'), time.strftime('%m/%d/%Y %I:%M %p', time.localtime(block['startTime']))
    block_station = serviceAreaIds.stationlist[block['serviceAreaId']]
    try:
        if filters.advanced_filter(block):
            with open('scandata/scanned_blocks', 'a') as f:
                print('----------------------------------', file=f)
                print('Scanned at', time.strftime('%m/%d/%Y %I:%M:%S %p'), file=f)
                print('----------------------------------', file=f)
                if block['offerType'] == 'EXCLUSIVE': print('* * R E S E R V E D * *', file=f)
                print(block_start, file=f)
                print(block_station, file=f)
                print(round(block_length, 1), 'Hours', file=f)
                print(round(block_price, 1), 'Dollars', file=f)
                print(round(block_rate, 2), '/hr', file=f)
                if block['offerType'] == 'EXCLUSIVE': print('* * R E S E R V E D * *', file=f)
                print('----------------------------------', file=f)
    except KeyError:
        print('print history glitch')




