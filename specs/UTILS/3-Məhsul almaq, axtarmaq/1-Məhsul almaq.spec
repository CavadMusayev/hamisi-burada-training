# 3-Məhsul almaq
   * Chrome'u aç, Sistemin əsas səhifəsini aç
    
## 3.1-Məhsul Almaq Saat
//SETUP -- 

   * Obyektə vur (class ilə): "search-bar-input"
 
   * Mətn yaz, klaviatura ilə: "Saat"

//EXERCISE --
//Listin Açılmasını gözlə.
   * "3" saniyə gözlə

// List-də 4-cü obyekti seç  
   * Obyektə vur (CSS label ilə): ".list-group-item:nth-child(4)"

//VERIFY --
//Doğru məhsulun seçildiyini təsdiqlə
   * YOXLA: mətnin səhifədə "olduğunu": mətn = "Qol saatı Casio Edifice LTP-15"; axtarma_yoxlama_ilk_səs_faylı = ""; mətn_ismi_ses_fayli = ""; tapildi_ses_fayli = "Mətn tapıldı"; tapilmadi_ses_fayli = "Mətn tapılmadı"; ehtiva_edir_ya_dəqiq_uyğunluq = "ehtiva_edir"; tapilmazsa_testi_fail_et="xeyr"
    
   * YOXLA: Əgər son test addımda xata göründü, testi xatalı durdur

//Məhsula daxil ol və səbətə əlavə et 

   * Obyektə vur (class ilə): "product-card"
 
   * Obyektə vur (class ilə): "btn-primary"

//Məhsulun kart-a əlavə edilməsini gözlə.
   * "3" saniyə gözlə

   *  3.1.1-Cart-a Daxil Ol

//Cart-ın yüklənməsini gözlə.

   * "3" saniyə gözlə
  
   * 3.1.2-Çatdırılma metodu (Azərpoçt) seç

//Rəsmiləşdirmə düyməsi  

   * 3.1.3-Rəsmiləşdirmə

   * "3" saniyə gözlə

// TEARDOWN --

## 3.2-Filteri Yoxla

//SETUP --

   *  3.2.1-Axtarış

//Birinci məhsula daxil ol
   * Obyektə vur (XPath ilə): "//*[@id='ajax-products']/div[1]"

   *  3.1.4-Səbətə əlavə et

//İkinci məhsula daxil ol
   * 3.2.1-Axtarış

   * Obyektə vur (XPath ilə): "//*[@id='ajax-products']/div[4]"
   
   * 3.1.4-Səbətə əlavə et

//Cart-a daxil ol.
   * 3.1.1-Cart-a Daxil Ol

//Cart-da kı məhsulu sil.
   * Obyektə vur (XPath ilə): "//i[@class='czi-close-circle mr-2']"

//Məhsul sayını artır

   * Obyektə vur (XPath ilə): "//select[@id='cartQuantity1']"
   
   * "1" saniyə gözlə
   
   * Obyektə vur (XPath ilə): "//select[@id='cartQuantity1']/option[@value='2']"

//Məhsulu al
   * 3.1.2-Çatdırılma metodu (Azərpoçt) seç

   * 3.1.3-Rəsmiləşdirmə

//TEARDOWN--


## 3.3-Məhsul axtarmaq (Pagination) 

//SETUP --
//Elektronika Və Texnika Bölməsinə Kursoru apar.
   * Kursoru XPATH ilə hərəkət etdir "//*[@id='navbarCollapse']/ul[2]"

//Audio, video, televizor və akksesuarlar Bölməsinə Kursoru apar.
   * Kursoru XPATH ilə hərəkət etdir "//*[@id='navbarCollapse']/ul[2]/li/ul/li[2]"

//Şəbəkə avadanlıqları Modemlər, Routerlər Bölməsinə Kursoru apar.
   * Kursoru XPATH ilə hərəkət etdir "//*[@id='navbarCollapse']/ul[2]/li/ul/li[2]/ul/li[1]/a/span"

//Şəbəkə avadanlıqları Modemlər, Routerlər Bölməsinə Daxil ol.
   * Obyektə vur (XPath ilə): "//*[@id='navbarCollapse']/ul[2]/li/ul/li[2]/ul/li[1]/ul/li[1]/a"

//Validation -- Duzgun kateqoriyada oldugumuzu tesdiqle
   * YOXLA: mətnin səhifədə "olduğunu": mətn = "Şəbəkə avadanlıqları Modemlər, Routerlər"; axtarma_yoxlama_ilk_səs_faylı = ""; mətn_ismi_ses_fayli = ""; tapildi_ses_fayli = "Mətn tapıldı"; tapilmadi_ses_fayli = "Mətn tapılmadı"; ehtiva_edir_ya_dəqiq_uyğunluq = "ehtiva_edir"; tapilmazsa_testi_fail_et="xeyr"

   * YOXLA: Əgər son test addımda xata göründü, testi xatalı durdur

//Pagination üçün XPATH
   * Obyektə vur (XPath ilə): "//*[@id='paginator-ajax']/ul/li[3]/a"

//Səhifənin gözlənilməsi üçün 3 saniyə gözləyirik.
   * "3" saniyə gözlə

//Birinci məhsula daxil ol.
   * Obyektə vur (XPath ilə): "//*[@id='ajax-products']/div[1]"

//Validation -- Diapozonlu WIFI oldugunu tesdiqle
   * YOXLA: mətnin səhifədə "olduğunu": mətn = "İki diapazonlu Wi‑Fi 6 Router TP-Link Archer AX53"; axtarma_yoxlama_ilk_səs_faylı = ""; mətn_ismi_ses_fayli = ""; tapildi_ses_fayli = "Mətn tapıldı"; tapilmadi_ses_fayli = "Mətn tapılmadı"; ehtiva_edir_ya_dəqiq_uyğunluq = "ehtiva_edir"; tapilmazsa_testi_fail_et="xeyr"

   * YOXLA: Əgər son test addımda xata göründü, testi xatalı durdur

//Məhsul sayını artır
   * Obyektə vur (XPath ilə): "//*[@id='add-to-cart-form']/div[2]/div[2]/div/div/span[2]/button"

//İndi al düyməsi
   * Obyektə vur (class ilə): "btn-secondary"

//TEARDOWN --
   * Chrome'u bağla

##3.5-Protechno Məhsul Kateqoriyasından al
//SETUP
   * 3.5.1-Sadə Axtarış

// Cəld bax. Birinci Məhsul
// Məhsul hover et.
   *  Kursoru XPATH ilə hərəkət etdir "//div[@id='ajax-products']/div[1]"

//Cəld bax click
   * Obyektə vur (XPath ilə): "(//i[contains(@class,'czi-eye align-middle mr-1')])[1]"

   * 3.5.3-Cəld Bax Bağla

// Cəld bax. İkinci Məhsul
// Məhsul hover et.
   * Kursoru XPATH ilə hərəkət etdir "//div[@id='ajax-products']/div[2]"
   
//Cəld bax click
   * Obyektə vur (XPath ilə): "(//i[contains(@class,'czi-eye align-middle mr-1')])[2]"

   * 3.5.2-Şəkillərə Bax

   * 3.5.3-Cəld Bax Bağla

// Cəld bax. Üçüncü Məhsul
   *  Kursoru XPATH ilə hərəkət etdir "//div[@id='ajax-products']/div[3]"

//Cəld bax click-lə

   * Obyektə vur (XPath ilə): "(//i[contains(@class,'czi-eye align-middle mr-1')])[3]"

   * 3.1.5-İndi al

//TEARDOWN
                                                                           