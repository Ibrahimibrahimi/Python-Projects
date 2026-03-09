"""
      This class can encrypt a text using a list of keywords.
      [PROCESS] : 
            - suffle given keys.
            @ [NOTE] : the given keys have to be same length as text unique words or more , not less than it !!
            - get unique items of given text
            - set a random unique key for each letter
            - save last encoded keys:value as Summary if u want to retreive it (because every time you encode a text , it generate differents keys event its the same text)
            - return an array : [encoded_text , keys_of_each_letter]
      [NOTE] :
            - Make sure the keys array has the same length as unique elements in the text you want to encode
            - Avoid to encode a text with keys in same type (example : text in english and also keys are english = DEFORMAT TEXT OUTPUT)

"""
import random
class Crypter :
      def __init__(self,keys:list,saveLastEncoding = False):
            self.keys = Crypter.shuffleString(Crypter.ToString(keys),random.randint(0,22))
            self.History = []
            self.saveLastEncoding = saveLastEncoding
      ######### TOOLS METHODS => STATIC METHODS
      # FUNCTION TOOLS
      @staticmethod
      def replaceAll(string:str , replace:str,by:str):
            o = string
            for i in list(replace) :
                  o = o.replace(i,by)
            return o
      @staticmethod
      def shuffleN(text:str):
            return Crypter.replaceAll(str(set(text)) , "{},' ","")
      @staticmethod
      def shuffleString(text:str ,n:int=1):
            o = text
            for i in range(n):
                  o = Crypter.shuffleN(o)
            return o
      @staticmethod
      def getKeyOfValueInDict(di:dict,value:str)->str:
            for i in di.keys() :
                  if di[i] == value :
                        return i
      @staticmethod
      def UniqueElements(text:str):
            """
                  get all unique items in a text
            """
            uniq = []
            for i in list(text) :
                  if i not in uniq and i != " ":
                        uniq.append(i)
            return sorted(uniq)
      @staticmethod 
      def ToString(obj:any):
            if isinstance(obj,str):
                  return obj
            if isinstance(obj,list) or isinstance(obj,set):
                  o = ""
                  for i in obj :
                        o += i
                  return o
            if isinstance(obj,int):
                  return str(obj)
            return str(obj) # if anything else
      ######### MAIN METHODS OF THIS CLASS 
      # check if length of unique items match or great than length of given keywords
      @staticmethod
      def checkAbilityToEncode(text:str):
            if len(Crypter.UniqueElements(text)) >= len(keys):
                  print("TEXT CAN'T BE ENCODED : The length of given keywords should be >= length of unique elements in text")
                  return False
            else : 
                  return True
      @staticmethod
      def enhanceDicts(d:dict):
            output = ""
            for k,v in d.items():
                  output += f"'{k}' => '{v}' ,"
            output = output[:-1] if output[-1] == "," else output
            return output

      # generate keys 
      def generateKeys(self,text:str):
            if not Crypter.checkAbilityToEncode(text) :
                  return
            summary = {}
            uniqItems = Crypter.UniqueElements(text)
            encoded = ""
            # SET A KEY FOR EACH ELEMENT IN THE GIVEN TEXT
            for k in self.keys :
                  if k not in summary.values() :
                        # set key for a letter
                        for l in uniqItems :
                              if l not in summary.keys() :
                                    summary[l] = k
                                    break # to next letter
            return summary
      def encode(self,text:str):
            if not Crypter.checkAbilityToEncode(text) :
                  return
            summary = self.generateKeys(text)
            encoded = text
            # ENCODE WITH DETERMINED KEYS
            for i in Crypter.UniqueElements(text):
                  encoded = encoded.replace(i,summary[i])
            # SAVE HISTORY IF MENTIONNED
            if self.saveLastEncoding :
                  self.History = [encoded,summary]
            # RETURN RESULT
            return [encoded,summary]
      
      def decode(self,encoded:str , summary:dict):
            """
                  decode a given text using its generated summary
            """
            out = encoded
            for i in out :
                  if i in summary.values() :
                        out = out.replace(i,Crypter.getKeyOfValueInDict(summary,i))
            return out
      def getHistory(self):
            return self.History
      def example(self,text:str):
            # show an example by showing the text , the encryptedText , and used summary
            return f"[EXAMPLE] : \n\t+ Input Text : '{text}'\n\t+ Keys : '{Crypter.ToString(self.keys)}'\n\t+ Result : {self.encode(text)}\n\t+ Encrypted With : {Crypter.enhanceDicts(self.History[1])}\n"
# THIS CLASS ENCODE EVERY TEXT : ARAB/ENG WITH KEYS THAT ARE RUSSIAN LETTERS
# EXAMPLE : 

russian = "йцукенгшщзждлорпавыфячсмитьбю"
symbols = "/*-+.=)çà_è('\"é&)~#{[|`]}\\"
keys = list(symbols)

crp = Crypter(keys=keys , saveLastEncoding=True)

print("============")
print(crp.example("ibrahim"))