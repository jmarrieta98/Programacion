package com.company;

public class Equipo{
    public String nombre;
    public  int pj = 0, pg = 0, pp = 0, pf = 0, pc = 0, m=0;

    public Equipo(String nombre){
        this.nombre = nombre;
    }

    @Override
    public String toString() {
        return this.nombre+'\t'+this.pj+'\t'+this.pg+'\t'+this.pp+'\t'+this.pf+'\t'+this.pc+'\t'+this.m;
    }
}
