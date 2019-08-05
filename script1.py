import gym

env = gym.make("MountainCar-v0")

env.reset() # always reset enviroment

done = False

while not done:
    action = 2 # there are 3 actions push left/do nothing/ push right
    new_state, reward, done, _ = env.step(action)
    env.render() # this will show it
env.close()