from tkinter import LEFT, Y, X, RIGHT, BOTTOM, TOP, BOTH, DISABLED

font = 'Hoefler Text'

background_color = '#23FB54'

font_small = (font, 24)
font_medium = (font, 36)
font_large = (font, 48)

# Button
button_args = {
    'fg': '#FFFFFF',
    'font' : font_small
}

#Arguments for packing
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
