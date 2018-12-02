import board
import pulseio
from adafruit_motor import servo
from adafruit_circuitplayground.express import cpx

cpx.pixels.brightness = 0.05

# create a PWMOut object on Pins A1 and A2.
pwm2 = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
pwm1 = pulseio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo_left = servo.Servo(pwm1)
my_servo_right = servo.Servo(pwm2)

while True:
    if cpx.button_a:
        cpx.pixels.fill((50, 50, 0))
        for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees 
            my_servo_left.angle = angle
        for angle in range(180, 0, -5):  # 180 - 0 degrees, 5 degrees
            my_servo_right.angle = angle
    
    elif cpx.button_b:
        cpx.pixels.fill((50, 0, 0))
        for angle in range(180, 0, -5):  # 180 - 0 degrees, 5 degrees at a time
            my_servo_left.angle = angle
        for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
            my_servo_right.angle = angle