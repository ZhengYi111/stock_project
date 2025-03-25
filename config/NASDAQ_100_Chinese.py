import pandas as pd

# 创建纳斯达克100指数成分股的数据
data = {
'Bank Ticker': [
'AAPL', 'MSFT', 'AMZN', 'GOOG', 'META', 'NVDA', 'TSLA', 'PYPL', 'INTC', 'CSCO',
'CMCSA', 'QCOM', 'AMD', 'GILD', 'ATVI', 'BIIB', 'AMGN', 'IDXX', 'REGN', 'ALXN',
'ISRG', 'ILMN', 'EXPE', 'MAR', 'BKNG', 'LULU', 'PTON', 'ZM', 'DOCU', 'SNPS',
'CDNS', 'KLAC', 'TER', 'LRCX', 'ASML', 'NXPI', 'SWKS', 'QRVO', 'AVGO', 'TXN',
'STM', 'ON', 'MU', 'WDC', 'STX', 'CSX', 'NSC', 'UNP', 'CARR', 'OTIS', 'CSX',
'NSC', 'UNP', 'CARR', 'OTIS', 'NDAQ', 'ICE', 'CME', 'SPGI', 'MSCI', 'INFO',
'FIS', 'FISV', 'PAYX', 'FLT', 'GPN', 'EFX', 'EXLS', 'CTSH', 'EPAM', 'IT',
'STT', 'BK', 'TROW', 'BEN', 'AMP', 'BLK', 'IVZ', 'VTV', 'VYM', 'SCHD', 'DVY',
'HDV', 'SDY', 'NOBL', 'SPHD', 'SCHG', 'SCHV', 'SCHA', 'SCHB', 'SLYG', 'SLYV',
'QQQ', 'QQQM', 'QQQJ', 'QQQE', 'QQQX', 'QQQY', 'TQQQ', 'SQQQ', 'QLD', 'QID',
'PSQ'
],
'Chinese Name': [
'苹果', '微软', '亚马逊', '谷歌', '脸书', '英伟达', '特斯拉', '贝宝',
'英特尔', '思科', '康卡斯特', '高通', '超威半导体', '吉列德科学', '动视暴雪',
'百时美施贵宝', '安进', 'IDEXX实验室', '瑞金制药', 'Alexion制药', 'Intuitive Surgical',
'Illumina', 'Expedia集团', '万豪国际集团', 'Booking Holdings', 'Lululemon', 'Peloton',
'Zoom', 'DocuSign', 'Synopsys', 'Cadence Design Systems', 'KLA', 'Teradyne',
'Lam Research', '阿斯麦', 'NXP半导体', 'Skyworks Solutions', 'Qorvo', '博通',
'德州仪器', '意法半导体', 'ON Semiconductor', '美光科技', '西部数据', '希捷科技',
'CSX', '诺福克南方', '联合太平洋', 'Carrier', 'Otis Worldwide', 'CSX',
'诺福克南方', '联合太平洋', 'Carrier', 'Otis Worldwide', '纳斯达克', '洲际交易所',
'CME集团', '标普全球', 'MSCI', 'IHS Markit', 'FIS', 'Fiserv', 'Paychex',
'Fleetcor', 'Global Payments', 'EQUIFAX', 'ExlService', 'Cognizant', 'EPAM Systems',
'Gartner', 'State Street', 'BNY Mellon', 'T. Rowe Price', 'Franklin Templeton',
'Ameriprise', '贝莱德', 'Invesco', 'Vanguard Value ETF', 'Vanguard High Dividend Yield ETF',
'Schwab U.S. Dividend Equity ETF', 'iShares Select Dividend ETF', 'iShares High Dividend Equity Fund',
'SPDR S&P Dividend ETF', 'ProShares S&P 500 Dividend Aristocrats ETF', 'Invesco S&P 500 High Dividend Low Volatility ETF',
'Schwab U.S. Large-Cap Growth ETF', 'Schwab U.S. Large-Cap Value ETF', 'Schwab U.S. Small-Cap ETF',
'Schwab U.S. Broad Market ETF', 'SPDR S&P 1500 Growth ETF', 'SPDR S&P 1500 Value ETF', 'Invesco QQQ Trust ETF',
'Invesco NASDAQ 100 ETF', 'Invesco NASDAQ Next Gen 100 ETF', 'First Trust NASDAQ-100 Equal Weighted Index Fund',
'Nuveen NASDAQ-100 Dynamic Overwrite Fund', 'Global X NASDAQ-100 Covered Call & Growth ETF', 'ProShares UltraPro QQQ',
'ProShares UltraShort QQQ', 'ProShares Ultra QQQ', 'ProShares UltraShort QQQ', 'ProShares Short QQQ'
]
}

# 创建DataFrame
NASDAQ_100_Chinese = pd.DataFrame(data)

# 显示DataFrame
NASDAQ_100_Chinese