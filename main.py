from SymbolTable import SymbolTable

def run():
    symbolTable = SymbolTable()
    symbolTable.add("flcd")
    symbolTable.add("DA")
    symbolTable.add("x")
    symbolTable.add("5")
    symbolTable.add("rr")
    symbolTable.add("ppp")
    symbolTable.add("YES")
    symbolTable.add("7")
    print(symbolTable)


if __name__ == '__main__':
    run()