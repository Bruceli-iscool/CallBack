import construct

def compile(file):
    final = "<!DOCTOTYPE html>\n\t<html>\n"
    with open(file) as file:
        for line in file:
            if line.startswith("//"):
                # ignore comments
                pass
            z = construct.construct(line)
            print(z)
            final = final + z
        return final + "\n</html>"

def start():
    return "<!DOCTOTYPE html>\n\t<html>\n"

def out(inputFile, file="out.html"):
    with open(file, "w") as file:
        file.write(compile(inputFile))

out("/Users/keli/Documents/GitHub/Lascal/CallBack/src/test.cb")