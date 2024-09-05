import re
from collections import defaultdict


input_file = 'C:\\Users\\emret\\OneDrive\\Masaüstü\\Yeni klasör\\matching_lines10.txt'
zararli_kelime = 'C:\\Users\\emret\\OneDrive\\Masaüstü\\Cyberwords.txt'
output_file = 'C:\\Users\\emret\\OneDrive\\Masaüstü\\10.txt'


with open(zararli_kelime, 'r', encoding='utf-8') as Zkelime:
    zararli_kelime_listesi = [line.strip().lower() for line in Zkelime]

# Kelime sayacı oluşturma
keyword_counts = defaultdict(int)


with open(input_file, 'r', encoding='utf-8') as iFile:
    content = iFile.read().lower()
    
    for keyword in zararli_kelime_listesi:
        # RegEx ile tüm eşleşmeleri bulma
        matches = re.findall(r'\b' + re.escape(keyword[:-1]) + r'\w*', content)
        keyword_counts[keyword] = len(matches)
#re.escape(keyword[:-1])--> son karakteri keser

with open(output_file, 'w', encoding='utf-8') as outFile:
    for keyword, count in keyword_counts.items():
        if count > 0:  # Sadece 0'dan büyük sayıları al
            output_line = f"{keyword}: {count}\n"
            print(output_line, end='')  # Ekrana yazdırma
            outFile.write(output_line)  # Dosyaya yazma

print(f"Kelime sayıları '{output_file}' dosyasına yazıldı.")
