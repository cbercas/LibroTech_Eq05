class Libro:
    def __init__(self, isbn, titulo, autor, genero, publicacion):
        self._isbn = isbn
        self._titulo = titulo
        self._autor = autor
        self._genero = genero
        self._publicacion = publicacion

    # Getters
    @property
    def isbn(self):
        return self._isbn

    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def genero(self):
        return self._genero

    @property
    def publicacion(self):
        return self._publicacion

    # Setters
    @isbn.setter
    def isbn(self, value):
        self._isbn = value

    @titulo.setter
    def titulo(self, value):
        self._titulo = value

    @autor.setter
    def autor(self, value):
        self._autor = value

    @genero.setter
    def genero(self, value):
        self._genero = value

    @publicacion.setter
    def publicacion(self, value):
        self._publicacion = value

    # Método para mostrar el objeto en formato de texto
    def __str__(self):
        return (f"Libro ID: {self.isbn}\n"
                f"Título: {self.titulo}\n"
                f"Autor: {self.autor}\n"
                f"Género: {self.genero}\n"
                f"Año de publicación: {self.publicacion}")

