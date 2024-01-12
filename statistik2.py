import pandas as pd

# load data ke dataframe (df)
df = pd.read_csv("data-kebakaran.csv")
df.head()

print (" 1. Filter kejadian kebakaran yang terjadi di bulan Maret: ")
kebakaran_maret = df[df['tanggal'].apply(lambda x: pd.to_datetime(x).month == 3)]
print(kebakaran_maret)
print()

print (" 2. Filter kejadian kebakaran yang nilai kerugiannya antara 50jt sampai 100jt: ")
kebakaran_50_100jt = df[(df['kerugian'] >= 50000000) & (df['kerugian'] <= 100000000)]
print(kebakaran_50_100jt)
print()

print ("3. Tampilkan/Filter 5 kejadian yang tingkat kerugiannya paling besar :")
kebakaran_top5 = df.nlargest(5, 'kerugian')
print(kebakaran_top5)
print()

print (" 4. Menggunakan groupby dan count, hitung banyaknya kejadian kebakaran per bulan:")
jumlah_kejadian_per_bulan = df.groupby(df['tanggal'].apply(lambda x: pd.to_datetime(x).month)).size().reset_index(name='jumlah_kejadian')
print(jumlah_kejadian_per_bulan)
print()

print("5. Menggunakan groupby dan sum, hitung jumlah kerugian akibat kebakaran per bulan:") 
total_kerugian_per_bulan = df.groupby(df['tanggal'].apply(lambda x: pd.to_datetime(x).month))['kerugian'].sum().reset_index(name='total_kerugian')
print(total_kerugian_per_bulan)
print()

print("6. Menggunakan groupby dan mean, hitung rata-rata kerugian akibat kebakaran per bulan:") 
rata_rata_kerugian_per_bulan = df.groupby(df['tanggal'].apply(lambda x: pd.to_datetime(x).month))['kerugian'].mean().reset_index(name='rata_rata_kerugian')
print(rata_rata_kerugian_per_bulan)
print()

print("7. Hitung banyaknya kejadian kebakaran yang disebabkan Listrik per bulan:")
kebakaran_listrik_per_bulan = df[df['penyebab'] == 'Listrik'].groupby(df['tanggal'].apply(lambda x: pd.to_datetime(x).month)).size().reset_index(name='jumlah_kejadian_listrik')
print(kebakaran_listrik_per_bulan)
print()

print("8. Hitung jumlah kerugian akibat kebakaran yang terjadi di kelurahan Kemayoran:")
kerugian_kemayoran = df[df['kelurahan'] == 'Kemayoran']['kerugian'].sum()
print("Jumlah kerugian akibat kebakaran di Kemayoran:", kerugian_kemayoran)
print()

print("9. Hitung rata-rata kerugian akibat kebakaran di bulan Juni dan Juli, di Pasar Rebo:")
rata_rata_kerugian_juni_juli_pasar_rebo = df[(df['tanggal'].apply(lambda x: pd.to_datetime(x).month in [6, 7])) & (df['kelurahan'] == 'Pasar Rebo')]['kerugian'].mean()
print(f"Rata-rata kerugian akibat kebakaran di Pasar Rebo pada bulan Juni dan Juli: {rata_rata_kerugian_juni_juli_pasar_rebo}")
print()

print("10. Menggunakan fungsi max, tampilkan nilai kerugian paling besar dari kejadian kebakaran per kelurahan:")
max_kerugian_per_kelurahan = df.groupby('kelurahan')['kerugian'].max().reset_index(name='max_kerugian')
print(max_kerugian_per_kelurahan)
print()
