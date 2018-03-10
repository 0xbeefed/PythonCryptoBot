import websocket
import json
from threading import Thread
import matplotlib.pyplot as plt
import urllib.request

def plotDepth(graph):
    for orderType in ['bids', 'asks']:
        colors = {'bids': 'g', 'asks': 'r'}
        coords = [[float(x[0]) for x in graph[orderType]], [], 0]
        for y in graph[orderType]:
            coords[2] += float(y[1])
            coords[1].append(coords[2])
        plt.plot(coords[0], coords[1], colors[orderType])
    plt.ylabel('Order book')
    plt.show()

url = 'https://www.binance.com/api/v1/depth?symbol=BTCUSDT'
depthGraph = json.loads(urllib.request.urlopen(url).read().decode('utf8'))
plotDepth(depthGraph)
