from client import DroidClient
droid = DroidClient()
droid.connect_to_R2D2()

#check that the robot is connected
droid.animate(10)
droid.set_stance(2)  # transition to bipod

#enable collisions, should beep when colliding with something
droid.enable_collision_detection()
droid.roll(0.3, 0, 3)

droid.sleep()
droid.quit()
