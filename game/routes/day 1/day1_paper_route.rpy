label day1_paper_route:
    scene bg roadside
    show paige at center_slot
    with dissolve

    p "Well, hey! How's it going, Reese?"

    r "Not bad, I suppose? I'm still sort of recovering from everything that happened, I guess."

    show emot concern at emot_center
    with dissolve
    p "Yeah - to be honest, you do look a little beat up."
    hide emot concern
    with dissolve

    r "Ouch."

    p "But don't worry, I'm willing to help! In fact, everyone can help clean things up."

    r "Hmm... like what?"

    p "Y'know... like maybe schools could host in-school/fieldtrip based clean-up events. You could make it fun, where students have the opportunity to complete a scavenger hunt. It could be a variety of things, like beach clean ups, park clean ups, or just around the local campus."

    r "Yeah... that's a great point, actually."

    p "Not only does it help clean up the local community, but it's also appealing to students because they can get out of classrooms and contribute to the community. There can be competition between grades or schools. Students could also be rewarded with volunteer hours as well, providing a good opportunity for everyone."

    r "That's really thoughtful, actually."

    p "This is my passion. It is very important that things look the way they're supposed to."

    $ affinity_paper += 1

    return