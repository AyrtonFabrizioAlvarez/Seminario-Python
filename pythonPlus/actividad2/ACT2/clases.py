class Usuario():
    
    generos = set()
        
    def __init__(self, nombre, genero=None):
        self.nombre=nombre
        self.genero=genero
        self._memes=[]
        Usuario.generos.add(genero)
        
    @property
    def memes(self):
         return self._memes
    
    @memes.setter
    def memes(self, lista):
         self._memes = lista

    def __str__(self):
        texto = f"El usuario {self.nombre} realizó los siguientes memes: "
        for elem in self.memes:
            texto += f"\n\t\t{elem}"
        return texto
