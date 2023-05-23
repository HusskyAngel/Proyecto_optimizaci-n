class Utils():
    @staticmethod
    def readDzn(path:str):
        with open(path, 'r') as f:
            file_content = f.read()
            file_content = file_content.split("\n")
            #vars 
            n_teams=int(file_content[0].replace(" ", ""))
            min_d=int(file_content[1].replace(" ", ""))
            max_d=int(file_content[2].replace(" ", ""))
            matriz= [ list(map(int, x.split())) for x in file_content[3:3+n_teams]]
            return (n_teams,min_d,max_d,matriz)
