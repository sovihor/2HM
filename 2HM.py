import requests

url = 'https://hide.mn/en/demo/'

# Попытка получить страницу и проверить статус ответа
try:
    response = requests.get(url)
    
    # Проверка на успешный ответ от сервера
    if response.status_code == 200:
        # Если текст на странице содержит "Your email", продолжаем
        if 'Your email' in response.text:
            email = input('Введите электронную почту для получения тестового периода: ')

            response = requests.post('https://hide.mn/en/demo/success/', data={
                "demo_mail": f"{email}"
            })

            if 'Your code has been sent to your email address' in response.text:
                print('✅ \033[1;32mВаш код уже в пути!\033[0m Проверь, если не веришь.')
            else:
                print('⚠️ \033[1;31mПочта не канает.\033[0m')
        else:
            print('⚠️ \033[1;31mНа странице не найдено нужного текста.\033[0m Проверьте доступность страницы.')
    else:
        print(f"❌ \033[1;31mХЗ, что это Пробуй ещё.\033[0m Код ответа: {response.status_code}")
        
except requests.RequestException as e:
    print(f"❌ \033[1;31mЧёт не так Пробуй ещё:\033[0m {e}")
