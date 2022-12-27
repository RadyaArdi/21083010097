import random
import string
from time import sleep

def start():
    print("==========================================================================")
    print("                                                                          ")
    print("                WELCOME TO RADYA'S LINUX GAMES                            ")
    print("                                                                          ")
    print("==========================================================================")
    print("                        ARE YOU READY ?                                   ")
    print("==========================================================================")
    print("|| RULES :                                                              ||")
    print("|| Kalian bisa memilih permainan yang kalian inginkan                   ||")
    print("|| 1. Tebak Angka                                                       ||")
    print("|| 2. Hangman                                                           ||")
    print("|| 3. Quit                                                              ||")
    print("==========================================================================")
    
    option=int(input("Game apa yang kamu inginkan? "))
    if option==1:
      tebak_angka()
    elif option==2:
      game_hangman()
    elif option==3:
      print ("SAMPAI JUMPA LAGI")
      exit()


    else:
      print ("pilihan anda salah")
      start()
  
def awal():
    mengulang = input("\n Mau Main Lagi? [y/n]")
    if mengulang == 'y':
      start()

    elif mengulang == 'n':
      print("\n SAMPAI JUMPA LAGI. HAVE A NICE DAY! \n")
      exit()

    else:
      print("Perhatikan kembali apa yang kamu inputkan!")
      start()


def tebak_angka():
    print("________________________________________________________________________________")
    print("               SELAMAT DATANG PADA PERMAINAN TEBAK ANGKA                        ")
    print("--------------------------------------------------------------------------------")
    print("  Kalian dapat memilih pilihan digit angka yang akan ditebak.                   ")
    print("  1. 1 digit angka (1-9)                                                        ")
    print("  2. 2 digit angka (10-99)                                                      ")
    print("  3. 3 digit angka (100-999)                                                    ") 
    print("________________________________________________________________________________")

    while True:
        num = int(input("Masukkan pilihan digit angka yang ingin kalian tebak: "))
        if num == 0:
            print("Coba lagi!")
            continue
        else:
            secret=str(random.randint(10**(num-1), 10**(num)-1))
            print("----------------------------------------------------------------")
            print("Kalian dapat memilih nyawa dalam permainan tebak angka ini: ",
                  "\n 1. Terserah sistem", "\n 2. Terserah aku"
                  )
            print("================================================================")
            nyawa=int(input("Masukkan pilihan jumlah nyawa: "))
            if nyawa == 1:
                pass
            elif nyawa == 2:
                pilihan=int(input("Masukkan nyawa: "))
            else:
                print("pilihan salah!")
                continue
            print("----------------------------------------------------------------")
            print("MULAI!")

            if nyawa == 1:
                while True:
                    tebakan=input("Angka Tebakan: ")
                    if tebakan.isdecimal() == False:
                        print("Mohon masukan bilangan")
                        continue
                    if len(tebakan)!=len(secret):
                        print(f"Bilangan harus {len(secret)} digit!")
                    else:
                        if tebakan == secret:
                            print("SELAMAT, TEBAKAN KAMU BENAR!")
                            break
                        else:
                            print(
                              "Tebakan kamu terlalu",
                              "kecil" if tebakan < secret else "besar"
                            )
            
            elif nyawa == 2:
                for i in range(pilihan):
                    i +=1
                    tebakan=input("Angka tebakan: ")
                    if tebakan.isdecimal() == False:
                        print("Mohon masukkan bilangan")
                        continue
                    if len(tebakan)!=len(secret):
                        print(f"Bilangan harus {len(secret)} digit!")
                    else:
                        if tebakan == secret:
                            print("SELAMAT TEBAKAN ANDA BENAR!")
                            break
                        else:
                            print(
                              "Tebakan kamu terlalu",
                              "kecil" if tebakan < secret else "besar"
                            )
                        if i == pilihan:
                            print("Nyawa kamu sudah habis, tebakan yang benar adalah",secret)
                            break
        awal()

        break
      


def game_hangman():

    import random
    def welcome():
        print("==============================================================================")
        print("                 SELAMAT DATANG DALAM PERMAINAN HANGMAN                       ")
        print("==============================================================================")
        name = input("Tak kenal maka tak sayang. Sebutkan nama kamu: ").capitalize()
        
        if name.isalpha() == True:

            print("\n   ------------- "
                  "Hi!", name, "senang bertemu denganmu di sini!"
                  " --------------"
                  )
        else:
            print("Perhatikan kembali yang kamu inputkan!")
            nama = input("Sebutkan nama kamu: ")
            print("Hi!", nama, "Perhatikan kembali peraturan yang berlaku!")
    
    def get_word():
        words = ['Tulus', 'Mahalini', 'Tiara', 'Lyodra', 'Afgan', 'Raisa', 'Isyana', 'Niki', 'Kahitna', 'RAN', 'Arsy', 'Andmesh',
                 'Chrisye', 'Fiersa', 'Glenn', 'Gangga', 'Once', 'Pamungkas', 'Sammysimorangkir', 'Tompi', 'VidiA','Brisia', 'BCL', 'Naura']
        return random.choice(words).lower()
    
    def game_run():
        welcome()
    
        alphabet = ('abcdefghijklmnopqrstuvwxyz')
    
        word = get_word()
    
        letters_guessed = []
    
        tries = 6
    
        guessed = False
    
        print()
    
        print('Kata ini memuat', len(word), 'huruf.')
        print(len(word) * '_')
        
        while guessed == False and tries > 0:
              print('Kamu mempunyai ' + str(tries) + ' percobaan')
              tebakan = input('Huruf yang ingin ditebak: ').lower()
              
              if len(tebakan) == 1:
                  if tebakan not in alphabet:
                      print('Perhatikan kembali apa yang kamu inputkan. pastikan yang kamu masukkan adalah huruf!')
                  elif tebakan in letters_guessed:
                      print('Kamu telah menebak huruf ini sebelumnya')
                  elif tebakan not in word:
                      print('Coba lagi!')
                      letters_guessed.append(tebakan)
                      tries -=1
                  elif tebakan in word:
                      print('Lanjutkan!')
                      letters_guessed.append(tebakan)
                  else:
                      print('Perhatikan kembali apa yang kamu inputkan!')
              
              elif len(tebakan) == len(word):
                  if tebakan == word:
                      print('Kerja bagus! Tebakan kamu tepat sasaran')
                      guessed = True
                  else:
                      print('Maaf, coba lagi!')
                      tries -= 1

              else:
                  print('Tebakan kamu masih kurang tepat')
                  tries -=1
              
              status = ''
              if guessed == False:
                  for letter in word:
                      if letter in letters_guessed:
                          status += letter
                      else:
                          status += '_'
                  print(status)

              if status == word:
                  print('Kerja bagus. Lanjutkan!')
                  guessed = True
              elif tries == 0:
                  print("Kesempatan kamu sudah habis. coba lagi nanti.")
        
    game_run()

    awal()

start()

