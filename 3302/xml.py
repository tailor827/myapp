def convert(data):
    xml = '<languages>'
    for i in data:
        lang = """
        <language level="{}">
            <name>{}</name>
            <creator>{}</creator>
        </language>
        """.format(i[2], i[0], i[1])
        xml += lang
    xml += '\n</languages>'
    return xml

languages = [
    ["C++", "Bjarne Stroustrup", "Low"],
    ["C", "Dennis Ritchie", "Low"],
    ["Java", "James Gosling", "High"],
    ["Python", "Guido van Rossum", "High"]
]

converted = convert(languages)
print(converted)

#end of file
