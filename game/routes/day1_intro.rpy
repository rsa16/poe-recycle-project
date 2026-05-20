label day1_intro:
    scene bg roadside
    show outro truck
    play sound "driving.mp3"
    with dissolve
    pause 0.5

    show reese at center_slot
    play sound "crash.mp3"
    with vpunch
    pause 0.3

    hide outro truck
    with dissolve

    scene black with fade
    scene bg roadside with fade
    
    r "Ow... my head... where am I?"

    show screen intro_card("name reese", "reese")
    with dissolve
    pause 0.5
    hide screen intro_card
    with dissolve

    r "I guess that was a pretty nasty fall, since I can't seem to remember anything. But..."

    show outro truck
    with dissolve
    hide outro truck
    with dissolve

    r "I can only seem to remember that three-arrow symbol on the truck..."
    r "Well, it seems the only option I have is to look for someone to gather information."

    "Faint chatter can be heard approaching"

    r "Hold on! Are those..."

    "A booming voice echoes down the street."
    "ALAS! A TRAVELER HAS ARRIVED UPON OUR CONCRETE SHORES!"
    "Gosh Alu! Do you always have to be so... unelegant with your introductions?!"
    "You're all insufferable..."
    "The voices get louder, and you see a miscellaneous assortment of five figures make their way towards you."
    "A plastic plate with food stains rolls over to you."

    show plato at center_slot
    with dissolve
    pl "Whoa, hi! Who are you? What's your name? My name's Plato. Where'd ya come from? Wow, you look so cool, I hope we can be friends! We can be best friends! Wow, I have a new best friend!!"

    show screen intro_card("name plato", "plato")
    with dissolve
    pause 0.5
    hide screen intro_card
    with dissolve

    r "Wow, hello! Uh... my name's Reese and... I love your energy."

    pl "Aww, thanks, you're so nice! Wow, you are such an awesome best friend, Reese! Reese, I like that name."

    "The plastic plate is quickly shoved aside by a flap of cardboard"

    show plato at left_slot
    show expression scaled_emot("emot blush", "g") at emot_center
    show paige at center_slot
    with dissolve
    p "You're so chatty it's making my FOLDS ache!!!"

    "The cardboard flusteredly turns its attention back to you"

    show emot blush at emot_center
    with dissolveR
    p "Oh... hi:) I'm Paige, who are you?"

    show screen intro_card("name paige", "paige")
    with dissolve
    pause 0.5
    hide screen intro_card
    with dissolve

    r "Hi! I'm Reese -"

    p "Wait, do you mind standing still? You have a little smudge on you. Ugh, and your lid is all crooked."

    r "Well, I-"

    p "You should really clean yourself up. This... look... isn't exactly appealing. At least, not to me."

    r "I did just fall out of a truck-"

    hide emot blush
    with dissolve

    hide plato
    with dissolve
    show paige at left_slot
    with move
    show alu at center_slot
    with dissolve
    alu "AHEM! Behold my brilliant luster, good fellow, for you are standing in the presence of none other than Alu, future big shot in the world of sustainability!"

    show screen intro_card("name alu", "alu")
    with dissolve
    pause 0.5
    hide screen intro_card
    with dissolve

    alu "It is absolutely delightful to make your acquaintance, dear friend!"

    r "U-uh, thank you! It's nice to meet you to-"

    p "Alu. I wasn't done TALKING with them!"

    alu "Well, since when did you get all the attention?"

    "Paige and Alu descend into a petty argument. Plato seems to be talking at them, simply adding noise."

    "A glass bottle rolls forward hesitantly"

    hide paige
    with dissolve
    show alu at left_slot
    with move
    show g at center_slot
    with dissolve

    show emot blush at emot_center
    with dissolve
    g "H-hello! My name is G."

    show screen intro_card("name g", "g")
    with dissolve
    pause 0.5
    hide screen intro_card
    with dissolve

    r "Hello G! It's nice to meet someone who seems a little more normal."

    g "Heh.. well, I'll assure you that although they seem rather childish, they're all super cool materials! I wish I was as cool as them..."

    r "Sorry, what was that?"

    hide emot blush
    with dissolve
    show emot surprise at emot_center
    with dissolve
    g "Oh! Just me thinking out loud! Don't worry about it..."

    hide emot surprise
    with dissolve

    g "Actually, you haven't met the last of the materials who live here!"

    "At the back of the group is a spray bottle, who upon being mentioned, seems to roll their eyes as they make their way over."

    hide alu
    with dissolve
    show g at left_slot
    with move
    show pepton at center_slot
    with dissolve
    pep "I'd rather not be associated with this gang of fools... but it's alright seeing a fresh face I guess."

    pep "I go by Pepton 'round these parts."

    show screen intro_card("name pepton", "pepton")
    with dissolve
    pause 0.5
    hide screen intro_card
    with dissolve

    g "Yup! Pepton's really cool! Did you know their family: the Pep-"

    pep "Annddd I'm gonna need you to stop talking there."

    p "There goes Pepton and their high and mighty self-importance. Too good to be called by their first name, and somehow too good for their family too."

    pep "Like you're any better, Paige."

    alu "Not like either of you compare to me."

    "I better do something before it's a full on war..."

    r "SO! Who's going to actually listen to me?"

    "The ensemble of materials shut up as you explain your situation"

    pl "Sounds like you've somehow hitched a ride onto a recycling truck and ended up here! Ooh boy, that sounds rough. But it also sounds so SO COOL!!! What's it like on a recycling truck? Oh wait, you forgot... soooo... are you like, a recycling bin or something? Oh, you also forgot that-"

    r "Yes, yes I forgot everything. Can you explain this whole...  recycling concept??"

    p "Did you seriously forget even what recycling is? Gosh, you poor thing..."

    pep "Well, recycling is a key part in this effort that the humans have dubbed: Going green."

    pep "Going green involves being more environmentally conscientious. In other words, reducing the pollution and waste generated, one human step at a time."

    pep "Recycling is a key part in this movement, since it takes old and used materials and reverts them back to brand new."

    pep "As materials, we've been tossed aside carelessly on this street. After seeing a bin such as yourself appear, which one of us wouldn't want to be taken off to a recycling center?"

    alu "AND, as the most stunning option in this rabble, I declare that we shall be the closest of companions! Come, let us party as we wait for our victory chariot to return in three days!"

    pep "Hey, they aren't yours to lay dibs on-"

    r "Hold on, three days?!"

    g "Y-yup! The recycling truck passes by here every three days."

    r "So, you're telling me that I, a recycling bin, must choose one of you to be recycled within the next three days?!?"

    p "Well, yes! I'm not going to recycle myself, am I? So what, who will you choose?"

    r "Hold on, let me get to know you all in these three days. On the day that the truck comes, I'll pick one of you to be recycled. Got it?"

    g "That's a great choice!"

    pep "Reasonable enough. How about you choose one of us to chat and get familiar with today, then?"

    r "Uh... I choose..."

    menu:
        "Paige (cardboard)":
            jump day1_paper_route
        "Alu (can)":
            jump day1_plastic_metal_route
        "G (glass bottle)":
            jump day1_glass_route
        "Plato (used plastic plate)":
            jump day1_food_route
        "Pepton (spray bottle)":
            jump day1_pesticide_route