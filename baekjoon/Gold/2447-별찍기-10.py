def draw_stars(L):
    if L == 1:
        return ['*']

    stars = draw_stars(L // 3)
    pattern = []

    for star in stars:
        pattern.append(star * 3)
    for star in stars:
        pattern.append(star + ' ' * (L // 3) + star)
    for star in stars:
        pattern.append(star * 3)

    return pattern


N = int(input())
print('\n'.join(draw_stars(N)))
