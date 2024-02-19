import requests


def check_vulnerabilities(url):
    r = requests.get(url)
    if r.status_code != 200:
        return "Произошла ошибка. Проверьте корректность введенного url"

    with open('urls.txt', 'r') as file:
        check_urls = file.read().split('\n')
    final = []
    for check in check_urls:
        r = requests.get(f'{url}/{check}')
        if r.status_code == 200 and "Filename is out of range" not in r.text:
            final.append(f'{url}/{check} -- Найдена уязвимость LFI !!!')
    if final:
        return '\n'.join(final)
    return 'Поздравляем, на вашем сайте не найден уязвимости LFI'


url_site = input('Введите url вашего сайта (например: "http://bitrix"): ')
print(check_vulnerabilities(url_site))
