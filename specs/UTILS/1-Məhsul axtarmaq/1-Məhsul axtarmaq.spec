# 1-Məhsul axtarmaq
//
    * Chrome'u aç, Sistemin əsas səhifəsini aç
    * Uİ obyektlərin locatorları load et - Məhsul axtarmaq
    
## 1.1-Məhsul axtarmaq-Samovar
    // Test mərhələ 1: SETUP = quraşdırma
    
    // Test mərhələ 2: EXERCİSE = icra etmək
    * MP3 oyna: "BU SİSTEMİN-Tipik bir məhsulu axtar qutusunda yazıb, və axtarıram"
    * Obyektə vur (XPathi=bu dəyişgənin dəyəri): "Məhsul axtar xanası"
    
    * Mətn yaz, klaviatura ilə: "Samovar"
    
    * MP3 oyna: "Axtar düyməsinə vururam"
    * Obyektə vur (XPathi=bu dəyişgənin dəyəri): "Axtar düyməsi"
    // Test mərhələ 3: VERİFY = yoxlamaq
    * MP3 oyna: "BU SİSTEMİN-Ekrandakı bütöv məhsulların adında, axtarılan kəlmənin olduğunu yoxlayıram"
    
    * YOXLA: Ekrandakı bütöv məhsulların adında bu yazı olmalı: "Samovar"
    
    // Test mərhələ 4: TEARDOWN = təmizləmək
    // Çünki bu test sistemdə heç dəyişiklilk etməyib, heç təmizlənməyə ehtiyac yox
    
## 1.2-Məhsul axtarmaq-Ayaqqabı
    //
    * Obyektə vur (XPathi=bu dəyişgənin dəyəri): "Məhsul axtar xanası"
    * Mətn yaz, klaviatura ilə: "Ayaqqabı"
    * Obyektə vur (XPathi=bu dəyişgənin dəyəri): "Axtar düyməsi"
    * YOXLA: Ekrandakı bütöv məhsulların adında bu yazı olmalı: "Ayaqqabı"
    
## 1.6.1 bir ve ya daha artiq mehsulu sebete elave etmek
    
    * Obyektə vur (XPathi=bu dəyişgənin dəyəri): "Məhsul axtar xanası"
    * Mətn yaz, klaviatura ilə: "blender"
    * Obyektə vur (XPathi=bu dəyişgənin dəyəri): "Axtar düyməsi"
    * Obyektə 2-KLIK vur (XPath ilə): "//div[@id='ajax-products']//div[1]//div[1]//div[1]//div[2]//a[1]//img[1]"
    * Obyektə 2-KLIK vur (XPath ilə): "(//button[contains(text(),'Səbətə əlavə et')])[1]"
    * Obyektə vur (XPathi=bu dəyişgənin dəyəri): "Məhsul axtar xanası"
    * Mətn yaz, klaviatura ilə: "blender"
    * Obyektə vur (XPathi=bu dəyişgənin dəyəri): "Axtar düyməsi"
    * Obyektə 2-KLIK vur (XPath ilə): "/html[1]/body[1]/div[4]/div[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[2]/a[1]/img[1]"
    * Obyektə 2-KLIK vur (XPath ilə): "(//button[contains(text(),'Səbətə əlavə et')])[1]"
    * Obyektə vur (XPath ilə): "//i[@class='navbar-tool-icon czi-cart']"
    * YOXLA: obyekt ekranda OLDUĞUNU (XPath ilə): "(//img[@alt='Product'])[3]"; tapilsa_ses="Mətn tapıldı"; tapilmazsa_ses="Mətn tapılmadı"
    * Obyektə vur (XPath ilə): "//div[@class='media-header d-flex justify-content-center align-items-center mr-2']//img[@alt='Product']"
    * Obyektə vur (XPath ilə): "(//button[normalize-space()='+'])[1]"
    * Obyektə vur (XPath ilə): "(//button[contains(text(),'Səbətə əlavə et')])[1]"
    * Chrome'u bağla
    
## 1.6.2 bir markaya girdikden sonra orada qiymet araliginin yoxlanmasi
    
    * Obyektə vur (XPathi=bu dəyişgənin dəyəri): "Məhsul axtar xanası"
    * Mətn yaz, klaviatura ilə: "blender"
    * Obyektə vur (XPathi=bu dəyişgənin dəyəri): "Axtar düyməsi"
    * Obyektə vur (ID ilə): "min_price"
    * Cari xananı təmizlə
    * Mətn yaz, klaviatura ilə: "75"
    * Obyektə vur (ID ilə): "max_price"
    * Cari xananı təmizlə
    * Mətn yaz, klaviatura ilə: "1500"
    * Obyektə vur (XPath ilə): "//div[@class='cz-sidebar-body pb-0']//button[@class='btn btn-primary btn-block']"
    * "10" saniyə gözlə "mesaj"
    
    // Endirim olunanda kohne qiymeti nezere alir
    
## 1.7 Girisin yoxlanilmasi
    
    * Obyektə vur (XPath ilə): "//i[@class='navbar-tool-icon czi-user']"
    * Obyektə vur (XPath ilə): "/html[1]/body[1]/header[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/a[1]"
    * Obyektə vur (ID ilə): "si-email"
    * Mətn yaz, klaviatura ilə: "balasef2601@gmail.com"
    * Obyektə vur (ID ilə): "si-password"
    * Mətn yaz, klaviatura ilə: "Aa123456"
    * Obyektə vur (XPath ilə): "/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/form[1]/button[1]"
    * "3" saniyə gözlə
    
## 1.7.1  Wishlist-in yoxlanilmasi
    //loginden sonra sehife yenilenmir
    * Obyektə vur (XPath ilə): "//i[@class='navbar-tool-icon czi-user']"
    * Obyektə vur (XPath ilə): "/html[1]/body[1]/header[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/a[1]"
    * Obyektə vur (ID ilə): "si-email"
    * Mətn yaz, klaviatura ilə: "balasef2601@gmail.com"
    * Obyektə vur (ID ilə): "si-password"
    * Mətn yaz, klaviatura ilə: "Aa123456"
    * Obyektə vur (XPath ilə): "/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/form[1]/button[1]"
    * "3" saniyə gözlə
    * Obyektə vur (XPath ilə): "//a[@class='navbar-brand d-none d-sm-block mr-3 flex-shrink-0 tab-logo']//img[@alt='Hamisiburada Shop Azərbaycan']"
    * Obyektə vur (XPath ilə): "//a[@class='navbar-brand d-none d-sm-block mr-3 flex-shrink-0 tab-logo']//img[@alt='Hamisiburada Shop Azərbaycan']"
    * Obyektə vur (XPath ilə): "//a[@class='navbar-brand d-none d-sm-block mr-3 flex-shrink-0 tab-logo']//img[@alt='Hamisiburada Shop Azərbaycan']"
    * Obyektə vur (XPath ilə): "//a[@class='navbar-brand d-none d-sm-block mr-3 flex-shrink-0 tab-logo']//img[@alt='Hamisiburada Shop Azərbaycan']"
    * Obyektə vur (XPath ilə): "//a[@class='navbar-brand d-none d-sm-block mr-3 flex-shrink-0 tab-logo']//img[@alt='Hamisiburada Shop Azərbaycan']"
    * Obyektə vur (XPathi=bu dəyişgənin dəyəri): "Məhsul axtar xanası"
    * Mətn yaz, klaviatura ilə: "Qulaqliq"
    * Obyektə vur (XPathi=bu dəyişgənin dəyəri): "Axtar düyməsi"
    * Obyektə vur (XPath ilə): "//body[1]/div[4]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]/img[1]"
    * Obyektə vur (XPath ilə): "//span[@class='countWishlist-21883']"

## Kofe bişirən mehsulunun axtar
* MP3 oyna: "Uğurlu daxil oluram"
* Obyektə vur (XPathi=bu dəyişgənin dəyəri): "Məhsul axtar xanası"
* MP3 oyna: "Mətn yazıram"
* Mətn yaz, klaviatura ilə: "Kofe"
* "3" saniyə gözlə
* MP3 oyna: "Obyektə vururam"
* MP3 oyna (durmadan): "Axtar düyməsinə vururam"
* Obyektə vur (XPath ilə): "//*[contains(text(), 'Kofe bişirən Bergamo BG-CM3840BSB')]"
* YOXLA: obyekt ekranda OLDUĞUNU (XPath ilə): "//div[@class='d-flex align-items-center justify-content-center d-block']"; tapilsa_ses="Mətn tapıldı"; tapilmazsa_ses="Mətn tapılmadı"
* Obyektə vur (XPath ilə): "//div[@class='d-flex align-items-center justify-content-center d-block']"
* MP3 oyna: "Obyektə vururam"
* "1" saniyə gözlə
* Obyektə 2-KLIK vur (XPath ilə): "(//button[contains(text(),'Səbətə əlavə et')])"
* "1" saniyə gözlə
* YOXLA: Açılan alertdə bu mətnin olduğunu: "Item has been added in your cart!"
* Obyektə vur (XPath ilə): "//div[@class='toast-message']"
* MP3 oyna: "Mətn səhifədə var, və olmalı idi"
* Obyektə vur (XPath ilə): "(//a[@class='navbar-tool-icon-box bg-secondary dropdown-toggle'])[2]"

* "3" saniyə gözlə
* YOXLA: obyekt ekranda OLDUĞUNU (XPath ilə): "(//*[contains(text(), 'Kofe bişirən Bergamo BG-CM3840BSB')])[2]"; tapilsa_ses="Mətn tapıldı"; tapilmazsa_ses="Mətn tapılmadı"






    

    
    
   