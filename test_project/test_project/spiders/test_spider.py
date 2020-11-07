from typing import Any

from scrapy import Request
from scrapy.crawler import CrawlerProcess
from scrapy.http import HtmlResponse
from scrapy.utils.project import get_project_settings
from scrapy_selenium_middleware import SeleniumSpider, RequestMetaKeys
from seleniumwire.webdriver import Firefox


class TestSpider(SeleniumSpider):
    name = "test"
    start_urls = ["https://www.ynet.co.il"]

    def start_requests(self):
        yield Request(
            url=self.start_urls[0],
            callback=self.parse,
            meta={RequestMetaKeys.use_middleware.value: True},
        )

    def browser_interaction_after_get(self, driver: Firefox, request: Request) -> Any:
        return driver.title

    def parse(self, response: HtmlResponse, **kwargs):
        page_title_from_selenium = response.meta.get(RequestMetaKeys.return_value_browser_interaction.value)
        print(page_title_from_selenium)


if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl(TestSpider)
    process.start()
