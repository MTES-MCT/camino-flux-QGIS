# Camino-flux-QGIS

> Plugin pour QGIS d'import des flux GeoJSON de [Camino](https://camino.beta.gouv.fr), le cadastre minier numérique ouvert

l'API de Camino expose des informations sur les titres miniers et autorisations sous forme de flux GeoJSON ([documentation](https://docs.camino.beta.gouv.fr/pages/Utilisation/04-flux.html)). 

Ce plugin simplifie l'import de ces flux GeoJSON dans QGIS.

---

## Installation

### Via le dépôt du Ministère

1. Configurer les dépôts d'extensions

Dans le menu _Extension_, sélectionner _Installer / Gérer les extensions_, puis l'onglet _Paramètres_, ajouter l'url suivante `http://piece-jointe-carto.developpement-durable.gouv.fr/NAT002/QGIS/plugins/plugins.xml`.

2. Installer et mettre à jour l'extension

Dans le menu _Extension_, sélectionner _Installer / Gérer les extensions, puis l'onglet _Tout_ et enfin _Rechercher_ `camino`.

### Manuellement

1. Télécharger et décomprésser le [zip du plugin](https://github.com/MTES-MCT/camino-flux-QGIS/releases).
2. Selon la version de QGIS utilisée, copier le contenu :
  - pour la version communautaire : `MonProfilAMoi\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\camino3`
  - pour la version QGIS packagée MTES : `C:\ProgramFiles\QGIS\profil\python\camino3`


---

## Utilisation

Le plugin est accessible via : 

- le menu _Extension / CAMINO (Titres MIniers) / CAMINO (Titres MIniers)_

![qgis extension screenshot](doc/camino-flux-qgis-extension.jpg)

- la barre d'outils 

![qgis toolsbar screenshot](doc/camino-flux-qgis-toolsbar.jpg)

### Interface

![camino plugin screenshot](doc/camino-flux-qgis.jpg)

Cliquer sur _Charger la couche_ pour importer les flux geojson et les charger dans une couche Vecteur QGIS.

#### Paramêtres

Les résultats peuvent être filtrés par : 

- types
- domaines
- statuts
- noms ou siret d'entreprise
- substances
- etc.

#### Authentification 

Les utilisateurs qui possèdent un compte sur Camino, peuvent se connnecter depuis le plugin et ainsi ainsi disposer d'accès restreint à certaines informations. 

Cliquer sur l'onglet _Connexion_.

---

## Documentation

Une documentation complète au format pdf est disponible [ici](https://github.com/MTES-MCT/camino-flux-QGIS/blob/master/doc/camino_doc.pdf)

---

## Crédits

### Production

- [La Fabrique Numérique, Ministère de la transition écologique et solidaire](https://www.ecologique-solidaire.gouv.fr/inauguration-fabrique-numerique-lincubateur-des-ministeres-charges-lecologie-et-des-territoires)

### Équipe

- Didier LECLERC, CMSIG développeur MTES/MCTRCT SG/SNUM/UNI/DRC
- Nicolas PETITOT, Développeur Camino, Appui métier pour Qgis

---

## Licence

Camino API, le cadastre minier numérique ouvert

[AGPL 3 ou plus récent](https://spdx.org/licenses/AGPL-3.0-or-later.html)

---           

## Technologies
- [Python 3.x]

---           

## Environnement
 - Version de QGIS 3.14 PI ( fonctionne en 3.x )
 - Qt 5.11.2 
 - OS Version Windows 10 (10.0)

## Suivi des anomalies
 - url : https://github.com/MTES-MCT/camino-flux-QGIS/issues    

---

## Structure des fichiers
```bash
.                        # `Racine où se trouve les sources .py`
│
├── doc                  # `documentation et flyer`
├── i18n                 # `fichiers des langues
└── icons                # `icones de l'application, menu, barre d'outils, IHM`
    └── metier           # `icones de la boite de dialogue de filtre`
    
.                        # `profil utilisateur windows`
│
└── camino3param         # `dossier par défaut création / lecture des fichiers *.par (urlcamino.par / logincaminocourriel.par)`
    └── requete          # `dossier par défaut de sauvegarde et de chargement des requetes (filtres)`
   
```
=================================================