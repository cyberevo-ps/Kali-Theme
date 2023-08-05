import os
os.system("clear")
os.system("cp kali.py $HOME")
os.system("cp bash.bashrc $HOME")
os.system("clear")
print ("""\033[1;34m
.....',,,,,'....
              ...',;:cloodxxoc;..
                            .':oxOOd:.
                   ....'',,;;;;:::cdkk
    ....''',,,,,,,,''...........,:ldlc
                        .,::cclllc::;.;
                  .,;;;;'.            .0d;'....   ....
             .,,,,.                   :0MNK000KXKxc,  ...
         .'',.                      dW0:.       .'cx0XO:o,.
       ..                          0W;                .:xX0x.
                                  cMc                    oXNK.
                                  OM.                      .;kk:
                                  kM:                         .
                                  .NW:
                                   .kW0:.
                                     .ckKXKOOkkxxxdoc:,.
                                          ......',;cokXMXkxo;.
                                                       .co:..:lc.
                                                          .::   ':,
                                                             :,    ,.
                                                              .c    .
                                                                c
                                                                .;
                                                                 ..
                                                                  .\033[1;32m
                        _  __     _ _   _     _
                       | |/ /__ _| (_) | |   (_)_ __  _   ___  __
                       | ' // _` | | | | |   | | '_ \| | | \ \/ /
                       | . \ (_| | | | | |___| | | | | |_| |>  <
                       |_|\_\__,_|_|_| |_____|_|_| |_|\__,_/_/\_\ \033[1;34m

                             Theme By BO HAYDAR ARB TXR TEAM




""")
vvvv = input ("\033[1;35mDo You Install Kali Linux Theme ??  n/y    :      ")
if vvvv =='n' :
   print (" Lech ma Bdk 😑???")
elif vvvv =='y' :
     os.system("cd $HOME && cd ../usr/etc && rm -rf bash.bashrc && cd && python kali.py && cd Kali-Theme && python kali-Theme.py")
     os.system("python kali.py")
