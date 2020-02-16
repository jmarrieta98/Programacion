package com.company;

import java.util.Arrays;
import java.util.List;

class Main {

    public static void main(final String[] args) {
        final List<String> palabras = Arrays.asList("Hola", "rallar", "ala", "coma");
        List<String> imprimir;
        imprimir = Palindromos(palabras);
        for (final String i : imprimir) System.out.println(i);
    }

    public static List<String> Palindromos(final List<String> palabras) {
        final List<String> palindromo = null;
        final StringBuilder Reverso = new StringBuilder();
        for (final String palabra : palabras) {
            Reverso.append(palabra).reverse();
            if (palabra.equals(Reverso.toString())) palindromo.add(palabra);
            Reverso.setLength(0);
        }
        return palindromo;
    }
}