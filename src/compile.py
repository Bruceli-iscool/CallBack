import construct

def compile(file, out):
    final = "<!DOCTOTYPE html>\n\t<html>\n"
    with open(file) as file:
        for line in file:
            if line.startswith("//"):
                # ignore comments
                pass
            z = construct.construct_html(line)
            final = final + z
        return final + "\n</html>"

def start():
    return "<!DOCTOTYPE html>\n\t<html>\n"

def out(inputFile, file="out.js"):
    with open(file, "w") as files:
        files.write(construct.compile(inputFile))

out(input())