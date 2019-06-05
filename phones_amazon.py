import scrapy

class Myspider(scrapy.Spider):
    name = "amazon_phones"

    def start_requests(self):

        urls = [
            "https://www.amazon.in/s?k=iphones&rh=n%3A1389401031&ref=nb_sb_noss",
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self,response):


        containers = response.css("div.sg-col-20-of-24.s-result-item.sg-col-0-of-12.sg-col-28-of-32.sg-col-16-of-20.sg-col.sg-col-32-of-36.sg-col-12-of-16.sg-col-24-of-28")
        for container in containers:
            phone = container.css("span.a-size-medium.a-color-base.a-text-normal::text").get()
            price = container.css("span.a-price-whole::text").get()
            ratings = container.css("span.a-icon-alt::text").get()

            yield{
                'Phone' : phone,
                'Price' : price,
                'Ratings' : ratings
            }
         
