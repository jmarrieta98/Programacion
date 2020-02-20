package com.company;

import java.util.ArrayList;
import java.util.List;

public class Mano{
    public List<Carta> cartas;
    public int valortotal;
    public Mano(){
        this.cartas = new ArrayList<>();
        this.valortotal = 0;
    }

    public void cogercarta(Mazo mazo) {
        this.cartas.add(mazo.darCarta());
        this.calcularvalortotal();
    }

    public void calcularvalortotal() {
        String valor = this.cartas.get(this.cartas.size()-1).valor;
        switch (valor){
            case "Sota": case "Reina": case "Rey": this.valortotal += 10; break;
            case "As":
                if (this.valortotal + 11 > 21){
                    this.valortotal +=1;
                }else {
                    this.valortotal +=11;
                }
                break;
            case "2": case "3": case "4": case "5": case "6": case "7": case "8": case "9": case "10":
                int numero = Integer.parseInt(valor);
                this.valortotal += numero;
                break;
        }
    }
}