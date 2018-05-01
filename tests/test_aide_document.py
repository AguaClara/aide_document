from aide_document import combine, convert, translate
from filecmp import cmp

def test_combine():
    combine.render_document('template.md', 'actual/input.yaml', 'actual/combined.md')
    assert cmp('actual/combined.md', 'expected/combined.md')

#def test_convert():
#    convert.md_to_pdf('data/output.md', 'data/output')
#    convert.docx_to_md("data/EtFlocSedFiEnglish.docx", "data/EtFlocSedFiEnglish")

#def test_translate():
#    translate.translate("data/output.md", "en", "es", "data/translated.md")
#    translate.translate("data/output.md", "en", "hi", "data/translated2.md")

#combine.render_document('template.md', 'actual/input.yaml', 'actual/combined.md')