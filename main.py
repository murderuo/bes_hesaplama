# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
baslangic_tutari=int(input('bes primini giriniz:'))
yillik_artis_miktari=int(input('yıllık artış miktarını giriniz:'))
yillik_getiri_miktari=int(input('yıllık getiri miktari:'))
degerlendirilecek_sure=int(input('süreyi giriniz:'))

aylik_getiri=yillik_getiri_miktari/12
birikim=0
birikim_getirisi=0
toplam_birikim=0
for ay in range(1,degerlendirilecek_sure):
    birikim+=baslangic_tutari
    birikim_getirisi=birikim*aylik_getiri/100
    toplam_birikim+=birikim_getirisi
    if ay%12==0:
        #aylik_getiri+=aylik_getiri*yillik_artis_miktari/100 aylık getiri oranı süre boyunca sabit tutuldu
        baslangic_tutari+=baslangic_tutari*yillik_artis_miktari/100
        print(f'''ödenen toplam pirim:{birikim:.2f}
                  prim getirisi:{birikim_getirisi:.2f}
                  prim miktarı:{baslangic_tutari:.2f}
                  aylık getiri oranı:{aylik_getiri}''')
    
print(f'Toplam ödenen prim + prim getirisi: {toplam_birikim:.2f}')
