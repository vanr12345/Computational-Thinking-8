###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
q1 = codesters.Square(-100, 100, 700,'red')
q1 = codesters.Square(100, 200, 200, 'blue')
q1 = codesters.Square(-100, 200, 300, 'gold')
q1 = codesters.Square(-100, -100, 400, 'green')

s1 = codesters.Sprite("dog", 100, 100)
s1.set_size(0.2)

s2 = codesters.Sprite("basketball", -100, 100)
s2.set_size(3)

s3 = codesters.Sprite("Seattle", -150, -100)
s3.set_size(0.1)

s4 = codesters.Sprite("earth", 100, -100)
s4.set_size(0.2)

message1 = codesters.Text("Van Robbins",0,220,"red")
message2 = codesters.Text("I like earth",0,-220,"blue")