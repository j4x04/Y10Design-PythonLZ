/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pandemicmodel;

/**
 *
 * @author leo.zhang
 */

import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.block.BlockBorder;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.chart.plot.XYPlot;
import org.jfree.chart.renderer.xy.XYLineAndShapeRenderer;
import org.jfree.chart.title.TextTitle;
import org.jfree.data.xy.XYDataset;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;

import javax.swing.BorderFactory;
import javax.swing.JFrame;
import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.EventQueue;
import java.awt.Font;

import java.util.*;

public class fluSimulationGraph extends JFrame {

    public fluSimulationGraph() {

        initUI();
    }

    private void initUI() {

        XYDataset dataset = createDataset();
        JFreeChart chart = createChart(dataset);

        ChartPanel chartPanel = new ChartPanel(chart);
        chartPanel.setBorder(BorderFactory.createEmptyBorder(15, 15, 15, 15));
        chartPanel.setBackground(Color.white);
        add(chartPanel);

        pack();
        setTitle("Simulation");
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    private XYDataset createDataset() {

        XYSeries S = new XYSeries("Susceptible");
        XYSeries I = new XYSeries("Infected");
        XYSeries R = new XYSeries("Recovered");
        
        PandemicModel flu = new PandemicModel(1000, 999, 1, 0, 0.29, 0.15); // ACTUAL FLU
        flu.simulateDays(125);
        ArrayList<dayStats> model = flu.getModel();
        
        for(int i = 0; i<model.size(); i++) {
            S.add(i, model.get(i).getS());
        }
        for(int i = 0; i<model.size(); i++) {
            I.add(i, model.get(i).getI());
        }    
        for(int i = 0; i<model.size(); i++) {
            R.add(i, model.get(i).getR());
        } 
        
        
        
        XYSeriesCollection dataset = new XYSeriesCollection();
        dataset.addSeries(S);
        dataset.addSeries(I);
        dataset.addSeries(R);

        return dataset;
    }

    private JFreeChart createChart(XYDataset dataset) {

        JFreeChart chart = ChartFactory.createXYLineChart(
                "SIR MODEL",
                "Day #",
                "# of People",
                dataset,
                PlotOrientation.VERTICAL,
                true,
                true,
                false
        );

        XYPlot plot = chart.getXYPlot();

        XYLineAndShapeRenderer renderer = new XYLineAndShapeRenderer();
        renderer.setSeriesStroke(0, new BasicStroke(3.0f));
        renderer.setSeriesShapesVisible(0,false);
        renderer.setSeriesStroke(1, new BasicStroke(3.0f));
        renderer.setSeriesShapesVisible(1,false);
        renderer.setSeriesStroke(2, new BasicStroke(3.0f));
        renderer.setSeriesShapesVisible(2,false);

        plot.setRenderer(renderer);
        plot.setBackgroundPaint(Color.white);

        plot.setRangeGridlinesVisible(true);
        plot.setRangeGridlinePaint(Color.BLACK);

        plot.setDomainGridlinesVisible(true);
        plot.setDomainGridlinePaint(Color.BLACK);

        chart.getLegend().setFrame(BlockBorder.NONE);

        chart.setTitle(new TextTitle("S-I-R MODEL",
                        new Font("Serif", java.awt.Font.BOLD, 18)
                )
        );

        return chart;
    }

    public static void main(String[] args) {

        EventQueue.invokeLater(() -> {
            fluSimulationGraph ex = new fluSimulationGraph();
            ex.setVisible(true);
        });
    }
}