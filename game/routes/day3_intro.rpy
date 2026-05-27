label day3_intro:
    scene bg roadside

    r "It was great getting to know more about the local materials!"

    r "Hold on. The recycling truck is arriving tomorrow!!!"

    r "I still need a material in order to return to my former role as a recycling bin."

    "How will you spend your final day?"

    menu:
        "A house lies a little further down the street. There seems to be a papery fellow around there...":
            jump day3_paper_route
        "Looking down the street, there seems to be a can and a spray bottle arguing with each other...":
            jump day3_plastic_metal_pesticide_route
        "It seems like a bottle is lying just up ahead alongside the road...":
            jump day3_glass_route
        "There's a park just across the road. You spot a plastic plate laying amidst the grass...":
            jump day3_food_route