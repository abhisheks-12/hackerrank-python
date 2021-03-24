def split_n_join(line):
    line = line.split(" ")
    line = ("-").join(line)
    return line

a = split_n_join("Heloo my nmae is")
print(a)


