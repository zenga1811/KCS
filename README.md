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

Zamjena testnih datoteka se izvršava promjenom varijable `test_dir` unutar skripte **6_knn.py**. 

Npr.
```python
test_dir = "test_files/test1/"
...
test_dir = "test_files/test2/"
...
test_dir = "test_files/test3/"
```

Za dodavanje novih testnih zapisa:
1. Dodati _.wav_ i _.lab_ datoteka unutar jednog od direktorija u **repoDB/test_files**
2. Preimenovati _.wav_ datoteku u _wav_file.wav_ i _.lab_ datoteku u _transkript.lab_
3. Pokrenuti skriptu **3_mel_coef_test.sh**
4. Pokrenuti skriptu **5_udaljenost.py** ili **6_knn.py**
