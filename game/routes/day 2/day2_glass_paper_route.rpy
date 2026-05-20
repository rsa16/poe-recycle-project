label day2_glass_paper_route:
    scene bg house
    show g at left_slot
    show paige at right_slot
    with dissolve

    show emot blush at emot_left
    with dissolve
    g "Oh Reese! I-it's so good to see you again... me and Paige were just... discussing something."
    hide emot happy
    with dissolve

    p "Oh, yes! We'd love to hear your input."

    r "Oh huh? I mean... sure I guess. What do you want to hear from me?"

    g "Well... it's just that, me and Paige were wondering... if you had to make something out of recyclable materials, what would it be?"

    menu:
        "Uhhh... well I really like art so probably something artistic.":
            $ affinity_glass += 2
            $ affinity_paper += 2
            show emot intrigue at emot_left
            with dissolve
            g "Oh no way! That's awesome! Did you know the Basilica Cathedral in St. Louis Missouri has over 41.5 million pieces of glass?"
            hide emot intrigue
            with dissolve
            r "Really? That's so impressive!"
            p "Yup! And did you know papier mache can be made out of strips of paper?"
            r "No, that's really cool!"
            show emot blush at emot_left
            with dissolve
            g "I didn't know you were such an art enthusiast Reese!"
            hide emot blush
            with dissolve
            p "That totally reminds me -"

        "Hmm, well I'd probably be thinking about how to make other usable items from recyclables.":
            $ affinity_plastic_metal += 1
            $ affinity_glass += 1
            show emot nonch at emot_left
            with dissolve
            g "Oh!... You might like Alu then. They're always thinking about the practical solution to things."
            hide emot nonch
            with dissolve
            p "They definitely do. Oh, and did you know steel is one of the most popular materials used for hand tools? That's Alu's cousin! They're practically a celebrity!"
            r "Ah, I know Alu... but now I feel so lucky to know them!"

        "Hmm... probably something practical... like a tool maybe.":
            $ affinity_plastic_metal += 2
            $ affinity_pesticide += 1
            g "Yeah, Pepton, I heard, is sort of like that too..."
            p "Ooh, no. His tool is a little more... deadly."

    return
