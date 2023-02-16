# -*- coding: utf-8 -*-

# Scrapy settings for artworks project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "artworks"

SPIDER_MODULES = ["artworks.spiders"]
NEWSPIDER_MODULE = "artworks.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "USER_AGENT=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    "artworks.pipelines.ArtworksPipeline": 300,
}
