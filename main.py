import os

ID = '100102'
# Pobierz ścieżkę do katalogu, w którym uruchomiono skrypt
base_path = os.getcwd()

# Przejdź po wszystkich folderach w bieżącym katalogu
for folder_name in os.listdir(base_path):
    folder_path = os.path.join(base_path, folder_name)

    # Sprawdź, czy to folder
    if os.path.isdir(folder_path):
        # Pobierz pliki w tym folderze
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

        # Posortuj pliki, aby mieć przewidywalną kolejność
        files.sort()

        # Zmieniaj nazwy plików
        for idx, filename in enumerate(files, start=1):
            ext = os.path.splitext(filename)[1]  # Zachowaj rozszerzenie
            new_name = f"{folder_name}_{ID}_{idx}{ext}"

            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_name)

            os.rename(old_path, new_path)
            print(f"{old_path} -> {new_name}")
