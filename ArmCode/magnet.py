wiringpi.pwmWrite(LED, 0)    # OFF
import wiringpi2 as wiringpi

# If using BCM GPIO numbers
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(18, 2)  # pwm only works on GPIO port 18
wiringpi.pwmWrite(18, 0)  # duty cycle between 0 and 1024. 0 = off, 1024 = fully on

# OR, using wiringpi numbers
wiringpi.wiringPiSetup()
wiringpi.pinMode(1, 2)  # pwm only works on wiringpi pin 1
wiringpi.pwmWrite(1, 0)  # duty cycle between 0 and 1024. 0 = off, 1024 = fully on

# OR, using P1 header pin numbers
wiringpi.wiringPiSetupPhys()
wiringpi.pinMode(12, 2)  # pwm only works on P1 header pin 12
wiringpi.pwmWrite(12, 0)  # duty cycle between 0 and 1024. 0 = off, 1024 = fully on
