from collections import deque

materials = [int(x) for x in input().split()]
magics = deque([int(x) for x in input().split()])

presents = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

crafted_presents = {}
while materials and magics:
    material = materials.pop()
    magic = magics.popleft()
    magic_level = material * magic
    if magic_level in presents:
        toy = presents[magic_level]
        if toy in crafted_presents:
            crafted_presents[toy] += 1
        else:
            crafted_presents[toy] = 1
    else:
        if magic_level < 0:
            materials.append(magic + material)
        elif magic_level > 0:
            materials.append(material + 15)
        else:
            if magic == 0 and material == 0:
                continue
            elif material == 0:
                magics.appendleft(magic)
            else:
                materials.append(material)

if ('Doll' in crafted_presents and 'Wooden train' in crafted_presents) or\
        ('Teddy bear' in crafted_presents and 'Bicycle' in crafted_presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}")

if magics:
    print(f"Magic left: {', '.join(str(x) for x in magics)}")

for presents, count in sorted(crafted_presents.items()):
    print(f"{presents}: {count}")