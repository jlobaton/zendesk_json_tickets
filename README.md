# zendesk_json_tickets
Bash que permite generar un archivo JSON a partir de un archivo CSV, para poder importarlo a la API Console de Zendesk v2 (Ticket)

## Dependencias:

* python >=  2.7.12

## Explicación:
 Por consola deberá ejecutar esta instrucción:
``` 
$ python generarJsonTicket.py -f example -r 2000
``` 
* Donde los parámetros de entradas, serian lo siguientes:
```
   example : Nombre de archivo CSV a procesar (sin la extención)
   -f  :  Especifica el nombre del archivo a leer
   -r  :  Cuantos Registros se va a Generar por archivo
```

* Archivo CSV, se necesita tener una estructura básica de Zendesk:
  * name
  * email
  * phone
  * custom_fields.nombre_del_campo1
  * custom_fields.nombre_del_campo2
  * custom_fields.nombre_del_campo3

* Imagen de muestra del Archivo example.csv
<p align="center">
<img src="http://www.seguridadsistema.com.ve/github/zendesk/users/img/csv.png" />
</p>

* Si no muestra algún error, te mostrará información acerca del nombre de los archivos generado
<p align="center">
<img src="http://www.seguridadsistema.com.ve/github/zendesk/users/img/console1.png" />
</p>

 * Luego abrir la página de **Api Console de Zendesk**
 
 ```
 https://developer.zendesk.com/requests/new

```
 Deberá personalizar la conexión en el cual, van a cargar los datos que se va a migrar, [más información](https://)
<p align="center">
<img src="http://www.seguridadsistema.com.ve/github/zendesk/users/img/apiconsole.png" />
</p>

 
## Screenshot(s):

### Imagen de muestra cuando se genera el archivo JSON
<p align="center">
<img src="http://www.seguridadsistema.com.ve/github/zendesk/users/img/json.png" />
</p>

### Imagen de muestra usando la herramienta API Console
<p align="center">
<img src="http://www.seguridadsistema.com.ve/github/zendesk/users/img/apiconsole.png" />
</p>


## Autor (Author)

  Jesus Maria Lobaton Escobar < jesuslobaton@gmail.com >

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

