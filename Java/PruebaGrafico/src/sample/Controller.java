package sample;

import javafx.beans.binding.Bindings;
import javafx.event.ActionEvent;
import javafx.scene.control.ComboBox;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;

import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import static java.lang.Math.round;

public class Controller {

    public ComboBox PFOL;
    public ComboBox PLM;
    public ComboBox PSI;
    public ComboBox PBD;
    public ComboBox PED;
    public ComboBox PPRO;
    public TextField nombre;
    public TextField apellidos;
    public Label resultado;
    public DecimalFormat df = new DecimalFormat("##.##");

    public void notamedia(ActionEvent actionEvent) {
        ArrayList<Integer> listanotas = new ArrayList<>();
        String nom = nombre.getText();
        String ap = apellidos.getText();
        float media = 0;
        listanotas.add(Integer.parseInt(PFOL.getSelectionModel().getSelectedItem().toString()));
        listanotas.add(Integer.parseInt(PLM.getSelectionModel().getSelectedItem().toString()));
        listanotas.add(Integer.parseInt(PSI.getSelectionModel().getSelectedItem().toString()));
        listanotas.add(Integer.parseInt(PBD.getSelectionModel().getSelectedItem().toString()));
        listanotas.add(Integer.parseInt(PED.getSelectionModel().getSelectedItem().toString()));
        listanotas.add(Integer.parseInt(PPRO.getSelectionModel().getSelectedItem().toString()));
        for (int nota : listanotas) media+=nota;
        media/=listanotas.size();
        String numCadena = df.format(media);

        if (media >= 5){
            resultado.setText(nom+" "+ap+" ha aprobado con "+numCadena);
        }else{
            resultado.setText(nom+" "+ap+" ha suspendido con "+numCadena);
        }

    }
}
