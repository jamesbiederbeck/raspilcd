import RPi_I2C_driver as I2C_LCD_driver
import fcntl
import struct

mylcd = I2C_LCD_driver.lcd()


mylcd.lcd_display_string("Hello World", 1) 
