import aiohttp
from bs4 import BeautifulSoup


class CurrencyParser:
    def __init__(self):
        # self.session = None
        self.exchange_rates_url = 'https://bank.gov.ua/ua/markets/exchangerates'

    # async def init_session(self):
    #     self.session = aiohttp.ClientSession()
    #
    # async def close_session(self):
    #     if self.session:
    #         await self.session.close()

    async def get_currency_list(self):
        tr_list = await self._get_tr_list()

        res = []
        for tr in tr_list:
            name = tr.find('a').text.strip()

            res.append(name)

        return res

    async def get_currency_rate(self, currency):
        tr_list = await self._get_tr_list()

        # res = {}
        for tr in tr_list:
            # currency_id = tr.find('span').text.strip()
            if currency == tr.find('a').text.strip():
                return tr.find_all('td')[-1].text.strip()

        return None

        #     rate = tr.find_all('td')[-1].text.strip()
        #
        #     res[name] = rate
        #
        # return res

    async def _get_tr_list(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.exchange_rates_url) as response:
                page = await response.text()
                soup = BeautifulSoup(page, 'html.parser')

                return soup.find('tbody').find_all('tr')
