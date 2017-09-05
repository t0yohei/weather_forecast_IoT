#!/usr/bin/python
# coding: utf-8

# モジュールをインポートする
import RPi.GPIO as GPIO
import time

# GPIO指定をGPIO番号で行う
GPIO.setmode(GPIO.BCM)

# GPIO18ピンを入力モードに設定
GPIO.setup(18, GPIO.IN)

# GPIO18ピンの入力状態を表示する
print GPIO.input(18)

# GPIOピンをリセット
GPIO.cleanup()
