"""1D Kalman filter: estimating a robot's position from noisy sensors.

The robot drives along a corridor at a known commanded speed, but its
wheels slip a little. A range sensor measures its position, but the
readings are noisy. The Kalman filter combines both to get an estimate
that is better than either one on its own.

Run:  python kalman.py
"""
import random

random.seed(1)

DT = 1.0
COMMANDED_SPEED = 1.0
MOTION_NOISE = 0.1    # std dev of wheel slip per step
SENSOR_NOISE = 2.0    # std dev of the range sensor
STEPS = 20


class Kalman1D:
    def __init__(self, x0, var0, process_var, sensor_var):
        self.x = x0             # position estimate
        self.var = var0         # how unsure we are about it
        self.q = process_var
        self.r = sensor_var

    def predict(self, velocity, dt):
        self.x += velocity * dt
        self.var += self.q          # moving adds uncertainty

    def update(self, z):
        k = self.var / (self.var + self.r)   # Kalman gain: how much to trust z
        self.x += k * (z - self.x)
        self.var *= (1 - k)                  # measuring removes uncertainty
        return k


if __name__ == "__main__":
    true_x = 0.0
    kf = Kalman1D(x0=0.0, var0=1.0,
                  process_var=MOTION_NOISE ** 2, sensor_var=SENSOR_NOISE ** 2)
    sensor_err = filter_err = 0.0

    print(" step   true   sensor  estimate   gain")
    for step in range(1, STEPS + 1):
        true_x += COMMANDED_SPEED * DT + random.gauss(0, MOTION_NOISE)
        z = true_x + random.gauss(0, SENSOR_NOISE)
        kf.predict(COMMANDED_SPEED, DT)
        k = kf.update(z)
        sensor_err += abs(z - true_x)
        filter_err += abs(kf.x - true_x)
        print(f"{step:5d} {true_x:6.2f} {z:8.2f} {kf.x:9.2f} {k:6.2f}")

    print(f"\nAverage sensor error: {sensor_err / STEPS:.2f}")
    print(f"Average filter error: {filter_err / STEPS:.2f}")
