package com.company;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import static com.company.Main.listaDePalos;
import static com.company.Main.listaDeValores;

/**
 * Metodo que crea el mazo de las cartas
 * @author Arrieta
 */
public class Mazo{
    public List<Carta> cartas = new ArrayList<>();
    public Mazo(){
        for (String palo:listaDePalos) {
            for (String valor:listaDeValores) {
                Carta x = new Carta(palo,valor);
                this.cartas.add(x);
            }
        }
        this.mezclar();
    }

    /**
     *Metodo que imprime el mazo
     * @return Mazo impreso
     */
    @Override
    public String toString() {
        String imprimir = "";
        for (Carta carta : cartas) {
            imprimir += " " + carta + "\n";
        }
        return (imprimir);
    }

    /**
     * Metodo que mezcla las cartas en el mazo
     */
    public void mezclar(){
        int ncartas = this.cartas.size();
        Random r = new Random();
        Carta aux1, aux2;
        for(int i = 0; i<ncartas; i++){
            int n = r.nextInt(ncartas);
            aux1 = this.cartas.get(i);
            aux2 = this.cartas.get(n);
            this.cartas.set(i,aux2);
            this.cartas.set(n,aux1);
        }
    }

    public Carta darCarta(){
        return this.cartas.remove(0);
    }
}
