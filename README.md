Primera Entrega del proyecto final 
Equipo: Kachinovsky, Gonzalez, Rivero


Las URLs utilizadas en el proyecto y su contenido son: 
- http://localhost:8000/index/  
    En ella se puede agregar un post a la pagina apretando el boton "Create Publication" y se muestra todos los posteos que hay
    La creacion de un posteo se hae utilizando:
        La funcion "index()" en el archivo views.py
        La clase "PublicationForm" en el archivo forms.py
        La clase "Publication" en el archivo models.py
        El template "index.html" (padre)

- http://localhost:8000/sign_up/
    En ella se puede registrar un usuario el cual se guarda en la BD 
    La registracion de un usuario se hace utilizando:
        La funcion "sign_up()" en el archivo views.py
        La clase "UserForm" en el archivo forms.py
        La clase "User" en el archivo models.py
        El template "signUp.html" (herencia utilizada, padre "index.html")
    
- http://localhost:8000/contact/
    En ella se puede enviar un mensaje el cual se guarda en la BD 
    El envio se hace utilizando:
        La funcion "contact()" en el archivo views.py
        La clase "ContactForm" en el archivo forms.py
        La clase "Contact" en el archivo models.py
        El template "contact.html" (herencia utilizada, padre "index.html")


- http://localhost:8000search/
    En ella se puede buscar un posteo. La busqueda se hace utilizando form queries, esto permite que se busque todo posteo en el cual el termino a buscar coincida con el campo author, subject o content ( buscar por ejemplo la palabra: "test")
    La busqueda se hace utilizando: 
        La funcion "search()" en el archivo views.py
        La clase "searchForm" en el archivo forms.py
        La clase "Publication" en el archivo models.py
        El template "search.html" (herencia utilizada, padre "index.html")

Cada una de ellas pueden ser accedidas a traves del Header el cual contiene links para cada una.
