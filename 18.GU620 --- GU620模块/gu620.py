import pyb
from pyb import UART

def DataConver(str_,flag):
	wei_=float(str_)/100
	wei_arr=str(wei_).split('.')
	val_=100000
	if flag==0:#纬度
		val_=10000
	wei_arr[1]=str(float(wei_arr[1])/60*val_).replace('.','')
	weidu=wei_arr[0]+'.'+wei_arr[1]
	return weidu

def	readgps(uart):
	u2 = UART(uart,115200)
	u2.init(115200,timeout=100)
	u2.write('AT+GPSPWR=1\r\n')
	u2.write('AT+GPSRST=2,0\r\n')
	u2.write('AT+GPSLOC=1\r\n')
	pyb.delay(1000)
	_dataRead=u2.read()
	u2.write('AT+GPSLOC=0\r\n')
	pyb.delay(1000)
	_dataRead=u2.read()
	if _dataRead!=None:
		if 60<len(_dataRead)<70:
			_dataRead =_dataRead.decode('utf-8')
			_dataRead1=_dataRead.split(',')
			if len(_dataRead1)>4:
#*******************纬度计算********************
				weidu=_dataRead1[1]
				WD=DataConver(weidu,0)
#*******************经度计算********************
				jingdu=_dataRead1[2]
				JD=DataConver(jingdu,1)
				return JD,WD
	return None

def main():
	while True:
		print(readgps(4))
	
main()