!/usr/bin/env python
# coding: utf-8

# # SAE : Implémentation d'un besoin client
# # <center> Codage et décodage </center>

# L'objectif de ce projet est d'implanter différentes techniques de codage et décodage de l'information. 
# Plus précisément, on s'intéressera ici à deux  méthodes qui ont des objectifs assez différents: 
# - le **codage à bit de parité simple** qui permet de vérifier que l'information reçue n'a pas été altérée au cours de la transmission;
# - le **chiffrement de César** qui permet de chiffrer l'information à transmettre.

# **Ce projet est à faire en binôme.**
# 
# #### Planning
# - Pour le 4 octobre : implanter les fonctions de la partie préliminaire et comprendre le principe du codage à bit de parité simple. 
# - Pour le 11 octobre : implanter les fonctions de ârtie codage à bit de parité simple et comprendre le principe du chiffrement de césar.
# - Pour le 18 octobre : implanter les fonctions et programmes des questions 1 à 5 de la partie chiffrement de César.
# - Pour le 24 octobre : implanter les fonctions et programmes des questions 6 à 8 de la partie chiffrement de César 
# - **Rendu** : l'ensemble est à envoyer au plus tard le dimanche **24 octobre**.
# 
# Pour chaque fonction demandée, un exemple d'appel ou des tests unitaires sont donnés de manière à vérifier la conformité de votre proposition.
# 
# Lorsque l'on convertit des chaînes de caractères en nombres et *vice versa*, on a souvent recours à des **casts**. 
# 
# Lorsque l'on manipule des caractères, il est également utile d'accéder à leur unicode et *vice versa*. En Python, cela se fait via les fonctions `ord` et `chr` respectivement.

# ## Préliminaires
# 
# Pour implanter les différentes méthodes de codage et décodage, certaines fonctions sont bien utiles. Ce sont ces fonctions qui font l'objet de cette partie préliminaire.

# ### Question 1 : Saisie contrôlée d'un entier positif
# Ecrire une fonction  de saisie contrôlée `saisieIntPos` demandant à l'utilisateur un entier positif ou nul et le lui redemandant jusqu'à ce que ce soit un entier positif ou nul.

# In[1]:


def saisieIntPos():
    """
    Fonction  demandant à l'utilisateur un entier positif ou nul et le lui 
    redemandant jusqu'à ce que ce soit un entier positif ou nul.
    retourne l'entier positif ou nul
    """
    entier = int(input())
    while entier < 0:
        entier = int(input())
    return entier

        


# In[2]:


# ------------  TEST/EXEMPLE ---------- #
print("l'entier saisi est", saisieIntPos())


# ### Question 2 : Saisie d'un entier positif  qui s'écrit sur 10 bits
# Le plus grand entier positif que l'on puisse écrire en binaire sur 10 bits est 1023 (car 10000000000 en binaire vaut 1024 en décimal).
# 
# Ecrire une fonction  de saisie contrôlée `saisieIntPos10Bits` demandant à l'utilisateur un entier compris entre 0 (inclus) et 1023 (inclus) et lui redemandant un entier jusqu'à ce que ce soit qu'il soit correct.

# In[3]:


def saisieIntPos10Bits():
    """
    Cette fonction demande à l'utilisateur un entier compris entre 0 (inclus) et 1023 (inclus)
    et lui redemandant un entier jusqu'à ce que ce soit qu'il soit correct.
    retourne l'entier correct
    """
    print("Saisissez un entier entre 0(inclus) et 1023(inclus)")
    entier = int(input())
    while entier < 0 or entier > 1023:
        print("Saisissez un entier entre 0(inclus) et 1023(inclus)")
        entier = int(input())
    return entier
        


# In[5]:


# ------------  TEST/EXEMPLE ---------- #
print("l'entier saisi est",saisieIntPos10Bits())


# ### Question 3 : Saisie contrôlée d'un entier compris entre a et b
# Ecrire une fonction  de saisie contrôlée `saisieIntab` demandant à l'utilisateur un entier compris entre a (inclus) et b (inclus) et lui redemandant un entier jusqu'à ce que ce soit qu'il soit dans le bon intervalle.
# 
# On ne vérifiera pas que a est plus petit que b.

# In[6]:


def saisieIntab(a, b):
    """
    Cette fonction demande à l'utilisateur un entier compris entre a (inclus) et b (inclus)
    et lui redemandant un entier jusqu'à ce que ce soit qu'il soit dans le bon intervalle.
    """
    print("Saisir un entier inclus dans l'intervalle a et b")
    entier = int(input())
    while entier < a or entier > b:
        print("Saisir un entier inclus dans l'intervalle a et b")
        entier = int(input())
    return entier



# In[7]:


# ------------  TEST/EXEMPLE ---------- #
print("l'entier saisi est",saisieIntab(1,25))


# ### Question 4 : Verification de la binarité d'une chaîne
# Ecrire une fonction `verifBin` qui permet de vérifier qu'une chaîne de caractères ne contient que des `0` et des `1`.
# Elle prendra en paramètre une chaîne de caractère `s_bin` et retournera `True` si la chaîne n'est composée que de`0` et de `1` et `False` sinon.

# In[8]:


def verifBin(s_bin):
    """
    Cette fonction permet de vérifier qu'une chaîne de caractères ne contient que des 0 et des 1.
    param s_bin : str
    Retourne True si s_bin ne contient que des 0 et des 1 sinon False
    """
    i = 0
    while i < len(s_bin):
        if s_bin[i] != '0' and s_bin[i] != '1':
            return False
        else:
            i += 1
        return True

    


# In[9]:


# ------------  TEST/EXEMPLE ---------- #
def test_verifBin():
    assert verifBin('0000')
    assert verifBin('0110')
    assert not verifBin('2981')
    assert not verifBin('andei')
    assert not verifBin('@l')
    print("test ok")

test_verifBin()


# ### Question 5 : Conversion d'un nombre décimal en binaire 
# 
# Pour transmettre l'information, on est souvent amené à convertir en binaire des nombres décimaux. Par exemple, Le nombre `13` écrit en base 10 se code `1101` en binaire.
# 
# *Comment effectuer ce codage ?*
# 
# On peut utiliser la méthode des divisions successives par 2.
# 
# **Rappels :** En Python,
# - le quotient d'une division euclidienne s'obtient en utilisant l'opérateur `//` ; ainsi `5//2=2`
# - le reste d'une division euclidienne s'obtient en utilisant l'opérateur `%`; ainsi `5%2=1`
# 
# ```
#    	             .
#    	            / \   <--- sens de lecture des restes pour former le nombre binaire
# 13 // 2   = 6   	|   
# 13 %  2   = 1    |   reste = 1
#                  |
# 6 // 2    = 3   	|   
# 6  %  2   = 0   	|   reste = 0
#                  |  
# 3 // 2    = 1    |   
# 3 %  2    = 1    |   reste = 1
#                  |
# 1  // 2   = 0  	 |                  <---- On arrête, car le quotient est égal à 0
# 1  % 2    = 1    |   reste = 1
#    	             |                  
# Le nombre 13 en base 10 se code 1101 en binaire.
# ```
# 
# Ecrire une fonction `int2bin` prenant en paramètre un entier positif `n` écrit en base 10  et retournant une chaine de caractères correspondant à ce nombre codé en binaire en utilisant la méthode des divisions successives.
# 
# On pensera à procéder à d'éventuels casts dans la fonction. On fera également attention au sens dans lequel on procède aux concaténations de chaînes de caractères.
# 
# Voici le prototype de la fonction :
# ```python
# def int2bin(n):
#     """
#     :param n: nombre en base 10 à convertir en binaire
#     :return: str contient la representation binaire de n
#     """
# ```
# **Note :** Aucun test ne sera fait dans la fonction pour vérifier la validité du paramètre.

# In[10]:


def int2bin(n):
    """
    :param n: int, nombre en base 10 à convertir en binaire
    :return: str contient la representation binaire de n
    """
    liste = []
    liste1 = ''
    i = 0
    if n == 0:
        return str(n)
    while n != 0:
        quotient = n % 2
        liste.append(int(quotient))
        n = n // 2
        i += 1
    while i!=0:
        liste1 = liste1 + str(liste[i-1])
        i -= 1

    return liste1

int2bin(1023)



# In[11]:


# ------------  TEST/EXEMPLE ---------- #
def test_int2bin():
    assert int2bin(0)=='0'
    assert int2bin(7)=='111'
    assert int2bin(16)=='10000'
    print("test OK")
    
test_int2bin()


# ## 1ère Partie : Code à parité simple
# 
# 
# Dans la technologie des objets de l'internet (IOT), il faut souvent transmettre des informations de capteurs  (par exemple, d'un capteur de température) vers un serveur (par exemple un serveur broker MQTT/*Message Queuing Telemetry Transport*).
# 
# Dans ce qui suit, on développe les outils logiciels qui interviennent dans la transmission d'un nombre entier (écrit en base 10).
# 
# Dans la partie préliminaire, une fonction de conversion de décimal en binaire a été définie. On sait donc comment mettre sous forme binaire l'information à transmettre. 

# ### Question 1 : Calcul du bit de parité
# 
# Lors d'une transmission, des erreurs peuvent se produire (dûes à des interférences par exemple). La technique dite du bit de parité permet de détecter simplement certaines erreurs.
# 
# **Principe :**
# - comptage du nombre de `1` dans la représentation binaire d'une information,
# - calcul du bit de parité : si le nombre de `1` est impair, le bit de parité vaut 1, sinon il vaut 0.
# 
# **Exemple :**
# ```
# information = 1101
# bit de parité  ---> 1
# ```
# Ecrire une fonction `parite` prenant en paramètres une chaine de caractères représentant une information binaire et qui retourne `True` si le bit de parité vaut 1 (*i.e.*, si le nombre de 1 est impair), `False` sinon.
# 
# Voici le prototype de la fonction :
# ```python
# def parite(str_bin):
#     """
#     Calcul du bit de parité du nombre binaire
#     :param str_bin: str contenant la représentation binaire d'un nombre
#     :return : bool, True -> bit de parité à 1, False -> bit de parité à 0
#     """
# ```

# In[12]:


def parite(str_bin):
    """
    Calcul du bit de parité du nombre binaire
    :param str_bin: str contenant la représentation binaire d'un nombre
    :return : bool, True -> bit de parité à 1, False -> bit de parité à 0
    """
    i = 0
    bitparite = 0
    while i < len(str_bin):
        if str_bin[i] == "1":
            bitparite += 1
        i +=1
    bitparite = bitparite % 2
    if bitparite == 1:
        return True 
    else:
        return False
    
    


# In[13]:


# ------------  TEST/EXEMPLE ---------- #
def test_parite():
    assert not parite('0000')
    assert parite('10000')
    assert not parite('1010')
    assert parite('11111')
    print("test ok")
    
test_parite()


# ### Question 2 : Constitution de la trame à envoyer
# 
# La trame à envoyer pour transmettre l'information est constituée de 11 bits :
# - le bit le plus à gauche (de poids le plus fort) est le bit de parité ;
# - les autres bits représentent l'information. Si l'information n'occupe pas tous les bits alors des `0` seront rajoutés en tête, par exemple si l'information n'occupe réellement que 4 bits (bit 0 à bit 3), tous les autres bits de poids supérieurs (bit 4 à bit 10) seront mis à zéro.
# 
# **Exemple :**
# ```
# information = 1101
# bit de parité ---> 1
# la trame à envoyer est donc 10000001101
# ```
# 
# Ecrire une fonction `trame` prenant un nombre entier compris entre 0 et 1023 (c'est le nombre décimal maximal codable sur 10 bits) et qui retourne une chaîne de caractères correspondant à la trame qui sera effectivement envoyée.
# 
# Voici le prototype de la fonction :
# ```python
# def trame(n):
#     """
#     Contruit une trame sur 11 bits sous la forme
#     bit parite | bit 10 | bit 9 | .... | bit 1 | bit 0 |
#     bit parite : est le bit de parité
#     bit 10 à bit 0 : information à transmettre
#     :param n: entier (en base 10) à transmettre dans la trame
#     :return : str, trame sur 11 bits qui sera transmise
#     """
# ```
# **Note :** Aucun test ne sera fait dans la fonction pour vérifier la validité du paramètre.

# In[14]:


def trame(n):
    """
    Contruit une trame sur 11 bits sous la forme
    bit parite | bit 10 | bit 9 | .... | bit 1 | bit 0 |
    bit parite : est le bit de parité
    bit 10 à bit 0 : information à transmettre
    :param n: entier (en base 10) à transmettre dans la trame
    :return : str, trame sur 11 bits qui sera transmise
    """
    
    res = int2bin(n) 
    # On initialise res1 avec le bit de parité
    res1 = parite(res)
    if res1 == False:
        res1 = "0"
    else:
        res1 = "1"
    #Rajoute des 0 jusqu'à que la longueur de la trame vaut 10
    while len(res) < 10:
        res = "0" + res

    res = res1 + res
        
        
    return res
    
trame(1023)
   
    


# In[15]:


# ------------  TEST/EXEMPLE ---------- #
def test_trame():
    assert trame(1023)=='01111111111'
    assert trame(16)=='10000010000'
    assert trame(31)=='10000011111'
    assert trame(0)=='00000000000'
    print("test ok")

test_trame()


# ### Question 3 : Vérification de la validité de la trame reçue
# 
# Lors de la réception du message, on peut tester s'il n'y a pas eu de problème de transmission du message en vérifiant que la trame est correcte. Il faut en effet que le bit de parité corresponde bien au 10 bits qui le précède. 
# 
# - Ecrire une fonction `verifTrame` prenant une chaîne de 11 caractères binaires et qui retourne `True` si la trame est correcte (*i.e*, la chaîne est de longueur 11, elle est composée de `0`et de `1` et que le premier bit correspond bien au bit de parité des 10 bit précédents et `False` sinon. 
# - Ecrire également une fonction `test_verifTrame` de tests unitaires permettant de vérifier la conformité de la fonction `verifTram`.
# 
# Voici le prototype de la fonction :
# ```python
# def verifTrame(trm):
#     """
#     Vérifie si la chaine est binaire, de longueur 11, et que le 
#     premier bit est le bit de parité des 10 bit précédents
#     :param trm: une chaine de caractères 
#     :return : bool, True -> c'est une trame de code de parité, 
#     False sinon 
#     """
# ```
# On pensera à utiliser la fonction `verifBin()` définie dans la partie préliminaire.

# In[16]:


def verifTrame(trm):
    """
    Vérifie si la chaine est binaire, de longueur 11, et que le 
    premier bit est le bit de parité des 10 bit précédents
    :param trm: une chaine de caractères 
    :return : bool, True -> c'est une trame de code de parité, 
    False sinon 
    """
    agarder = 0
    if len(trm) < 11:
        return False
    i = 0
    while i < 11:
        if trm[i] == "0" or trm[i] == "1":
            i += 1
        else:
            return False
    agarder = trm[0]
    #Permet de commencer par la 2eme lettre directement
    fixed = trm[1:]
    res = parite(fixed)
    if res:
        res = "1"
    else:
        res = "0"
    if res == agarder:
        return True
    else:
        return False
verifTrame("0")


# In[17]:


def test_verifTrame():
    assert verifTrame("01111111111")
    assert not verifTrame("10000001010")
    assert not verifTrame("0")
    assert verifTrame("10000000001")
    print("test ok")

test_verifTrame()
    


# ### Question 4 : Décodage de la trame reçue 
# Après avoir vérifié que la trame est correcte, il reste à décoder l'information.
# - Ecrire une fonction `decodeTrame()`qui prend en paramètre une trame que l'on suppose correcte et qui retourne sous forme décimale l'information contenue dans cette trame, *i.e* l'entier qui est codé en binaire.
# - Ecrire également une fonction `test_decodeTrame` de tests unitaires permettant de vérifier la conformité de la fonction `decodeTram`.

# In[18]:


def decodeTrame(trame):
    """
     Décode une trame que l'on suppose correcte et qui 
     retourne sous forme décimale l'information contenue dans cette trame
     (l'entier qui est codé en binaire).
     :param trame: une chaine de caractères 
     :return : resultat-> qui est la forme decimal de trame  
     """
    i = 10
    puissancede2 = 0
    resultat = 0
    while i > 0:
        if trame[i] == '1':
            #L'opérateur ** nous permet de calculer des puissances
            resultat += 2 ** puissancede2
        i -= 1
        puissancede2 += 1
    return resultat


    
decodeTrame('01111111111')


# In[19]:


def test_decodeTrame():
    assert decodeTrame('01111111111') == 1023
    assert decodeTrame('10000010000') == 16
    assert decodeTrame('10000011111') == 31
    assert decodeTrame('00000000000') == 0
    print("Tout est ok")

test_decodeTrame()
    


# ### Question 5 : Programme principal
# On souhaite pouvoir transmettre des nombres entre 0 et 1023 (qui est le plus grand entier que l'on écrire sur 10 bits).
# 
# - Demander à l'utilisateur de saisir un nombre en utilisant la fonction de saisie contrôlée appropriée définie dans la partie préliminaire.
# - Coder ce nombre selon le codage à bit de parité simple à l'aide de la fonction définie précédemment.
# - Afficher ce codage.
# - Après avoir vérifié que la trame est correcte, decoder l'information à l'aide de la fonction définie pour cela.
# - Afficher le nombre obtenu.
# - Vérifier qu'il s'agit du nombre initial.

# In[21]:


res = saisieIntPos10Bits()
res1 = trame(res)
print(res1)
res2 = verifTrame(res1)
print(res2)
res3 = decodeTrame(res1)
print(res3)
res4 = trame(res3)
if res4 == res:
    print("Tout fonctionne")

    


# ## 2ème partie : Chiffrement de César

# Le chiffrement de César est une des plus anciennes méthodes de cryptographie. Il repose sur la rotation vers la droite de l’alphabet d’un nombre fixé de caractères. 
# 
# Par exemple, si on considère une rotation de 3 positions, on obtient pour les lettres minuscules la table de conversion ci-dessous :
# 
# 
# 
# |lettre originale|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|
# |----------------|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
# |lettre codée    |d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|a|b|c|
# 
# On a une table analogue pour les lettres majuscules. Les autres caractères ne sont pas cryptés mais simplement recopiés. 
#  
# Pour la rotation de 3 positions, si la phrase à chiffrer est `bonjour, il fait beau`, le message chiffré est alors `erqmrxu, lo idlw ehdx`. 
# 
# Il est bien sûr possible de changer le nombre de positions
# correspondant à la rotation. Ainsi, si l'on décide de décaler d'une seule position, le même message est alors chiffré en `cpokpvs jm gbju cfbv`. 
# 
# Le nombre correspondant à la rotation est appelé la *clé* du code
# car il permet le déchiffrementdu message. *La clé est un entier
#   compris entre 1 et 25*.
# 
# L'objectif est d'écrire des fonctions de chiffrement et de déchiffrement de textes pour le code de César.

# ### Question 1 : Chiffrement d'un caractère
# Ecrire une fonction `chiffreCar_cesar` prenant en paramètres
# un caractère et la clé de chiffrement.  Cette fonction retournera le
# caractère codé si le caractère est une lettre minuscule ou majuscule. Sinon, la fonction renverra le caractère initial.  Ainsi `chiffreCar_cesar('a',3)` renvoie `'d'`, `chiffreCar_cesar('d', 23)` renvoie `'a'`, `chiffreCar_cesar('C',4)` renvoie `'G'`.
# 
# **Indications :** 
# On rappelle que l'on peut comparer des caractères avec les opérateurs `<,>, ==`et `!=`.
# 
# La fonction `ord(c)` retourne le code Unicode du caractère `c` et la fonction `chr(i)` retourne la lettre dont le code Unicode est `i`. Par exemple :
#   ```python
#   uni = ord("a") # uni vaut 97 car l'unicode de "a" est 97
#   lettre = chr(98)  # lettre vaut "b" car 98 est son unicode
#   print( chr(ord("a")) == "a") # affiche True
#   ```
#   
# On rappelle que les unicodes des lettres minuscules sont consécutifs, compris entre 97 et 122  et suivent l'ordre alphabétique :  l'unicode de `'a'` est 97, celui de `'b'` est 98, etc, celui de `'z'` est 12. Il en est de même pour les unicodes des lettres majuscules qui varient de 65 pour `'A'`à 90 pour `'Z'`.

# In[22]:


def chiffreCar_cesar(lettre, cle):
    lettre = ord(lettre)
    if lettre >= 97 and lettre <= 122:
        lettre += cle
        if lettre > 122:
            lettre -= 122 
            lettre += 97 - 1
    elif lettre >= 65 and lettre <= 90:
        lettre += cle
        if lettre > 90:
            lettre -= 90 
            lettre += 65 - 1
    return chr(lettre)

chiffreCar_cesar(' ', 3)


# In[23]:


# ------------  TEST/EXEMPLE ---------- #
def test_chiffreCar_cesar():
    assert chiffreCar_cesar('a',3)=='d'
    assert chiffreCar_cesar('d', 23) =='a'
    assert chiffreCar_cesar('C',4)=='G'
    assert chiffreCar_cesar('@',17)=='@'
    print("test OK")
    
test_chiffreCar_cesar()


# ### Question 2 : Chiffrement d'une chaîne de caractères
# 
# En utilisant la fonction `chiffreCar_cesar`, écrire une fonction `chiffre_cesar` qui prend en paramètres une chaîne de caractères et la clé de chiffrement et qui retourne la chaîne chiffrée. 

# In[24]:


def chiffre_cesar(phrase, cle):
    i = 0
    phrasefini = ''
    while i < len(phrase):   
        res = chiffreCar_cesar(phrase[i], cle)
        phrasefini += res
        i += 1
    return phrasefini
    
chiffre_cesar('bonjour', 1)


# In[32]:


# ------------  TEST/EXEMPLE ---------- #
def test_chiffre_cesar():
    assert chiffre_cesar("bonjour, il fait beau",3)== "erqmrxu, lo idlw ehdx"
    assert chiffre_cesar("Bonjour",7)=="Ivuqvby"
    assert chiffre_cesar("C'est super la cryptographie",5)== "H'jxy xzujw qf hwduytlwfumnj"
    print("Test ok")

test_chiffre_cesar()


# ### Question 3
# Ecrire une fonction `dechiffre_cesar()` permettant de
# déchiffrer un message codé avec le chiffrement de César. Cette fonction prendra comme paramètres la chaîne chiffrée et la clé de chiffrement.
# 
# **Remarque**: Les valeurs des clés de chiffrement et de déchiffrement sont liées : la somme de la valeur de la clé de codage et de celle de décodage est égale à 26.  Ainsi si le codage est fait avec la clé 3, le décodage se fait avec la clé 23. Si le codage est fait avec la clé 10, le décodage se fait avec la clé 16.

# In[26]:


def dechiffre_cesar(mescode, cle):
    return chiffre_cesar(mescode, (26 - cle))


# In[31]:


# ------------  TEST/EXEMPLE ---------- #
def test_dechiffre_cesar():
    assert dechiffre_cesar("uryyb JBEYQ",13)=="hello WORLD"
    assert dechiffre_cesar("Ivuqvby",7)=="Bonjour"
    assert dechiffre_cesar("jgnnq YQTNF",2)=="hello WORLD"
    print("Test ok")
    
test_dechiffre_cesar()


# ### Question 4 : "C'est super la cryptographie"
# Ecrire un progamme qui vérifie que le message `C'est super la cryptographie !` chiffré avec la clé 5 donne `H'jxy xzujw qf hwduytlwfumnj !` et que le déchiffrement de cette chaîne avec la clé 5 redonne bien `C'est super la cryptographie !`.

# In[30]:


message = "C'est super la cryptographie !"
res = chiffre_cesar(message, 5)
print(res)
res1 =  dechiffre_cesar(res, 5) 
print(res1)


# ### Question 5 : ROT 13
# 
# Un cas particulier du chiffrement de César est le chiffrement [ROT13](https://fr.wikipedia.org/wiki/ROT13) qui correspond au chiffrement de César avec la clé 13. L'intérêt de ce chiffrement est que le chiffrement correspond au déchiffrement.
# Définir les fonctions `chiffre_ROT13` et `dechiffre_ROT13` en utilisant la fonction `chiffre_cesar`.
# 
# Afficher le chiffrement de `hello world` selon le chiffrement ROT13. Déchiffrer le message obtenu, afficher le résultat et vérifier que c'est bien `hello word`.

# In[33]:


def chiffre_ROT13(message):
    res = chiffre_cesar(message, 13)
    return res

res = chiffre_ROT13("hello world")
print(res)

def dechiffre_ROT13(message):
    res = dechiffre_cesar(message, 13)
    return res

res1 = dechiffre_ROT13(res)
print(res1)


# ### Question 6 : Vulnérabilité du code de César
# 
# Le code de César est très simple, il nécessite seulement que le destinataire connaisse la clé de chiffrement. Il est également très vulnérable.
# 
# Comment déchiffrer `oaz jk borrkzgtkayk` ? 
# 
# Ecrire une fonction `hackCesar` qui prend en paramètre un message chiffré et affiche tous les décodages possibles. 
# 
# Qu'est-ce qui se cache derrière le message  `oaz jk borrkzgtkayk`?

# In[34]:


def hackCesar(message):
    i = 0
    while i < 26:
        res = dechiffre_cesar(message, i)
        print(res)
        i += 1

hackCesar("oaz jk borrkzgtkayk ?")
print("Le message est : iut de villetaneuse ?")


# ### Question 7 : Chiffrement d'un fichier 
# 
# - Ecrire une fonction `chiffre_fichier` prenant en paramètres le chemin `fichier` d'un fichier, une clé `clé` de chiffrement et le chemin d'un fichier `fichier_chiffré` et qui écrit dans `fichier_chiffré` la version chiffrée.
# 
# - Tester cette fonction sur les fichiers `files/lorem.txt` puis `files/zadig.txt` avec des clés de votre choix.

# In[35]:


def chiffre_fichier(fichier, cle, fichier_chiffre):
    f_input = open(fichier, 'r')
    ligne1 = f_input.read()
    res = chiffre_cesar(ligne1, cle)
    f_input.close()
    
    f_output = open(fichier_chiffre, 'w')
    f_output.write(res)
    f_output.close()

chiffre_fichier("../07_Tableaux/files/lorem.txt", 3, "../09_Dictionnnaires/files/loremchiffre8.txt")


# ### Question 8 : Déchiffrement d'un fichier 
# - Ecrire une fonction qui prend en paramètres un fichier chiffré `fichier_chiffré` et la clé de chiffrement et qui écrit dans `fichier_déchiffré` ce qui a été déchiffré.
# 
# - Tester cette fonction sur les chiffrés des fichiers `files/lorem.txt` puis `files/zadig.txt` et les clés adaptées.
# 
# - Vérifier dans un terminal grâce à la fonction `diff` que la version déchiffrée des fichiers est bien la même que la version d'origine. 

# In[36]:


def dechiffre_fichier(fichier_chiffre, cle, fichier_dechiffre):
    f_input = open(fichier_chiffre, 'r')
    ligne1 = f_input.read()
    res = dechiffre_cesar(ligne1, cle)
    f_input.close()
    
    f_output = open(fichier_dechiffre, 'w')
    f_output.write(res)
    f_output.close()

dechiffre_fichier("../09_Dictionnnaires/files/loremchiffre8.txt", 3, "../09_Dictionnnaires/files/loremdechffre8.txt")

 
    
    

