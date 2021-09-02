#Har 2 soniyada ekranga vaqtni ko'rsatadigan kod yozing.
# Ctrl + C bosilganda (kod to'xtatilganda) ekranga "stopped" deb yozib, loopni to'xtating.
import datetime,time
while True:
    now = datetime.datetime.now()
    print(now.strftime("%X"))
    try:
        time.sleep(2)
    except KeyboardInterrupt:
        print('Stopped!')
        break
