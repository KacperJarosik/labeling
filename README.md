# 🏷️ File Labeling - Sign Language Dataset

A simple Python script for automatically labeling files based on folder names, a manually set ID, and sequential numbering. Includes an additional script for quickly clearing folders of their contents.

## 📂 Repository Contents

- `main.py` – file labeling script
- `clear.py` – folder cleaning script
- `etykietowanie.rar` – archive with sample folders for testing

## ✅ Requirements

- Python **3.11.9**
- OS: **Windows 10 (64-bit)**
- Libraries used: **os** (standard library)

## ⚙️ How to Use

1. **Create folders** in the repo directory — the folder names will be used in the new file names.
2. **Place files** (images, videos, etc.) into the appropriate folders.
3. **Set the value of `ID`** in `main.py`, for example: `ID = '000022'`.
4. **Run `main.py`** from the directory containing your folders.
5. The files will be **renamed** using the following format:  
`[FOLDER_NAME]_[ID]_[NUMBER]`  
Example: `A_000022_1.jpg`, `B_000022_2.mp4`
6. Copy or move the labeled files to your dataset.  
⚠️ **Warning:** Do **not** run `clear.py` from an incorrect location — it may delete important files!
7. To **clean the folders**, run `clear.py` from the folder containing the subfolders to clean.
8. Repeat the process as needed, changing the `ID` value and folder contents.

## 🔁 Labeling Rule

The file names follow the structure:

`[FOLDER_NAME]_[MANUALLY SET ID]_[SEQUENTIAL NUMBER FOR SAME LABEL AND ID]`


## 🧹 Script Overview

### `main.py` – Labeling

- Iterates through folders in the current directory.
- Lists and sorts files inside each folder.
- Renames each file using folder name, fixed ID, and a sequential number.

### `clear.py` – Cleaning

- Deletes **all files** in subfolders (excluding `.git` directories).
- Prepares folders for re-use.

## 🖼️ Sample Data

The `etykietowanie.rar` archive includes example folders used for sign language labeling.

---

# 🏷️ Etykietowanie plików – Zbiór znaków języka migowego

Prosty skrypt w Pythonie do automatycznego etykietowania plików na podstawie nazw folderów, ręcznie ustawionego ID oraz numerów porządkowych. Zawiera również skrypt do szybkiego czyszczenia folderów z plików.

## 📂 Zawartość repozytorium

- `main.py` – skrypt do etykietowania
- `clear.py` – skrypt czyszczący foldery
- `etykietowanie.rar` – archiwum z przykładowymi folderami
## ✅ Wymagania

- Python **3.11.9**
- System: **Windows 10 (64-bitowy)**
- Biblioteki: tylko **os** (standardowa biblioteka Pythona)

## ⚙️ Instrukcja działania

1. **Utwórz foldery** w katalogu repozytorium – ich nazwy będą użyte do etykietowania.
2. **Umieść pliki** (np. zdjęcia, filmy) w odpowiednich folderach.
3. **Ustaw wartość `ID`** w `main.py`, np. `ID = '000022'`.
4. **Uruchom `main.py`** z folderu zawierającego Twoje foldery.
5. Pliki zostaną **przemianowane** zgodnie z formatem:  
`[NAZWA_FOLDERU]_[ID]_[NUMER]`  
Przykład: `A_000022_1.jpg`, `B_000022_2.mp4`
6. Skopiuj lub przenieś etykietowane pliki do swojego zbioru danych.
7. Aby **wyczyścić foldery**, uruchom `clear.py` w katalogu z folderami do wyczyszczenia.  
⚠️ **Uwaga:** Nie uruchamiaj `clear.py` w złym miejscu — może to doprowadzić do usunięcia ważnych danych!
8. Powtórz proces według potrzeb, zmieniając `ID` i zawartość folderów.

## 🔁 Zasada etykietowania

Format nazw plików:

'[NAZWA_FOLDERU]_[RĘCZNIE USTAWIONE ID]_[KOLEJNY NUMER DLA TYCH SAMYCH ETYKIET]'


## 🧹 Opis działania skryptów

### `main.py` – Etykietowanie

- Iteruje po folderach w bieżącej lokalizacji.
- Sortuje pliki w każdym folderze.
- Zmienia nazwy plików według ustalonego wzoru.

### `clear.py` – Czyszczenie

- Usuwa **wszystkie pliki** z podfolderów (z wyjątkiem `.git`).
- Przygotowuje foldery do ponownego użycia.

## 🖼️ Dane przykładowe

Archiwum `etykietowanie.rar` zawiera przykładowe foldery użyte do etykietowania znaków języka migowego.

