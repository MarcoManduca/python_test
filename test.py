import os
#os.system("mkdir .ssh") #esegue il comando indicato sul terminale

### how to set up github repository for versioning
""" 
SSH: sorta di chiave per connettere il terminale in modo sicuro a git
creare cartella .ssh
spostarsi all'interno della cartella e lanciare il comdando:
 sshkeygen -t rsa
confermare il nome del file (id_rsa)
e quindi inserire una password
A questo punto sono stati generati 2 file:
id_rsa e id_rsa.pub
lanciare il seguente comando per copiare la password da inserire sul sistema di versioning
 pbcopy < ~/.ssh/id_rsa.pub

"""


### git commands
"""

#git config
git config --global user.name "Marco Manduca"
$ git config --global user.email "marco.manduca95@gmail.com"
$ git config --global push.default matching
$ git config --global alias.co checkout
$ git init

#git versioning
git add .
git commit -am "commento che descrive le modifiche apportate"
git push
"""