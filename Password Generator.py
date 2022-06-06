import secrets
def passwordGenerators():
    password_list = []
    newpassword = password = secrets.token_urlsafe(16)
    password_list.append(password)
    print(f'Yeni şifre oluşturuldu \nYeni Şifreniz = {newpassword} \nKaydedilen Şifreleriniz : {password_list}')

passwordGenerators()