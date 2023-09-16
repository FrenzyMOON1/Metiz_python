def get_city(country, city, population=''):
    if population == '':
        answer = country + ' ' + city
    else:
        answer = country + ' ' + city + ' - ' + population
    return answer.title()
