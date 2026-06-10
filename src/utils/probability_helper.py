# src/utils/probability_helper.py
"""
PROBABILITAS: Menghitung kemungkinan sesuatu terjadi

Rumus: P(A) = (Jumlah A terjadi) / (Total kejadian)

Contoh:
- Jika dari 100 laporan, 20 adalah kekerasan seksual
- Maka P(kekerasan seksual) = 20/100 = 0.2 = 20%
"""

def calculate_probability(count, total):
    """
    Hitung probabilitas
    
    Args:
        count (int): Berapa banyak kejadian yang ingin dihitung
        total (int): Total semua kejadian
        
    Returns:
        float: Probabilitas (0.0 - 1.0)
        
    Contoh:
        >>> calculate_probability(20, 100)
        0.2  # 20%
    """
    if total == 0:
        return 0.0
    
    probability = count / total
    print(f"  P({count} dari {total}) = {count}/{total} = {probability:.4f} ({probability*100:.1f}%)")
    return probability


def calculate_multiple_probabilities(data):
    """
    Hitung probabilitas untuk multiple items
    
    Args:
        data (dict): Dictionary dengan format {label: count}
        
    Returns:
        dict: Dictionary dengan format {label: probability}
        
    Contoh:
        >>> data = {
        ...     'assault': 20,
        ...     'harassment': 30,
        ...     'safe': 50
        ... }
        >>> calculate_multiple_probabilities(data)
        {'assault': 0.2, 'harassment': 0.3, 'safe': 0.5}
    """
    print("\n📊 Menghitung probabilitas:")
    total = sum(data.values())
    
    probabilities = {}
    for label, count in data.items():
        prob = calculate_probability(count, total)
        probabilities[label] = prob
    
    print()
    return probabilities


# CONTOH PRAKTIS: Mari kita bayangkan data kekerasan seksual di kampus
if __name__ == "__main__":
    print("=" * 60)
    print("CONTOH: Probabilitas Jenis Laporan di Kampus")
    print("=" * 60)
    
    # Data laporan yang masuk
    laporan_data = {
        'assault': 15,          # Serangan/pemerkosaan
        'harassment': 25,       # Pelecehan
        'discrimination': 10,   # Diskriminasi
        'false_report': 5,      # Laporan palsu
    }
    
    print(f"\n📋 Total laporan: {sum(laporan_data.values())}")
    print("Breakdown:")
    for label, count in laporan_data.items():
        print(f"  - {label}: {count}")
    
    # Hitung probabilitas
    print("\n" + "=" * 60)
    prob = calculate_multiple_probabilities(laporan_data)
    
    print("✅ Hasil Probabilitas:")
    for label, p in prob.items():
        print(f"  - {label}: {p:.4f} ({p*100:.1f}%)")
