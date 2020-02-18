package sample;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

import java.io.IOException;

public class Controller {
    @FXML
    public TextField textfield;
    public Button Button;

    @FXML
    public void llamada(ActionEvent actionEvent) {
        FXMLLoader loader = new FXMLLoader(getClass().getResource("second_view.fxml"));
        try {
            Parent root = (Parent) loader.load();
            SecondController secController = loader.getController();
            secController.myFunction(textfield.getText());
            Stage stage = new Stage();
            stage.setScene(new Scene(root));
            stage.show();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
