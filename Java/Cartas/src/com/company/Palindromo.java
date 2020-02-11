package com.company;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Main {

    public static void main(String[] args) {
        List<String> palabras = Arrays.asList("Hola", "rallar", "ala", "coma");
        List<String> imprimir;
        imprimir = Palindromos(palabras);
        for (String i : imprimir) System.out.println(i);
    }

    public static List<String> Palindromos(List<String> palabras) {
        List<String> palindromo = new ArrayList<>();
        StringBuilder Reverso = new StringBuilder();
        for (String palabra : palabras) {
            Reverso.append(palabra).reverse();
            if (palabra.equals(Reverso.toString())) palindromo.add(palabra);
            Reverso.setLength(0);
        }
        return palindromo;
    }
}