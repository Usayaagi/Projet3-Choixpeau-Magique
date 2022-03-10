importer csv
 à partir de maths importer sqrt
 à partir d' une importation aléatoire randint

avec  open ( "Caracteristiques_des_persos.csv" , mode = 'r' , encoding = 'utf-8' )  as f : 
    test_reader = csv . DictReader ( f , delimiter = ';' ) 
    élèves =  [ { key : valeur pour key , valeur dans element . items ( ) }  pour l' élément danstest_reader ] 
    élèves =  [ { key : valeur pour key , valeur dans element . éléments ( ) }  pour élément dans élèves ]

for index in  range ( len ( élèves ) )  : 
    élèves [ index ] [ 'Courage' ]  =  int ( élèves [ index ] [ 'Courage' ] ) 
    élèves [ index ] [ 'Ambition' ]  =  int ( élèves [ index ] [ 'Ambition' ] ) 
    élèves [ index ] ['Intelligence' ]  =  int ( élèves [ index ] [ 'Intelligence' ] ) 
    élèves [ index ] [ 'Bon' ]  =  int ( élèves [ index ] [ 'Bon' ] ) 
    élèves [ index ] [ 'Id' ]  = index +  1

avec  open ( "Houses.csv" , mode = 'r' , encoding = 'utf-8' )  as f : 
    test_reader = csv . DictReader ( f , delimiter = ';' ) 
    maisons =  [ { key : valeur pour key , valeur dans element . items ( ) }  pour l' élément dans test_reader ]
    maisons =  [ { clé : valeur de la clé , valeur de l'élément . items ( ) }  pour élément dans maisons ]

for index in  range ( len ( maisons ) )  : 
    maisons [ index ] [ 'Courage' ]  =  int ( maisons [ index ] [ 'Courage' ] ) 
    maisons [ index ] [ 'Ambition' ]  =  int ( maisons [ index ] [ 'Ambition' ] ) 
    maisons [ index ] ['Intelligence' ]  =  int ( maisons [ index ] [ 'Intelligence' ] ) 
    maisons [ index ] [ 'Bien' ]  =  int ( maisons [ index ] [ 'Bien' ] ) 
    maisons [ index ] [ 'Id' ]  = index +  1

def  distance ( profil1 , profil2 , methode = 'euclidienne' ) :
    
    """"
    cette fonction permet de définir une distance entre deux profils fournis.
    
    entrée : deux profils sous forme de dictionnaire\
    et la méthode utilisée, ici euclidienne.
    
    sortie : la distance entre les deux profils.
    
    """
    
    return sqrt ( ( profil1 [ 'Courage' ]  - profil2 [ 'Courage' ] )  **  2 
                +  ( profil1 [ 'Ambition' ]  - profil2 [ 'Ambition' ] )  **  2  
                +  ( profil1 [ 'Intelligence' ]  - profil2 [ 'Intelligence' ] )  **  2  
                +  ( profil1 [ 'Bien' ]  - profil2[ 'Bon' ] )  **  2 )

def  ajout_distances ( onglet , profil_inconnu ) :
    
    """
    
    cette fonction permet d'ajouter les distances entre un profil d'une liste\
    et un profil inconnu.
    
    entrée : liste de profils avec différentes caractéristiques et un profil inconnu.
    
    sortie : la nouvelle liste créée contenant les distances entre les deux profils.
    
    """
    
    pour l' élément dans l'onglet : 
        élément [ 'Distance' ]  = distance ( profil_inconnu , élément ) 
    return tab

name =  str ( input ( 'Name : ' ) ) 
courage =  int ( input ( 'Courage : ' ) ) 
ambition =  int ( input ( 'Ambition : ' ) ) 
intelligence =  int ( input ( 'Intelligence : ' ) ) 
good =  int ( entrée ( 'Bien : ' ) )
    
test =  { 'Nom' : nom ,  'Courage' : courage ,  'Ambition' : ambition , \
             'Intelligence' : intelligence ,  'Bon' : bon } 
élèves = ajout_distances ( élèves , test ) 
maisons = ajout_distances ( maisons , test ) 
print ( "liste des élèves et de leurs caractéristiques + leurs distances avec toi : " ,élèves ) 
print ( ) 
print ( " liste des maisons et de leurs caractéristiques + leurs distances avec ton profil : " \
           , maisons ) 
print ( )
    
k =  5

élèves_voisins =  sorted ( élèves , key = lambda x : x [ 'Distance' ] ) 
print ( "tes 5 élèves plus proches voisins : " , élèves_voisins [ : k ] ) 
print ( ) 
maisons_voisines =  sorted ( maisons , key = lambda x : x [ 'Distance' ] ) 
imprimer ("tes 5 maisons plus proches voisines : " , maisons_voisines [ : k ] ) 
imprimer ( )
    

def modèle ( onglet ) :
    
    """"
    
    cette fonction permet d'attribuer une maison lorsqu'on lui fournit\
    les 5 plus proches voisins d'un profil d'élève cible.
    
    entrée : profil d'élève cible et ses 5 plus proches voisins
    sortie : maison attribuée
    
    """
    
    maisons =  { } 
    for maisons_voisines in tab : 
        if maisons_voisines [ 'House' ]  in maisons : 
            maisons [ maisons_voisines [ 'House' ] ]  +=  1 
        else : 
            maisons [ maisons_voisines [ 'House' ] ]  =  1 
    print ( maisons ) 
    maximum =  0 
    pour maison , nbdans les maisons . items ( ) : 
        si nb > maximum : 
            maximum = nb
            top_maison = maison
     retour top_maison

print ( "votre maison : " , modèle ( maisons_voisines [ : k ] ) )
