label day2_pesticide_route:
    scene bg roadside
    show pepton at center_slot
    with dissolve

    pep "Oh... hey."

    r "Is that all you're going to say to me? I feel like you want to say more than just that"

    pep "Tsk. It's just that I think that you don't know the truth. Not the whole of it, at least."

    r "What do you mean?"

    pep "You're telling me that, despite knowing nothing except for a hunch, you truly want to be a recycling bin? Be honest... Would you recycle if you were a human?"

    menu:
        "Like, what does recycling even do?":
            $ affinity_pesticide += 1
            $ affinity_food += 1
            r "Like, what does recycling even do?"
            pep "Psh! You're truly clueless! That's the issue! You don't know enough to really make a sound judgement of your own role... Although they seem a little cuckoo, Plato appreciates thinkers like you. Maybe we should hang out."

        "I mean everyone does it, do they not? If they do it, there's no good reason for me not to.":
            $ affinity_pesticide -= 1
            $ affinity_paper += 1
            r "I mean everyone does it, do they not? If they do it, there's no good reason for me not to."
            pep "... I didn't take you to be such a malleable bin. If you wanted to go with the crowd, I suggest you go talk with Paige instead."

        "... You make a good point. I really don't know enough to make a fair judgement.":
            $ affinity_pesticide += 2
            r "... You make a good point. I really don't know enough to make a fair judgement."
            pep "Heh. So you do realize you're completely out of your game huh? I was worried you were just blindly following what we were saying."

    pep "Anywho, I'll let you in on this information I heard from... acquaintances"

    pep "There's this more recent recycling method that humans are using, where they take materials and break them down to their original chemical components. These components can then be used to be made into better products. There's several variations, like depolymerization, pyrolysis, and solvolysis."

    pep "You get the general gist of the process, yeah?"

    pep "Anywho, this new technology makes it way easier to recycle contaminated materials or materials that are difficult to recycle without chemically modifying them."

    r "Hey! That sounds pretty good! Doesn't that mean that more materials can be recycled?"

    pep "Righty-o."

    r "Thanks for teaching me more about recycling. I appreciate your efforts to make sure I'm not running into this blind."

    pep "Heh. It's nothing."

    return
