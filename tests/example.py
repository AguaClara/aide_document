from aide_document import convert, translate

# [yaml_to_md] takes three file names:
# <input>, <output>, <template>
# convert.yaml_to_md("input.yml", "output.md", "template.md")

# convert.docx_to_md("data/start/EtFlocSedFiEnglish.docx", "data/finish/EtFlocSedFiEnglish")

# [translate] takes four arguments:
# <input>, <source_language>, <target_language>, <output>
# Notice: the output file will be created.
# If there is a file with the same name, it gets replaced.
translate.translate("data/finish/output.md", "en", "es", "data/finish/translated.md")
#translate.translate("output.md", "en", "hi", "translated2.md")
