import os

# Ścieżka do katalogu, w którym uruchomiono skrypt
base_path = os.getcwd()

# Iteruj po wszystkich elementach w katalogu głównym
for folder_name in os.listdir(base_path):
    folder_path = os.path.join(base_path, folder_name)

    # Sprawdź, czy to folder (i nie bieżący katalog)
    if os.path.isdir(folder_path):
        # Iteruj po wszystkich plikach i folderach wewnątrz tego folderu
        for root, dirs, files in os.walk(folder_path, topdown=False):
            # Usuń wszystkie pliki
            for file in files:
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Usunięto plik: {file_path}")
