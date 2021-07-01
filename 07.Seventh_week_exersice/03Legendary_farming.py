from collections import defaultdict

stash = {"fragments": 0, "shards": 0, "motes": 0}
stash_junk = defaultdict(int)
count_shards = 0
count_fragments = 0
count_motes = 0
enough = True

while enough:
    data = input().lower().split()

    for i in range(0, len(data), 2):
        quantity = int(data[i])
        material = data[i + 1]

        if material == "shards":
            count_shards += quantity
            stash[material] += quantity
            if count_shards >= 250:
                print("Shadowmourne obtained!")
                stash['shards'] -= 250
                break
        elif material == "fragments":
            count_fragments += quantity
            stash[material] += quantity
            if count_fragments >= 250:
                print("Valanyr obtained!")
                stash['fragments'] -= 250
                break
        elif material == "motes":
            count_motes += quantity
            stash[material] += quantity
            if count_motes >= 250:
                print("Dragonwrath obtained!")
                stash['motes'] -= 250
                break
        else:
            stash_junk[material] += quantity

    if count_fragments >= 250 or count_shards >= 250 or count_motes >= 250:
        enough = False

for k, v in sorted(stash.items(), key=lambda x: (-x[1], x[0])):
    if k == "shards":
        print(f"{k}: {v}")
        del stash[k]
    elif k == "fragments":
        print(f"{k}: {v}")
        del stash[k]
    elif k == "motes":
        print(f'{k}: {v}')
        del stash[k]

for k, v in sorted(stash_junk.items(), key=lambda x: x[0]):
    print(f"{k}: {v}")
