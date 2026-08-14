print("Задание 2")
packets = [1, 1, 0, 1, 1, 1, 0, 0, 1, 1]
deliver_packets = 0
for packet in packets:
    if packet == 1:
        deliver_packets += 1
print(f"Общее количество успешных пакетов: {deliver_packets}")
process_packets = 0
success_packets = None
for packet in packets:
    if packet == 1:
        process_packets += 1
    if packet == 0 and success_packets == 0:
        print( "Обнаружен критический сбой сети! Соединение разорвано.")
        break
    success_packets = packet
print(f"Количество успешно обработанных пакетов: {process_packets}")
