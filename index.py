import urllib.request
import requests
import binanceAPI


print('CryptoBot v1')

VERBOSE = False
lotsSize = {"ETHBTC": [0.001, 0.000001, 0.001], "LTCBTC": [0.01, 0.000001, 0.001], "BNBBTC": [1, 0.00000001, 0.001], "NEOBTC": [0.01, 0.000001, 0.001], "GASBTC": [0.01, 0.000001, 0.001], "BCCBTC": [0.001, 0.000001, 0.001], "MCOBTC": [0.01, 0.000001, 0.001], "WTCBTC": [1, 0.00000001, 0.001], "QTUMBTC": [0.01, 0.000001, 0.001], "OMGBTC": [0.01, 0.000001, 0.001], "ZRXBTC": [1, 0.00000001, 0.001], "STRATBTC": [0.01, 0.000001, 0.001], "SNGLSBTC": [1, 0.00000001, 0.001], "BQXBTC": [1, 0.00000001, 0.001], "KNCBTC": [1, 0.00000001, 0.001], "FUNBTC": [1, 0.00000001, 0.001], "SNMBTC": [1, 0.00000001, 0.001], "LINKBTC": [1, 0.00000001, 0.001], "XVGBTC": [1, 0.00000001, 0.001], "CTRBTC": [1, 0.00000001, 0.001], "SALTBTC": [0.01, 0.000001, 0.001], "IOTABTC": [1, 0.00000001, 0.001], "MDABTC": [1, 0.00000001, 0.001], "MTLBTC": [1, 0.000001, 0.001], "SUBBTC": [1, 0.00000001, 0.001], "EOSBTC": [1, 0.00000001, 0.001], "SNTBTC": [1, 0.00000001, 0.001], "ETCBTC": [0.01, 0.000001, 0.001], "MTHBTC": [1, 0.00000001, 0.001], "ENGBTC": [1, 0.00000001, 0.001], "DNTBTC": [1, 0.00000001, 0.001], "BNTBTC": [1, 0.00000001, 0.001], "ASTBTC": [1, 0.00000001, 0.001], "DASHBTC": [0.001, 0.000001, 0.001], "ICNBTC": [1, 0.00000001, 0.001], "OAXBTC": [1, 0.00000001, 0.001], "BTGBTC": [0.01, 0.000001, 0.001], "EVXBTC": [1, 0.00000001, 0.001], "REQBTC": [1, 0.00000001, 0.001], "LRCBTC": [1, 0.00000001, 0.001], "VIBBTC": [1, 0.00000001, 0.001], "HSRBTC": [1, 0.000001, 0.001], "TRXBTC": [1, 0.00000001, 0.001], "POWRBTC": [1, 0.00000001, 0.001], "ARKBTC": [0.01, 0.0000001, 0.001], "YOYOBTC": [1, 0.00000001, 0.001], "XRPBTC": [1, 0.00000001, 0.001], "MODBTC": [1, 0.0000001, 0.001], "ENJBTC": [1, 0.00000001, 0.001], "STORJBTC": [1, 0.00000001, 0.001], "VENBTC": [1, 0.00000001, 0.001], "KMDBTC": [1, 0.0000001, 0.001], "RCNBTC": [1, 0.00000001, 0.001], "NULSBTC": [1, 0.00000001, 0.001], "RDNBTC": [1, 0.00000001, 0.001], "XMRBTC": [0.001, 0.000001, 0.001], "DLTBTC": [0.001, 0.00000001, 0.001], "AMBBTC": [0.001, 0.00000001, 0.001], "BATBTC": [1, 0.00000001, 0.001], "ZECBTC": [0.001, 0.000001, 0.001], "BCPTBTC": [1, 0.00000001, 0.001], "ARNBTC": [1, 0.00000001, 0.001], "GVTBTC": [0.01, 0.0000001, 0.001], "CDTBTC": [1, 0.00000001, 0.001], "GXSBTC": [0.01, 0.0000001, 0.001], "POEBTC": [1, 0.00000001, 0.001], "QSPBTC": [1, 0.00000001, 0.001], "BTSBTC": [1, 0.00000001, 0.001], "XZCBTC": [0.01, 0.000001, 0.001], "LSKBTC": [0.01, 0.0000001, 0.001], "TNTBTC": [1, 0.00000001, 0.001], "FUELBTC": [1, 0.00000001, 0.001], "MANABTC": [1, 0.00000001, 0.001], "BCDBTC": [0.001, 0.000001, 0.001], "DGDBTC": [0.001, 0.000001, 0.001], "ADXBTC": [1, 0.00000001, 0.001], "ADABTC": [1, 0.00000001, 0.001], "PPTBTC": [0.01, 0.0000001, 0.001], "CMTBTC": [1, 0.00000001, 0.001], "XLMBTC": [1, 0.00000001, 0.001], "CNDBTC": [1, 0.00000001, 0.001], "LENDBTC": [1, 0.00000001, 0.001], "WABIBTC": [1, 0.00000001, 0.001], "TNBBTC": [1, 0.00000001, 0.001], "WAVESBTC": [0.01, 0.000001, 0.001], "ICXBTC": [0.01, 0.0000001, 0.001], "GTOBTC": [1, 0.00000001, 0.001], "OSTBTC": [1, 0.00000001, 0.001], "ELFBTC": [1, 0.00000001, 0.001], "AIONBTC": [0.01, 0.0000001, 0.001], "NEBLBTC": [0.01, 0.0000001, 0.001], "BRDBTC": [1, 0.00000001, 0.001], "EDOBTC": [0.01, 0.0000001, 0.001], "WINGSBTC": [1, 0.00000001, 0.001], "NAVBTC": [0.01, 0.0000001, 0.001], "LUNBTC": [0.01, 0.0000001, 0.001], "TRIGBTC": [0.01, 0.0000001, 0.001], "APPCBTC": [1, 0.00000001, 0.001], "VIBEBTC": [1, 0.00000001, 0.001], "RLCBTC": [0.01, 0.0000001, 0.001], "INSBTC": [0.01, 0.0000001, 0.001], "PIVXBTC": [0.01, 0.0000001, 0.001], "IOSTBTC": [1, 0.00000001, 0.001], "CHATBTC": [1, 0.00000001, 0.001], "STEEMBTC": [0.01, 0.0000001, 0.001], "NANOBTC": [0.01, 0.0000001, 0.001], "VIABTC": [0.01, 0.0000001, 0.001], "BLZBTC": [1, 0.00000001, 0.001], "AEBTC": [0.01, 0.0000001, 0.001], "RPXBTC": [1, 0.00000001, 0.001], "NCASHBTC": [1, 0.00000001, 0.001], "POABTC": [1, 0.00000001, 0.001], "ZILBTC": [1, 0.00000001, 0.001], "ONTBTC": [1, 0.00000001, 0.001], "BNBETH": [1, 0.00000001, 0.01], "QTUMETH": [0.01, 0.000001, 0.01], "SNTETH": [1, 0.00000001, 0.01], "BNTETH": [0.01, 0.000001, 0.01], "EOSETH": [0.01, 0.000001, 0.01], "OAXETH": [1, 0.0000001, 0.01], "DNTETH": [1, 0.00000001, 0.01], "MCOETH": [0.01, 0.000001, 0.01], "ICNETH": [1, 0.0000001, 0.01], "WTCETH": [0.01, 0.000001, 0.01], "OMGETH": [0.01, 0.000001, 0.01], "ZRXETH": [1, 0.00000001, 0.01], "STRATETH": [0.01, 0.000001, 0.01], "SNGLSETH": [1, 0.00000001, 0.01], "BXQETH": [1, 0.0000001, 0.01], "KNCETH": [1, 0.0000001, 0.01], "FUNETH": [1, 0.00000001, 0.01], "SNMETH": [1, 0.00000001, 0.01], "NEOETH": [0.01, 0.00000001, 0.01], "LINKETH": [1, 0.00000001, 0.01], "XVGETH": [1, 0.00000001, 0.01], "CTRETH": [1, 0.0000001, 0.01], "SALTETH": [0.01, 0.000001, 0.01], "IOTAETH": [1, 0.00000001, 0.01], "MDAETH": [1, 0.0000001, 0.01], "MTLETH": [1, 0.000001, 0.01], "SUBETH": [1, 0.00000001, 0.01], "ETCETH": [0.01, 0.000001, 0.01], "MTHETH": [1, 0.00000001, 0.01], "ENGETH": [1, 0.0000001, 0.01], "ASTETH": [1, 0.0000001, 0.01], "DASHETH": [0.001, 0.00001, 0.01], "BTGETH": [0.01, 0.000001, 0.01], "EVXETH": [1, 0.0000001, 0.01], "REQETH": [1, 0.00000001, 0.01], "LRCETH": [1, 0.00000001, 0.01], "VIBETH": [1, 0.00000001, 0.01], "HSRETH": [0.01, 0.000001, 0.01], "TRXETH": [1, 0.00000001, 0.01], "POWRETH": [1, 0.00000001, 0.01], "ARKETH": [0.01, 0.000001, 0.01], "YOYOETH": [1, 0.00000001, 0.01], "XRPETH": [1, 0.00000001, 0.01], "MODETH": [1, 0.000001, 0.01], "ENJETH": [1, 0.00000001, 0.01], "STORJETH": [1, 0.0000001, 0.01], "VENETH": [1, 0.00000001, 0.01], "KMDETH": [1, 0.000001, 0.01], "RCNETH": [1, 0.00000001, 0.01], "NULSETH": [1, 0.00000001, 0.01], "RDNETH": [1, 0.0000001, 0.01], "XMRETH": [1, 0.00001, 0.01], "DLTETH": [1, 0.00000001, 0.01], "AMBETH": [1, 0.00000001, 0.01], "BCCETH": [1, 0.00001, 0.01], "BATETH": [1, 0.00000001, 0.01], "ZECETH": [0.001, 0.00001, 0.01], "BCPTETH": [1, 0.00000001, 0.01], "ARNETH": [1, 0.00000001, 0.01], "GVTETH": [0.01, 0.000001, 0.01], "CDTETH": [1, 0.00000001, 0.01], "GXSETH": [0.01, 0.000001, 0.01], "POEETH": [1, 0.00000001, 0.01], "QSPETH": [1, 0.00000001, 0.01], "BTSETH": [1, 0.00000001, 0.01], "XZCETH": [0.01, 0.000001, 0.01], "LSKETH": [0.01, 0.000001, 0.01], "TNTETH": [1, 0.00000001, 0.01], "FUELETH": [1, 0.00000001, 0.01], "MANAETH": [1, 0.00000001, 0.01], "BCDETH": [0.001, 0.00001, 0.01], "DGDETH": [0.001, 0.00001, 0.01], "ADXETH": [1, 0.0000001, 0.01], "ADAETH": [1, 0.00000001, 0.01], "PPTETH": [1, 0.000001, 0.01], "CMTETH": [1, 0.00000001, 0.01], "XLMETH": [1, 0.00000001, 0.01], "CNDETH": [1, 0.00000001, 0.01], "LENDETH": [1, 0.00000001, 0.01], "WABIETH": [1, 0.00000001, 0.01], "LTCETH": [0.001, 0.00001, 0.01], "TNBETH": [1, 0.00000001, 0.01], "WAVESETH": [0.01, 0.000001, 0.01], "ICXETH": [0.01, 0.000001, 0.01], "GTOETH": [1, 0.00000001, 0.01], "OSTETH": [1, 0.00000001, 0.01], "ELFETH": [1, 0.00000001, 0.01], "AIONETH": [0.01, 0.000001, 0.01], "NEBLETH": [0.01, 0.000001, 0.01], "BRDETH": [1, 0.0000001, 0.01], "EDOETH": [0.01, 0.000001, 0.01], "WINGSETH": [1, 0.0000001, 0.01], "NAVETH": [0.01, 0.000001, 0.01], "LUNETH": [0.01, 0.000001, 0.01], "TRIGETH": [0.01, 0.000001, 0.01], "APPCETH": [1, 0.0000001, 0.01], "VIBEETH": [1, 0.0000001, 0.01], "RLCETH": [0.01, 0.000001, 0.01], "INSETH": [0.01, 0.000001, 0.01], "PIVXETH": [0.01, 0.000001, 0.01], "IOSTETH": [1, 0.00000001, 0.01], "CHATETH": [1, 0.00000001, 0.01], "STEEMETH": [0.01, 0.000001, 0.01], "NANOETH": [0.01, 0.000001, 0.01], "VIAETH": [0.01, 0.000001, 0.01], "BLZETH": [1, 0.00000001, 0.01], "AEETH": [0.01, 0.000001, 0.01], "RPXETH": [1, 0.00000001, 0.01], "NCASHETH": [1, 0.00000001, 0.01], "POAETH": [1, 0.00000001, 0.01], "ZILETH": [1, 0.00000001, 0.01], "ONTETH": [1, 0.00000001, 0.01], "VENBNB": [0.01, 0.0001, 1], "YOYOBNB": [0.01, 0.00001, 1], "POWRBNB": [0.01, 0.0001, 1], "NULSBNB": [0.01, 0.00001, 1], "RCNBNB": [0.01, 0.00001, 1], "RDNBNB": [0.01, 0.00001, 1], "DLTBNB": [0.01, 0.00001, 1], "WTCBNB": [0.01, 0.00001, 1], "AMBBNB": [0.01, 0.00001, 1], "BCCBNB": [0.00001, 0.01, 1], "BATBNB": [0.01, 0.00001, 1], "BCPTBNB": [0.01, 0.00001, 1], "NEOBNB": [0.001, 0.001, 1], "QSPBNB": [0.01, 0.00001, 1], "BTSBNB": [0.01, 0.00001, 1], "XZCBNB": [0.001, 0.001, 1], "LSKBNB": [0.001, 0.0001, 1], "IOTABNB": [0.01, 0.00001, 1], "ADXBNB": [0.01, 0.00001, 1], "CMTBNB": [0.01, 0.00001, 1], "XLMBNB": [0.01, 0.00001, 1], "CNDBNB": [0.01, 0.00001, 1], "WABIBNB": [0.01, 0.00001, 1], "LTCBNB": [0.00001, 0.01, 1], "WAVESBNB": [0.01, 0.0001, 1], "ICXBNB": [0.01, 0.00001, 1], "GTOBNB": [0.01, 0.00001, 1], "OSTBNB": [0.01, 0.00001, 1], "AIONBNB": [0.01, 0.00001, 1], "NEBLBNB": [0.01, 0.00001, 1], "BRDBNB": [0.01, 0.00001, 1], "MCOBNB": [0.01, 0.00001, 1], "NAVBNB": [0.01, 0.00001, 1], "TRIGBNB": [0.01, 0.00001, 1], "APPCBNB": [0.01, 0.00001, 1], "RLCBNB": [0.01, 0.00001, 1], "PIVXBNB": [0.01, 0.00001, 1], "STEEMBNB": [0.01, 0.00001, 1], "NANOBNB": [0.01, 0.0001, 1], "VIABNB": [0.01, 0.00001, 1], "BLZBNB": [0.01, 0.00001, 1], "AEBNB": [0.01, 0.00001, 1], "RPXBNB": [0.01, 0.00001, 1], "NCASHBNB": [0.01, 0.00001, 1], "POABNB": [0.01, 0.00001, 1], "ZILBNB": [0.01, 0.00001, 1], "ONTBNB": [0.01, 0.00001, 1], "BTCUSDT": [0.000001, 0.01, 10], "ETHUSDT": [0.00001, 0.01, 10], "BNBUSDT": [0.01, 0.0001, 10], "BCCUSDT": [0.00001, 0.01, 10], "NEOUSDT": [0.001, 0.001, 10], "LTCUSDT": [0.00001, 0.01, 10]}
pairsList = []
currencies = ["USDT" ,"BNB" ,"BCPT" ,"OST" ,"NEO" ,"XRP" ,"APPC" ,"LTC" ,"BTC" ,"ETH" ,"BCC" ,"BTM" ,"PIVX" ,"HCC" ,"HSR" ,"OAX" ,"DNT" ,"MCO" ,"ICN" ,"ZRX" ,"OMG" ,"WTC" ,"LRC" ,"LLT" ,"YOYO" ,"TRX" ,"STRAT" ,"SNGLS" ,"BQX" ,"KNC" ,"SNM" ,"FUN" ,"LINK" ,"XVG" ,"CTR" ,"SALT" ,"MDA" ,"IOTA" ,"SUB" ,"ETC" ,"MTL" ,"MTH" ,"ENG" ,"AST" ,"DASH" ,"BTG" ,"EVX" ,"REQ" ,"VIB" ,"POWR" ,"ARK" ,"QTUM" ,"MOD" ,"ENJ" ,"STORJ" ,"VEN" ,"KMD" ,"RCN" ,"NULS" ,"RDN" ,"XMR" ,"EOS" ,"AMB" ,"BAT" ,"ZEC" ,"SNT" ,"ARN" ,"GVT" ,"CDT" ,"GXS" ,"POE" ,"QSP" ,"BTS" ,"LSK" ,"XZC" ,"TNT" ,"FUEL" ,"MANA" ,"BCD" ,"DGD" ,"ADX" ,"ADA" ,"PPT" ,"CMT" ,"XLM" ,"CND" ,"LEND" ,"WABI" ,"SBTC" ,"BCX" ,"WAVES" ,"TNB" ,"GTO" ,"ICX" ,"BNT" ,"ELF" ,"AION" ,"LUN" ,"ONT" ,"NCASH" ,"BRD" ,"BLZ" ,"AE" ,"STEEM" ,"RLC" ,"ZIL" ,"VIBE" ,"POA" ,"NEBL" ,"RPX" ,"VIA" ,"NANO" ,"ETF" ,"IOST" ,"INS" ,"CHAT" ,"EDO" ,"NAV" ,"WINGS" ,"TRIG" ,"GAS" ,"DLT"]
# https://www.binance.com/userCenter/depositWithdraw.html
# out = '[';for (var i = 0; i < document.getElementsByClassName("coin").length; i++){ out += '"' + document.getElementsByClassName("coin")[i].innerText + '" ,'; } out += ']'; console.log(out);

# First, find a good opportunity (euristic)
while True:
    pairs = {}
    grabPairs = binanceAPI.prices()
    for pairSymbol in grabPairs:
        pairPrice = grabPairs[pairSymbol]
        
        if pairSymbol not in pairsList:
            pairsList.append(pairSymbol)
            
        for currency in currencies:
            index = pairSymbol.find(currency)
            if index != -1:
                if index == 0:
                    symbol = [pairSymbol[len(currency):], pairSymbol[0:len(currency)]]
                else:
                    symbol = [pairSymbol[index:], pairSymbol[:-len(currency)]]


                if (symbol[0] not in pairs):
                    pairs[symbol[0]] = {}
                if (symbol[1] not in pairs):
                    pairs[symbol[1]] = {}
                pairs[symbol[0]][symbol[1]] = float(pairPrice)
                pairs[symbol[1]][symbol[0]] = 1/float(pairPrice)
                break

    # Find best path
    proxies = ['BTC', '', '']
    bestReturn = [['', '', ''], 0]
    for pair1 in pairs[proxies[0]]:
        proxies[1] = pair1
        for pair2 in pairs[proxies[1]]:
            proxies[2] = pair2
            if (proxies[1] in pairs[proxies[0]]
                and proxies[2] in pairs[proxies[1]]
                and proxies[0] in pairs[proxies[2]]):
                simulated = 1
                simulated = (simulated / pairs[proxies[0]][proxies[1]]) * 0.9995
                simulated = (simulated / pairs[proxies[1]][proxies[2]]) * 0.9995
                simulated = (simulated / pairs[proxies[2]][proxies[0]]) * 0.9995
                if (simulated > bestReturn[1]):
                    bestReturn[1] = simulated
                    bestReturn[0] = [proxies[0], proxies[1], proxies[2]]
                    
    profit = (bestReturn[1] - 1) * 100

    # Real
    if profit >= 1.1:
        balance = 1
        

        for symbols in [[0, 1], [1, 2], [2, 0]]:
            if bestReturn[0][symbols[0]] + bestReturn[0][symbols[1]] in pairsList:
                side = 'sell'
                symbol = bestReturn[0][symbols[0]] + bestReturn[0][symbols[1]]
            else:
                side = 'buy'
                symbol = bestReturn[0][symbols[1]] + bestReturn[0][symbols[0]]


            depth = binanceAPI.depth(symbol)
            bid = float(list(depth['bids'])[0])
            ask = float(list(depth['asks'])[0])
            price = bid if side == 'buy' else ask
            qtt = balance / price
            balance = qtt * price * 0.9995

            if (VERBOSE):
                print('    ' + side + ' ' + symbol + ' at price ' + str(price))
        if balance*100-100 > -0.149:
            print(bestReturn[0])
            print('  Income: ' + str(balance*100-100) + ' %')

        

