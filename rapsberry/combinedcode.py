#type: ignore
import time
import board
import busio
import adafruit_gps
import adafruit_mpu6050

sda_pin = (board.GP14)
scl_pin = (board.GP15)
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)
X = (mpu.acceleration[0])
Y = (mpu.acceleration[1])
Z = (mpu.acceleration[2])

uart = busio.UART(tx=board.GP16, rx=board.GP17, baudrate=9600, timeout=10)
gps = adafruit_gps.GPS(uart, debug=False)
gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
gps.send_command(b"PMTK220,1000")

last_print = time.monotonic()
start_time = time.monotonic()
with open("data.txt", "a") as datalog:

    while True:
        print(mpu.acceleration)
        time.sleep(.5)
        gps.update()
        current = time.monotonic()
        if current - last_print >= 1.0:
            last_print = current
            if not gps.has_fix:
                # Try again if we don't have a fix yet.
                print("Waiting for fix...")
                continue
            # We have a fix! (gps.has_fix is true)
            # Print out details about the fix like location, date, etc.
            print("=" * 40)  # Print a separator line.

            print("Latitude: {0:.6f} degrees".format(gps.latitude))
            print("Longitude: {0:.6f} degrees".format(gps.longitude))
            print(
                "Precise Latitude: {:2.}{:2.4f} degrees".format(
                    gps.latitude_degrees, gps.latitude_minutes
                )
            )
            print(
                "Precise Longitude: {:2.}{:2.4f} degrees".format(
                    gps.longitude_degrees, gps.longitude_minutes
                )
            )
            print("Fix quality: {}".format(gps.fix_quality))
           
            if gps.altitude_m is not None:
                print("Altitude: {} meters".format(gps.altitude_m))
                altitude = gps.altitude_m
            if gps.speed_knots is not None:
                print("Speed: {} knots".format(gps.speed_knots))
                speed = gps.speed_knots
                lat = gps.latitude
                longi = gps.longitude 
            time.sleep(.25)

            # data structure: (1) time, (2) altitude, (3) speed, (4) latitude/longitude 
            datalog.write(f'{time.monotonic()-start_time},{altitude},{speed},{lat},{longi}\n')
            datalog.flush()
            time.sleep(.5)
