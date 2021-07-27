import pdfplumber
import requests

snils = 'xxx-xxx-xxx xx' #укажите свой снилс
path = '/home/...' #укажите рабочий путь (где будут лежать файлы для работы программы)

print('выбери вуз: 1 - Макаровка \n2 - Лесотехнический(в разработке) \n...')
x = int(input())
if x == 1:
    vus = 'https://abitur.gumrf.ru/hod-priema'
    with open(path + 'Front.html', 'w') as s:
        s.write(requests.get(vus).text)
    with open(path + 'Front.html', 'rb') as s:
        urlFile = s.readlines()[219][28:125]
    with open(path + 'pdf.pdf', 'wb') as file:
        file.write(requests.get(urlFile).content)

    with pdfplumber.open(path + 'pdf.pdf') as file:
        pages = file.pages
        for i in range(len(pages)):
            a = pages[i].extract_text()
            if a[0] == 'Ф':
                text = a[83:411]
            if snils in a:
                id = a.index(snils)
                ball = a[id + 15:id + 19]
                ans = a[id - 3:id]

                print(text, '\nТВОЕ МЕСТО: ', ans, '\nТВОЙ БАЛЛ ЕГЭ: ', ball)
elif x == 2:
    vus = 'https://pk.spbftu.ru/lists/specialties'


    
else:
    print('дурак')


