/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pandemicmodel;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;

import java.util.*;
/**
 *
 * @author leo.zhang
 */
/**
 * This program demonstrates how to draw XY line chart with XYDataset
 * using JFreechart library.
 * @author www.codejava.net
 *
 */
public class secondGraph extends JFrame {
 
    public secondGraph() {
        super("second try at making a graph");
 
        JPanel chartPanel = createChartPanel();
        add(chartPanel, BorderLayout.CENTER);
 
        setSize(640, 480);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
    }
 
    private JPanel createChartPanel() {
        // creates a line chart object
        // returns the chart panel
    }
 
    private XYDataset createDataset() {
        // creates an XY dataset...
        // returns the dataset
    }
 
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new XYLineChartExample().setVisible(true);
            }
        });
    }
}