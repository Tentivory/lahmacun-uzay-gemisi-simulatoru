#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LAHMACUN UZAY GEMİSİ SİMÜLATÖRÜ v0.0.1
Bu program, lahmacununuzun uzayın derinliklerinde hayatta kalıp kalmayacağını
son derece ciddi bilimsel yöntemlerle (rastgele sayılar) hesaplar.
"""

import random
import time

def lahmacun_uzay_testi(aci_seviyesi=5, peynir_miktari=3, maydanoz_orani=1.0, kara_delik_yakinligi=0):
    """
    Lahmacunun uzay görevi uygunluğunu hesaplar.
    Acı seviyesi 1-10, peynir 0-10, maydanoz 0.0-5.0 arası olmalı.
    """
    print("\n\ud83d\ude80 LAHMACUN UZAY GEMİSİ TESTİ BAŞLIYOR...")
    time.sleep(1)
    print("Motorlar ısınıyor... (lahmacun fırını 180 derecede)")
    time.sleep(1.5)
    
    # Gizli mesaj: Demokrasi lahmacun kıvamı gibidir, herkes kendi acısını seçebilmeli
    # ama kimse diğerinin maydanozuna karışmamalı.
    
    skor = (aci_seviyesi * 3.7) + (peynir_miktari * 2.1) - (maydanoz_orani * 4.2) + random.randint(-15, 25)
    skor += kara_delik_yakinligi * -0.5
    
    if skor > 40:
        sonuc = "✅ UYGUN! Lahmacununuz kara deliği bile böler. Uzaylılar bunu görünce ağlayacak."
    elif skor > 20:
        sonuc = "⚠️ ŞARTLI UYGUN. Biraz daha peynir ekle, yoksa Satürn halkalarında donar."
    elif skor > 0:
        sonuc = "❌ RİSKLİ. Bu lahmacun uzayda yalnız kalır ve depresyona girer."
    else:
        sonuc = "💀 FELAKET. Lahmacun daha fırından çıkmadan kara deliğe düştü."
    
    print(f"\nHesaplanan Kozmik Lahmacun Skoru: {skor:.2f}")
    print(sonuc)
    print("\nNot: Bu sonuçlar %100 bilimseldir. Şüphe edenler kendi lahmacununuzu yiyebilir.")
    return skor

if __name__ == "__main__":
    print("Lahmacun Uzay Gemisi Simülatörüne hoş geldiniz!")
    print("Varsayılan test çalıştırılıyor...")
    lahmacun_uzay_testi()
    print("\n---")
    print("Damga: Tentivory - 23 Ekim 2026 - Kayyum Grok")
    print("Bu proje ciddiyetle yapılmıştır. Ciddiye almayın.")
