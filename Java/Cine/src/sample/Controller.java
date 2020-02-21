package sample;

import javafx.event.ActionEvent;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;

public class Controller {
    public ImageView butaca00;
    public ImageView butaca01;
    public ImageView butaca02;
    public ImageView butaca03;
    public ImageView butaca10;
    public ImageView butaca11;
    public ImageView butaca12;
    public ImageView butaca13;

    public void cambiar00(MouseEvent mouseEvent) {
        if (butaca00.getId().equals("libre")){
            butaca00.setImage(new Image("sample/Seleccionado.png"));
            butaca00.setId("seleccionado");
        } else if (butaca00.getId().equals("seleccionado")){
            butaca00.setImage(new Image("Libre.png"));
            butaca00.setId("libre");
        }
    }

    public void cambiar01(MouseEvent mouseEvent) {
        if (butaca01.getId().equals("libre")){
            butaca01.setImage(new Image("sample/Seleccionado.png"));
            butaca01.setId("seleccionado");
        } else if (butaca01.getId().equals("seleccionado")){
            butaca01.setImage(new Image("Libre.png"));
            butaca01.setId("libre");
        }
    }

    public void cambiar02(MouseEvent mouseEvent) {
        if (butaca02.getId().equals("libre")){
            butaca02.setImage(new Image("sample/Seleccionado.png"));
            butaca02.setId("seleccionado");
        } else if (butaca02.getId().equals("seleccionado")){
            butaca02.setImage(new Image("Libre.png"));
            butaca02.setId("libre");
        }
    }

    public void cambiar03(MouseEvent mouseEvent) {
        if (butaca03.getId().equals("libre")){
            butaca03.setImage(new Image("sample/Seleccionado.png"));
            butaca03.setId("seleccionado");
        } else if (butaca03.getId().equals("seleccionado")){
            butaca03.setImage(new Image("Libre.png"));
            butaca03.setId("libre");
        }
    }

    public void cambiar10(MouseEvent mouseEvent) {
        if (butaca10.getId().equals("libre")){
            butaca10.setImage(new Image("sample/Seleccionado.png"));
            butaca10.setId("seleccionado");
        } else if (butaca10.getId().equals("seleccionado")){
            butaca00.setImage(new Image("Libre.png"));
            butaca00.setId("libre");
        }
    }

    public void cambiar11(MouseEvent mouseEvent) {
        if (butaca00.getId().equals("libre")){
            butaca00.setImage(new Image("sample/Seleccionado.png"));
            butaca00.setId("seleccionado");
        } else if (butaca00.getId().equals("seleccionado")){
            butaca00.setImage(new Image("Libre.png"));
            butaca00.setId("libre");
        }
    }

    public void cambiar12(MouseEvent mouseEvent) {
        if (butaca00.getId().equals("libre")){
            butaca00.setImage(new Image("sample/Seleccionado.png"));
            butaca00.setId("seleccionado");
        } else if (butaca00.getId().equals("seleccionado")){
            butaca00.setImage(new Image("Libre.png"));
            butaca00.setId("libre");
        }
    }

    public void cambiar13(MouseEvent mouseEvent) {
        if (butaca00.getId().equals("libre")){
            butaca00.setImage(new Image("sample/Seleccionado.png"));
            butaca00.setId("seleccionado");
        } else if (butaca00.getId().equals("seleccionado")){
            butaca00.setImage(new Image("Libre.png"));
            butaca00.setId("libre");
        }
    }

    public void comprar(ActionEvent actionEvent) {
        if (butaca00.getId().equals("seleccionado")){
            butaca00.setImage(new Image("Ocupado.png"));
            butaca00.setId("ocupado");
        }
        if (butaca01.getId().equals("seleccionado")){
            butaca01.setImage(new Image("Ocupado.png"));
            butaca01.setId("ocupado");
        }
        if (butaca02.getId().equals("seleccionado")){
            butaca02.setImage(new Image("Ocupado.png"));
            butaca02.setId("ocupado");
        }
        if (butaca03.getId().equals("seleccionado")){
            butaca03.setImage(new Image("Ocupado.png"));
            butaca03.setId("ocupado");
        }
        if (butaca10.getId().equals("seleccionado")){
            butaca10.setImage(new Image("Ocupado.png"));
            butaca10.setId("ocupado");
        }
        if (butaca11.getId().equals("seleccionado")){
            butaca11.setImage(new Image("Ocupado.png"));
            butaca11.setId("ocupado");
        }
        if (butaca12.getId().equals("seleccionado")){
            butaca12.setImage(new Image("Ocupado.png"));
            butaca12.setId("ocupado");
        }
        if (butaca13.getId().equals("seleccionado")){
            butaca13.setImage(new Image("Ocupado.png"));
            butaca13.setId("ocupado");
        }
    }
}
