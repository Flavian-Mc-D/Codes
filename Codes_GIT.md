Arquivo criado para os Codes de GIT HUB

Crear Usuario

$ git config --global user.name "Nome"

Crear Email 

$ git config --global user.email "bla@email.com"

Configurar Editor 

$ git config --global core.editor Vi

Crear directorio dónde van los datos.  

$ mkdri nome-do-diretorio

Iniciar el diretorio

$ git init

Crear o arquivo a ser editado

$ (nome/alias do editor) nome-do-arquivo.(extensão)
Ejemplo:
$ ST arquivo1.md 

Dependiendo del editor va a ser necesario declararlo, el por defecto es Vim, el editor se abre com el apodo vi nome-do-arquivo.md 
**md = markdown**

En el caso de usar otro editor se necesitará declarar el apodo del editor durante la sesión en cuestión

$ alias st='"C:\Program Files\Sublime Text 3\sublime_text.exe"'
 
**Estando dentro del editor, presionar:** 

1. "I" para entrar en el modo inserción (permite agregar información) 
2. "Esc" para salir del modo inserción 
3. ":" es necesario
4. ":wq" write, quit. 
5. "enter" para salir 

