# Override – Projet d’Exploitation Binaire (École 42)

Projet de groupe réalisé avec [Valentin mondor](https://github.com/vmondor)

## 📌 Description

**Override** est un projet d’exploitation binaire axé sur l’analyse et l’exploitation d’une application vulnérable. L’objectif principal est d’identifier une vulnérabilité de type buffer overflow, comprendre son fonctionnement au niveau assembleur et injecter un shellcode ou rediriger le flux d’exécution pour obtenir le flag de l’utilisateur suivant.

Le projet met l’accent sur le reverse-engineering, la manipulation de la mémoire (pile/heap), la construction de payloads et les protections modernes (ASLR, NX, Canary…).

Le projet met en pratique des notions de **reverse engineering**, de **buffer overflow**, de **gestion mémoire** et d’**exploitation de failles système**.

---

## 🎯 Objectifs pédagogiques

- Comprendre et exploiter un buffer overflow réel.
- Étudier le binaire au niveau assembleur et identifier les points d’injection.
- Construire et tester des shellcodes.
- Contourner ou tirer parti des protections (NX, ASLR, canary) selon le contexte.
- Automatiser l’exploitation avec des scripts (génération de payloads).

---

## 🛠️ Environnement

- Machine Linux (local via SSH).
- Un exécutable vulnérable à analyser et exploiter.
- Pas d’accès root requis (objectif : obtenir le flag de l’utilisateur cible).
- Travail en ligne de commande / terminal.

---

## 🔧 Outils utilisés

- `gdb` (debugging interactif)
- `objdump`, `strings` (analyse statique)
- `ltrace` (traçage des appels)
- `python` (scripts d’exploitation et génération de payloads)
- `ghidra`, `hex-ray` (décompilation)

---

---

## 📚 Ressources utiles

- [GDB Cheat Sheet](https://darkdust.net/files/GDB%20Cheat%20Sheet.pdf)
- [Buffer Overflow 101](https://exploit.education/)
- [Ghidra, Hex-ray](https://dogbolt.org/)
- [HackTricks – Binary Exploitation](https://book.hacktricks.xyz/)

---

## 👨‍💻 Auteur

Projet réalisé dans le cadre du cursus cybersécurité de l’[École 42](https://42.fr/).
