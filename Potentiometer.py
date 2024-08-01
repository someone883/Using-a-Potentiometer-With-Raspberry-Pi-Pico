#importing libraries
import machine
import time
#making variables
potPin=28
myPot=machine.ADC(potPin)
while True:
    #reads on a ~430 to ~65535 range
    potVal=myPot.read_u16()
    'voltage=(3.3/65106)*potVal-(430*3.3/65106)'#<-- uncomment this line if you want a ~0V to ~3.3V range
    print(potVal)#<--change potVal to voltage if you want a ~0V to ~3.3V reading
    time.sleep_ms(500)                               