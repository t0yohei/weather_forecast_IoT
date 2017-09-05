#!/usr/bin/python
# coding: utf-8

# ------------------------
#   モジュールインポート
# ------------------------
# GPIOモジュールインポート
import RPi.GPIO as GPIO
# timeモジュールインポート
import time

# ----------------------------
#   GPIO番号の定義(GPIO番号)
# ----------------------------
# GPIOの番号の定義(LED)
gpioLed = (21, 20, 16, 12, 25, 24, 23)

# GPIOの番号の定義(スイッチ)
gpioSwitch = 18

# ------------------
#   GPIOモード設定
# ------------------
# GPIO番号指定をBCM(GPIO番号)に設定
# ボードピン番号に設定する場合は GPIO.setmode(GPIO.BOARD)にする
GPIO.setmode(GPIO.BCM)

# GPIOの初期化(LED)
GPIO.setup(gpioLed, GPIO.OUT)

# GPIOの初期化(スイッチ)
GPIO.setup(gpioSwitch, GPIO.IN)


# -------------------------
#   LEDを配列の順番で点灯
# -------------------------
try:
    # 最初のLEDのGPIO番号を配列から取得して点灯させる
    # 点灯後は1秒間そのままにする
    currentLed = gpioLed[0]
    GPIO.output(currentLed, 1)
    time.sleep(1)

    # gpioLed配列の残りの要素を取得する
    restGpioLed = gpioLed[1:]

    # 残りの要素について順次点滅制御する
    for nextLed in restGpioLed:
        # 現在点灯しているLEDを消灯させる
        GPIO.output(currentLed, 0)
        # 次のLEDを点灯させる
        GPIO.output(nextLed, 1)
        # 点灯させたLEDのGPIO番号を現在のLED番号にする
        currentLed = nextLed
        # 1秒間そのままにする
        time.sleep(1)

    # 最後のLEDを消灯する
    GPIO.output(currentLed, 0)


    # ------------------------------------
    #   スイッチの状態を1秒ごとに3回表示
    # ------------------------------------
    for num in range(0, 3):
        print GPIO.input(gpioSwitch)
        time.sleep(1)

# ---------------
#   GPIOリセット
# ---------------
finally:
    GPIO.cleanup()
