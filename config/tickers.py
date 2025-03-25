# config/tickers.py
"""
股票代码配置文件
数据来源：NASDAQ官网/恒生指数公司/中证指数公司
更新频率：建议每季度更新一次
"""

# 美股市场---------------------------------------------------------------------
# NASDAQ 100指数成分股（按市值排序）
NASDAQ_100 = [
    'AAPL',   # 苹果 (Apple Inc.) - 市值约$2.7万亿
    'MSFT',   # 微软 (Microsoft) - 市值约$2.4万亿
    'AMZN',   # 亚马逊 (Amazon) - 市值约$1.3万亿
    'NVDA',   # 英伟达 (NVIDIA) - 市值约$1.1万亿
    'GOOGL',  # Alphabet A类股 (Google) - 市值约$1.6万亿
    'META',   # Meta Platforms (Facebook) - 市值约$8000亿
    'TSLA',   # 特斯拉 (Tesla) - 市值约$8000亿
    'AVGO',   # 博通 (Broadcom) - 市值约$5000亿
    'PEP',    # 百事公司 (PepsiCo) - 市值约$2500亿
    'COST',   # 好市多 (Costco) - 市值约$2500亿
    'CSCO',   # 思科 (Cisco) - 市值约$2000亿
    'ADBE',   # Adobe - 市值约$2000亿
    'AMD',    # 超威半导体 (AMD) - 市值约$1800亿
    'INTC',   # 英特尔 (Intel) - 市值约$1400亿
    'TMUS',   # T-Mobile US - 市值约$1700亿
    'CMCSA',  # 康卡斯特 (Comcast) - 市值约$1600亿
    'QCOM',   # 高通 (Qualcomm) - 市值约$1500亿
    'AMGN',   # 安进 (Amgen) - 市值约$1400亿
    'SBUX',   # 星巴克 (Starbucks) - 市值约$1200亿
    'INTU',   # Intuit (TurboTax母公司) - 市值约$1400亿
    'ISRG',   # 直觉外科 (达芬奇手术机器人) - 市值约$1200亿
    'REGN',   # 再生元制药 (Regeneron) - 市值约$900亿
    'GILD',   # 吉利德科学 (Gilead) - 市值约$1000亿
    'VRTX',   # Vertex制药 (囊性纤维化药物龙头) - 市值约$900亿
    'MRNA',   # Moderna (新冠疫苗厂商) - 市值约$400亿
    'BKNG',   # Booking Holdings (Booking.com母公司) - 市值约$1000亿
    'ADP',    # 自动数据处理公司 (人力资源服务) - 市值约$1000亿
    'LRCX',   # 泛林集团 (半导体设备) - 市值约$1000亿
    'PANW',   # Palo Alto Networks (网络安全) - 市值约$800亿
    'SNPS',   # 新思科技 (芯片设计软件) - 市值约$700亿
    'ASML',   # ASML Holding (光刻机巨头) - 市值约$3000亿
    'MNST',   # 怪物饮料 (Monster Energy) - 市值约$600亿
    'MELI',   # MercadoLibre (拉美电商巨头) - 市值约$600亿
    'CHTR',   # Charter通信 (电信服务) - 市值约$600亿
    'MDLZ',   # 亿滋国际 (零食巨头，奥利奥母公司) - 市值约$900亿
    'FISV',   # Fiserv (金融科技) - 市值约$700亿
    'CSX',    # CSX运输 (铁路货运) - 市值约$700亿
    'CTSH',   # 高知特 (Cognizant，IT服务) - 市值约$350亿
    'KLAC',   # 科磊 (KLA，半导体检测设备) - 市值约$600亿
    'MAR',    # 万豪国际 (酒店集团) - 市值约$600亿
    'PDD',    # 拼多多 (中国电商) - 市值约$1200亿
    'DXCM',   # Dexcom (血糖监测设备) - 市值约$500亿
    'IDXX',   # IDEXX (动物诊断设备) - 市值约$400亿
    'BIIB',   # 百健 (Biogen，阿尔茨海默药物) - 市值约$350亿
    'FAST',   # Fastenal (工业零件分销) - 市值约$350亿
    'CDNS',   # Cadence Design Systems (电子设计自动化) - 市值约$700亿
    'KDP',    # Keurig Dr Pepper (饮料公司) - 市值约$450亿
    'ADSK',   # Autodesk (工业设计软件) - 市值约$500亿
    'CPRT',   # Copart (二手车拍卖平台) - 市值约$400亿
    'ROST',   # Ross Stores (折扣零售商) - 市值约$400亿
    'AEP',    # 美国电力公司 (American Electric Power) - 市值约$450亿
    'EXC',    # Exelon (公用事业) - 市值约$450亿
    'NXPI',   # 恩智浦半导体 (NXP Semiconductors) - 市值约$500亿
    'PAYX',   # Paychex (人力资源服务) - 市值约$400亿
    'XEL',    # Xcel Energy (能源公司) - 市值约$400亿
    'DLTR',   # 美元树 (Dollar Tree) - 市值约$300亿
    'CTAS',   # 信达思 (Cintas，企业制服服务) - 市值约$500亿
    'WBA',    # 沃尔格林联合博姿 (Walgreens Boots Alliance) - 市值约$250亿
    'EBAY',   # eBay - 市值约$250亿
    'BKR',    # 贝克休斯 (油田服务) - 市值约$300亿
    'ANSS',   # ANSYS (工程仿真软件) - 市值约$300亿
    'MTCH',   # Match Group (Tinder母公司) - 市值约$100亿
    'SGEN',   # Seagen (癌症药物，2023年被辉瑞收购)
    'SIRI',   # Sirius XM (卫星广播) - 市值约$200亿
    'VRSN',   # VeriSign (域名注册商) - 市值约$200亿
    'ILMN',   # Illumina (基因测序) - 市值约$300亿
    'SWKS',   # Skyworks Solutions (射频芯片) - 市值约$150亿
    'INCY',   # Incyte (生物制药) - 市值约$130亿
    'ZM',     # Zoom视频通讯 - 市值约$200亿
    'LULU',   # Lululemon (运动服饰) - 市值约$400亿
    'OKTA',   # Okta (身份验证服务) - 市值约$100亿
    'TEAM',   # Atlassian (协作软件) - 市值约$500亿
    'CRWD',   # CrowdStrike (网络安全) - 市值约$400亿
    'ZS',     # Zscaler (云安全) - 市值约$200亿
    'DDOG',   # Datadog (云监控) - 市值约$300亿
    'FTNT',   # Fortinet (防火墙) - 市值约$400亿
    'LCID',   # Lucid Group (电动汽车) - 市值约$150亿
    'RIVN',   # Rivian Automotive (电动卡车) - 市值约$200亿
    # 注：部分公司可能因并购或市值变动被调整出指数
]
