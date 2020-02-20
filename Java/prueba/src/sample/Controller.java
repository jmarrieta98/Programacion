package sample;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.stage.Stage;

import java.io.File;
import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;

public class Controller implements Initializable {
    public TextField textfield;
    public Button Button;
    public Controller controller;
    public Label enviar;

    public void llamada(ActionEvent actionEvent) {
        FXMLLoader loader = new FXMLLoader(getClass().getResource("second_view.fxml"));
        try {
            Parent root = (Parent) loader.load();
            SecondController secController = loader.getController();
            secController.myFunction(controller, textfield.getText());
            Stage stage = new Stage();
            stage.setScene(new Scene(root));
            stage.show();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void initialize(URL location, ResourceBundle resources) {
        controller = this;
    }

}
