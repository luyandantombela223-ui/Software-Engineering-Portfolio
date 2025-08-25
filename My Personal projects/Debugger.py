# A program to debug error in a program
# Luyanda Ntombela
# 14 May 2025

print("***** Program Trace Utility *****")
filename = input("Enter the name of the program file: ")

try:
    f = open(filename, "r")
    lines = f.readlines()
    f.close()

    if len(lines) > 0 and lines[0].strip() == '"""DEBUG"""':
        print("Program contains trace statements")
        # remove debug lines
        new_lines = []
        for line in lines:
            if line.strip() == '"""DEBUG"""':
                continue
            elif '"""DEBUG""";print(' in line:
                continue
            else:
                new_lines.append(line)
        f = open(filename, "w")
        f.writelines(new_lines)
        f.close()
        print("Removing...Done")
    else:
        print("Inserting...", end="")
        new_lines = ['"""DEBUG"""\n']
        for line in lines:
            new_lines.append(line)
            if line.strip().startswith("def "):
                name = line.strip().split()[1]
                name = name[:name.index("(")]
                space = " " * (len(line) - len(line.lstrip()) + 4)
                trace = space + '"""DEBUG""";print(\'' + name + '\')\n'
                new_lines.append(trace)
        f = open(filename, "w")
        f.writelines(new_lines)
        f.close()
        print("Done")

except:
    print("Something went wrong.")
