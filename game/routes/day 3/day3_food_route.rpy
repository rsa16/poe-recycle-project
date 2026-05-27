label day3_food_route:
    scene bg park
    show plato at center_slot
    with dissolve

    r "Oh, hey Plato!"

    pl "Reese! The coolest and the most awesomest! My best friend! What's up!? I'm so glad to see you!"

    r "I'm glad to see you, too! You know what, Plato? I can always count on you to be energized."

    pl "Hahaha, I get that a lot! That's why I started being more active! What about you? What do you like to do in your free time, Reese?"

    menu:
        "I love exploring! No matter where I go, I just enjoy the journey more than the destination.":
            $ affinity_pesticide += 1
            r "I love exploring! No matter where I go, I just enjoy the journey more than the destination."
            pl "Oh, you do, huh? Well, that's amazing! I personally prefer going through the park everyday, but it's kind of the same idea! Actually, you know what? You sound a lot like Pepton! They love exploring, too! They have a really interesting personality - so unique! But I'm sure you can get along with them (you're that cool)."
            r "Maybe they and I can be friends, too... exploring with someone else would be fun!"

        "Well, the park is a rather nice place to stroll through. I love nature!":
            $ affinity_food += 1
            r "Well, the park is a rather nice place to stroll through. I love nature!"
            pl "Wait, really!? Wow, I love going through the park! O.M.G., this is great to know! Now I can have a walking partner! And you love nature, just like me! Gardening is my favorite thing EVER!"
            r "Yay, this is exciting!"
            pl "Gardening is kind of what I'm known for. As food waste, I'm great at making compost, which plants love."
            r "How cool! You're so helpful, I'm sure all the plants appreciate you."
            pl "Aww, thank you! You're so awesome and kind and amazing! This is why we're best friends, by the way. Our walks are going to be so amazing and fun - I can't wait!!"

        "Oh, heh, I'm not really too active... I prefer staying at home.":
            $ affinity_glass += 1
            r "Oh, heh, I'm not really too active... I prefer staying at home."
            pl "Oh, hmm, that's cool too! I personally CAN'T sit still or do nothing. I always have to be going somewhere, you know? Life is just more fun that way! But don't worry, you're not the only one like that. In fact, G is just like that! Y'know, you and G are both really awesome! Man, you guys are the best."
            r "Oh, G, huh? Well, they and I are definitely compatible then! I'm not really the adventurous type."
            pl "Yeah! Actually, G told me that they really like to preserve their energy. In fact, they are made of 25 percent recycled glass, which conserves energy! Isn't that awesome? Many other glass products are also made of around 25 percent recycled glass. So cool!"
            r "I can definitely respect saving that much energy. We're similar in that way!"

    return
