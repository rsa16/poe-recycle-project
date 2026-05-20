# =========================
# Character Definitons
# =========================
define r = Character("Reese")
define p = Character("Paige")
define pl = Character("Plato")
define g = Character("G")
define pep = Character("Pepton")
define alu = Character("Alu")

init python:
    if "background" not in config.layers:
        config.layers.insert(0, "background")

    def scaled_emot(emot_image, char_image, max_ratio=0.35):
        emot_w, _ = renpy.image_size(renpy.displayable(emot_image))
        char_w, _ = renpy.image_size(renpy.displayable(char_image))
        
        max_width = char_w * max_ratio
        if emot_w > max_width and emot_w > 0:
            scale = max_width / float(emot_w)
            return Transform(emot_image, zoom=scale)

        return emot_image

# =========================
# Affinities
# =========================
default affinity_paper = 0
default affinity_food = 0
default affinity_glass = 0
default affinity_plastic_metal = 0
default affinity_pesticide = 0

# =========================
# Flags
# =========================
default met_paper = False
default met_food = False
default met_glass = False
default met_pesticide = False

# =========================
# Images
# =========================
image bg house = Transform("bg house.png", xysize=(config.screen_width, config.screen_height), fit="contain")
image bg park = Transform("bg park.png", xysize=(config.screen_width, config.screen_height), fit="contain")
image bg roadside = Transform("bg roadside.png", xysize=(config.screen_width, config.screen_height), fit="contain")
image bg sidewalk = Transform("bg sidewalk.png", xysize=(config.screen_width, config.screen_height), fit="contain")

image alu = "char alu.png"
image g = "char g.png"
image paige = "char paige.png"
image pepton = "char pepton.png"
image plato = "char plato.png"
image reese = "char reese.png"

image emot angry = "emot angry.png"
image emot blush = "emot blush.png"
image emot concern = "emot concern.png"
image emot intrigue = "emot intrigue.png"
image emot nonch = "emot nonch.png"
image emot surprise = "emot surprise.png"

image intro accent = "intro accent.png"
image intro bottom = "intro bottom.png"
image intro char = "intro char.png"
image intro reese = "intro reese.png"
image intro top = "intro top.png"

image name alu = "name alu.png"
image name g = "name g.png"
image name paige = "name paige.png"
image name pepton = "name pepton.png"
image name plato = "name plato.png"
image name reese = "name reese.png"

image outro foreground = "outro foreground.png"
image outro truck = "outro truck.png"

# =========================
# Screems
# =========================
screen base_bg:
    layer "background"
    add Solid("#000")

screen intro_card(name_image, char_image=None):
    layer "screens"
    zorder -10

    add "intro char" xalign 0.5 yalign 0.5 at intro_card_in, intro_char_zoom
    add "intro top" xalign 0.5 yalign 0.5 at intro_card_in
    add "intro bottom" xalign 0.5 yalign 0.5 at intro_card_in, intro_bottom_slide

    if name_image is not None:
        add name_image xalign 0.5 yalign 0.5 at intro_card_in

    if char_image is not None:
        add char_image xalign 0.5 yalign 0.5 at intro_card_in

    add "intro accent" xalign 1.0 yalign 0.5 at intro_card_in

# =========================
# Positions
# =========================
transform intro_card_in:
    alpha 0.0
    zoom 0.98
    linear 0.18 alpha 1.0 zoom 1.0

transform intro_char_zoom:
    zoom 0.9
    linear 0.25 zoom 1.0

transform intro_bottom_slide:
    yoffset 40
    linear 0.25 yoffset 0

transform flashback_fx:
    alpha 0.0
    zoom 1.02
    linear 0.15 alpha 0.85
    linear 0.25 zoom 1.0

transform left_slot:
    xalign 0.25
    yalign 1.0
    yoffset -40

transform center_slot:
    xalign 0.5
    yalign 1.0
    yoffset -300

transform right_slot:
    xalign 0.75
    yalign 1.0
    yoffset -300

transform emot_left:
    xalign 0.25
    yalign 1.0
    yoffset -360

transform emot_center:
    xalign 0.5
    yalign 1.0
    yoffset -500

transform emot_right:
    xalign 0.75
    yalign 1.0
    yoffset -500

# =========================
# Start
# =========================
label start:
    show screen base_bg
    jump day1_intro