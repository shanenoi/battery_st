datas = [ ele.split('=') for ele in open('/sys/class/power_supply/BAT0/uevent').read().split('\n') if ele]
info = {ele[0]: ele[1] for ele in datas}
print(info)
