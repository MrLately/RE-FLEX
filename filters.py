import time



def simple_filter(block):
    # Filtering out blocks that you don't want.
    # Comment out individual filters that you don't want applied
    block_length = (block["endTime"] - block["startTime"]) / 3600
    block_price = block["rateInfo"]["priceAmount"]
    block_headstart = block["startTime"] - int(time.time())
    block_rate = block_price / block_length
    return (
        block_rate > 18
        and not block["hidden"]
        #and block_price > 110
        #and block_headstart >= 1500
        #and block_length < 5
    )

def advanced_filter(block):
    #You can use a number of combinations here
    block_length = (block["endTime"] - block["startTime"]) / 3600
    block_price = block["rateInfo"]["priceAmount"]
    block_headstart = block["startTime"] - int(time.time())
    block_rate = block_price / block_length
    block_station = block['serviceAreaId']
    # You can copy the code below and past for however many stations you want special filters for
    # identify Station
    if block_station == 'a5e1a8d5-c368-4cb8-a2c6-3b71b3eb8178' and block_headstart >= 0:#Sample Station
        if block_rate >= 0:
            return (
                not block["hidden"]
                #and block_price >= 0
                and block_length >= 0
            )
        else:
            return (
                not block["hidden"]
                and block_rate >= 0
                #and block_price >= 0
                and block_length <= 0
            )

def print_filter(block):
    # Comment out the second line if you want to print base rate
    block_length = (block["endTime"] - block["startTime"]) / 3600
    block_price = block["rateInfo"]["priceAmount"]
    block_headstart = block["startTime"] - int(time.time())
    block_rate = block_price / block_length
    return (
        not block["hidden"]
        and block_rate > 18
    )

def baserate_filter(block):
    # Comment out the second line if you want to print base rate
    block_length = (block["endTime"] - block["startTime"]) / 3600
    block_price = block["rateInfo"]["priceAmount"]
    block_headstart = block["startTime"] - int(time.time())
    block_rate = block_price / block_length
    return (
        #not block["hidden"]
        block_rate == 18
    )
