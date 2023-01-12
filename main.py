from IntenetSpeedBot import InternetSpeedTwitterBot

promised_speed = 10

complaint = InternetSpeedTwitterBot()
list = complaint.get_internet_speed()

try:
    down = float(list[0])
    up = float(list[1])

except ValueError:
    print('ok')

else:
    if down < 0.6*promised_speed:
        complaint.text_provider(down=down, up=up)
        print('success')


