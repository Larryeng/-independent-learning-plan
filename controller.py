import pyfirmata

comport='COM5' #your usb-port

board=pyfirmata.Arduino(comport)

led_1=board.get_pin('d:8:o') #pin8
led_2=board.get_pin('d:9:o') #pin9
led_3=board.get_pin('d:10:o') #pin10
led_4=board.get_pin('d:11:o') #pin11
led_5=board.get_pin('d:12:o') #pin12
def led(fingerUp):
    if fingerUp==[0,0,0,0,0]: #no finger
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)

    elif fingerUp==[0,1,0,0,0]: #forefinger
        led_1.write(1)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif fingerUp==[0,1,1,0,0]: #forefinge+middle finger
        led_1.write(1)
        led_2.write(1)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)    
    elif fingerUp==[0,1,1,1,0]: #forefinge+middle finger+ring finger
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(0)
        led_5.write(0)
    elif fingerUp==[0,1,1,1,1]: #forefinge+middle finger+ring finger+little finger
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(0)
    elif fingerUp==[1,1,1,1,1]: #forefinge+middle finger+ring finger+little finger+big thumb
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)
    elif fingerUp==[0,0,1,0,0]: #middle finger
        led_1.write(0)
        led_2.write(0)
        led_3.write(1)
        led_4.write(0)
        led_5.write(0)
