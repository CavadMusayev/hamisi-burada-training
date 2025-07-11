using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;


namespace netcore.template
{

  public class CONSTANTlar
  {
#pragma warning disable 0169

    readonly int _______for_Vahid_PC;

    public readonly static int NUM_OF_MONITORS = 2;
    public const bool ENABLE_OBS = false;
    public const string OBS_SOCKET_PORT="4444"; 
    public const string OBS_EXECUTABLE_LOCATION = @"C:\Program Files\obs-studio\bin\64bit\obs64.exe";

    // https://googlechromelabs.github.io/chrome-for-testing/

    //Vəhid Driver Path
    // public readonly static String CHROME_DRIVER_PATH="d:\\Code\\ChromeDriver\\";

    //Anar Driver Path
    //public readonly static String CHROME_DRIVER_PATH="C:\\Users\\anar.abbas\\Desktop\\QA Automation\\chromedriver-win64\\";

    //Sakit Driver Path
    //public readonly static String CHROME_DRIVER_PATH="C:\\Users\\QA-AutomationDriver\\chromedriver-win64\\";
    //Balasaf
    public readonly static String CHROME_DRIVER_PATH = @"C:\chromedriver";


    public readonly static Boolean MP3_SES_OYNA = true;
    //public readonly static Boolean MP3_SES_OYNA =false;

    readonly int _______for_ProSys_server;
    /*
    public readonly  static int NUM_OF_MONITORS = 1;

    readonly String CHROME_DRIVER_PATH="E:\\DMS_test_otomasyon\\ChromeDriver";

    public readonly static  Boolean MP3_SES_OYNA =false;

    */

    readonly int _______same_for_both_test_environments;

    public readonly static String Sistemin_əsas_səhifə_URLi =
       "https://www.hamisiburada.az";


    public readonly static double SELENIUM_ELEMENT_GOZLEME_SANIYESI = 4.0;

    // 1 olsa, normal hiz
    // 1'den cox, suret coxalir
    // 1'den az, suret azalir        
    public readonly static double GÖZLƏMƏ_ORANI = 1.0;

    public readonly static String VLC_EXE_PATH = @"C:\Program Files\VideoLAN\VLC\vlc.exe";

    // XATA
    public readonly static Boolean XETA_METNINI_FAYLA_YAZ = false;
    // false / true
    public readonly static Boolean XETA_SCREENSHOT_AL_VE_FAYLA_YAZ = false;

    public readonly static Boolean CIDDI_XATALARDA_TESTI_FAIL_ET = true; //false;


    public readonly static String UI_DA_YAZI_YOXLAMA_KƏNAR_RƏNGI = "green";
    public readonly static String UI_DA_DUYMEYE_VURMA_KƏNAR_RƏNGI = "red";
  }
}