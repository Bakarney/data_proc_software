import proc


if __name__ == '__main__':
    print("\nPart 1")
    print(proc.pollutantmean("specdata", "sulfate", range(1, 11)))
    print(proc.pollutantmean("specdata", "nitrate", range(70, 73)))
    print(proc.pollutantmean("specdata", "nitrate", 23))

    print("\nPart 2")
    print(proc.complete("specdata", 1))
    print(proc.complete("specdata", [2, 4, 8, 10, 12]))
    print(proc.complete("specdata", range(30, 24, -1)))

    print("\nPart 3")
    print(proc.corr("specdata", 150))
    print(proc.corr("specdata", 400))
    print(proc.corr("specdata", 5000))
