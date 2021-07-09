import matplotlib.pyplot as plt
import base64
from io import BytesIO
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import numpy as np

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph
    
def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(16,8))
    plt.cla()
    plt.plot(x,y)
    plt.locator_params(axis='x', nbins=10)
    plt.xticks(rotation=90)
    plt.gca().set_xlim(left=(len(x)-10),right=len(x))
    plt.tight_layout()
    graph = get_graph()
    return graph
