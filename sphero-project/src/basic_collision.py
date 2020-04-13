from client import DroidClient
from collision_reactions import collisionReaction
droid = DroidClient()
droid.connect_to_R2D2()

#check that the robot is connected
droid.animate(10)
droid.set_stance(2)  # transition to bipod

#enable collisions, should beep when colliding with something
xThreshold = 50
yThreshold = 50
xSpeed = 50
ySpeed = 50
deadTime = 10
reaction = collisionReaction.BEEP
droid.enable_collision_detection(xThreshold, yThreshold, xSpeed, ySpeed, deadTime, reaction)
droid.roll(0.5, 0, 3)

droid.sleep()
droid.quit()
