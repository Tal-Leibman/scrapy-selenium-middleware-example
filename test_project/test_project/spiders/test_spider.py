from typing import Any

from scrapy import Request
from scrapy.crawler import CrawlerProcess
from scrapy.http import HtmlResponse
from scrapy.utils.project import get_project_settings
from selenium.webdriver.support import expected_conditions as EC
from scrapy_selenium_middleware import SeleniumSpider, RequestMetaKeys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from seleniumwire.webdriver import Firefox


class TestSpider(SeleniumSpider):
    name = "test"
    start_urls = ["https://en.wikipedia.org/wiki/Web_scraping"]

    def start_requests(self):
        yield Request(
            url=self.start_urls[0],
            callback=self.parse,
            meta={RequestMetaKeys.use_middleware.value: True},
        )

    def browser_interaction_after_get(self, driver: Firefox, request: Request) -> Any:
        recorded_requests = driver.requests
        print(f"from url {request.url} a total of {len(recorded_requests)} requests were recorded")
        # wait for web elements to load from javascript
        WebDriverWait(driver, 5, poll_frequency=2).until(
            EC.presence_of_all_elements_located((By.ID, "content"))
        )
        # interact with page
        # driver.find_element_by_tag_name("h1").click()
        return driver.title

    def parse(self, response: HtmlResponse, **kwargs):
        page_title_from_selenium = response.meta.get(RequestMetaKeys.return_value_browser_interaction.value)
        print(page_title_from_selenium)


if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl(TestSpider)
    process.start()
