# src/utils/word_counter.py
"""
WORD COUNTER: Menghitung kata-kata yang sering muncul di setiap kategori

Ide: Beberapa kata lebih sering muncul di laporan kekerasan seksual
- "diperkosa" sering di laporan kekerasan
- "halo" bisa di laporan apapun

Kita akan menghitung ini!
"""

from collections import defaultdict


class WordCounter:
    """
    Kelas untuk menghitung kata-kata per kategori
    """
    
    def __init__(self):
        # Dictionary untuk menyimpan: {label: {word: count}}
        # Contoh: {'assault': {'diperkosa': 5, 'dipukul': 3}}
        self.word_counts = defaultdict(lambda: defaultdict(int))
        self.total_words_per_label = defaultdict(int)
        self.vocab = set()  # Kumpulan semua kata unik
    
    def add_words(self, label, words):
        """
        Tambahkan kata-kata ke dalam counter
        
        Args:
            label (str): Kategori (assault, harassment, dll)
            words (list): Daftar kata-kata
            
        Contoh:
            >>> counter = WordCounter()
            >>> counter.add_words('assault', ['saya', 'diperkosa'])
        """
        for word in words:
            self.word_counts[label][word] += 1
            self.total_words_per_label[label] += 1
            self.vocab.add(word)
            print(f"  ➕ {label}: '{word}'")
    
    def get_word_count(self, label, word):
        """
        Ambil jumlah berapa kali kata muncul di kategori tertentu
        
        Args:
            label (str): Kategori
            word (str): Kata
            
        Returns:
            int: Berapa kali kata muncul
            
        Contoh:
            >>> counter.get_word_count('assault', 'diperkosa')
            5
        """
        return self.word_counts[label][word]
    
    def print_report(self):
        """Print laporan kata-kata yang dihitung"""
        print("\n" + "=" * 60)
        print("📊 LAPORAN KATA-KATA")
        print("=" * 60)
        
        print(f"\n🔤 Total kata unik: {len(self.vocab)}")
        print(f"   Kata-kata: {sorted(list(self.vocab))}")
        
        print(f"\n📋 Total kata per kategori:")
        for label, count in self.total_words_per_label.items():
            print(f"   - {label}: {count} kata")
        
        print(f"\n📈 Kata-kata per kategori:")
        for label in self.word_counts.keys():
            print(f"\n   [{label}]")
            for word, count in sorted(self.word_counts[label].items(), key=lambda x: x[1], reverse=True):
                print(f"      - '{word}': {count}x")


# TEST
if __name__ == "__main__":
    print("=" * 60)
    print("TEST WORD COUNTER")
    print("=" * 60)
    
    counter = WordCounter()
    
    # Simulasi: data training (sudah dibersihkan dan di-tokenize)
    print("\n📥 Menambahkan kata-kata:")
    
    # Kategori: assault (kekerasan)
    print("\n🔴 [assault]")
    counter.add_words('assault', ['saya', 'diperkosa', 'kemarin'])
    counter.add_words('assault', ['dia', 'diperkosa', 'saya'])
    
    # Kategori: harassment (pelecehan)
    print("\n🟡 [harassment]")
    counter.add_words('harassment', ['dia', 'menyentuh', 'saya', 'tanpa', 'izin'])
    counter.add_words('harassment', ['dia', 'mengganggu', 'terus'])
    
    # Kategori: false_report (laporan palsu)
    print("\n🟢 [false_report]")
    counter.add_words('false_report', ['halo', 'apa', 'kabar'])
    
    # Print report
    counter.print_report()
