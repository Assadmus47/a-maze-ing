*This project has been created as part of the 42 curriculum by elbarry and mkacemi*

---

## C'est quoi un labyrinthe ?

Un labyrinthe c'est une grille de cases avec des **murs** entre les cases. Tu rentres d'un côté et tu dois trouver la sortie.

Voilà un vrai labyrinthe 4x3 visuellement :

```
┌───┬───┬───┬───┐
│ E     │       │
├───┘   └───┬───┤
│       │       │
├───┬───┘   └───┤
│               S│
└───┴───┴───┴───┘
```

**E** = entrée, **S** = sortie. Les `─` et `│` c'est les murs.

---

## Zoom sur UNE cellule

Prends la cellule du milieu. Elle ressemble à ça :

```
        NORD
         ───
OUEST │  (2,1) │ EST
         ───
        SUD
```

Une cellule c'est juste **une case** avec **4 côtés possibles**. Chaque côté peut avoir un mur ou pas.

Cellule avec tous ses murs :
```
┌───┐
│   │
└───┘
```

Cellule sans mur au NORD et à l'EST :
```
    
│   
└───┘
```

---

## La grille entière avec les cellules

Voilà le même labyrinthe 4x3, mais cette fois je montre chaque cellule et ses coordonnées :

```
┌───┬───┬───┬───┐
│0,0│1,0│2,0│3,0│   ← ligne 0
├───┼───┼───┼───┤
│0,1│1,1│2,1│3,1│   ← ligne 1
├───┼───┼───┼───┤
│0,2│1,2│2,2│3,2│   ← ligne 2
└───┴───┴───┴───┘
```

Ça c'est **avant** que le DFS casse des murs. Toutes les cellules sont fermées.

**Après** que le DFS passe :

```
┌───┬───┬───┬───┐
│0,0  1,0│2,0  3,0│
│   ┌───┘ └───┤
│0,1  1,1│2,1  3,1│
├───┘   └───┐   │
│0,2  1,2  2,2  3,2│
└───┴───┴───┴───┘
```

Le DFS a cassé des murs entre certaines cellules pour créer des chemins.

---

## Ce qu'une cellule contient

Une cellule contient **juste un nombre** qui dit quels murs elle a.

Prenons la cellule **(1,0)** dans ce labyrinthe :

```
┌───┬───┬───┬───┐
│0,0  1,0│2,0  ...
```

La cellule (1,0) :
- Mur NORD → **OUI** (c'est le bord du labyrinthe)
- Mur EST → **OUI** (il y a un mur entre (1,0) et (2,0))
- Mur SUD → **NON** (on peut aller vers (1,1))
- Mur OUEST → **NON** (on peut aller vers (0,0))

En bits ça donne :
```
OUEST  SUD  EST  NORD
  0     0    1    1    =  0011  =  3
```

Donc dans la grille : `grille[0][1] = 3`

Et la cellule **(0,0)** :
- Mur NORD → OUI (bord)
- Mur EST → NON (chemin vers (1,0))
- Mur SUD → NON (chemin vers (0,1))
- Mur OUEST → OUI (bord)

```
OUEST  SUD  EST  NORD
  1     0    0    1    =  1001  =  9
```

Donc : `grille[0][0] = 9`

---

## La grille complète en chiffres

Ce labyrinthe 4x3 en mémoire ressemble à ça :

```
grille = [
  [9,  3,  6,  12],   ← ligne 0  (y=0)
  [5,  10, 5,  10],   ← ligne 1  (y=1)
  [12, 6,  12, 6 ]    ← ligne 2  (y=2)
]
```

Chaque chiffre = une cellule = ses murs encodés.

---

## Le lien avec tout le projet

```
config.txt dit WIDTH=4, HEIGHT=3
        ↓
on crée grille = [[15,15,15,15],[15,15,15,15],[15,15,15,15]]
        ↓
DFS change les 15 en d'autres chiffres (en cassant des murs)
        ↓
grille = [[9,3,6,12],[5,10,5,10],[12,6,12,6]]
        ↓
BFS lit la grille et trouve le chemin
        ↓
Affichage lit la grille et dessine les murs
        ↓
Output écrit les chiffres en hex dans maze.txt
```

---

C'est plus clair maintenant ? Tu veux qu'on aille plus loin sur les bits ou tu veux qu'on passe à comment coder la classe `Maze` ? 🎯

## BFS Maze.generate:

random.seed(seed)
stack = []
visited = set()
visited.add((0,0))
stack.append((0,0))

while stack:                              ← début boucle
    regarder cellule en haut de stack
    trouver voisins valides non visités
    choisir un voisin au hasard
    casser le mur
    marquer visité + push dans stack
    si pas de voisin → pop             ← fin boucle

nb voisin valide:
1. Il est dans les limites de la grille
2. Il n'est pas dans visited

---

# Stack en python:

## créer
stack = []

## push (ajouter en haut)
stack.append(element)

## pop (enlever le dernier)
stack.pop()

## regarder le dernier sans l'enlever
stack[-1]

## vérifier si vide
len(stack) == 0

---

# set en Python:

## créer
visited = set()

## ajouter
visited.add((1, 0))

## vérifier si dedans
(1, 0) in visited   # True
(2, 0) in visited   # False

## taille
len(visited)

# condition pour pattern
WIDTH < 9   (7 pour le pattern + 1 marge de chaque côté)
HEIGHT < 7  (5 pour le pattern + 1 marge en haut et en bas)

█░█░███
█░█░░░█
███░███
░░█░█░░
░░█░███

WIDTH  = nombre de colonnes  (horizontal, gauche → droite)
HEIGHT = nombre de lignes    (vertical, haut → bas)

---

## BFS (trouver le plus court chemin)

Maintenant que le labyrinthe est généré, il faut trouver le chemin entre l’entrée et la sortie.

On utilise **BFS (Breadth-First Search)**.

Contrairement au DFS :

* DFS explore en profondeur
* BFS explore **niveau par niveau**

👉 Donc BFS trouve **le chemin le plus court**

---

### Principe

```text
partir de l'entrée
↓
explorer tous les voisins accessibles
↓
continuer en largeur
↓
atteindre la sortie
↓
reconstruire le chemin
```

---

### Structure utilisée

```python
queue = deque([start])
visited = {start}
came_from = {}
```

* `queue` → cellules à explorer
* `visited` → éviter les doublons
* `came_from` → permet de reconstruire le chemin

---

### Reconstruction du chemin

On part de la sortie et on remonte :

```python
current = goal

while current != start:
    current = came_from[current]
    path.append(current)
```

Puis on inverse :

```python
path.reverse()
```

---

### Important

Le chemin est stocké sous deux formes :

```python
self.path_list = path   # ordre du chemin
self.path = set(path)   # affichage rapide
```

👉 La liste est nécessaire pour garder l’ordre
👉 Le set est utilisé pour le display

---

## Parsing (lecture du config.txt)

Le programme lit un fichier :

```text
WIDTH=10
HEIGHT=8
ENTRY=0,0
EXIT=9,7
PERFECT=True
SEED=8
```

---

### Étapes

```text
ouvrir le fichier
↓
lire ligne par ligne
↓
split avec "="
↓
stocker dans un dictionnaire
```

---

### Validation

On vérifie :

* WIDTH et HEIGHT présents
* ENTRY et EXIT présents
* PERFECT présent
* types corrects (int, bool)
* coordonnées dans la grille
* ENTRY ≠ EXIT

---

### Gestion d’erreurs

Le programme ne crash pas :

```text
WIDTH=abc → erreur
ENTRY=100,100 → hors limites
ligne sans "=" → erreur
```

On utilise :

```python
try:
    ...
except:
    ...
```

---

## Output file (écriture du résultat)

Le programme génère un fichier :

```text
HEX GRID

ENTRY
EXIT
PATH
```

---

### Exemple

```text
D391793953
BAE852C47A
AAFAFAFFFA
...

0,0
9,7
ESSSSSEESSEEEEEE
```

---

### Écriture de la grille

Chaque cellule est convertie en hex :

```python
format(cell, "X")
```

---

### Conversion du chemin

Le chemin BFS :

```python
[(0,0),(1,0),(1,1)]
```

devient :

```text
E S
```

---

### Logique

```python
dx = x2 - x1
dy = y2 - y1
```

* `dx = 1` → E
* `dx = -1` → W
* `dy = 1` → S
* `dy = -1` → N

---

## Organisation finale du programme

```text
config.txt
↓
parsing
↓
generate (DFS)
↓
solve (BFS)
↓
write_output
↓
display
```

---

## Important

Chaque fois que le labyrinthe est régénéré :

```text
generate → solve → write_output
```

👉 Le fichier output est toujours à jour

---

## Résumé

* DFS → génère le labyrinthe
* BFS → trouve le plus court chemin
* parsing → lit et valide les données
* output → écrit le résultat
* set + list → performance + ordre

---