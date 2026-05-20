label day3_paper_route:
    scene bg house
    show paige at center_slot
    with dissolve

    r "Well, I'm always willing to make changes-"

    p "Okay, I'm glad we're on the same page! Tidiness and organization are very important to me. They are for you, too, right?"

    menu:
        "I think you caught me at a bad time... really, I need everything in order.":
            $ affinity_paper += 1
            r "I think you caught me at a bad time... really, I need everything in order."
            p "Well, if that's true, then we might get along pretty well."
            p "Did you know that creating recycled paper takes 64% less energy and 58% less water? If that isn't enough to convince you, I don't know what is."
            r "Well, that's what's giving you your youthful glow! I would never have guessed that you were recycled."
            p "Aww... thank you :)"

        "Oh, yes... or-gan-ization... um, remind me what that is again?":
            $ affinity_food += 1
            r "Oh, yes... or-gan-ization... um, remind me what that is again?"
            p "Okay, good one, but I'm being serious."
            r "I wasn't kidding..."
            p "Oh, that's... uh... awkward..."
            p "Hey, you kind of remind me of Crusty... they aren't very orderly, either. In fact, only 5% of food waste is organized and composted. That's not an exaggeration!"
            r "As worrisome as that is, maybe Crusty and I would get along."
            p "In that case, you would definitely get along with Crusty better than you would with me."

        "Well, I might not look tidy, but trust me, this hot mess is reaaaaal organized.":
            $ affinity_plastic_metal += 1
            r "Well, I might not look tidy, but trust me, this hot mess is reaaaaal organized."
            p "Haha, you're clever. But half the work is actually looking orderly."
            r "Why, thank you."
            p "Speaking of which, have you met Alu? They were created from aluminum, which is easy to organize into recycling bins and can be easily recycled for generations!"
            r "That sounds really cool. Alu and I might really get along!"

    return
