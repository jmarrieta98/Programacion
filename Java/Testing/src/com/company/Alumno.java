package com.company;

//Lo que gira en torno a clases en comparación con Python es mucho mayor. Tendréis que aprender más cosas pero también le veréis más utilidades.
//La primera de las utilidades. Atributos, clases y métodos públicos o privados. Los segundos son los más restrictivos, y sólo esa misma clase podrá acceder a ellos.
//Hay otros dos tipos más, package y protected. El primero es para que se pueda usar desde el mismo paquete, osea proyecto. Y protected también puede acceder desde clases que hereden de esta.
//Tenéis numerosos recursos de "modificadores" (que es como se llama técnicamente) en internet para utilizar el que más os convenga en cada momento.

import javafx.util.Pair;

import java.util.Arrays;
import java.util.List;

import static javafx.util.Pair.*;


public class Alumno { //Esta es la inicialización de la clase. Al ser pública, cualquiera que tenga acceso al módulo o lo importe, podrá hacer uso de ella.
    private String AlumnoDNI; //A diferencia de Python, no hace falta inicializarlas.Este atributo sólo lo puede usar esta clase.
    public double media;
    public List<Pair<String, Integer>> asignaturas; //Podemos crear listas de tuplas como esta anidandolas.

    public Alumno(String DNI) {
        //Este es el constructor
        AlumnoDNI = DNI;
        asignaturas = Arrays.asList(new Pair<String, Integer>("Programación", 0), new Pair<String, Integer>("Entornos", 0)); //Ya sabéis que al anidar estructuras de datos, se vuelve un poco caótico.
        media = 0;
    }

    public Alumno(){ //A esto se le llama sobrecarga. Hay dos constructores y se ejecutará uno u otro, en función de si recibe un parametro o ninguno.
        AlumnoDNI = "Desconocido";
    }
    public String getAlumnoDNI() {
        //Esta es la única manera de acceder al DNI y obtenerlo. Si no existiera, no se podría saber. Eso ya es decisión del programador.
        //Si se quisiera cambiar, haría falta el setter de igual forma.
        return AlumnoDNI;
    }
    public String EsProgramador(){
        //Crearemos esta función para terminar de ver un concepto de clases junto a la herencia.
        return "No se sabe"; //Devolveremos que no sabemos si es programador.
    }
}

//La herencia es algo que hemos visto en Python, en Java se realiza de igual manera pero con una sintaxis distinta.
class AlumnoDAW extends Alumno{ //extends nos dirá que AlumnoDAW es hijo de Alumno
    int nivelProgramacion = 0;
    public AlumnoDAW(String DNI, int nivelProgramacion){
        //ESte es el constructor. Pero en vez de escribir lo mismo, podemos llamar a la función constructor del padre con super();
        super(DNI);
        //Y luego hacer lo que necesitemos extra.
        this.nivelProgramacion = nivelProgramacion; //Podemos utilizar this, al igual que self en Python.
    }

    //Ahora si queremos devolver su nivel de programacion cuando llamemos a EsProgramador(), sin embargo, esa función ya existe porque al tiene el padre.
    //Llega el momento de utilizar el Override, con la cual podremos redefinir la función.

    @Override
    public String EsProgramador(){ //Intellij te añade unas marcas a la izquierda cuando un método se le ha hecho override.
        return "Es un programador de nivel " + nivelProgramacion;
    }




}