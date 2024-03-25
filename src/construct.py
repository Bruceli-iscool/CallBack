# Construct compilable source code
# Basically create an AST
parens = 0
render = ""
stateparens = 0
def construct(line):
    global parens, render, stateparens
    line = line.lstrip()
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
                parse(line, 1)
    else:
        if "(" in line and stateparens == 0:
            parens = parens - 1
            x = "\t</body>\n" if render == "body" else "\t</head>\n"
            return x
        else:
            return parse(line, 2)
def parse(line, mode):
    if mode == 2:
        if line.startswith("p(") and render == "body":
            line = line.replace("p(", "")
            line = line.replace(")", "")
            return "<p>" + line + "</p>"