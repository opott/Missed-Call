default persistent.safeending = False
default persistent.badending = False
default persistent.loopending = False

define y = Character("You", voice_tag="you", color="#51e019ff")
define c = Character("Caller", voice_tag="caller", color="#ff2626")

image nightbedroom:
    "images/Dark Bedroom.jpg"

image footprints:
    "images/Footprints.jpg"

image frontdoor:
    "images/Front Door.jpg"

image incoming:
    "images/Incoming Call.jpg"

image morningroom:
    "images/Morning Bedroom.jpg"

image oncall:
    "images/On Call.jpg"

image persontowards:
    "images/Person Under Lamp Post - Looking Towards.jpg"

image personlamp:
    "images/Person Under Lamp Post.jpg"

image phoneon:
    "images/Phone On.jpg"

$name = ""

label start:
    $name = renpy.input(default='player', prompt="What is your name?")

    "Good luck, [name]!"

    if persistent.safeending == True or persistent.badending == True or persistent.loopending == True:
        "Seems like you've been here before :)"

label game:
    scene nightbedroom

    "It is 2:13 AM."

    "You are trying to sleep."

    play sound "audio/vibrate.opus"

    "Your phone suddenly vibrates on the bedside table."

    "You look at the screen."

    scene incoming

    "You stare at it for a second, confused."

    menu:
        "Answer":
            jump answer
        "Decline":
            jump decline

label answer:
    "You answer slowly."

    scene oncall

    y "\"Hello?\""

    "There is static for a while."

    play sound "audio/static.opus"

    c "\"Don't hang up. You need to listen to me.\""

    "You freeze..."

    "The voice sounds exactly like yours."

    y "\"Who is this!?!?\""

    c "\"It's you... In about ten minutes.\""

    "You think this is a prank, but the caller keeps speaking quickly, like they're in danger."

    c "\"Somebody if going to knock on your front door... Don't answer it...\""

    "You bolt upright in bed."

    y "\"What are you talking about!?!?\""

    c "\"Please... Just trust me...\""

    play sound "audio/knock.opus"

    "A few seconds later, there is a loud knock from downstairs."

    jump knock

label decline:
    "You reject the call."

    scene nightbedroom

    "The room goes silent."

    "A few seconds later, your phone vibrates with a voicemail notification."

    "You don't remember voicemail ever being that fast."

    "You play it."

    scene oncall

    c "(whispering) \"Don't answer the door.\""

    play sound "audio/knock.opus"

    "There's a knock downstairs."

    jump knock

label knock:
    "The knocking is slow and deliberate."

    "Not frantic."

    "Not random."

    "Like whoever is outside knows you are awake."

    play sound "audio/vibrate.opus"

    scene incoming

    menu:
        "Answer":
            jump answer2
        "Decline and check the window":
            jump decline2

label answer2:
    "You answer."

    scene oncall

    c "\"Good, you still have time.\""

    y "\"Time for what!?!?\""

    c "\"To avoid making the same mistake..."
    c "\"See, I answered the door..."
    c "\"The person outside never spoke..."
    c "\"Now..."
    c "\"Everything seems to be going wrong.\""

    play sound "audio/knock.opus"

    "You hear another knock."

    "This time, more aggressive."

    c "\"Whatever you do, don't look directly at them.\""

    menu:
        "Stay in your room":
            jump safeending
        "Go downstairs anyway":
            jump badending

label decline2:
    scene personlamp

    "You ignore the call and creep towards the window."
    
    "Peeking around the curtain you see someone standing at your front door, underneath the streetlight."

    "They're completely still."

    "You can't get a clear look at their face."

    play sound "audio/vibrate.opus"

    "Your phone starts ringing again behind you."

    "You glance between the screen and the figure outside."

    scene persontowards

    "The figure turns its head slowly towards your window."

    "Your phone stops ringing."

    "Then you hear movement downstairs..."

    "Like the front door opening..."

    menu:
        "Hide":
            jump loopending
        "Run downstairs":
            jump badending

label safeending:
    scene nightbedroom

    "You lock your bedroom door and stay completely silent."

    "The knocking continues for a while."

    "Then it stops."

    "Your phone line goes dead."

    "You fall asleep..."

    "Morning comes."

    "You head towards the window and lift the curtain hesitantly."

    "There are muddy footprints leading to your house..."

    "But none leading away..."

    "Your phone shows no calls from last night."

    "The End"

    $ persistent.safeending = True

    return

label badending:
    scene frontdoor

    "You reach the front door."

    "The hallway feels colder with each step."

    "You open the door."

    "Nobody is there."

    scene phoneon

    "You look down and see your phone lying on the doorstep, screen on."

    scene oncall

    "You look up, someone is standing at the end of the road."

    "They look exactly like you."

    "You've lost consciousness."

    "The End"

    $ persistent.badending = True

    return

label loopending:
    scene nightbedroom

    "You hide and wait."

    "Eventually everything goes quiet."

    "Your phone screen lights up again."

    "It begins dialling a number automatically..."

    "Your own number..."

    scene oncall

    play sound "audio/vibrate.opus"

    "You hear a phone start to ring somewhere else in the room."

    "On the bedside table."

    "You realised, you were the caller."

    "The End"

    $ persistent.loopending = True

    return