package com.company;

import java.lang.annotation.Documented;
import java.util.Arrays; //Manejo de Arrays
import java.util.List; //Manejo de listas
import java.util.Scanner; //El import para leer por teclado.
import java.util.logging.*;

public class Main {

    public static void main(String[] args) {
	// Aquí va vuestro código, no podéis escribir sin más como en Python. Lo bueno es que el IDE te autogenera esta estructura.
        System.out.println("Hola"); //println es como el print de Python. Añade un salto de línea al final.
        System.out.print("Hola");  //print es como el print como el end = "" al final. No tiene salto de línea por lo que el siguiente print irá seguido.
        System.out.print("Seguido\n"); //Si quieres manualmente añadir el salto de línea... usad \n
        System.out.print("Adios\n");
        //Ahora, las variables, tienen que estar definidas del tipo que son en el momento en el que las creas.
        int a = 5; //Ah! Y no olvidéis los puntos y comas al final de cada sentencia.
        float b = 2.2f; //El símbolo décimal es el punto. Pero no basta con esto, hay que añadir la f al final.
        //Si queremos guardarlo en una nueva variable, nuevamente tienes que indicar el tipo.
        //También existe el tipo double. Es un decimal con más precisión (puede tener más decimales).
        float resultadoFlotante = a + b;
        //Aquí el convertir tipos de uno a otro no es tan fácil. Y tampoco podemos sumar enteros a decimales del tirón.
        //Como véis, Java es bastante más restrictivo. La manera de convertir el flotante a entero de abajo no es lo normal.
        int resultadoEntero = a + (int) b;
        System.out.println("El resultado décimal de sumar " + a + " y " + b + " es " + resultadoFlotante + " y el entero es " + resultadoEntero);
        //A continuación vemos cómo inicializamos un carácter, una string y cómo convertimos esta última a entero.
        char caracter = '2'; //MUCHO OJITO. Los carácteres van comillas simples, no dobles. Java es sensible a esto a diferencia de Python.
        String curso = "DAW"; //En Java, String es una CLASE. Por eso no cambia de color y se usan funciones distintas para ella.
        String numero = "1"; //Ahora si queremos convertir esto a entero, no valdrá con (int) pues String es una clase.
        System.out.println("La cadena se imprime sin problema " + curso);
        //Si queremos pasar numero a entero llega el problema y se hace así:
        int convertido = Integer.parseInt(numero);
        int convertidoCaracter = (int) caracter; //¿Saldrá esto lo que debe salir?
        System.out.println("Hemos convertido a enteros " + convertido + " y " + convertidoCaracter); //Convirtiendo el caracter usando (int) ha salido 50. Su valor en ASCII.
        //¿Qué debemos hacer para que salga el número 2 en lugar de su correspondiente en ASCII?
        int convertidoCaracterBien = Character.getNumericValue(caracter); //Tiene su propia función.
        System.out.println("Ahora sí vale lo que debe " + convertidoCaracterBien);
        //Esto implica que váis a tener que aprender a buscar en internet numerosas peculiaridades que os vayan surgiendo sobre la marcha.
        //Hasta aquí lo que debíamos ver a grandes rasgos de variables.

        boolean flag = true; // Boolean es un tipo de variable que permite ser false o true. Útil para condiciones y while.
        //Y si queremos pedirlo por teclado...
        //String variable = System.console().readLine(); //Pero esto no funciona en un IDE
        //Hay muchas maneras pero por ahora nos valdrá con esto.
        //Hay que añadir java.util.Scanner a los package del programa al principio del código y luego inicializar el Scanner, que es un evento que espera algo por teclado.
        Scanner leer = new Scanner(System.in);  // Crea el objeto Scanner, debe estar siempre al principio del main.
        System.out.println("Introduce si entra o no entra");
        String leido = leer.nextLine(); //Pero no permite añadir texto, por lo que necesitáis de println antes para pedir lo que tengas que pedir
        //Siempre devuelve una string. Es igual que en Python, por lo que ya luego lo convertís a lo que necesitéis.

        //La condición con booleanos es así.
        if(flag == true){ //La condición va entre parentesis
            //Dos peculiaridades extra de Java son los corchetes. Lo que esté dentro de los corchetes, está dentro de este if. Además, los tabuladores no son obligatorios
            System.out.println("He entrado al if");
        } else if(flag == false) { //Y así el else if.
            System.out.println("No he entrado al if");
        }

        //Y ahora utilizando la variable que metimos por teclado...
        if(leido == "entra") {
            System.out.println("Ha entrado");
        }else if(leido == "no entra"){
            System.out.println("No entra");
        }else{ System.out.println("Variable incorrecta");} //Como veis, no es obligatorio el tabulado ni el cambio de línea como en Python.

        //La lectura por teclado no es importante, pues la salida por consola en Java no la vamos a utilizar. Pero está bien que para haceros al cambio de lenguaje, veáis el simil.

        //En cuanto a bucles.
        for (int i=0; i<=10; i++){ //Similar a Python. Esta vez int i=0 es la variable con la que vamos a recorrer el bucle. i<=10 cuándo parará e i++ es el aumento en cada iteración. Podéis usar también i-- para hacer el recorrido a la inversa  o multiples maneras.
            System.out.println("Cuento el valor "+ i);
        }
        //Si queremos usar el bucle for para recorrer una lista como en Python se hace de la siguiente manera.
        List<String> lista = Arrays.asList("1DAW", "1SMR", "2DAW", "2SMR"); //Así creo una lista, necesario el import indicado al principio. Esta vez, la lista tiene que ser de un tipo y ser indicado en el momento de la creación. Como cualquier variable de Java.
        for (String i: lista) System.out.println("El curso " + i + " existe"); //Si el for o el if son relativamente simples, es posible escribirlo de esta manera y omitir los corchetes. El for tiene un String i (String porque lo que tiene la lista dentro son cadenas)
                                                                                // y la lista que se va a recorrer. A este tipo de bucle se le llama foreach.
                                                                                //Hay más usos de for pero con esos bastará para lo básico
        //De igual manera podemos utilizar los bucles while y do while. La diferencia es que el segundo se ejecuta tras comprobar la condición de parada y el primero comprueba la condición al finalizarse.
        a = 0;
        while (a < 10){ //Primero comprueba la condición y como 0 < 10, se ejecuta. Si hubiese valido 10 o más, no se hubiese ejecutado ni una sola vez.
            System.out.println("El valor de a es " + a);
            a++;
        }
        do { //Primero lo hace
            System.out.println("El valor de a es " + a + " y aún así me he ejecutado");
            a++;
        }while(a<10); // Y luego lo comprueba. Por lo que aún siendo 10, se ejecturá el bucle una vez.

        //Una utilidad curiosa que en Python se perdía es el uso del switch case. Es una especie de if múltiple. Como quien selecciona una opción de un menú (de hecho se suele utilizar para esto).
        //Se suele utilizar en conjunto con do while en caso de querer que se repita hasta introducir un fin o algo similar.
        String opcion = new String(); //Inicializada una variable String en blanco. Si no lo haces, el while dará error porque opcion para él no existe de primeras.
        do {
            System.out.println("Introduce la opción que quieras realizar : \n" +
                    "\t- Suma : Sumar 5 + \n" +
                    "\t- Resta :  Restar 10 - 5\n" +
                    "\t- Fin");
            opcion = leer.nextLine();
            switch (opcion.toLowerCase()) { //Convertido a minusculas, no hay nada que quede por inventar, así que sólo tenéis que ver cómo "traducís" código.
                case "suma":
                    System.out.println("El resultado de 5+5 es 10");
                    break; //sino ponemos esto, se ejecutarían todos los cases que hay seguidos, uno tras otro.
                case "resta":
                    System.out.println("El resultado de 10-5 es 5");
                    break;
                case "fin":
                    System.out.println("Acaba el menu");
                    break;
                default: //es un case que se ejecutará en cualquiera de los otros casos que no estén especificados.
                    System.out.println("Opción errónea");
                    break;
            }
        }while(!opcion.toLowerCase().equals("fin")); //otra manera de comparar cadenas. La admiración está negando la comparación.
        //Hasta aquí hemos visto lo general. Faltarían diccionarios, sets, tuplas, rangos...etc. Que tan sólo sería seguir la misma mecánica que hasta ahora, buscando su correspondiente función o sintaxis en Java.
        //Insistir que la manera de trabajar en Java será creando interfaces y programando su lógica de control (funcionamiento), no utilizando la consola. Por lo tanto, acabaremos esta parte de la introducción viendo los logs.
        Logger logger = Logger.getLogger("aprendiendo"); //Inicializado el logger
        FileHandler fh = null; //FileHanlder es un tipo de variable que nos permite crear un log en un archivo. Existe también el ConsoleLogger.
        try { //Aprovechamos este momento para ver el try except de Java. Hay constructores que obligan a usarlos con try except. FileHandler es uno de ellos ya que controla si el archivo existe o no.
            fh = new FileHandler("aprendiendo.log"); //Añado el fichero log. Hay una utilidad en Intellij para sacar fácilmente el path relativo y absoluto de cualquier archivo desde el navegador de proyectos.
        }catch(Exception e) {
        }
        fh.setLevel(Level.ALL); //Indico cuáles niveles de "gravedad" vamos a almacenar en este handler.
        logger.addHandler(fh); //añado el handler al logger.
        logger.info("Hola"); //Añadimos una información al log
        logger.log(Level.WARNING, "CUIDADO!"); //Con esto creamos una entrada al LOG de warning para indicar que algo no va bien, por ejemplo, que no entra a la condición correcta o que un parsing ha fallado.
        /* Si comprobamos el archivo aprendiendo.log veremos que se ha guardado el log en un formato algo extraño. Es XML, un lenaguje extendido de marcas.
        El formato se puede cambiar fácilmente por otro, la información la tenéis en la documentación.
        De manera que esto será como costumbre lo que haremos, en lugar de imprimir por consola ya que no dispondremos siempre de ella y este método nos permite hacer las dos cosas simultaneamente.
        * Esto es otro modo poner comentarios. Es un comentario de bloque y puede ocupar varias lineas*/






        //Esto es para probar nuestro Método Suma.
        int resultado = Metodos.suma(5,3); //Debemos llamar a su clase y luego a su función en concreto. Así podemos agrupar métodos que pueden ser agrupados y luego especificar cuál de ellos. Por ejemplo, podríamos añadir la resta u otros. De manera que todos estén agrupados en algo que les represente.
        System.out.println(resultado);

        //Esto es para probar nuestra clase Alumno
        Alumno Miguel = new Alumno("222222A"); //Creación del alumno Miguel.
        System.out.println("\n\nComprobación clase padre\n" + Miguel.asignaturas); //Si intento acceder al atributo DNI ni siquiera me aparecerá. Para acceder a él deberíamos crear un get para verlo.
        System.out.println(Miguel.getAlumnoDNI()); //Este sería el modo de acceder al DNI
        System.out.println(Miguel.EsProgramador()); //Función a la que voy a hacer Override

        //Esto es para probar nuestra subclase AlumnoDAW
        AlumnoDAW Javi  = new AlumnoDAW("111111B", 10);
        System.out.println("\n\nComprobación clase hijo\n" + Javi.asignaturas); //Javi sigue teniendo las asignaturas, ya que las hereda de la clase padre Alumno
        System.out.println(Javi.EsProgramador()); //Pero su función EsProgramador funciona distinta.

    }
}
