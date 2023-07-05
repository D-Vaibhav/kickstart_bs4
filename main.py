import logging
import requests
from bs4 import BeautifulSoup

logging_level = logging.INFO
logging_path = './logs/main.log'
logging.basicConfig(level = logging_level, filename = logging_path, filemode = 'w', format = '%(asctime)s - %(levelname)s - %(message)s', force = True)
logger = logging.getLogger(__name__)


def use_using_proxy(scrap_url):
    # curl ifconfig.me - 223.233.71.25
    proxies = {
        'http': 'http://223.233.71.25:3128',
        'https': 'https://223.233.71.25:1080'
    }

    res = requests.get(scrap_url, proxies=proxies)
    print(res.json())

# todo: write selenium code in-order to automate log.json genration
# inorder to get the network logs as json and writing it
def featch_and_write_scraped_data(scrap_url, output_file_path):
    print(f'scrap_url is {scrap_url}\n')

    try:
        res = requests.get(scrap_url)

        with open(output_file_path, 'w') as file:
            file.write(res.text)

    except:
        print(f'unable to make get request, please check internet connection !!!')


# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
def get_scraped_data(html_file_path):
    with open(html_file_path, 'r') as file:
        html_doc = file.read()

    # soup = BeautifulSoup(html_doc, 'html.parser')
    soup = BeautifulSoup(html_doc, 'lxml')

    # getting complete tag just by it's name
    print(f'page soup.title is : {soup.title}')
    print(f'page soup.find("title") is : {soup.find("title")}\n')

    print(f'page soup.title.text is : {soup.title.text}')
    print(f'page soup.title.name is : {soup.title.name}\n')

    print(f'soup.title.parent.name : {soup.title.parent.name}\n')

    # <body class="_a3wf _-kb">
    print(f'page soup.body["class"] is : {soup.body["class"]}\n')

    # getting for very first <div> tag
    print(f'soup.find("div").attrs : {soup.find("div").attrs}')
    print(f'soup.div.attrs : {soup.div.attrs}\n')

    print(f"soup.find('div')['id'] : {soup.find('div')['id']}")
    print(f"soup.div['id'] : {soup.div['id']}\n")

    print(f"soup.find('div')['style'] : {soup.find('div')['style']}")


    print(f'soup.link is : {soup.link}')


    link_list = soup.find_all('link')
    href_list = []
    for link in link_list:
        href_list.append(link.get('href'))


    print(link_list)
    print(f'href_list is : {href_list}')
    # print(soup.getText)

def main():
    scrap_url = 'https://www.instagram.com/coderpukku/'
    output_file_path = 'scraped_data/insta-scrap-coderpukku.html'

    featch_and_write_scraped_data(scrap_url, output_file_path)
    # use_using_proxy(scrap_url)

    html_file_path = output_file_path
    get_scraped_data(html_file_path)


if __name__ == '__main__':
    main()