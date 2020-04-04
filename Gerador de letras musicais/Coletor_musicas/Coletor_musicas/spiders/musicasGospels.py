# -*- coding: utf-8 -*-
import scrapy


class MusicassertanejasSpider(scrapy.Spider):
    name = 'MusicasGospels'

    allowed_domains = ['letras.mus.br']
    start_urls = ['https://www.letras.mus.br/mais-acessadas/gospelreligioso/']
    
    def parse(self, response):
        seed = 'https://www.letras.mus.br'
        musicas = response.css('ol.top-list_mus li a::attr(href)').getall()
        for musica in musicas:
            yield scrapy.Request(url=seed+musica, callback=self.parse_letra) 
  

    def parse_letra(self, response):
        letra = response.css('div.cnt-letra p::text').getall()
        return { 'letra': letra}
        
