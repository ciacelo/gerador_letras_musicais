# -*- coding: utf-8 -*-
import scrapy


class MusicassertanejasSpider(scrapy.Spider):
    name = 'MusicasSertanejas'

    allowed_domains = ['letras.mus.br']
    start_urls = ['https://www.letras.mus.br/mais-acessadas/sertanejo']

    def parse(self, response):
        seed = 'https://www.letras.mus.br'
        musicas = response.css('ol.top-list_mus li a::attr(href)').extract()
        for musica in musicas:
            yield scrapy.Request(url=seed+musica, callback=self.parse_letra)

    def parse_letra(self, response):
        letra = response.css('div.cnt-letra p::text').extract()
        return {'letra': letra}
