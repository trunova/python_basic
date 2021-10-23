site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

def siteOutput(n):
    for _ in range(1, n + 1):
        name = input('Введите название продукта для нового сайта: ')
        if not name in dictSite.keys():
            site['html']['body']['h2'] = 'У нас самая низкая цена на {}'.format(name)
            dictSite[name] = site
        for site_name, value in dictSite.items():
            print('Сайт для {}:'.format(site_name))
            print('site = {')
            print(value)
            print('}')

n = int(input('Сколько будет сайтов? '))
list_site = list()
tupleSite = tuple()
dictSite = dict()
siteOutput(n)
