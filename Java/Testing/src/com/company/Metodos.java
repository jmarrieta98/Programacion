package com.company;
// En Java no hablamos de funciones. Hablamos de métodos. Esto se debe a que una función no existe por si sola, sino que existe enlazada a la clase con su mismo nombre.
public class Metodos { // De manera que este es el nombre de la función, que en realidad se declara como una clase
    public static int suma(int a, int b){ //Debemos decirle qué parámetros recibirá y además su tipo... Por lo que ya en este paso se realiza la validación de datos. Justo antes del main pone int, ya que devolverá un entero.
        //Si devolviese float sería float, o si no devolviese nada, sería void. Así sea cual sea el caso.
        return a+b; //Y este el return al igual que en Python.


    }
}
