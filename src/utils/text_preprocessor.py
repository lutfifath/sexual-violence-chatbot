# src/utils/text_preprocessor.py
"""
FILE PALING DASAR: Membersihkan Text

Tujuan: Ubah text kotor menjadi text bersih yang siap dianalisis

Contoh:
INPUT:  "Saya DIPERKOSA!!! Tolong!!! 😭😭😭"
OUTPUT: ["saya", "diperkosa", "tolong"]
"""

import re

def clean_text(text):
    """
    Bersihkan text dari simbol, angka, dan spasi berlebih
    
    Args:
        text (str): Text yang ingin dibersihkan
        
    Returns:
        str: Text yang sudah bersih
        
    Contoh:
        >>> clean_text("Saya DIPERKOSA!!!")
        'saya diperkosa'
    """
    # 1. Ubah ke lowercase (huruf kecil)
    text = text.lower()
    print(f"  [1] Lowercase: '{text}'")
    
    # 2. Hapus simbol khusus (!, @, #, dll)
    # Regex [^a-z0-9\s] artinya: hapus semua karakter yang BUKAN huruf a-z, angka 0-9, atau spasi
    text = re.sub(r'[^a-z0-9\s]', '', text)
    print(f"  [2] Hapus simbol: '{text}'")
    
    # 3. Hapus spasi berlebih (multiple spaces jadi single space)
    text = re.sub(r'\s+', ' ', text)
    print(f"  [3] Hapus spasi berlebih: '{text}'")
    
    # 4. Strip spasi di awal dan akhir
    text = text.strip()
    print(f"  [4] Strip spasi awal/akhir: '{text}'")
    
    return text


def tokenize(text):
    """
    Pisahkan text menjadi kata-kata (tokens)
    
    Args:
        text (str): Text yang ingin dipotong
        
    Returns:
        list: Daftar kata-kata
        
    Contoh:
        >>> tokenize("saya diperkosa tolong")
        ['saya', 'diperkosa', 'tolong']
    """
    # Split by spasi
    words = text.split(' ')
    print(f"  [tokenize] Hasil split: {words}")
    
    # Hapus kata kosong
    words = [w for w in words if len(w) > 0]
    print(f"  [tokenize] Hapus kata kosong: {words}")
    
    return words


def preprocess(text):
    """
    Kombinasi: bersihkan text + tokenize
    
    Args:
        text (str): Text asli
        
    Returns:
        list: Daftar kata-kata yang sudah bersih
        
    Contoh:
        >>> preprocess("Saya DIPERKOSA!!! Tolong!!!")
        ['saya', 'diperkosa', 'tolong']
    """
    print(f"\n📝 Preprocessing: '{text}'")
    cleaned = clean_text(text)
    tokens = tokenize(cleaned)
    print(f"✅ Hasil akhir: {tokens}\n")
    return tokens
