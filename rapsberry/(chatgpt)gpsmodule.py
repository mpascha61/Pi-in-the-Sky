#type: ignore
import time
import board
import busio
import adafruit_gps

# Create a serial connection for the GPS connection using default speed and
# a slightly higher timeout (GPS modules typically update once a second).
uart = busio.UART(board.TX, board.RX, baudrate=9600, timeout=30)
gps = adafruit_gps.GPS(uart)

# Turn on the basic GGA and RMC info (what you typically want)
gps.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')

# Set update rate to once a second (1Hz) which is the default for most GPS modules.
gps.send_command(b'PMTK220,1000')

# Main loop runs forever printing the location, etc. every second.
last_print = time.monotonic()
while True:
    # Make sure to call gps.update() every loop iteration and at least twice
    # as fast as data comes from the GPS unit (usually every second).
    # This returns a bool that's true if it parsed new data (you can ignore it
    # though if you don't care and instead look at the has_fix property).
    gps.update()
    # Every second print out current location details if there's a fix.
    current = time.monotonic()
    if current - last_print >= 1.0:
        last_print = current
        if not gps.has_fix:
            # Try again if we don't have a fix yet.
            print('Waiting for fix...')
            continue
        # We have a fix! (gps.has_fix is true)
        # Print out details about the fix like location, date, etc.
        print('Altitude = ', gps.altitude)
        print('Latitude: {0:.6f} degrees'.format(gps.latitude))
        print('Longitude: {0:.6f} degrees'.format(gps.longitude))
        print('Fix timestamp: {}/{}/{} {:02}:{:02}:{:02}'.format(
              gps.timestamp_utc.tm_mon,   # Grab parts of the time from the
              gps.timestamp_utc.tm_mday,  # struct_time object that holds
              gps.timestamp_utc.tm_year,  # the fix time.  Note you might
              gps.timestamp_utc.tm_hour,  # not get all data like year, day,
              gps.timestamp_utc.tm_min,   # month!
              gps.timestamp_utc.tm_sec))

