"""PID speed controller for a simple robot wheel.

A motor has to reach and hold a target speed. The PID controller looks at
the error (target - actual) and decides how much power to send:
  P reacts to the current error,
  I removes leftover steady error,
  D damps overshoot.

Try changing KP, KI and KD to see how the response changes.

Run:  python pid.py
"""

KP, KI, KD = 0.6, 0.3, 0.05
TARGET_SPEED = 10.0   # m/s
DT = 0.1              # seconds per step
STEPS = 80


class PID:
    def __init__(self, kp, ki, kd, limit=None):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.limit = limit
        self.integral = 0.0
        self.prev_error = None

    def update(self, error, dt):
        self.integral += error * dt
        derivative = 0.0 if self.prev_error is None else (error - self.prev_error) / dt
        self.prev_error = error
        out = self.kp * error + self.ki * self.integral + self.kd * derivative
        if self.limit is not None:
            out = max(-self.limit, min(self.limit, out))
        return out


class Motor:
    """First-order model: speed moves towards (gain * power), minus friction."""

    def __init__(self, gain=4.0, time_constant=0.5, friction=0.5):
        self.speed = 0.0
        self.gain, self.tau, self.friction = gain, time_constant, friction

    def step(self, power, dt):
        target = self.gain * power - self.friction
        self.speed += (target - self.speed) * dt / self.tau
        return self.speed


def bar(value, scale=4):
    return "#" * max(0, int(value * scale))


if __name__ == "__main__":
    pid = PID(KP, KI, KD, limit=5.0)
    motor = Motor()
    print(f"Target speed {TARGET_SPEED}   (| marks the target)")
    for i in range(STEPS):
        power = pid.update(TARGET_SPEED - motor.speed, DT)
        speed = motor.step(power, DT)
        if i % 4 == 0:
            line = bar(speed).ljust(int(TARGET_SPEED * 4))
            line = line[:int(TARGET_SPEED * 4)] + "|" + line[int(TARGET_SPEED * 4):]
            print(f"t={i * DT:4.1f}s speed={speed:5.2f} {line}")
    print(f"Final error: {TARGET_SPEED - motor.speed:.3f}")
