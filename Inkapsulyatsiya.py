# # inkapsulyatsiya
 

# class Komputer:
#     __number = 0
#     def __init__(self, nomi, protsessori, xotirasi, narxi):
#          Komputer.__number += 1
#          self.__id = Komputer.__number
#          self.nomi=nomi
#          self.protsessori=protsessori
#          self.xotirasi=xotirasi
#          self.narxi=narxi   
         
#     def get_id(self):
#         return self.__id
    
#     @classmethod
#     def get_count(cls):
#         return cls.__number
       
#     def get_info(self):
#         return f"{self.nomi}"
    
# obj1=Komputer("hp", "intel core i5", "512Gb", "6000000")
        
class Talaba:
    talabalar_soni=0
    def __init__(self, ism, familiya, guruh, shartnoma):
        Talaba.talabalar_soni+=1
        self.__id=Talaba.talabalar_soni
        self.ism=ism
        self.familiya=familiya
        self.guruh=guruh
        self.shartnoma=shartnoma 
        
    def get_info(self):
        return f"{self.ism} {self.familiya}"
    
    @classmethod
    def get_count(cls):
        return cls.talabalar_soni
    
    def get_id(self):
        return self.__id
    
    def change_id(self):
        return self.__id
    
class Shaxs:
    odamlar_soni=0
    def __init__(self, JSHSHIR, ism, familiya, ish_joyi):
        self.__JSHSHIR=JSHSHIR
        self.ism=ism
        self.familiya=familiya
        self.ish_joyi=ish_joyi
        
    def get_info(self):
        return f"{self.ism} {self.familiya}"
    
    def get_JSHSHIR(self):
        return self. JSHSHIR
    
    def change_JSHSHIR(self):
        return self.JSHSHIR
    
    @classmethod 
    def get_count(cls):
        return cls.odamlar_soni
    
talaba1=Talaba("Mashhura", "Quralova", "932-22", "grand")
talaba2=Talaba("Dilnura", "Hayitboyeva", "932-22", "grand")
shaxs1=Shaxs("Mashhura", "Quralova", "65412365412365", "TATU UF")
shaxs2=Talaba("Dilnura", "Hayitboyeva", "78965412365478", "TATU UF")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        