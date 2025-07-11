# 4-Qeydiyyat Loqin
   * Chrome'u aç, Sistemin əsas səhifəsini aç

## 4.1-Qeydiyyatdan keç
//SETUP
   * 4.1.1-User iconuna kursoru gətir

   * Kursoru XPATH ilə hərəkət etdir "//a[normalize-space()='Qeydiyyatdan keç']"

//Qeydiyyatdan keç düyməsinə vur.

   * Obyektə vur (XPath ilə): "//a[normalize-space()='Qeydiyyatdan keç']"

//VERIFY
   *  YOXLA: Səhifə URLi bumu: "https://www.hamisiburada.az/customer/auth/register"

   * YOXLA: Əgər son test addımda xata göründü, testi xatalı durdur
   //Qeydiyyat formunu doldur
      //Ad bölməsi tap və doldur.
   * Obyektə vur (XPath ilə): "//input[@name='f_name']"
   * Mətn yaz, klaviatura ilə: "Elnur"

   //Soyard bölməsini tap və doldur.
   * Obyektə vur (XPath ilə): "//input[@name='l_name']"
   * Mətn yaz, klaviatura ilə: "Abaslı"

   //Email bölməsini tap və doldur.
   * Obyektə vur (XPath ilə): "//input[@name='email']"
   * 4.1.3-Email daxil et

   //Telefon nömrəsini tap və doldur.
   * Obyektə vur (XPath ilə): "//input[@name='phone']"
   * Mətn yaz, klaviatura ilə: "055 855 11 26"

   //Parol bölməsini yaz və doldur.
   * Obyektə vur (XPath ilə): "(//input[@id='si-password'])[1]"
   * 4.1.4-Parol daxil et

   //Parol təsdiqlə bölməsini yaz və doldur.
   * Obyektə vur (XPath ilə): "(//input[@id='si-password'])[2]"
   * 4.1.4-Parol daxil et

   //Şərtlərlə razıyam
   *  Obyektə vur (XPath ilə): "//input[@id='inputCheckd']"

   //Qeydiyyatdan keç
   *  Obyektə vur (XPath ilə): "//button[@id='sign_in']"

//TEARDOWN
   * "3" saniyə gözlə

