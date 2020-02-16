package sample;

import javafx.event.ActionEvent;
import javafx.scene.control.Label;


public class Window2 {
    public Label ventana2;

    public void initialize() {
        String recibir = Controller.notamedia();
        System.out.print("-"+recibir+"-");
        ventana2.setText("/" +recibir+"/");
    }

    public void cerrando(ActionEvent actionEvent) {
    }
}
