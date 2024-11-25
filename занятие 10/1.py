with open('AntonovSergeiRomanovich_y-242_vvod.txt', 'r') as f:
    content = f.read()
    print(content)
    with open('AntonovSergeiRomanovich_y-242_vivod.txt', 'w') as g:
        g.write(content)