from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np

class Image:
    def __init__(self):
        """Initialisation d'une image composee d'un tableau numpy 2D vide
        (pixels) et de 2 dimensions (H = height et W = width) mises a 0
        """
        self.pixels = None
        self.H = 0
        self.W = 0
    

    def set_pixels(self, tab_pixels):
        """ Remplissage du tableau pixels de l'image self avec un tableau 2D (tab_pixels)
        et affectation des dimensions de l'image self avec les dimensions 
        du tableau 2D (tab_pixels) 
        """
        self.pixels = tab_pixels
        self.H, self.W = self.pixels.shape


    def load(self, file_name):
        """ Lecture d'un image a partir d'un fichier de nom "file_name"""
        self.pixels = io.imread(file_name)
        self.H,self.W = self.pixels.shape 
        print("lecture image : " + file_name + " (" + str(self.H) + "x" + str(self.W) + ")")


    def display(self, window_name):
        """Affichage a l'ecran d'une image"""
        fig = plt.figure(window_name)
        if (not (self.pixels is None)):
            io.imshow(self.pixels)
            io.show()
        else:
            print("L'image est vide. Rien à afficher")


    #==============================================================================
    # Methode de binarisation
    # 2 parametres :
    #   self : l'image a binariser
    #   S : le seuil de binarisation
    #   on retourne une nouvelle image binarisee
    #==============================================================================
    def binarisation(self, S):
        # creation d'une image vide
        im_bin = Image()
        
        # affectation a l'image im_bin d'un tableau de pixels de meme taille
        # que self dont les intensites, de type uint8 (8bits non signes),
        # sont mises a 0
        im_bin.set_pixels(np.zeros((self.H, self.W), dtype=np.uint8))

        # TODO: boucle imbriquees pour parcourir tous les pixels de l'image im_bin
        # et calculer l'image binaire
        for l in range (self.H):
            for c in range (self.W):
                if(self.pixels[l][c]>=S): 
                    im_bin.pixels[l][c]=255
                else:
                    im_bin.pixels[l][c]=0
        return im_bin  


    #==============================================================================
    # Dans une image binaire contenant une forme noire sur un fond blanc
    # la methode 'localisation' permet de limiter l'image au rectangle englobant
    # la forme noire
    # 1 parametre :
    #   self : l'image binaire que l'on veut recadrer
    #   on retourne une nouvelle image recadree
    #==============================================================================
    def localisation(self):
        l_min=self.H
        l_max=0
        c_min=self.W
        c_max=0
        for i in range(self.H):
            for j  in range(self.W):
                if(self.pixels[i][j]==0):
                    if j<c_min:
                        c_min=j
                    if j>c_max:
                        c_max=j
                    if i<l_min:
                        l_min=i
                    if i>l_max:
                        l_max=i
        new_image=Image()
        new_image.set_pixels(self.pixels[l_min:l_max,c_min:c_max])
        return new_image

    #==============================================================================
    # Methode de redimensionnement d'image
    #==============================================================================
    def resize(self, new_H, new_W):
        new_image=Image()
        n=resize(self.pixels,(new_H,new_W),0)
        new_image.set_pixels(np.uint8(n*255))
        return new_image

    #==============================================================================
    # Methode de mesure de similitude entre l'image self et un modele im
    #==============================================================================
    def similitude(self, im):
        nombre_similitude = 0 
        for x in range(self.H):
            for y in range(self.W):
                if self.pixels[x][y] == im.pixels[x][y]:
                    nombre_similitude += 1
        taux = nombre_similitude/(self.H * self.W)
        return taux

