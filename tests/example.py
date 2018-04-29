from aide_document import combine, convert, translate

# Test combine
combine.render_document('template.md', 'data/input.yml', 'data/output.md')

# Test convert
#convert.md_to_pdf('data/output.md', 'data/output')
#convert.docx_to_md("data/EtFlocSedFiEnglish.docx", "data/EtFlocSedFiEnglish")

# Test translate
translate.translate("data/output.md", "en", "es", "data/translated.md")
translate.translate("data/output.md", "en", "hi", "data/translated2.md")
