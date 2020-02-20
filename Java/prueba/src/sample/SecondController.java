package sample;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.stage.Stage;

import java.net.URL;
import java.util.ResourceBundle;

public class SecondController implements Initializable {
    public Label label;
    public Controller controlador;
    public Button secbutton;

    @Override
    public void initialize(URL location, ResourceBundle resources) {

    }
    public void myFunction(Controller ConPadre, String text){
        controlador = ConPadre;
        label.setText(text);
    }

    public void devolver(ActionEvent actionEvent) {
        controlador.enviar.setText("Has cerrado la ventana");
        Stage stage = (Stage) secbutton.getScene().getWindow();
        stage.close();
    }
}
