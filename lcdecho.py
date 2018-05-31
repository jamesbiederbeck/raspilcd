#!/usr/bin/python2
import RPi_I2C_driver as I2C_LCD_driver
import sys

message = " ".join(sys.argv()[1:])

mylcd = I2C_LCD_driver.lcd()


mylcd.lcd_display_string(message, 1) 
