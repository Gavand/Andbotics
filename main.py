def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    PCA9685.set_servo_position(PCA9685.ServoNum.SERVO4, 80, 64)
    PCA9685.set_servo_position(PCA9685.ServoNum.SERVO13, 100, 64)
    basic.pause(2000)
    PCA9685.set_servo_position(PCA9685.ServoNum.SERVO7, 0, 64)
    basic.pause(100)
    PCA9685.set_servo_position(PCA9685.ServoNum.SERVO5, 90, 64)
    basic.pause(500)
    PCA9685.set_servo_position(PCA9685.ServoNum.SERVO6, 0, 64)
    basic.pause(200)
    PCA9685.set_servo_position(PCA9685.ServoNum.SERVO6, 90, 64)
    basic.pause(200)
    PCA9685.set_servo_position(PCA9685.ServoNum.SERVO6, 0, 64)
    basic.pause(200)
    PCA9685.set_servo_position(PCA9685.ServoNum.SERVO6, 80, 64)
    basic.pause(200)
    PCA9685.set_servo_position(PCA9685.ServoNum.SERVO7, 180, 64)
    basic.pause(200)
    PCA9685.set_servo_position(PCA9685.ServoNum.SERVO6, 60, 64)
    basic.pause(200)
    PCA9685.set_servo_position(PCA9685.ServoNum.SERVO5, 45, 64)
input.on_button_pressed(Button.B, on_button_pressed_b)

PCA9685.reset(PCA9685.chip_address("0x40"))