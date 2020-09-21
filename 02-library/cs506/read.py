def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    matrix = []
    with open(csv_file_path, "r+") as f:
        lines = f.readlines()
        for row in lines:
            entries = row.split(",")
            toAdd = []
            for i in range(len(entries)):
                entries[i] = entries[i].rstrip('\n')
                if entries[i].isnumeric():
                    toAdd.append(int(entries[i]))
                else:
                    try:
                        toAdd.append(float(entries[i]))
                    except ValueError:
                        toAdd.append(entries[i])
            matrix.append(toAdd)
        f.close()
    return matrix

