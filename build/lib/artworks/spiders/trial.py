# -*- coding: utf-8 -*-
import scrapy
from artworks.spiders import parser


class TrialSpider(scrapy.Spider):
    name = "trial"
    start_urls = ["http://pstrial-2019-12-16.toscrape.com/browse/"]
    base_url = parser.parse_url(start_urls[0])

    def start_requests(self):
        self.log("Starting spider")
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.navigate_urls)

    def navigate_urls(self, response):
        if uris := parser.is_link_to_follow(response):
            for uri in uris:
                url = response.urljoin(uri)
                yield scrapy.Request(url=url, callback=self.handle_navigate)

    def handle_navigate(self, response):
        if items_urls := parser.has_items_page(response):
            for item_url in items_urls:
                categories = parser.parse_categories(response)
                url = f"{self.base_url}{item_url}"
                yield scrapy.Request(
                    url=url,
                    callback=self._parse_item,
                    cb_kwargs={"categories": categories},
                )
            if next_page := parser.has_next_page(response):
                url = response.url.split("?")[0]
                url = f"{url}?page={next_page}"
                yield scrapy.Request(url=url, callback=self.handle_navigate)
        return self.navigate_urls(response)

    def _parse_item(self, response, categories):
        output = parser.parse_item(response, categories, self.base_url)
        yield output
