import os
#os.system("mkdir .ssh") #esegue il comando indicato sul terminale

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


ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCo7L0yntTKZIu8bPBwHle4ARvdciLW3gTGLVklkO0xm5EThLlue7sptW0WPuewIegmcjPxFgsulAsVDqCER9BV18iRmLIhZzcd2lSBv26p/3YCEHXMyFuf6R093GETw9K854nXX6ZJmjETyDlbl9448291xFh0dzD45ZChPLtgCuiiVG05z1qIg2oQ+pFzTD7Xk5Yfzuir9i20bl0hcWVD0HKKoiq7Vx65dkNRuxVP3DhqVVLvf6Wd1NdH5jcWxEl6LW2SI9BKYzGMaPxXbPStNAhcFreN/kBx+Mu7FihS4yUJqRTTMAJOU0XLlhU0DpcQuQ9PJeo6l2x/6H6hIrsuy36LLIs3UrvuPTKE9/DwT8hZys9YolkFPSV+/HzvSLCr3VMALezg73Z9oflAB8Qq0rVX6fntY74xJQ8e/6Hsvz5q6aB7DKkybZL706lZRLsv9SXcMtwRINREiAtRfTQI8fT1SYZXyNAMrhUeK9JrYjKK3BFlM/6Utj+BqF4jwoE= marcomanduca@MacBookPro

"""