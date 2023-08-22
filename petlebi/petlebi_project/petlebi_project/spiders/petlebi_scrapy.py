import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import PetlebiProjectItem
import requests
from bs4 import BeautifulSoup
import re
#TERMINAL COMMAND TO GET THE OUTPUT FILE TO DISPLAY THE TURKISH CHARS : 
#scrapy crawl petlebis -o petlebi_products.json -s FEED_EXPORT_ENCODING=utf-8
#scrapy crawl petlebis -o petlebi_project/petlebi_products.json -s FEED_EXPORT_ENCODING=utf-8
# product URL => DONE
# - product name => DONE
# - product barcode => DONE
# - product price => DONE
# - product stock => DONE
# - product images => DONE
# - description => DONE
# - sku
# - category => DONE
# - product ID 
# - brand => DONE



class PetlebiSpider(CrawlSpider):  
    name = 'petlebis'
    allowed_domains = ['petlebi.com']
    start_urls = ['https://www.petlebi.com/']

    rules = ( 
        Rule(LinkExtractor(allow= 'kedi-urunleri') ,callback='parse_item'),
        Rule(LinkExtractor(allow= 'kopek-urunleri'), callback='parse_item'),
        Rule(LinkExtractor(allow= 'kus-urunleri'),callback='parse_item'),
    )


    def parse_item(self, response):
        product_description = response.css('#myTabContent #productDescription').get()
        # Remove HTML tags from the description using regular expression
        cleaned_description = re.sub('<.*?>', '', product_description)
        stock_html = response.css('select#quantity.form-control.form-control-lg.pd-basket-select').get()
        clean_stock = re.sub('<.*?>', '', stock_html)
        yield{
            'product_name': response.css('h1.product-h1::text').get().replace('\n', ' ').strip(),
            'price': response.css('p.new-price::text').get().replace('\n', ' ').strip(),
            'stock': clean_stock.replace('\n', '').strip(),
            'barcode': response.css('div.brand-line+ .mb-2 .pd-d-v::text').get().replace('\n', ' ').strip(),
            'description': cleaned_description.replace('\n', '').strip(),
            'image': response.css('div.col-sm-5 a::text').get().replace('\n', ' ').strip(),
            'category': response.css('li.breadcrumb-item:nth-child(2) span::text').get().replace('\n', ' ').strip(),
            'brand': response.css('div#myTabContent div.col-10.pd-d-v a::text').get().replace('\n', ' ').strip(),
            'image': response.css('#photoGallery img::attr(src)').get().replace('\n', ' ').strip(),
            'product_url': response.css('div.mb-0 a::attr(href)').get(),
            'product_id':' ',
            'sku': ' '

        }

    

#     def getPageLinks(url):
#         r = requests.get(url)
#         sp = BeautifulSoup(r.text, 'lxml')
#         print("SP IS: ", sp)
#         links = sp.select('div.pb-0 a')
#         #print("LINKS ARE: ", links)
#         return [link.attrs['href'] for link in links]
    
#     def productData(url):
#         r = requests.get(url)
#         sp = BeautifulSoup(r.text, 'lxml')
#         product ={
#             'product_name': sp.select_one('h1.product-h1').text,
#             'price': float(sp.select_one('p.new-price').text),
#             'stock': sp.select_one('#quantity').text.strip().replace('\n', ' '),
#             'barcode': sp.select_one('div.brand-line+ .mb-2 .pd-d-v').text,
#             'description': sp.select_one('#productDescription').text.strip().replace('\n', ' '),
#             'image': sp.select_one('div.col-sm-5 a').attrs['href'],
#             'category': sp.select_one('li.breadcrumb-item:nth-child(2) span').text,
#             'brand': sp.select_one('div.brand-line~ .mb-2+ .mb-2 .pd-d-v , .brand-line .pd-d-v').text,
#         }

#         #print("PRODUCT IS: ", product)
        
    

#     #     results = [productData(spider.url) for url in urls]
    
#     def main():
#         urls = getPageLinks('https://www.petlebi.com/kedi-urunleri/me-o-yengecli-kremali-sivi-odul-mamasi-15gr-4-lu.html')
#         results = [productData(spider.url) for url in urls]
#         return results
   
# print("MAIN IS: ", main())



    #productData('https://www.petlebi.com/kedi-urunleri/me-o-yengecli-kremali-sivi-odul-mamasi-15gr-4-lu.html')
   

    # def parse(self, response):
    #     title = response.css('title::text').extract()
    #     products = response.css('.mb-0::text').extract()
    #     product = [product.strip() for product in products if product.strip()]
    #     price = response.css(".commerce-discounts::text").extract()
    #     barcode = response.css(".pd-d-v::text").extract()
    #     print("PRODUCT IS: ", product[0])
    #     item = PetlebiProjectItem(TITLETEXT=title, PRODUCTTEXT=product, PRICE=price, BARCODE=barcode)
    #     next_page = response.css('div.pr-3 a::attr(href)').get()
    #     if next_page is not None:   
    #         yield response.follow(next_page, callback=self.parse)  
    #     yield item