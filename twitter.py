import time
import requests , os
import pyfiglet

mydata = { "api" : "SGB-TonVyZ7w93 SGB-b5cbU3rrfT SGB-1wZuH7mmgL SGB-8zDavscKTL SGB-2y9CLdXKVX SGB-l1K4XDsU1N SGB-CUw8woruRn SGB-cg8fUJsp4E SGB-qGui24rcZc SGB-IzJVOEUwvP SGB-Yd0ng4tYQS SGB-ZKpu6r00to SGB-ZM5qPvZmRp SGB-dOJ2toJBl1 SGB-CTEVtzclaV SGB-nCVmi0P4Vr SGB-qEEdfrZ5vs SGB-u8FIiT31SE SGB-YDH0RkMF0U SGB-IqeBFday1c SGB-lsIrYr7wJm SGB-dWnTa680rk SGB-LErb2V2cST SGB-BJhIix0Md2 SGB-rVDhs4huSG SGB-Opi9XCN5qH SGB-T6nIEAA6AW SGB-EtBM87kwnJ SGB-3JhjLBgocf SGB-bHkEQmpicc SGB-TvdAsi1SIl SGB-vbZDb3ECkF SGB-iHCZoWQUFN SGB-r8P5C251nq SGB-IAQmVqh772 SGB-uywivkh5XU SGB-WIHEMl2CmL SGB-THsLF8Zfiz SGB-kZyd2ObEo5 SGB-DQH64QDoQW SGB-sOo3ARbt4H SGB-RkzvvRNUn3 SGB-39zdaj85pS SGB-9Ti0ONG3ed SGB-1vrEZtAmXr SGB-CKPXHQYO4R SGB-XzraafDIUY SGB-0a3dTUbLAA SGB-Jj8EDhinKf SGB-oFBtzZOxeq SGB-PekA8KSVlt SGB-r2AnW1CGmM SGB-gs7gZKDa0C SGB-lNs5JYOucT SGB-TFOrUvnz4y SGB-iCdcNJt9vo SGB-1SgEhlvC9X SGB-Fkc1Cthb5O SGB-Vk5dflyEy0 SGB-VCQININdx8 SGB-6ecYJDfF1f SGB-IKPq8oL8YK SGB-jy36mZYapl SGB-VKLkJxFuZA SGB-FSoU8CQnSS SGB-uBht9uXbch SGB-K5i8rFwNxv SGB-6mHexOFLZI SGB-DFsXu1Vm2p SGB-EcbbgH9KDn SGB-4WjkpgzB1c SGB-VLvZwl9F8q SGB-2J226eieo8 SGB-bqhu4N2zvu SGB-woizMwG3cq SGB-0rKO5bAtN1 SGB-l7EwzzqYfZ SGB-eSDPwJVmkR SGB-Q9AJakdje7 SGB-bNSKqyQR6n SGB-wkHNZSYlnh SGB-FFWYzzc1Sm SGB-5MLR8LMp2h SGB-oCUjYneRMV SGB-LMgfzTccDF SGB-sH7cm5RB7y SGB-hRRRJdzEBt SGB-p0cBVzhg5Z SGB-jIeSEtig8U SGB-j0zInCpy57 SGB-cy4RPDsyXL SGB-drAAo5Lr7H SGB-8FAkcxHlrA SGB-hM1kJn0yWT SGB-Yfgjjl7Bub SGB-9e3WiwHf0N SGB-nnAWgKiX1p SGB-WZOFXo4xAg SGB-oO0tDb1hVh SGB-57PVvHzAu8",
         "consumer_key" : "tLZYeHDfJAH1N6hnU5fnjk77v",
         "consumer_secret" : "1001802249406889984-y6VtIxarVB5RvdhNl8QfolqhcvRanI",
         "access_token" : "1001802249406889984-y6VtIxarVB5RvdhNl8QfolqhcvRanI",
         "access_token_secret" : "CDh2H3XFwuZZOGykXZukf5QiyTvNOL3BgSaEKaGOJUNz4"}


status1 = True
def banner():
        os.system('clear')
        ascii_banner = pyfiglet.figlet_format("Tweeter Media")
        print(ascii_banner)
        

while status1 == True:
    banner()
    print("==============================================")
    print ("COMMAND ||              MENU  :              |")
    print("==============================================")
    print (" 'UNF'  ||   1. Unfollow Not Follback        |")
    print (" 'UAF'  ||   2. Unfollow ALL FOLLOWING [HOT] |")
    print (" 'FFT'  ||   3. Follow Followers Target      |")
    print (" 'exit'                                      |")
    print("==============================================|")
    pil = input("Pilihan Kamu (UNF / UAF / FFT / exit) : ")
    n = 0
    i = 1
    if pil == "UNF":
        r = requests.post("https://tweetermedia.zapto.org/private/notfollback.php", data = mydata)
        if r.status_code == 500:
            print ("ERROR 500")
        print (r.text)
        input("Press Anything..")
    elif pil == "UAF":
         print ("May cause your twitter token expired, broken, and your twitter might be temporary or permanently suspended.")
         pil2 = 0
         status=True
         while status:
             pil2 = input("1. Continue 2. Exit    CHOOSE : ")
             if pil2 == "1":
                 status = False
                 r = requests.post("https://tweetermedia.zapto.org/private/unfollowall.php", data = mydata)
                 print(r.text)
    elif pil== "FFT": 
        while n != 1:
            r = requests.post("https://tweetermedia.zapto.org/private/fftmantap.php", data = mydata)
            print ("Percobaan ke-", i)
            print(r.text)
            if "TARGET" in r.text:
                isi = True
                while isi:
                    isi1 = input("Mau isi username Target? : 1. Ya 2. Tidak")
                    if isi1 == "1":
                       username = input("Input username target : ")
                       target = {"username" : username , "api": "hamzadln99"}
                       r = requests.post("https://tweetermedia.zapto.org/private/add_target.php", data = target)
                       print(r.text)
                    elif isi1 == "2":
                        isi = False
                    else:
                        print("ISI YANG BENERLAH GOBLOG")
            if "Berhasil" in r.text:
                print("Berhasil")
                if i==1:
                    time.sleep(45)
                elif i>1:
                    time.sleep(40)
            elif "Gagal" in r.text:
                n = 1
                input("END. Press anything..")
                print("Gagal")
            elif "Duplikat" in r.text:
                print("Duplikat")
            i += 1
    elif pil=="exit":
         status1 = False
print ("END. Thank You.")
