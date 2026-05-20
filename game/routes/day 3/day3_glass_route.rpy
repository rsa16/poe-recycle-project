label day3_glass_route:
    scene bg roadside
    show g at center_slot
    with dissolve

    r "G? Is that you? What are you doing next to the road??"

    show emot surprise at emot_center
    with dissolve
    g "Huh? Reese? I... I didn't expect to see you here! I'm just... I'm looking for inspiration."
    hide emot surprise
    with dissolve

    r "Inspiration for what?"

    show emot surprise at emot_center
    with dissolve
    g "Why... art of course! Er... I mean..."
    hide emot surprise
    with dissolve

    show emot concern at emot_center
    with dissolve
    g "I-I really like art, that's all... Do you?"
    hide emot concern
    with dissolve

    menu:
        "Of course! I love doing hands-on things. Multi-media art is my calling!":
            $ affinity_plastic_metal += 1
            g "Oh, well I'm more into mosaics, but... that's cool too."
            r "Yeah? You don't sound too convinced."
            show emot concern at emot_center
            with dissolve
            g "Oh... well to be honest... it's just that, that seems more up Alu's lane than mine... Did you know that over 460 million metric tons of plastic are produced every year?"
            hide emot concern
            with dissolve
            r "Oh wow, that's impressive! I never knew that about Alu."
            g "Oh... I mean... okay. B-but just so you know, even though Alu brags about that 460 only 9% of plastic ever made has been recycled."

        "Oh, me? Well to be honest... I'm more of a methodical and calculated type of bin myself.":
            $ affinity_paper += 1
            show emot nonch at emot_center
            with dissolve
            g "Oh... You might like Paige then... Have you guys ever met? Paige is always so structured and reliable... and popular..."
            hide emot nonch
            with dissolve
            g "Did you know that over 84% of corrugated boxes are recycled each year in the EU? Meanwhile only about 40% of glass is accepted in recycling facilities... Gosh I wish I could be like Paige!"

    return
