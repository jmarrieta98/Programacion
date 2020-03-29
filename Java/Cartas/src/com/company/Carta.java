package com.company;

public class Carta{

    public String palo;
    public String valor;
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
