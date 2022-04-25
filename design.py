from tkinter import LEFT, Y, X, RIGHT, BOTTOM, TOP, BOTH, DISABLED

font = 'Hoefler Text'

background_color = '#29cf4f'

#font variations
font_small = (font, 24)
font_medium = (font, 36)
font_large = (font, 48)

# Button args
button_args = {
    'fg': '#FFFFFF',
    'font' : font_small
}

#pack args
pack_left_and_fill_y = {
    'side' : LEFT,
    'fill' : Y
}

#Frame properties
hightlight_frame_with_white = {
    'highlightthickness' : 1,
    'highlightcolor' : '#FFFFFF',
    'highlightbackground' : '#FFFFFF'
}
