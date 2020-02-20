package com.company;

import java.text.ParseException;
import java.util.*;

import static com.company.Main.listaDePalos;
import static com.company.Main.listaDeValores;

public class Main {

    public static List<String> listaDePalos = Arrays.asList("Tréboles","Diamantes","Corazones","Picas");
    public static List<String> listaDeValores =  Arrays.asList("As","2","3","4","5","6","7","8","9","10","Sota","Reina","Rey");

    public static void main(String[] args) {
        Mazo mazo = new Mazo();
        Mano jugador = new Mano();
        Mano maquina = new Mano();
        Scanner leer = new Scanner(System.in);
        jugador.cogercarta(mazo);
        System.out.println("Tu carta es "+jugador.cartas.get(0).toString()+" y el valor total es "+jugador.valortotal);
        while (true){
            if(!player(leer, jugador, mazo)){
                break;
            }
            if (jugador.valortotal >= 21) {break;}
        }
        do {
            maquina.cogercarta(mazo);
        } while (maquina.valortotal < 18);
        comprobar(jugador,maquina);
    }
    public static void comprobar(Mano jugador, Mano maquina){
     if (jugador.valortotal > 21){
         System.out.println("Has perdido, te has pasado :(");

     }else if (jugador.valortotal == 21 && maquina.valortotal == 21){
         System.out.println("Empate a blackjack");
     }else if (jugador.valortotal ==21 && (maquina.valortotal != 21)){
         System.out.println("Blacjack, has ganado");
     } else if (jugador.valortotal <21 && maquina.valortotal == 21){
         System.out.println("Has perdido, blackjack de la maquina");
     }else if (jugador.valortotal < 21 && maquina.valortotal < 21){
         if (jugador.valortotal < maquina.valortotal){
             System.out.println("Has ganado, estas mas cerca del blackjack que la maquina");
         }
         else if (jugador.valortotal < maquina.valortotal){
             System.out.println("Has perdido, la maquina se ha acercado mas al blackjack");
         }
         else{
             System.out.println("Empate");
         }
     }
     System.out.println("Jugador "+jugador.valortotal+" Máquina "+maquina.valortotal);
    }

    public static Boolean player(Scanner leer, Mano jugador, Mazo mazo) {
        System.out.print("¿Desea coger otra carta?\t");
        String opcion = leer.nextLine();
        switch (opcion.toLowerCase()){
            case "si":
            jugador.cogercarta(mazo);
            System.out.print("Tus cartas son ");
            for (Carta i:jugador.cartas) {
                    System.out.print(i+", ");
                }
            System.out.println("\nValor total: "+jugador.valortotal);
                return true;
            case "no":
                return false;
            default:
                System.out.println("Opcion errónea");
                return true;
        }

    }
}