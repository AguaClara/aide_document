import google_trans

def translate(filename, src, tar, dest):
    with open("data/" + filename) as f:
        content = f.readlines()
    content = [x.rstrip() for x in content]
    text = []
    for elt in content:
        t = google_trans.api(elt, src, tar)
        text = text + [t.encode('utf-8')]
    with open("data/" + dest, "w") as f:
        for l in text:
            f.write(l)
            f.write("\n")
