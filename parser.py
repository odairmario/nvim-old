import re


def parser_line(delimiter,line ):
    p = re.split("[\s,^]*\{}[\s,\n]*".format(delimiter),line)

    return p[1:-1]
def parser(string, delimiter,end_delimiter,lines):
    """TODO: Docstring for parser.

    :lines: TODO
    :returns: TODO

    """
    data = []
    string = string.lower()

    for index,line in enumerate(lines):
        line = line.lower()

        if string in line:
            if lines[index+1].startswith(delimiter) and index+1 < len(lines):
                header = parser_line(delimiter,lines[index+1])
            index +=2

            while lines[index].startswith(delimiter) and index < len(lines):
                line = lines[index]
                index += 1
                _data = parser_line(delimiter,lines[index])

                if _data:
                    data.append(dict(zip(header,_data)))

    return data


def main():
    """TODO: Docstring for main.
    :returns: TODO

    """
    with open("README.md","r") as f:
        lines = f.readlines()
        result = parser("### general settings","|","\n",lines)
        __import__('pprint').pprint(result)

if __name__ == "__main__":
    main()
