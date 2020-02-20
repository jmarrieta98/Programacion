package com.company;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import static com.company.Main.listaDePalos;
import static com.company.Main.listaDeValores;

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

    @Override
    public String toString() {
        String imprimir = "";
        for (Carta carta : cartas) {
            imprimir += " " + carta + "\n";
        }
        return (imprimir);
    }

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
