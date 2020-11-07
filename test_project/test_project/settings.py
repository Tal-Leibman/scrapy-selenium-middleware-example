BOT_NAME = "test_project"

SPIDER_MODULES = ["test_project.spiders"]
NEWSPIDER_MODULE = "test_project.spiders"
DOWNLOADER_MIDDLEWARES = {"scrapy_selenium_middleware.SeleniumDownloader": 451}
CONCURRENT_REQUESTS = 1  # multiple concurrent browsers are not supported yet
SELENIUM_IS_HEADLESS = False
# SELENIUM_PROXY = (
#     "http://user:password@my-proxy-server:port"  # set to None to not use a proxy
# )
SELENIUM_PROXY = None
SELENIUM_USER_AGENT = "User-Agent: Mozilla/5.0"
# a list of regular expression to record the incoming requests by matching the url
# recorded requests can be found on driver.requests property
SELENIUM_REQUEST_RECORD_SCOPE = [".*"] # This will record all requests
SELENIUM_FIREFOX_PROFILE_SETTINGS = {}
