# Mini-Bibliothèque — Gestion des prêts et retours

**Membres du groupe :**
- Hanane Rousafi
- Amal Jabbour
- Imane Hanane

**Module :** Programmation Python 2 — Pr. Yassin Eljakani
**Filière :** IA-2 | Université Ibn Zohr, Agadir
**Année universitaire :** 2025–2026

---

## Description du projet

Application de bureau permettant à un bibliothécaire de gérer une mini-bibliothèque :
catalogue des livres, enregistrement des prêts et retours, recherche, et export de rapport.
L'interface graphique est réalisée avec **customTkinter**.

---

## Installation

### Prérequis

- Python 3.10 ou supérieur
- pip

### Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## Lancement

```bash
python main.py
```

Si le fichier `data/bibliotheque.txt` est absent au premier lancement,
l'application démarre à vide et le crée automatiquement au premier enregistrement.

---

## Format des données

Fichier : `data/bibliotheque.txt`
Séparateur : `;`
Encodage : UTF-8
Première ligne : en-tête obligatoire

**Colonnes (ordre exact) :**

| Colonne      | Description                              | Exemple                 |
|--------------|------------------------------------------|-------------------------|
| titre        | Titre du livre                           | Le Petit Prince         |
| auteur       | Auteur du livre                          | Antoine de Saint-Exupéry|
| isbn         | Identifiant unique du livre              | 978-2070408504          |
| emprunteur   | Nom de l'emprunteur (vide si disponible) | Sara Bennani            |
| date_pret    | Date du prêt au format YYYY-MM-DD        | 2026-03-01              |
| date_retour  | Date du retour (vide si en cours)        | 2026-03-15              |
| statut       | `emprunté` ou `retourné`                 |  emprunté               |

**Exemple de lignes valides :**
```
titre;auteur;isbn;emprunteur;date_pret;date_retour;statut
Le Petit Prince;Saint-Exupéry;978-001;Sara Bennani;2026-03-01;;emprunté
1984;George Orwell;978-002;Ali Amrani;2026-02-01;2026-02-15;retourné
Dune;Frank Herbert;978-003;;;;retourné
```

---

## Fonctionnalités

- **Catalogue** : affichage de tous les livres avec leur statut (disponible / emprunté)
- **Ajouter un livre** : titre, auteur, ISBN obligatoires — doublon ISBN refusé
- **Enregistrer un prêt** : ISBN + emprunteur + date (auto si vide) — refusé si déjà emprunté
- **Marquer un retour** : ISBN + date (auto si vide) — incohérences de statut détectées et corrigées
- **Supprimer un livre** : uniquement si disponible
- **Rechercher** : par titre, auteur, emprunteur ou ISBN (insensible à la casse)
- **Rapport** : export dans `output/rapport.txt` de tous les prêts en cours
- **Persistance automatique** : chaque modification est sauvegardée immédiatement

---

## Structure du projet

```
mini_bibliotheque/
├── README.md
├── requirements.txt
├── main.py                  ← point d'entrée
├── src/
│   ├── __init__.py
│   ├── app.py               ← interface graphique (customTkinter)
│   └── core/
│       ├── __init__.py
│       ├── models.py        ← classes Livre et Pret
│       ├── storage.py       ← lecture / écriture fichier .txt
│       └── logic.py         ← règles métier (BiblioController)
├── data/
│   └── bibliotheque.txt     ← données persistantes
├── output/
│   └── rapport.txt          ← généré par l'application
├── tests/
│   └── self_check.py        ← tests unitaires
└── reports/
    ├── rapport_groupe.pdf
    └── rapport_individuel_NOM.pdf
```

---

## Gestion des erreurs

| Situation                        | Comportement                                           |
|----------------------------------|--------------------------------------------------------|
| Fichier absent au démarrage      | Démarrage à vide, création au 1er enregistrement       |
| Ligne mal formée dans le fichier | Ignorée avec message console, pas de crash             |
| Statut invalide dans le fichier  | Ligne ignorée avec message console                     |
| Champ obligatoire vide           | Message d'erreur rouge dans l'interface                |
| ISBN déjà existant               | Refus avec message explicite                           |
| Prêt sur livre déjà emprunté     | Refus avec message explicite                           |
| Retour sur livre déjà disponible | Refus avec message explicite                           |
| Incohérence statut/prêts         | Correction automatique + message à l'utilisateur       |

---

## Tests unitaires

```bash
python tests/self_check.py
```

Tous les tests doivent afficher `[OK]`.
