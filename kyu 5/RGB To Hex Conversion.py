# The rgb function is incomplete.
# Complete it so that passing in RGB decimal values will result in a
# hexadecimal representation being returned. Valid decimal values
# for RGB are 0 - 255. Any values that fall out of that range must be
# rounded to the closest valid value.

# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3

def rgb(r, g, b):
    re=""
    for i in [r,g,b]:
        if i<0:i=0
        if i>255:i=255
        re+=(str(hex(i)).upper().replace("0X","")).zfill(2)
    return re