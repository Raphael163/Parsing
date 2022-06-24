import requests
import json


def get_data():
    cookies = {
        '__lhash_': '0fb14bf84910322145f2cdf1c53e73a3',
        'COMPARISON_INDICATOR': 'false',
        'HINTS_FIO_COOKIE_NAME': '2',
        'MAIN_PAGE_VARIATION_1': '2',
        'MVID_2_exp_in_1': '1',
        'MVID_AB_SERVICES_DESCRIPTION': 'var4',
        'MVID_ADDRESS_COMMENT_AB_TEST': '2',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
        'MVID_CART_MULTI_DELETE': 'false',
        'MVID_CATALOG_STATE': '1',
        'MVID_CITY_ID': 'CityCZ_1780',  # Код города, если парсить другой нужно менять(samara)
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_GUEST_ID': '20932625879',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '6300000100000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_LOGIN': 'true',
        'MVID_NEW_LK_MENU_BUTTON': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_NEW_SUGGESTIONS': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_REGION_ID': '4',
        'MVID_REGION_SHOP': 'S972',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'new',
        'MVID_TIMEZONE_OFFSET': '4',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'flacktory': 'no',
        'searchType2': '2',
        '__SourceTracker': 'google__organic',
        'admitad_deduplication_cookie': 'google__organic',
        'authError': '',
        'SMSError': '',
        'tmr_lvid': '821d644ee58ba2673354d4a22076b98c',
        'tmr_lvidTS': '1656009506891',
        '_ym_uid': '1656009507206828191',
        '_ym_d': '1656009507',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': 'e95e0b62-056e-4485-88a2-fbff2e071ea8',
        '_gid': 'GA1.2.907755435.1656009507',
        'advcake_session_id': '72546c2e-72f2-af6d-e512-c2217512965f',
        'advcake_track_id': 'c91cb464-73d6-1e93-645d-e4823f9bdf2a',
        'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
        '_ym_isad': '2',
        'afUserId': '255e728c-0ca6-4ff4-a5fa-368fe9e5c4b4-p',
        'AF_SYNC': '1656009508334',
        'adrcid': 'AiUgYrTM3UbAvyWRueCOpXg',
        'adrdel': '1',
        'st_uid': '8f79298fbbaba6bdf990c87b590d1fb7',
        'flocktory-uuid': 'ecf54906-708d-4c33-ad06-4d1fd8d02a2c-3',
        'uxs_uid': 'cf4dcc70-f323-11ec-9d79-138d45e1b9a5',
        'BIGipServeratg-ps-prod_tcp80': '2433014794.20480.0000',
        'bIPs': '53593859',
        'wurfl_device_id': 'generic_web_browser',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        'BIGipServeratg-ps-prod_tcp80_clone': '2433014794.20480.0000',
        'MVID_GTM_BROWSER_THEME': '1',
        'deviceType': 'desktop',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VSTTNbLUcrMWBwEB1oHhEjFEEJPzUVZHRvJU1TNzQNRxhIXmkXEzxDV0NtViEhTwtQXTcyGjhrJWdQXSBIWk5qJh8WfWsjWA0LXERGb2UlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeC87ZiBhTV0oRVVJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=T3hPQA==',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VSTTNbLUcrMWBwEB1oHhEjFEEJPzUVZHRvJU1TNzQNRxhIXmkXEzxDV0NtViEhTwtQXTcyGjhrJWdQXSBIWk5qJh8WfWsjWA0LXERGb2UlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeC87ZiBhTV0oRVVJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=T3hPQA==',
        'cfidsgib-w-mvideo': 'PJ/u09poez8KKNK3m+2HKzX5npLpp8JfqV1D1G63Y/rgSsWHOOuvcyf3sDI+wytDe4DkMS3TnVmkl+vzd8NMPcYQt8D5IubsEBG2UJnb2L5yzWkpM9hHw7I5fbmKcfgl1SHQ/Qkr73jHKbNJ/6DNryJIVTU3arIeBMbX',
        'cfidsgib-w-mvideo': 'PJ/u09poez8KKNK3m+2HKzX5npLpp8JfqV1D1G63Y/rgSsWHOOuvcyf3sDI+wytDe4DkMS3TnVmkl+vzd8NMPcYQt8D5IubsEBG2UJnb2L5yzWkpM9hHw7I5fbmKcfgl1SHQ/Qkr73jHKbNJ/6DNryJIVTU3arIeBMbX',
        'gsscgib-w-mvideo': 'VXSDQwUYAYr1gtzrYGGnNEVT+vFsPxCpWkf/DoRHRVXrSQpbEpU9vB8r++qBKh628lysXB+TtnkmYE5vwGw4BVBLVRNSOYgYCqYGGkom4x9Rfxk0ztlDT+CiXHGnX+dDu7NStJkjdgqhorQF9+p4bMqlBrqsZHUjKrf96u0FWMDMws7V0UhOM+k2z0mBVjlzkdD/VRXQ/EV7CHzd40Ry4G6d8GQh4aZ7VZ0s/RJ4owE942ExCdV1wpayoA8QFw==',
        'gsscgib-w-mvideo': 'VXSDQwUYAYr1gtzrYGGnNEVT+vFsPxCpWkf/DoRHRVXrSQpbEpU9vB8r++qBKh628lysXB+TtnkmYE5vwGw4BVBLVRNSOYgYCqYGGkom4x9Rfxk0ztlDT+CiXHGnX+dDu7NStJkjdgqhorQF9+p4bMqlBrqsZHUjKrf96u0FWMDMws7V0UhOM+k2z0mBVjlzkdD/VRXQ/EV7CHzd40Ry4G6d8GQh4aZ7VZ0s/RJ4owE942ExCdV1wpayoA8QFw==',
        'fgsscgib-w-mvideo': 'Y8FV7f5bc8f8aae9bcc52bd184e11b4e85e4ab60',
        'fgsscgib-w-mvideo': 'Y8FV7f5bc8f8aae9bcc52bd184e11b4e85e4ab60',
        'cfidsgib-w-mvideo': 'wAy8qnAu3AFGGTigRw3hexUoZEHnk4y2diBj/EmvFyMGUyf3zqszTcesB6KezFAOBBs0kXGZKl1TvUb+t4R9InkxVF1EH3oKtq6M2fh+KK11tVi3m9wbfGeVxiKoDKXVjjuggqFUqfk3pIhBLLMnccPSOkO6I19X47Yz',
        'CACHE_INDICATOR': 'false',
        'MVID_GEOLOCATION_NEEDED': 'false',
        '_dc_gtm_UA-1873769-1': '1',
        'MVID_ENVCLOUD': 'canary',
        '_dc_gtm_UA-1873769-37': '1',
        'JSESSIONID': 'bpTnv01PQkJt9jjLRv9zSgnxNsgLFlQNgB0G1HkcQGgSfQnRJ2ZL!-688941551',
        'mindboxDeviceUUID': '5510054d-7932-4706-a1df-c3941f098bf1',
        'directCrm-session': '%7B%22deviceGuid%22%3A%225510054d-7932-4706-a1df-c3941f098bf1%22%7D',
        '_ga_CFMZTSS5FM': 'GS1.1.1656013173.2.1.1656016369.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1656013173.2.1.1656016369.58',
        '_ga': 'GA1.2.1726506095.1656009507',
        'tmr_reqNum': '156',
        'tmr_detect': '0%7C1656016372316',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        # Requests sorts cookies= alphabetically
        # 'cookie': '__lhash_=0fb14bf84910322145f2cdf1c53e73a3; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=2; MAIN_PAGE_VARIATION_1=2; MVID_2_exp_in_1=1; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=true; MVID_CART_MULTI_DELETE=false; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_1780; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GUEST_ID=20932625879; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=6300000100000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_LOGIN=true; MVID_NEW_LK_MENU_BUTTON=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_NEW_SUGGESTIONS=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=4; MVID_REGION_SHOP=S972; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; MVID_TIMEZONE_OFFSET=4; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; flacktory=no; searchType2=2; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; authError=; SMSError=; tmr_lvid=821d644ee58ba2673354d4a22076b98c; tmr_lvidTS=1656009506891; _ym_uid=1656009507206828191; _ym_d=1656009507; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=e95e0b62-056e-4485-88a2-fbff2e071ea8; _gid=GA1.2.907755435.1656009507; advcake_session_id=72546c2e-72f2-af6d-e512-c2217512965f; advcake_track_id=c91cb464-73d6-1e93-645d-e4823f9bdf2a; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; _ym_isad=2; afUserId=255e728c-0ca6-4ff4-a5fa-368fe9e5c4b4-p; AF_SYNC=1656009508334; adrcid=AiUgYrTM3UbAvyWRueCOpXg; adrdel=1; st_uid=8f79298fbbaba6bdf990c87b590d1fb7; flocktory-uuid=ecf54906-708d-4c33-ad06-4d1fd8d02a2c-3; uxs_uid=cf4dcc70-f323-11ec-9d79-138d45e1b9a5; BIGipServeratg-ps-prod_tcp80=2433014794.20480.0000; bIPs=53593859; wurfl_device_id=generic_web_browser; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; BIGipServeratg-ps-prod_tcp80_clone=2433014794.20480.0000; MVID_GTM_BROWSER_THEME=1; deviceType=desktop; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VSTTNbLUcrMWBwEB1oHhEjFEEJPzUVZHRvJU1TNzQNRxhIXmkXEzxDV0NtViEhTwtQXTcyGjhrJWdQXSBIWk5qJh8WfWsjWA0LXERGb2UlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeC87ZiBhTV0oRVVJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=T3hPQA==; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VSTTNbLUcrMWBwEB1oHhEjFEEJPzUVZHRvJU1TNzQNRxhIXmkXEzxDV0NtViEhTwtQXTcyGjhrJWdQXSBIWk5qJh8WfWsjWA0LXERGb2UlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeC87ZiBhTV0oRVVJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=T3hPQA==; cfidsgib-w-mvideo=PJ/u09poez8KKNK3m+2HKzX5npLpp8JfqV1D1G63Y/rgSsWHOOuvcyf3sDI+wytDe4DkMS3TnVmkl+vzd8NMPcYQt8D5IubsEBG2UJnb2L5yzWkpM9hHw7I5fbmKcfgl1SHQ/Qkr73jHKbNJ/6DNryJIVTU3arIeBMbX; cfidsgib-w-mvideo=PJ/u09poez8KKNK3m+2HKzX5npLpp8JfqV1D1G63Y/rgSsWHOOuvcyf3sDI+wytDe4DkMS3TnVmkl+vzd8NMPcYQt8D5IubsEBG2UJnb2L5yzWkpM9hHw7I5fbmKcfgl1SHQ/Qkr73jHKbNJ/6DNryJIVTU3arIeBMbX; gsscgib-w-mvideo=VXSDQwUYAYr1gtzrYGGnNEVT+vFsPxCpWkf/DoRHRVXrSQpbEpU9vB8r++qBKh628lysXB+TtnkmYE5vwGw4BVBLVRNSOYgYCqYGGkom4x9Rfxk0ztlDT+CiXHGnX+dDu7NStJkjdgqhorQF9+p4bMqlBrqsZHUjKrf96u0FWMDMws7V0UhOM+k2z0mBVjlzkdD/VRXQ/EV7CHzd40Ry4G6d8GQh4aZ7VZ0s/RJ4owE942ExCdV1wpayoA8QFw==; gsscgib-w-mvideo=VXSDQwUYAYr1gtzrYGGnNEVT+vFsPxCpWkf/DoRHRVXrSQpbEpU9vB8r++qBKh628lysXB+TtnkmYE5vwGw4BVBLVRNSOYgYCqYGGkom4x9Rfxk0ztlDT+CiXHGnX+dDu7NStJkjdgqhorQF9+p4bMqlBrqsZHUjKrf96u0FWMDMws7V0UhOM+k2z0mBVjlzkdD/VRXQ/EV7CHzd40Ry4G6d8GQh4aZ7VZ0s/RJ4owE942ExCdV1wpayoA8QFw==; fgsscgib-w-mvideo=Y8FV7f5bc8f8aae9bcc52bd184e11b4e85e4ab60; fgsscgib-w-mvideo=Y8FV7f5bc8f8aae9bcc52bd184e11b4e85e4ab60; cfidsgib-w-mvideo=wAy8qnAu3AFGGTigRw3hexUoZEHnk4y2diBj/EmvFyMGUyf3zqszTcesB6KezFAOBBs0kXGZKl1TvUb+t4R9InkxVF1EH3oKtq6M2fh+KK11tVi3m9wbfGeVxiKoDKXVjjuggqFUqfk3pIhBLLMnccPSOkO6I19X47Yz; CACHE_INDICATOR=false; MVID_GEOLOCATION_NEEDED=false; _dc_gtm_UA-1873769-1=1; MVID_ENVCLOUD=canary; _dc_gtm_UA-1873769-37=1; JSESSIONID=bpTnv01PQkJt9jjLRv9zSgnxNsgLFlQNgB0G1HkcQGgSfQnRJ2ZL!-688941551; mindboxDeviceUUID=5510054d-7932-4706-a1df-c3941f098bf1; directCrm-session=%7B%22deviceGuid%22%3A%225510054d-7932-4706-a1df-c3941f098bf1%22%7D; _ga_CFMZTSS5FM=GS1.1.1656013173.2.1.1656016369.0; _ga_BNX5WPP3YK=GS1.1.1656013173.2.1.1656016369.58; _ga=GA1.2.1726506095.1656009507; tmr_reqNum=156; tmr_detect=0%7C1656016372316',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195/f/price=570-75999/skidka=da/tolko-v-nalichii=da',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'x-set-application-id': '4adfd525-ef28-44bf-bfbe-29df6c461bcc',
    }

    params = {
        'categoryId': '195',  # категория товаров
        'offset': '0',
        'limit': '20',
        'filterParams': [
            'WyJwcmljZSIsIiIsIjU3MC03NTk5OSJd',
            'WyLQotC+0LLQsNGA0Ysg0YHQviDRgdC60LjQtNC60L7QuSIsIi04Iiwi0JHQvtC70LXQtSA1JSJd',
            'WyLQotC+0LvRjNC60L4g0LIg0L3QsNC70LjRh9C40LgiLCItOSIsItCU0LAiXQ==',
        ],
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                            headers=headers).json()

    # print(response)

    products_ids = response.get("body").get('products')

    with open("1_products_ids.json", 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)
    # print(products_ids)
    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data).json()
    with open('2_items.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)
    # print(len(response.get("body").get('products')))

    products_ids_str = ','.join(products_ids)
    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                            headers=headers).json()
    with open('3_price.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    items_prices = {}

    material_prices = response.get("body").get("materialPrices")

    for item in material_prices:
        item_id = item.get('price').get("productId")
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        items_prices[item_id] = {
            "item_basePrice": item_base_price,
            "item_salePrice": item_sale_price,
            "item_bonus": item_bonus

        }
    with open("4_items_prices.json", "w") as file:
        json.dump(items_prices, file, indent=4, ensure_ascii=False)


def get_result():
    with open('2_items.json') as file:
        products_data = json.load(file)

    with open('4_items_prices.json') as file:
        products_prices = json.load(file)

    products_data = products_data.get('body').get('products')

    for item in products_data:
        product_id = item.get('productId')

        if product_id in products_prices:
            prices = products_prices[product_id]

        item["item_basePrice"] = prices.get('item_basePrice')
        item["item_salePrice"] = prices.get('item_salePrice')
        item["item_bonus"] = prices.get('item_bonus')

    with open("5_result.json", "w") as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)


def main():
    get_data()
    get_result()


if __name__ == '__main__':
    main()
