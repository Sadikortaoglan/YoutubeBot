from selenium import webdriver
from bs4 import BeautifulSoup
import time
import random
import  re

adres=input("Lütfen çekilişi yapacağınız sohbet url'sini giriniz: ")
kelime=input("Lütfen cekilis kelimesini giriniz: ")
if re.search("www.youtube.com",adres):
    ytUrl=adres
else:
    exit("Hatalı bir link girdiniz uygun formatta link giriniz('www.youtube.com')")
keyword=kelime
Kullanıcılar=set()
# start web browser
tercih=input("Tarayıcı secim\n 1:Chrome \n 2:Firefox \ntercihiniz: ")
if(tercih=="1"):
    browser = webdriver.Chrome()
elif(tercih=="2"):
    browser = webdriver.Firefox()
else:
    print("Lütfen geçerli bir seçenek seçiniz")

def getHtml(url):
    browser.get(ytUrl)
    page_source=browser.page_source
    time.sleep(2)
    return page_source

def parseHtml(html_source):
     return BeautifulSoup(html_source,'html.parser')

def getMessages(soup):
    return soup.find_all("yt-live-chat-text-message-renderer")
def kullanıcılarGüncelleme(message):
    for messag in message:
        #Find metoduyla div ulaştık burada
        content=messag.find("div",{"id":"content"})
        #Burada Yazarların İsimlerini Çektik
        author=content.find("span",{"id":"author-name"}).text
        #Burada Mesajları Text Olarak Çektik
        message_content=content.find("span",{"id":"message"}).text
        #Keyword konrol ederek yazar ekleme
        if keyword in  message_content.lower():
            #print("Eklendi ",author)
            Kullanıcılar.add(author)

def Baslat(Kullanıcılar):
    print("Çekiliş Başlıyor..{ToplamKullanici} kişi hak kazandı ".format(
         ToplamKullanici=len(Kullanıcılar)))
    time.sleep(2)
    for i in range(0,5):
        nokta="."*i
        print("Rasgele bir sayı çekiliyor",nokta)
        time.sleep(2)
    print("Son kontrollerimi yapıyorum.... ")
    time.sleep(2)
    listUsers=list(Kullanıcılar)
    print("Ve {ToplamKullanici} kişi arasından Kazanan: ".format(ToplamKullanici=len(Kullanıcılar)),
          random.choice(listUsers))

def main():
    for i in range(0,8):
        html_source=getHtml(ytUrl)
        soup=parseHtml(html_source)
        messages=getMessages(soup)
        kullanıcılarGüncelleme(messages)
        time.sleep(2)
        print("{count} kisi katılmış durumda ".format(count=len(Kullanıcılar)))
        time.sleep(10)
    listUsers=list(Kullanıcılar)
    Baslat(listUsers)
    browser.close()

main()

