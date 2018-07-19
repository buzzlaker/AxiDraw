import sys
import os
import serial
from serial.tools.list_ports import comports

class AxiDraw():
    port = None
    baud = 9600
    timeout = 1
    TIMESLICE_MS = 10
    microstep = 1
    servo_min = 7500
    servo_max = 28000
    STEP_DIVIDER = 2 ** (microstep - 1)
    STEPS_PER_INCH = 2032 / STEP_DIVIDER
    STEPS_PER_MM = 80 / STEP_DIVIDER
    z_up_position = 60
    z_up_speed = 150
    z_up_delay = 0
    z_down_position = 40
    z_down_speed = 150
    z_down_delay = 0
    ACCELERATION = 16
    MAX_VELOCITY = 4
    CORNER_FACTOR = 0.001
    JOG_ACCELERATION = 16
    JOG_MAX_VELOCITY = 8
    AxiDraw = '04D8:FD92'
    connection = None
    stack = []
    def __init__(self, **kwargs):
        self.port = self.get_port()
        assert (self.port is not None), "No AxiDraw Found."
        self.serial_connect()

    def get_port(self):
        for port in comports():
            if self.AxiDraw in port[2]:
                return port[0]
        return None

    def serial_connect(self):
        self.connection = serial.Serial(self.port, self.baud, timeout=self.timeout)
        if self.connection.isOpen():
             print(self.connection.name + ' is open...')

    def pen_up(self):
        return self.add_command(['SP', 1, self.z_up_delay])

    def pen_down(self):
        return self.add_command(['SP', 0, self.z_down_delay])

    def toggle_pen(self):
        return self.add_command(['TP'])

    def enable_motors(self):
        return self.add_command(['EM',1,1])

    def disable_motors(self):
        return self.add_command(['EM',0,0])

    def add_command(self, vals):
        self.stack.append(','.join(str(x) for x in vals))
        return True

    def doXYMove(self, delta_x, delta_y, duration):
        return self.add_command(['SM',duration,delta_y,delta_x])

    def run_commands(self):
        results = []
        for command in self.stack:
            self.connection.write((command + '\r').encode('utf-8'))
            results.append(self.connection.readline().decode('utf-8').strip())
        return results

ad = AxiDraw()
ad.disable_motors()
ad.enable_motors()
ad.toggle_pen()
ad.disable_motors()
ad.enable_motors()
ad.doXYMove(500, 0, 500)
ad.toggle_pen()
ad.doXYMove(500, 0, 500)
for command in ad.stack:
    print("Running:",command)
    ad.connection.write((command + '\r').encode('utf-8'))
    resp = ad.connection.readline().decode('utf-8').strip()
    print(resp.lower())
    while resp.lower() != 'ok':
        pass
