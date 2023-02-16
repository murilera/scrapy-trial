import re
from urllib.parse import urlparse
from artworks.items import ArtworksItem


def parse_url(start_url):
    parsed_start_url = urlparse(start_url)
    url_scheme = parsed_start_url.scheme
    url_netloc = parsed_start_url.netloc
    base_url = f"{url_scheme}://{url_netloc}"
    return base_url


def is_link_to_follow(response):
    links = response.xpath("//a//h3/../@href").getall()
    return links


def has_items_page(response):
    items_urls = response.xpath("//a[contains(@href,'item')]/@href").getall()
    return items_urls or []


def parse_categories(response):
    parsed_start_url = urlparse(response.url)
    categories = parsed_start_url.path.split("/")
    return list(filter(None, categories))


def has_next_page(response):
    next_page = response.xpath(
        "//form[@class='nav next']/input[@name='page']/@value"
    ).get()
    return next_page


def parse_item(response, categories, base_url):
    item = ArtworksItem()

    url = response.url
    artist = response.xpath(f"//h2[@class='artist']/text()").get()
    title = response.xpath("//div[@id='content']/h1/text()").get()
    image = base_url + response.xpath("//img/@src").get()
    dimensions = response.xpath(
        "//td[contains(text(),'Dimensions')]/following-sibling::td/text()"
    ).get()
    width, height = parse_dimensions(dimensions)
    description = response.xpath("//div[@class='description']/p/text()").get()

    item.update(
        {
            "url": url,
            "artist": artist,
            "title": title,
            "image": image,
            "height": height,
            "width": width,
            "description": description,
            "categories": categories,
        }
    )
    return item


def parse_dimensions(dimensions):
    # here I take in consideration that dimensions come with the following order: H x W x D
    # and that's because I search for patterns for artworks dimensions and found it like that
    if dimensions and "cm" in dimensions:
        pattern = "in. \((.*? cm)\)"
        if dimensions_cm := re.findall(pattern, dimensions):
            splitted_dimensions = dimensions_cm[0].split("x")
            if len(splitted_dimensions) >= 2:
                height = splitted_dimensions[0].strip().lstrip()
                width = (
                    splitted_dimensions[1].replace("cm", "").strip().lstrip()
                )
                return float(height), float(width)
    return None, None
