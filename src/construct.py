# Construct compilable source code
# Basically create an AST
parens = 0
render = ""
stateparens = 0
# save type
var = {}

def construct_html(line):
    global parens, render, stateparens
    line = line.lstrip(" ")
    if parens == 0:
        if line.startswith("render "):
            # HTML rendering
            line = line.replace("render ", "")
            if line.startswith("head("):
                parens = parens + 1
                render = "head"
                return "\t<head>\n"
            elif line.startswith("body("):
                parens = parens + 1
                render = "body"
                return "\t<body>\n"
            else:
                parse_html(line, 1)
    else:
        if ")" in line and stateparens == 0:
            parens = parens - 1
            x = "\t</body>\n" if render == "body" else "\t</head>\n"
            return x
        else:
            return parse_html(line, 2)
def parse_html(line, mode):
    if mode == 2:
        if line.startswith("p{") and render == "body":
            line = line.replace("p{", "")
            line = line.replace("}", "")
            return "\t\t<p>" + line.rstrip('\n') + "</p>\n"
        else:
            return ""
    else:
        return ""
def parse(line):
    # CallBack parsing
    # syntax: let int x = 5;
    line = line.replace(";", "")
    if line.lstrip().startswith("let"):
        if " int " in line:
            modified_line = line.replace("let int ", "")
            name, modified_line = modified_line.split("=")
            name = name.replace(" ", "")
            try:
                modified_line = int(modified_line)
            except ValueError:
                pass
            finally:
                if checkType(modified_line, int):
                    var[name] = int
                    return line.replace(" int", "")
                else:
                    print(f"ValueError!: {modified_line} is not compatiable with int!")
        elif " String " in line:
            modified_line = line.replace("let String ", "")
            name, modified_line = modified_line.split("=")
            name = name.replace(" ", "")
            if checkType(modified_line, str):
                var[name] = str
                return line.replace(" String", "")
            else:
                print(f"ValueError!: {modified_line} is not compatiable with String!")
        elif " bool " in line:
            modified_line = line.replace("let bool ", "")
            name, modified_line = modified_line.split("=")
            name = name.replace(" ", "")
            try:
                modified_line = bool(modified_line)
            except ValueError:
                pass
            finally:
                if checkType(modified_line, bool):
                    var[name] = bool
                    return line.replace(" bool", "")
                else:
                    print(f"ValueError!: {modified_line} is not compatiable with bool!")
    if line.lstrip().startswith("var"):
        if " int " in line:
            modified_line = line.replace("var int ", "")
            name, modified_line = modified_line.split("=")
            name = name.replace(" ", "")
            try:
                modified_line = int(modified_line)
            except ValueError:
                pass
            finally:
                if checkType(modified_line, int):
                    return line.replace(" int", "")
                else:
                    print(f"ValueError!: {modified_line} is not compatiable with int!")
        elif " String " in line:
            modified_line = line.replace("var String ", "")
            name, modified_line = modified_line.split("=")
            name = name.replace(" ", "")
            if checkType(modified_line, str):
                return line.replace(" String", "")
            else:
                print(f"ValueError!: {modified_line} is not compatiable with String!")
        elif " bool " in line:
            modified_line = line.replace("var bool ", "")
            name, modified_line = modified_line.split("=")
            name = name.replace(" ", "")
            try:
                modified_line = bool(modified_line)
            except ValueError:
                pass
            finally:
                if checkType(modified_line, bool):
                    return line.replace(" bool", "")
                else:
                    print(f"ValueError!: {modified_line} is not compatiable with bool!")
    if line.lstrip().startswith("const"):
        if " int " in line:
            modified_line = line.replace("const int ", "")
            name, modified_line = modified_line.split("=")
            name = name.replace(" ", "")
            try:
                modified_line = int(modified_line)
            except ValueError:
                pass
            finally:
                if checkType(modified_line, int):
                    return line.replace(" int", "")
                else:
                    print(f"ValueError!: {modified_line} is not compatiable with int!")
        elif " String " in line:
            modified_line = line.replace("const String ", "")
            name, modified_line = modified_line.split("=")
            name = name.replace(" ", "")
            if checkType(modified_line, str):
                return line.replace(" String", "")
            else:
                print(f"ValueError!: {modified_line} is not compatiable with String!")
        elif " bool " in line:
            modified_line = line.replace("const bool ", "")
            name, modified_line = modified_line.split("=")
            name = name.replace(" ", "")
            try:
                modified_line = bool(modified_line)
            except ValueError:
                pass
            finally:
                if checkType(modified_line, bool):
                    return line.replace(" bool", "")
                else:
                    print(f"ValueError!: {modified_line} is not compatiable with bool!")
# Check type
def checkType(value, type):
        x = isinstance(value, type)
        return x

parse("let String hi = 5")
print(var)
with open(input()) as files:
    for line in files:
        parse(line)