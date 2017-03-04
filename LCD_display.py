import time
from RPLCD import CharLCD
lcd = CharLCD(cols=16, rows=2, pin_rs=26, pin_e=24, pins_data=[22,18,16,12])
lcd.cursor_pos = (0,4)
lcd.write_string(u'HIQUALOGY')
lcd.cursor_pos = (1,3)
lcd.write_string(u'DriverGuard')
time.sleep(2)
lcd.clear()
lcd.cursor_pos = (0,2)
lcd.write_string(u'Alcohol check')
time.sleep(2)
lcd.clear()
lcd.cursor_pos = (0,4)
lcd.write_string(u'Blow into')
lcd.cursor_pos = (1,2)
lcd.write_string(u'breathalyzer')
time.sleep(2)
lcd.clear()

#alcohol_level = None

#def breathalyzer_results(alcohol_level)

#Blowdetected = False
#i = 0
#While Blowdetected:
#i = i+1
#breathalyzer_results(alcohol_level)
#if i == 5:
#lcd.clear()
#lcd.cursor_pos = (0,2)
#lcd.write_string(u'Alcohol check')
#time.sleep(2)
#lcd.clear()

framebuffer = [
    'Safety Messages:' ,
    '' ,
]

def write_to_lcd(lcd, framebuffer, num_cols):
    lcd.home()
    for row in framebuffer:
        lcd.write_string(row.ljust(num_cols)[:num_cols])
        lcd.write_string('\r\n')

from RPLCD import CharLCD
lcd = CharLCD(cols=16, rows=2, pin_rs=26, pin_e=24, pins_data=[22,18,16,12])
write_to_lcd(lcd, framebuffer, 16)

import time
long_string = 'This string is too long to fit'
for i in range(len(long_string) - 16 + 1):
    framebuffer[1] = long_string[i:i+16]
    write_to_lcd(lcd, framebuffer, 16)
    time.sleep(0.5)

def loop_string(string, lcd, framebuffer, row, num_cols, delay=0.5):
    padding = ' ' * num_cols
    s = padding  + string + padding
    for i in range(len(s) - num_cols + 1):
        framebuffer[row] = s[i:i+num_cols]
        write_to_lcd(lcd, framebuffer, num_cols)
        time.sleep(delay)

while True:
    loop_string(long_string, lcd, framebuffer, 1, 16)

