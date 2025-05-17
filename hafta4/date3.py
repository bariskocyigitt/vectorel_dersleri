import datetime as ts,time,os

while True:
    os.system("cls")
    tarih= ts.datetime.now()
    print(tarih.strftime(">>> %H:%M:%S <<<"))
    time.sleep(1)
    
    