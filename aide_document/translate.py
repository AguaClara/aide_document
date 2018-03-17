import google_trans

with open("data/output.md") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
text = []

for sentence in content:
    t = google_trans.trans(sentence, "en", "es")
    text = text + [t.encode('utf-8')]

print text

with open("data/translated.md", "a") as f:
    for l in text:
        f.write(l)
        f.write("\n")
