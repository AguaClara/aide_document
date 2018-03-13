import convert

# [render_documentation_template] takes three file names:
# <input>, <output>, <template>
convert.yaml_to_md("input.yml", "output.md", "template.md")
convert.docx_to_md("EtFlocSedFiSpanish.docx", "EtFlocSetFi Spanish.md")
