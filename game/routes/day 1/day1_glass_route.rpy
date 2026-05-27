label day1_glass_route:
    scene bg roadside
    show g at center_slot
    with dissolve

    g "Oh my gosh! I almost bumped into you! Are you OK?"

    r "Oh no, that was my fault. I wasn't paying attention, sorry..."

    show emot concern at emot_center
    with dissolve
    g "Well, no it's totally my fault... I didn't scratch you by any chance did I? If I did I totally didn't mean to! I'm so sorry!"
    hide emot concern
    with dissolve

    r "Huh? No, I'm fine! These scratches are from something else... your name is... G right?"

    show emot nonch at emot_center
    with dissolve
    g "Wha- oh me? Y-yeah, that's my name... It's... not very unique I know. I'm not very unique..."
    hide emot nonch
    with dissolve

    r "What? Noo, what makes you say that?"

    show emot blush at emot_center
    with dissolve
    g "Well... I mean it's really nothing, but... people always call me simple to make... I'm mostly made out of three ingredients, you know? Sand, soda ash, and limestone... and I'm 100 percent recyclable too... and honestly, I just... I don't know how that could be so interesting to anyone."
    hide emot concern
    with dissolve

    r "I think that's pretty interesting! You've got a cute luster you know."

    show emot blush at emot_center
    with dissolve
    g "O-oh you really think so? Thank you Reese... I... I hope to see you around some time."
    hide emot blush
    with dissolve

    $ affinity_glass += 1

    return
