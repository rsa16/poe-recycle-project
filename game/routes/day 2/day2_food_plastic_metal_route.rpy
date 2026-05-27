label day2_food_plastic_metal_route:
    scene bg park
    show plato at left_slot
    show alu at right_slot
    with dissolve

    pl "O.M.G., hey!"

    alu "Why, hello there, good fellow!"

    r "Hey, what's up?"

    pl "Nothing much, but you came at the perfect time! We were just on a walk, and I had a random thought - hold on, have you been in a convenience store before?"

    r "Yeah, why?"

    pl "Okay, awesome sauce! So, like, this is kind of strange, but what do you like to get from these stores? Because, personally, I love convenience stores. Like, they're literally perfect! I mean, it's in the name, convenience store. It's the best place to get whatever you need! But anyways, what would you get? Because I'm not sure what my favorite thing to get is."

    alu "I had told Plato that I personally prefer carbonated drinks, especially delightfully sugary sodas."

    menu:
        "That's actually a great question! Hmm... I haven't really thought about it too much before, but I'd probably grab a snack of some sort. Gotta stay energized!":
            $ affinity_food += 2
            $ affinity_plastic_metal += 1
            $ affinity_paper += 1
            r "That's actually a great question! Hmm... I haven't really thought about it too much before, but I'd probably grab a snack of some sort. Gotta stay energized!"
            pl "Wait, really!? Omigosh, that's literally perfect! I love that answer so much, I have to go with you now. You're so cool, we're getting along so well! This is so awesome!!!"
            alu "\"Energizing\" eatables require money to be purchased. The US recycling industry creates $117 billion in economic activity annually. The Recycling Economic Information report states that 681,000 jobs, $37.8 billion in wages, and $5.5 billion in tax revenues are generated from recycling and reuse based activities. This means there are around 1.17 jobs for every 1,000 tons of recycled material."
            pl "Wow, that was... really smart. Dang, you're so awesome!"
            r "First of all, I'm deeply impressed by your knowledge on all of this. Second of all, those are some big numbers."

        "Hmm... I'm not sure. Well, I'm more of a drink person. I'd definitely get something refreshing.":
            $ affinity_glass += 2
            r "Hmm... I'm not sure. Well, I'm more of a drink person. I'd definitely get something refreshing."
            alu "Oh, a fellow enjoyer of the beverage, huh? I know of another just like you, they go by \"G.\" You two would surely find each other's company quite fulfilling."
            pl "Ooh, that's true! You guys would complement each other pretty well!"
            alu "You see, refreshing drinks require money to be bought. The US recycling industry creates $117 billion in economic activity annually. The Recycling Economic Information report states that 681,000 jobs, $37.8 billion in wages, and $5.5 billion in tax revenues are generated from recycling and reuse based activities. This means there are around 1.17 jobs for every 1,000 tons of recycled material."
            pl "Wow, that was... really smart. Dang, you're so awesome!"
            r "First of all, I'm deeply impressed by your knowledge on all of this. Second of all, those are some big numbers."

        "Dude, not trying to be rude, but why would I be in a situation where I'd need to be in a convenience store? I mean, no offense, but still.":
            $ affinity_plastic_metal += 1
            $ affinity_food -= 2
            r "Dude, not trying to be rude, but why would I be in a situation where I'd need to be in a convenience store? I mean, no offense, but still."
            alu "Oh, dear! There was no need for such a combative stance on the topic! Oh, poor Plato, they don't deserve this - Plato, do tell me you are alright!?"
            pl "Um... ha... It's not a big deal. Uhh... well, I don't know, I guess. I was just a little curious, I didn't mean to be... annoying, or anything."

    return
