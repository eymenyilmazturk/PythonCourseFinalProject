def choosingProfession():
    jobs = []

    name = str(input('Hoşgeldiniz, lütfen isminizi giriniz : '))
    print(50*'*')
    print(f'Merhaba, {name} \nSorulara Evet veya Hayır şeklinde cevap veriniz...')
    print(50*'*')
    pcEngineer = str(input('Donanım ve yazılım bilginiz var mı ? :'))
    print(50 * '*')
    softwareEngineer = str(input('Program yazmayı seviyormusunuz ? :'))
    print(50 * '*')
    electricEngineer = str(input('Elektrik ile uğraşmayı seviyormusunuz ? :'))
    print(50 * '*')
    teacher = str(input('Çocuklar / gençlerle vakit geçirmeyi ve birşeyler öğretmeyi seviyormusunuz ? :'))
    print(50 * '*')
    architect = str(input('Mimari eserler ile uğraşmayı seviyormusunuz ? :'))
    print(50 * '*')

    if pcEngineer == 'evet' :
        jobs.append('Bilgisayar Mühendisliği')
    if softwareEngineer == 'evet' :
        jobs.append('Yazılım Mühendisliği')
    if electricEngineer == 'evet' :
        jobs.append('Elektrik Mühendisliği')
    if teacher == 'evet' :
        jobs.append('Öğretmenlik')
    if architect == 'evet' :
        jobs.append('Mimarlık')

    print(f'Yatkın olabileceğiniz meslekler : {jobs}')

choosingProfession()