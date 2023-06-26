# Klasifikacija glasova (KCS)
Klasifikacija glasova iz zvučnog zapisa pomoću analize mel-kepstralnih koeficijenata

Potrebni alati: __Python 3__, __SPTK__

Potrebne _Python_ knjižnice: __PyDub__, __Levenshtein__, __NumPy__, __SciPy__, __Scikit-Learn__

## Upute
1. U folder **repoDB/lab_sm04** extractati _.lab_ datoteke
2. U folder **repoDB/wav_sm04** extractati _.wav_ datoteke
3. Pokretati redom skripte **1_split.py** do **4_generate_dataset.py**

**Napomena: **ocjena.py** se ne pokreće**

Za klasifikaciju korištenjem euklidske udaljenosti pokrenuti skriptu **5_udaljenost.py**

Za klasifikaciju korištenjem KNN algoritma poreknuti skriptu **6_knn.py**

Zamjena testnih datoteka se izvršava dodavanjem _.wav_ i _.lab_ datoteka unutar direktorija **repoDB/test_files/test_jedan_zapis/**

Za dodavanje novih testnih zapisa:
1. Dodati _.wav_ i _.lab_ datoteka unutar direktorija u **repoDB/test_files/test_jedan_zapis/**
2. Preimenovati _.wav_ datoteku u _wav_file.wav_ i _.lab_ datoteku u _transkript.lab_
3. Pokrenuti skriptu **6_knn.sh**

Za pokretanje klasifikacije 20% baze podataka potrebno je pokrenuti skriptu **7_knn.py**