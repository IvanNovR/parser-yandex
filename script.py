import requests
from bs4 import BeautifulSoup


class PostID:
    def __init__(self, org_inn, service_id, region_id):
        self.org_inn = org_inn
        self.lic_status_id = '1'
        self.service_id = service_id
        self.region_id = region_id
        self.url = 'https://rkn.gov.ru/communication/register/license/'
        self.HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
        }

        self.data = {
            'act': 'search',
            'org_name_full': '',
            'org_inn': f'{org_inn}',
            'lic_num': '',
            'lic_status_id': f'{self.lic_status_id}',
            'periodmon': '00',
            'periodyear': '0000',
            'service_id': f'{service_id}',
            'region_id': f'{region_id}',
            'csrftoken': '16cf9302a5099ccbc2ef622ce95c8aad1cfd01eedfa2a83c92ccd13a7dc40344af6e0ab7ec333d89'
        }
        self.file = open('inns.txt', 'a')


    def dopost(self):
        try:
            response = requests.post(url=self.url, data=self.data, headers=self.HEADERS).text
            html = BeautifulSoup(response, 'html.parser')
            #print(html)
            #print(type(html))
            table = html.select(".TblList")
            #print(table)
            td = table[0].find_all('a')
            #print(td)
            if len(td) > 1:
                # self.file.write(''.join(td))
                print(self.data)
                print(td)
                print('---------------------------------------------------------')
            # self.file.close()
            # res = td[0].text
            print(td)
            return td
        except IndexError:
            return '-'