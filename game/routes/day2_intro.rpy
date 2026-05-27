label day2_intro:
    scene bg roadside

    r "I had a lot of fun discussion yesterday!"

    r "Based on the information I gathered, it seems like I'm meant to help recycle one of these local materials."

    r "I was told the truck would come... two days from now!"

    r "I better get to know the materials better before it's recycle day. Where should I head off today?"

    menu:
        "At the park, there seems to be a plastic plate and a can excitedly conversing with each other...":
            call day2_food_plastic_metal_route
        "A spray bottle can be seen further down the street...":
            call day2_pesticide_route
        "At the house, it seems the glass bottle and a cardboard-ish figure are discussing something...":
            call day2_glass_paper_route

    scene black
    show text "Day 3" with dissolve
    pause 1.0
    hide text with dissolve
    jump day3_intro
