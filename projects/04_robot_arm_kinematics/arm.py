"""Forward and inverse kinematics of a 2-link planar robot arm.

Forward kinematics: given the joint angles, where is the gripper?
Inverse kinematics: given where we want the gripper, what joint angles?

Run:  python arm.py
"""
import math

L1 = 1.0   # length of the upper arm
L2 = 0.8   # length of the forearm


def forward(theta1, theta2):
    """Joint angles (radians) -> (elbow, gripper) positions."""
    elbow = (L1 * math.cos(theta1), L1 * math.sin(theta1))
    gripper = (elbow[0] + L2 * math.cos(theta1 + theta2),
               elbow[1] + L2 * math.sin(theta1 + theta2))
    return elbow, gripper


def inverse(x, y, elbow_up=True):
    """Gripper target (x, y) -> joint angles, or None if out of reach."""
    d2 = x * x + y * y
    cos_t2 = (d2 - L1 ** 2 - L2 ** 2) / (2 * L1 * L2)   # law of cosines
    if not -1.0 <= cos_t2 <= 1.0:
        return None
    theta2 = math.acos(cos_t2)
    if elbow_up:
        theta2 = -theta2
    theta1 = math.atan2(y, x) - math.atan2(L2 * math.sin(theta2),
                                           L1 + L2 * math.cos(theta2))
    return theta1, theta2


if __name__ == "__main__":
    print("Forward kinematics")
    for a1, a2 in [(0, 0), (90, 0), (45, 45), (30, -60)]:
        _, (gx, gy) = forward(math.radians(a1), math.radians(a2))
        print(f"  angles ({a1:4d}, {a2:4d}) deg -> gripper ({gx:5.2f}, {gy:5.2f})")

    print("\nInverse kinematics (checked with forward kinematics)")
    for tx, ty in [(1.2, 0.6), (0.5, 1.0), (1.8, 0.0), (3.0, 0.0)]:
        sol = inverse(tx, ty)
        if sol is None:
            print(f"  target ({tx}, {ty}) is out of reach")
            continue
        _, (gx, gy) = forward(*sol)
        print(f"  target ({tx}, {ty}) -> angles "
              f"({math.degrees(sol[0]):6.1f}, {math.degrees(sol[1]):6.1f}) deg"
              f" -> gripper ({gx:.2f}, {gy:.2f})")
