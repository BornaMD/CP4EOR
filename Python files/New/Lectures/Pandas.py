import numpy as np
import pandas as pd
import math
import scipy
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup


#res = requests.get("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv")
#soup = BeautifulSoup(res.content, '')

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
chipo = pd.read_csv(url, sep = '\t')

first_view = pd.head(chipo, 10)

chipo.count()
chipo.describe()
##
chipo.shape[0]
chipo.info()

chipo.shape[1]

