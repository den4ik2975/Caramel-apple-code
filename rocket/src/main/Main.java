package main;

import graphics.Window;

import java.awt.*;

public class Main {
    static public void main(String[] args) {

        Window window = new Window();
//        window.getPanel().setBackground(Color.decode(""));
        window.getPanel().setBackground(Color.BLACK);
        window.getPanel().updateUI();
    }
}