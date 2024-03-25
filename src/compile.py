import construct
import webbrowser

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

def out(inputFile, file="out.html"):
    with open(file, "w") as files:
        files.write(compile(inputFile, files))
        webbrowser.open(file)

out("/Users/keli/Documents/GitHub/Lascal/CallBack/src/test.cb")