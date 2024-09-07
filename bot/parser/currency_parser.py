from datetime import datetime
import aiohttp


class CurrencyParser:
    def __init__(self):
        self.exchange_rates_url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={date}&json'

        self.exchange_rates_cache = {}
        self.last_update_date = None

    async def get_currencies_list(self):
        await self._update()

        return self.exchange_rates_cache.keys()

    async def get_rate(self, currency):
        await self._update()

        return self.exchange_rates_cache[currency]

    async def _update(self):
        if self.last_update_date is None:
            self.last_update_date = await self._get_date()
            return await self._parse_exchange_rates(self.last_update_date)

        date = await self._get_date()
        
        if date != self.last_update_date:
            await self._parse_exchange_rates(date)
    
    async def _parse_exchange_rates(self, date):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.exchange_rates_url.format(date=date)) as response:
                if response.status != 200:
                    return None

                res_list = await response.json()
                if not res_list:
                    return None

                exchange_rates_list = {}

                for item in res_list:
                    exchange_rates_list[item['txt']] = item['rate']

                self.exchange_rates_cache = exchange_rates_list

    @staticmethod
    async def _get_date():
        return datetime.now().strftime('%Y%m%d')

    # parse from site

    # v __init__ -> self.exchange_rates_url = 'https://bank.gov.ua/ua/markets/exchangerates'
    # async def get_currency_list(self):
    #     tr_list = await self._get_tr_list()
    #
    #     res = []
    #     for tr in tr_list:
    #         name = tr.find('a').text.strip()
    #
    #         res.append(name)
    #
    #     return res
    #
    # async def get_currency_rate(self, currency):
    #     tr_list = await self._get_tr_list()
    #
    #     for tr in tr_list:
    #         if currency == tr.find('a').text.strip():
    #             return tr.find_all('td')[-1].text.strip()
    #
    #     return None
    #
    # async def _get_tr_list(self):
    #     async with aiohttp.ClientSession() as session:
    #         async with session.get(self.exchange_rates_url) as response:
    #             page = await response.text()
    #             soup = BeautifulSoup(page, 'html.parser')
    #
    #             return soup.find('tbody').find_all('tr')
