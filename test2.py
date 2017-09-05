#!/usr/bin/python
# coding: utf-8

# モジュールをインポートする
import RPi.GPIO as GPIO
import time

# GPIO指定をGPIO番号で行う
GPIO.setmode(GPIO.BCM)

# GPIO21ピンを出力モードに設定
GPIO.setup(21, GPIO.OUT)

# GPIO21番ピンを3.3Vに設定
GPIO.output(21, 1)

# 1秒待つ
time.sleep(1)

# GPIO21番ピンを0Vに設定
GPIO.output(21, 0)

# GPIO設定をリセット
GPIO.cleanup()
