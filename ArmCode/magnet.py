import wiringpi

def init_pwm():
    wiringpi.wiringPiSetupGpio()
    wiringpi.pinMode(18, 2)  # pwm only works on GPIO port 18
    wiringpi.pwmWrite(18, 0)  # duty cycle between 0 and 1024. 0 = off, 1024 = fully on

def mag_on():
    wiringpi.pwmWrite(18, 1024)


def mag_off():
    wiringpi.pwmWrite(18, 0)


if __name__ == "__main__":
    init_pwm()
    on = True
    while on:
        entry = input("enter desired action: ")
        if entry == "on":
            mag_on()
        elif entry == "off":
            mag_off()
        else:
            on = False
            mag_off()