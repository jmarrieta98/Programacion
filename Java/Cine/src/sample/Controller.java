package sample;

import javafx.scene.Node;
import javafx.scene.control.Label;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.GridPane;

import java.util.ArrayList;
import java.util.List;

public class Controller {
    public GridPane butacas;
    public List<ImageView> reservado = new ArrayList<>();
    public Label label1;
    public Label label2;
    public Label label3;

    public void cambiar(MouseEvent mouseEvent) {
        ImageView aux = (ImageView) mouseEvent.getSource();
        if (aux.getId().equals("libre")) {
            reservado.add(aux);
            aux.setImage(new Image("sample/Seleccionado.png"));
            aux.setId("seleccionado");
        } else if (aux.getId().equals("seleccionado")) {
            reservado.remove(aux);
            aux.setImage(new Image("Libre.png"));
            aux.setId("libre");
        }
        contar();

    }

    public void comprar() {
        for (ImageView i : reservado) {
            i.setImage(new Image("Ocupado.png"));
            i.setId("ocupado");
        }
        reservado.clear();
        contar();
    }

    public void contar() {
        int contl = 0, conts = 0, conto = 0;
        for (Node i : butacas.getChildren()) {
            if (i.getId().equals("boton")) {
                break;
            } else if (i.getId().equals("libre")) {
                contl++;
            } else if (i.getId().equals("seleccionado")) {
                conts++;
            } else if (i.getId().equals("ocupado")) {
                conto++;
            }
        }
        label1.setText("Sitios libres: " + contl);
        label2.setText("Sitios reservados: " + conts);
        label3.setText("Sitios ocupados: " + conto);
    }
}