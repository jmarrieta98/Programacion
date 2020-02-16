package sample;


import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.ComboBox;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

import java.io.IOException;
import java.text.DecimalFormat;
import java.util.ArrayList;


public class Controller {

    private static String mensaje2;
    public static String mensaje;
    public static ComboBox PFOL;
    public static ComboBox PLM;
    public static ComboBox PSI;
    public static ComboBox PBD;
    public static ComboBox PED;
    public static ComboBox PPRO;
    public static TextField nombre;
    public static TextField apellidos;
    public static DecimalFormat df = new DecimalFormat("##.##");
    public Controller() throws IOException { }

    public static String notamedia() {
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
        Parent root = new Parent(){};
        try {
            root = FXMLLoader.load(Controller.class.getResource("window2.fxml"));
        } catch (IOException e) {
            e.printStackTrace();
        }
        Scene newScene;
        newScene = new Scene(root,700,700);
        Stage newWindow = new Stage();
        newWindow.setTitle("Resultado");
        newWindow.setScene(newScene);
        newWindow.show();
        if (media >= 5){
            mensaje = (nom+" "+ap+" ha aprobado con "+numCadena);

        }else{
            mensaje = (nom+" "+ap+" ha suspendido con "+numCadena);
        }
        return mensaje;
    }
}
