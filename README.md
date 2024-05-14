# PSIiM

## INSTALACJA I URUCHOMIENIE
Poniższe instrukcje pozwolą na zainstalowanie projektu na Twoim komputerze:
1. Sklonuj repozytorium na swój komputer za pomocą komendy: ```git clone https://github.com/opti0/psiim.git```	
2. Uruchom Visual Studio Code z zainstalowanym rozszerzeniem do Pythona.
3. Otwórz w programie katalog z projektem.
4. Na klawiaturze wciśnij kombinację klawiszy ```CTRL + Shift + P``` i wybierz komendę ```Python: Create Enviroment```. Z listy dostępnych środowisk wybierz ```venv```, następnie wybierz interpreter. Gdy zostaniesz zapytany o plik z zależnościami wybierz ```psiim/requirements.txt```.
5. W terminalu wpisz komendę ```.psiim\.venv\Scripts\activate``` by aktywować środowisko wirtualne.
6. Aby uruchomić aplikację wpisz ````python .\main.py````.
7. Otwórz stronę http://127.0.0.1:5000 aby przetestować działanie aplikacji.

*UWAGA: Wszelkie zmiany w kodzie pythona trzeba zapisać (komenda ``CTRL + S``) i ponownie uruchomić aplikację (komenda `CTRL + C` w terminalu, a następnie ``python .\main.py``) aby zmiany weszły w życie.*
