label day3_plastic_metal_pesticide_route:
    scene bg sidewalk
    show alu at left_slot
    show pepton at right_slot
    with dissolve

    "Leaving the initial crash site behind, you walk further along the concrete sidewalk. The rumble of the highway fades slightly, and you hear someone sigh and another person sharply muttering ahead of you."

    "As you approach further, you spot a sleek, flashy orange soda can, striking a weird dramatic pose while a bottle of pesticide sits in the shadow of a nearby weed, looking thoroughly annoyed."

    alu "Ah! Look, Pepton! Company! The traveler has drifted onto our stretch of the pavement! Haha! How do I look, hmm?? Fantabulous I'm sure!"

    "Not quite sure what to say, you simply nod with a certain awkwardness."

    show emot nonch at emot_left
    with dissolve
    pep "Don't drag them into your delusions, Alu. They're probably just taking a stroll around town. Like, you know, the rest of us."
    hide emot nonch
    with dissolve

    alu "Gosh Pepton. You could really afford to be more peppy. I mean, look at yourself. You constantly look like you crawled out of some... under the sink cabinet."

    show emot angry at emot_right
    with dissolve
    pep "Hey. I take great offense to that. And, I look perfectly normal, I'll have you know."
    hide emot angry
    with dissolve

    "Alu gets closer and whispers in your ear."

    alu "My good fellow Reese... I think we know who looks better of the two of us... Pfft."

    show emot angry at emot_right
    with dissolve
    pep "I can hear you. You're insufferable, know that?"
    hide emot angry
    with dissolve

    show emot intrigue at emot_left
    with dissolve
    alu "Ah, insufferable maybe, but fashionable, definitely."
    hide emot intrigue
    with dissolve

    pep "Here, how about we have Reese decide. Who looks \"better\"?"

    menu:
        "I can't lie with you... Alu does look way more put together.":
            $ affinity_plastic_metal += 1
            alu "Heh, but of course! My splendorous and glimmering coat is way better than Pepton's sad ensemble of... whatever that is. I'm glad you have good taste my friend."
            pep "Tsk."
            pep "I mean... I guess you have a point."

        "I mean... does it really matter what we look like? We're all kind of left-overs on the side of the street anyways...":
            $ affinity_paper += 1
            alu "You have forsaken whimsy for practicality... but I can't blame you."
            pep "That's a kind of practicality Paige would appreciate."
            alu "Hah, for sure!"

        "Hey, who said Pepton doesn't look nice? They have a very good figure.":
            $ affinity_pesticide += 1
            alu "Friend. It seems like that fall damaged more than just your memory."
            pep "HAH! I'm never letting you live this down Alu."

    alu "On top of that, refreshing drinks are commonly purchased in these types of stores by workers. For example, the thousands of recycling-based jobs, which, while incredibly helpful to thousands of people, can be tiring."

    pl "Ohh, that does make sense!"

    alu "It does, indeed. In fact, on average, recycling-based work creates nine times more jobs compared to trash-based jobs. Composting creates twice as many jobs compared to landfills, and four times as many jobs as incineration facilities. Additionally, reuse makes 30 times more jobs than landfills."

    pl "That's actually a really huge amount. I never would've thought it'd be so much!"

    r "Yeah, that's pretty crazy. But wait, how do you know all of thi-"

    return
