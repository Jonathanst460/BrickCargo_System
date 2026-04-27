from pybricks.hubs import TechnicHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = TechnicHub()
Motor1 = Motor(Port.A)
Motor2 = Motor(Port.B)
Motor3 = Motor(Port.C)
Motor4 = Motor(Port.D)

Motor1.run_angle(100,100) # erster schritt (zentrieren)
Motor2.run_angle(200, -485);
Motor3.run_angle(100, 90)
Motor2.run_angle(200, 485);
Motor3.run_angle(100, -90)
Motor4.run_time(1000,2500,Stop.BRAKE)
Motor1.run_angle(100,320) # 2ter schritt (zentrieren)
Motor2.run_angle(200, -485);
Motor3.run_angle(100, 90)
Motor2.run_angle(200, 485);
Motor3.run_angle(100, -90)
Motor4.run_time(1000,2500,Stop.BRAKE)
Motor1.run_angle(100,420) # 3ter
Motor2.run_angle(200, -485);
Motor3.run_angle(100, 90)
Motor2.run_angle(200, 485);
Motor3.run_angle(100, -90)
Motor4.run_time(1000,2500,Stop.BRAKE)
Motor1.run_angle(100,-840)