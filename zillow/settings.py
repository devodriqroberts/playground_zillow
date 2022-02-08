# Scrapy settings for zillow project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zillow'

SPIDER_MODULES = ['zillow.spiders']
NEWSPIDER_MODULE = 'zillow.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 10
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zillow.middlewares.ZillowSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zillow.middlewares.ZillowDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
# #    'zillow.pipelines.ZillowImagePipeline': 1,
#    'zillow.pipelines.SaveZillowHousePipeline': 100,
#    'zillow.pipelines.DuplicatesPipeline': 300,
# }

# IMAGES_STORE = "."

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

DB_CONNECTION_STRING = "sqlite:///zillow_houses.db"

ZILLOW_CITIES_DICT = {
    'Atlanta': 'https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState={"pagination":{"currentPage":1},"usersSearchTerm":"Atlanta,%20GA","mapBounds":{"west":-84.73523648339844,"east":-84.22574551660156,"south":33.671398471115744,"north":33.876873347414715},"regionSelection":[{"regionId":37211,"regionType":6}],"isMapVisible":true,"filterState":{"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":true},"isCondo":{"value":false},"isMultiFamily":{"value":false},"isManufactured":{"value":false},"isLotLand":{"value":false},"isTownhouse":{"value":false},"isApartment":{"value":false},"isApartmentOrCondo":{"value":false}},"isListVisible":true,"mapZoom":11}&wants={"cat1":["listResults","mapResults"],"cat2":["total"]}&requestId=4',
    'Miami': 'https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState={"pagination":{"currentPage":1},"usersSearchTerm":"Miami, FL","mapBounds":{"west":-80.5720313803711,"east":-80.02340161962891,"south":25.46001179611515,"north":25.991992347926896},"mapZoom":11,"regionSelection":[{"regionId":12700,"regionType":6}],"isMapVisible":false,"filterState":{"isCondo":{"value":false},"isApartment":{"value":false},"isMultiFamily":{"value":false},"isAllHomes":{"value":true},"sortSelection":{"value":"globalrelevanceex"},"isLotLand":{"value":false},"isTownhouse":{"value":false},"isManufactured":{"value":false},"isApartmentOrCondo":{"value":false}},"isListVisible":true}&wants={"cat1":["listResults"],"cat2":["total"]}&requestId=2',
    'Los Angeles': 'https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState={"pagination":{"currentPage":1},"usersSearchTerm":"Los Angeles, CA","mapBounds":{"west":-119.05923921386719,"east":-117.76422578613281,"south":33.530224675404185,"north":34.509093731577615},"regionSelection":[{"regionId":12447,"regionType":6}],"isMapVisible":false,"filterState":{"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":true},"isCondo":{"value":false},"isMultiFamily":{"value":false},"isManufactured":{"value":false},"isLotLand":{"value":false},"isTownhouse":{"value":false},"isApartment":{"value":false},"isApartmentOrCondo":{"value":false}},"isListVisible":true}&wants={"cat1":["listResults"],"cat2":["total"]}&requestId=4',
    'Houston': 'https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState={"pagination":{"currentPage":1},"usersSearchTerm":"Houston, TX","mapBounds":{"west":-95.788087,"east":-95.060608,"south":29.523624,"north":30.110732},"regionSelection":[{"regionId":39051,"regionType":6}],"isMapVisible":false,"filterState":{"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":true},"isCondo":{"value":false},"isMultiFamily":{"value":false},"isManufactured":{"value":false},"isLotLand":{"value":false},"isTownhouse":{"value":false},"isApartment":{"value":false},"isApartmentOrCondo":{"value":false}},"isListVisible":true}&wants={"cat1":["listResults"],"cat2":["total"]}&requestId=2',
    'Dallas': 'https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState={"pagination":{"currentPage":1},"usersSearchTerm":"Dallas, TX","mapBounds":{"west":-96.999347,"east":-96.555516,"south":32.618763,"north":33.016646},"regionSelection":[{"regionId":38128,"regionType":6}],"isMapVisible":false,"filterState":{"isCondo":{"value":false},"isApartment":{"value":false},"isMultiFamily":{"value":false},"isAllHomes":{"value":true},"sortSelection":{"value":"globalrelevanceex"},"isLotLand":{"value":false},"isTownhouse":{"value":false},"isManufactured":{"value":false},"isApartmentOrCondo":{"value":false}},"isListVisible":true}&wants={"cat1":["listResults"],"cat2":["total"]}&requestId=2',
    'New York': 'https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState={"pagination":{"currentPage":1},"usersSearchTerm":"New York, NY","mapBounds":{"west":-74.25909,"east":-73.700272,"south":40.477399,"north":40.917577},"regionSelection":[{"regionId":6181,"regionType":6}],"isMapVisible":false,"filterState":{"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":true},"isCondo":{"value":false},"isMultiFamily":{"value":false},"isManufactured":{"value":false},"isLotLand":{"value":false},"isTownhouse":{"value":false},"isApartment":{"value":false},"isApartmentOrCondo":{"value":false}},"isListVisible":true}&wants={"cat1":["listResults"],"cat2":["total"]}&requestId=2',
    'San Diego': 'https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState={"pagination":{"currentPage":1},"usersSearchTerm":"San Diego, CA","mapBounds":{"west":-117.309797,"east":-116.90816,"south":32.534175,"north":33.114249},"regionSelection":[{"regionId":54296,"regionType":6}],"isMapVisible":false,"filterState":{"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":true},"isCondo":{"value":false},"isMultiFamily":{"value":false},"isManufactured":{"value":false},"isLotLand":{"value":false},"isTownhouse":{"value":false},"isApartment":{"value":false},"isApartmentOrCondo":{"value":false}},"isListVisible":true}&wants={"cat1":["listResults"],"cat2":["total"]}&requestId=2',
    'Nashville': 'https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState={"pagination":{"currentPage":1},"usersSearchTerm":"Nashville, TN","mapBounds":{"west":-87.054903,"east":-86.515588,"south":35.989226,"north":36.405496},"regionSelection":[{"regionId":6118,"regionType":6}],"isMapVisible":false,"filterState":{"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":true},"isCondo":{"value":false},"isMultiFamily":{"value":false},"isManufactured":{"value":false},"isLotLand":{"value":false},"isTownhouse":{"value":false},"isApartment":{"value":false},"isApartmentOrCondo":{"value":false}},"isListVisible":true}&wants={"cat1":["listResults"],"cat2":["total"]}&requestId=2',
}
