default persistent.safeending = False
default persistent.badending = False
default persistent.loopending = False

define y = Character("You", voice_tag="you", color="#51e019ff")
define c = Character("Caller", voice_tag="caller", color="#ff2626")

$name = ""

label start:
    $name = renpy.input(default='player', prompt="What is your name?")

    "Good luck, [name]!"

    if persistent.safeending == True or persistent.badending == True or persistent.loopending == True:
        "Seems like you've been here before :)"

label game:
    "It is 2:13 AM."

    "You are trying to sleep."

    "Your phone suddenly vibrates on the bedside table."

    "You look at the screen."

    # image of phone screen = caller is you

    "You stare at it for a second, confused."

    menu:
        "Answer":
            jump answer
        "Decline":
            jump decline

label answer:
    "You answer slowly."

    y "\"Hello?\""

    "There is static for a second."

    # static sfx

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

    "A few seconds later, there is a loud knock from downstairs."

    # knocking sfx

label decline:
    "You reject the call."

    "The room goes silent."

    "A few seconds later, your phone vibrates with a voicemail notification."

    "You don't remember voicemail ever being that fast."

    "You play it."

    c "(whispering) \"Don't answer the door.\""

    "There's a knock downstairs."

    # knocking sfx

label knock:
    "The knocking is slow and deliberate."

    "Not frantic."

    "Not random."

    "Like whoever is outside knows you are awake."

    # vibration sfx
    # image of phone screen = caller is you

    menu:
        "Answer":
            jump answer2
        "Decline and check the window":
            jump decline2

label answer2:
    "You answer."

    c "\"Good, you still have time.\""

    y "\"Time for what!?!?\""

    c "\"To avoid making the same mistake..."
    c "\"See, I answered the door..."
    c "\"The person outside never spoke..."
    c "\"Now..."
    c "\"Everything seems to be going wrong.\""

    # louder knocking sfx

    "You hear another knock."

    "This time, more aggressive."

    c "\"Whatever you do, don't look directly at them.\""

    menu:
        "Stay in your room":
            jump safeending
        "Go downstairs anyway":
            jump badending

label decline2:
    "You ignore the call and creep towards the window."
    
    "Peeking around the curtain you see someone standing at your front door, underneath the streetlight."

    "They're completely still."

    "You can't get a clear look at their face."

    "Your phone starts ringing again behind you."

    # vibrating sfx

    "You glance between the screen and the figure outside."

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
    "You reach the front door."

    "The hallway feels colder with each step."

    "You open the door."

    "Nobody is there."

    "You look down and see your phone lying on the doorstep, screen on."

    # image of phone screen = caller is you

    "You look up, someone is standing at the end of the road."

    "They look exactly like you."

    "You've lost consciousness."

    "The End"

    $ persistent.badending = True

    return

label loopending:
    "You hide and wait."

    "Eventually everything goes quiet."

    "Your phone screen lights up again."

    "It begins dialling a number automatically..."

    "Your own number..."

    "You hear a phone start to ring somewhere else in the room."

    "On the bedside table."

    "You realised, you were the caller."

    "The End"

    $ persistent.loopending = True

    return