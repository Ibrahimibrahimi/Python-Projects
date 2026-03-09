
class Tools :
    @staticmethod
    def _dict_to_table(Dict): 
        """ Pour visualiser le resultat de retourne de certains fonctions : _test_t() , _puissance_correlation()... """
        # Get max lengther key
        Max , last = 0,0
        word = ""
        # Calculer le len du max key
        n = 50
        Max = 0
        word = ""
        output = ""
        for i in list(Dict.keys()):
            if len(i) > Max :
                word = i
                Max = len(i)
        # Difference de space
        diff = len(word)
        # Header
        print(" ","_" * (int(n / 2)) , "_"*n,sep="")
        for key,value in Dict.items():
            last = len(word) - len(key)
            output += "|   " + len(key) * " " + " " * last + "   |" + "\n"
            output += "|   "+str(key)+" " * last + "   |   "+str(value) + "\n" # Contenue
            output += "|___"+len(key) * "_"+"_" * last + "___|"+"_"*n + "\n"
            output += "|   "+len(key) * " "+" " * last + "   |"+ "\n"
        return output
