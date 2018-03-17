import google_trans

def translate(filename, src, tar, dest):
    with open("data/" + filename) as f:
        content = f.readlines()
    content = [x.rstrip() for x in content]
    out = open("data/" + dest, "w")
    for elt in content:
        print elt + "\n"
        t = google_trans.api(elt, src, tar)
        out.write(t.encode('utf-8'))
        out.write("\n")
    out.close()

translate("output.md", "en", "hi", "translated2.md")
