# generated by mBlock5 for HaloCode
# codes make you happy

import halo, event, time



@event.start
def on_start():
    pass

@event.button_pressed
def on_button_pressed():
    global color_scheme
    color_scheme = (color_scheme + 1) % 4

@event.touchpad0_active
def on_0_active():
    halo.led.off_all()
    halo.stop_all_scripts()

color_scheme = 0

@event.touchpad3_active
def on_3_active1():
    halo.led.off_all()
    halo.stop_other_scripts()

    global color_scheme
    
    while True:
        if color_scheme == 0: #Red
            halo.led.show_all((0 + halo.microphone.get_loudness("maximum")), 0, 0)
        elif color_scheme == 1: #Green
            halo.led.show_all(0, (0 + halo.microphone.get_loudness("maximum")), 0)
        elif color_scheme == 2: #Blue
            halo.led.show_all(0, 0, (0 + halo.microphone.get_loudness("maximum")))
        elif color_scheme == 3: #Yellow
            halo.led.show_all((0 + halo.microphone.get_loudness("maximum")), (0 + halo.microphone.get_loudness("maximum")), 0)
        

@event.touchpad2_active
def on_2_active2():
    halo.led.off_all()
    halo.stop_other_scripts()

    while True:
        volume = halo.microphone.get_loudness("maximum")

        if volume < 2:
            halo.led.off_all()
        else:
            halo.led.off_all()
            light_num =volume // 12 + 3
            if light_num > 11:
                light_num=12

            halo.led.off_all()
            light_multiple(light_num, 'blue')

def light_multiple(light_num, color_scheme):
    if light_num==0:
        return

    pause=0.05
    rgb_step = 20
    light_multiple(light_num-1, color_scheme)

    if color_scheme == 'green':
        halo.led.show_single(light_num, light_num*rgb_step, 255-light_num*rgb_step, 0)
    elif color_scheme == 'blue':
        halo.led.show_single(light_num, 0, 0, 255-light_num*rgb_step)
    time.sleep(pause)

@event.touchpad1_active
def on_1_active3():
    halo.led.off_all()
    halo.stop_other_scripts()

    while True:
        if halo.microphone.get_loudness("maximum") < 2:
            halo.led.off_all()

        else:
            if halo.microphone.get_loudness("maximum") > 2 and halo.microphone.get_loudness("maximum") < 8:
                halo.led.off_all()
                light_multiple(1, 'green')

            if halo.microphone.get_loudness("maximum") > 8 and halo.microphone.get_loudness("maximum") < 12:
                halo.led.off_all()
                light_multiple(2, 'green')

            if halo.microphone.get_loudness("maximum") > 12 and halo.microphone.get_loudness("maximum") < 16:
                halo.led.off_all()
                light_multiple(3, 'green')

            if halo.microphone.get_loudness("maximum") > 16 and halo.microphone.get_loudness("maximum") < 20:
                halo.led.off_all()
                light_multiple(4, 'green')

            if halo.microphone.get_loudness("maximum") > 20 and halo.microphone.get_loudness("maximum") < 25:
                halo.led.off_all()
                light_multiple(5, 'green')

            if halo.microphone.get_loudness("maximum") > 25 and halo.microphone.get_loudness("maximum") < 30:
                halo.led.off_all()
                light_multiple(6, 'green')

            if halo.microphone.get_loudness("maximum") > 30 and halo.microphone.get_loudness("maximum") < 40:
                halo.led.off_all()
                light_multiple(7, 'green')
                
            if halo.microphone.get_loudness("maximum") > 40 and halo.microphone.get_loudness("maximum") < 45:
                halo.led.off_all()
                light_multiple(8, 'green')

            if halo.microphone.get_loudness("maximum") > 45 and halo.microphone.get_loudness("maximum") < 50:
                halo.led.off_all()
                light_multiple(9, 'green')
                
            if halo.microphone.get_loudness("maximum") > 50 and halo.microphone.get_loudness("maximum") < 60:
                halo.led.off_all()
                light_multiple(10, 'green')

                
            if halo.microphone.get_loudness("maximum") > 60 and halo.microphone.get_loudness("maximum") < 70:
                halo.led.off_all()
                light_multiple(11, 'green')

            if halo.microphone.get_loudness("maximum") > 70:
                halo.led.off_all()
                light_multiple(12, 'green')

