package com.company;

/**
 *Metedo que crea las cartas
 * @author Arrieta
 */
public class Carta{

    public String palo;
    public String valor;

    /**
     *
     * @param pal
     * @param val
     */
    public Carta(String pal, String val){
        this.valor = val;
        this.palo = pal;
        System.out.println(this.valor+" "+this.palo);
    }
    @Override
    public String toString() {
        return (this.valor+" de "+this.palo);
    }
}
