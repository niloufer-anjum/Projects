cats = {
    "hats": [],
    "no_hats": []
}

def add_cats(num):
    for i in range(1, num+1):
        cats["no_hats"].append(i)

# TODO: Reduce complexity from n^4 to n^2
def put_hats(num):
    add_cats(num)
    for el in range(1, num+1):                                                          # n
        for i in range(el, num+1, el):                                                  # n
            if i in cats["hats"]:                                                       # n
                cat = cats["hats"].pop(cats["hats"].index(i))                           # n
                cats["no_hats"].append(cat)
            else:
                cat = cats["no_hats"].pop(cats["no_hats"].index(i))
                cats["hats"].append(cat)


put_hats(100)

cats_with_hats = cats["hats"]
print(f"Cats {str(cats['hats'])[1:-1]} have hats!")