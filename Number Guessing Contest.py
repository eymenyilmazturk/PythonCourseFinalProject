def NumberGuessingContest():
    import random
    name = str(input('Hoşgeldiniz, oyuna başlamak için isminizi giriniz : '))
    print(f'Hoşgeldin, {name} \nBu oyunda bilgisayar 3 ile 20 arasında bir sayı seçer ve sizden 3 adet sayı ister.\nEğer girdiğiniz sayıların toplamı bilgisayarın seçtiği sayıya eşit ise oyunu kazanırsınız.\nBaşarılar...')
    print(50 * '*')
    number = random.randint(3,20)
    counter = 0
    while True:
        counter +=1
        no1 = int(input('1. sayıyı giriniz : '))
        no2 = int(input('2. sayıyı giriniz : '))
        no3 = int(input('3. sayıyı giriniz : '))
        print(50*'*')
        total = no1 + no2 + no3
        if total < 3:
            print('Toplamları 3ten büyük sayılar yazınız')
            print(50 * '*')
            continue
        elif total > 20:
            print('Toplamları 20den küçük sayılar yazınız')
            print(50 * '*')
            continue
        elif total == number:
            print(f'Tebrikler oyunu kazandınız...\nBilgisayarın seçtiği sayı : {number}\nSizin seçtiğiniz sayıların toplamı : {total}\nTahmin sayınız : {counter}')
            print(50 * '*')
            break


NumberGuessingContest ()
