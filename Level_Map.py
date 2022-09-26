level_map_1 = [
    '                            ',  # Row 0
    '                            ',
    '                            ',
    ' XX    XXX            XX    ',
    ' XX P                       ',
    ' XXXX         XX         XX ',
    ' XXXX       XX              ',
    ' XX    X  XXXX    XX  XX    ',
    '       X  XXXX    XX  XXX   ',
    '    XXXX  XXXXXX  XX  XXXX  ',
    'XXXXXXXX  XXXXXX  XX  XXXX  ']  # Row 10 (Inclusive)

# Column 0 to Column 27 (Inclusive)

tile_size = 64  # what each x will equal.
screen_width = 1200
screen_height = len(level_map_1) * tile_size  # find the amount of rows which = height so level always fit on screen
