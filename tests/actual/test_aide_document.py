from aide_document import combine, jekyll, convert, translate
from filecmp import cmp

def test_combine():
    combine.render_document('template.md', 'actual/input.yaml', 'actual/combined.md')
    assert cmp('actual/combined.md', 'expected/combined.md')

def test_jekyll():
    jekyll.add_frontmatter('actual/combined.md', 'test', True)
    assert cmp('actual/combined_added_frontmatter.md', 'expected/combined_added_frontmatter.md')

def test_convert():
    convert.md_to_pdf('actual/combined.md', 'actual/converted')
    assert cmp('actual/converted.pdf', 'expected/converted.pdf')
    convert.docx_to_md('actual/EtFlocSedFiEnglish.docx', 'actual/EtFlocSedFiEnglish')
    assert cmp('actual/EtFlocSedFiEnglish.docx', 'expected/EtFlocSedFiEnglish.md')

def test_translate():
    translate.translate('actual/combined.md', 'actual/translated_es.md', 'es')
    assert cmp('actual/translated_es.md', 'expected/translated_es.md')
    translate.translate('actual/combined.md', 'actual/translated_hi.md', 'hi')
    assert cmp('actual/translated_hi.md', 'expected/translated_hi.md')