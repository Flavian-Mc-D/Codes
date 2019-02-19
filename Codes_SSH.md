**SSH**

**CD: Change directory**
<br>
   sube un nivel:    ..
   sube dos niveles: ../..
<br>
**LS: List**
 1.  -a: All data.
 2.  -l: Lista completa.
 3.  -t: Tiempo relacionado con el archivo.
> Nota: pueden ser usados en conjunto, LS -alt
<br>
**PWD**: Print Working Directory
<br>
**mkdir**: Make Directory
<br>
**Touch**: Creates a file 
<br>
Ejem: touch file.txt
<br>
####ECHO
**Echo**: Crea dentro de un archivo X pedido
    echo "Hello" >> Hello.txt 
    Creará dentro de Hello.txt el texto entre comillas.
<br>
####CAT
<br>
**CAT**: Muestra los datos que están dentro de un archivo. 
Ejem: CAT texto.txt
<br>
**CP**:  COPY
<br>
    CP folder/file.txt destinationfile/destinationName(opcional)

    CP M*.TXT/ DestinationFolder/ En este caso copia todos los archivos de la carpeta donde se encuentre simpre que comeiencen con M y que sean .txt
***
To copy between directories

cp filename-to copy.txt ../../new-directory/filename-to-copy.txt
For example

cp contactus.php ../contact/contactus.php
To copy all files from one directory to another, use the * character, which unofficially means all (except files that begin with . or ..):

cp images/* ../skin/
To copy all files including files that begin with . (1 dot) from one directory to another:

rsync -a ./ ../
To show a progress bar of files being copied:

rsync --progress /copy/from /copy/to