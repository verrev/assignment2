from pandas import read_excel, concat

def merge_two_excel_files(filenameA, filenameB, filenameOut):
    a = read_excel(filenameA)
    b = read_excel(filenameB)
    c = concat([a, b])
    c.to_excel(filenameOut)

def main():
    merge_two_excel_files('a.xlsx', 'b.xlsx', 'c.xlsx')

if __name__ == "__main__":
    main()
