# 4-Loqin
   * Chrome'u aç, Sistemin əsas səhifəsini aç
   * Uİ obyektlərin locatorları load et - Login
## 4.2-Login Et

//SETUP
   * 4.1.1-User iconuna kursoru gətir
   * 4.1.2-Login iconuna daxil ol

//VERIFY
   * YOXLA: Səhifə URLi bumu: "https://www.hamisiburada.az/customer/auth/login"

   * YOXLA: Əgər son test addımda xata göründü, testi xatalı durdur

   //Email Daxil Et
   * Obyektə vur (XPath ilə): "//input[@name='email']"
   * 4.1.3-Email daxil et

   //Parol Daxil Et
   * Obyektə vur (XPath ilə): "(//input[@id='si-password'])[1]"
   * 4.1.4-Parol daxil et

   //Giriş Et
   *  4.1.5-Daxil ol düyməsinə bas
   
   //YOXLA Alertinin düzgünlüyünü yoxla.  
   * YOXLA: Açılan alertdə bu mətnin olduğunu: "Signed in successfully!" 
//TEARDOWN

## 4.3-Login et (Yanlış email)

//SETUP
   * 4.1.1-User iconuna kursoru gətir
   * 4.1.2-Login iconuna daxil ol

   //Yanlış email daxil et.
   * Obyektə vur (XPath ilə): "//input[@name='email']"
   * Mətn yaz, klaviatura ilə: "a@example.com"

   //Parol daxil et
   * Obyektə vur (XPath ilə): "(//input[@id='si-password'])[1]"
   * 4.1.4-Parol daxil et

   * 4.1.5-Daxil ol düyməsinə bas
//VERIFY
   * YOXLA: Açılan alertdə bu mətnin olduğunu: "Credentials do not match or account has been suspended."

//TEARDOWN
   * YOXLA: Əgər son test addımda xata göründü, testi xatalı durdur



 ## Giriş et
//////////////////// MEHSETI//////////////////////////////////
* SETUP LOGIN
* EMAIL DAXIL EDIREM
* SIFRE DAXIL EDIREM
* SIFRENI GOSTERMEK UCUN OLAN GOZ SEKILLI DUYMEYE VURURAM
* MENI XATIRLA CHECKBOX-UNU SECIREM
* VERIFY
* TEARDOWN