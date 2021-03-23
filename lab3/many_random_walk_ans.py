import numpy as np


walks = []
for i in range(5000):
    nsteps = 1000
    draws = np.random.randint(0, 2, size=nsteps)
    steps = np.where(draws > 0, 1, -1)
    walk = steps.cumsum()
    walks.append(walk)


min_positions, max_positions, min_jump_over_30 = [], [], []
for walk in walks:
    min_positions.append(walk.min())
    max_positions.append(walk.max())
    jump = (np.abs(walk) >= 30).argmax()
    min_jump_over_30.append(jump if jump > 0 else np.Inf)

print("Minimum position from all walks: {0}\nMaximum position: {1}\nMinimum jump over 30: {2}"
      .format(np.array(min_positions).min(), np.array(max_positions).max(), np.array(min_jump_over_30).min()))
