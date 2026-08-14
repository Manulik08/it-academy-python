print("Задание 1")
logs = [ 200, 200, 404, 200, 500, 200, 503, 400, 200, 404, 500, 200, 503 ]
success_request = 0
client_error = 0
server_error = 0
temp_server_error = None
for log in logs:
    if log == 200:
        success_request += 1
    elif log == 404:
        client_error += 1
    elif log == 500 or log == 503:
        server_error += 1
    if log == 500 and temp_server_error == 503:
        print("Сервер считается недоступным.")
        break
    temp_server_error = log
print(f"Статистика: \nКоличество успешных запросов: {success_request}\nКоличество клиентских ошибок: {client_error}\nКоличество серверных ошибок: {server_error}")