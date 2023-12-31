from ..async_web_crawler import AsyncBaseWebCrawler
from ...schema import HttpJsonResponse, HttpJsonResponse
from ..._typing import Union


class ParseOneOFourCrawler(AsyncBaseWebCrawler):
    def get_job_urls(self):
        ...
