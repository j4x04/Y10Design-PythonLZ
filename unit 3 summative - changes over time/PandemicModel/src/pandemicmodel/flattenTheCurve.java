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

public class flattenTheCurve extends JFrame {

    public flattenTheCurve() {

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

        XYSeries N1 = new XYSeries("Some Social Distancing");
        XYSeries N2 = new XYSeries("More Social Distancing");
        XYSeries N3 = new XYSeries("Ideal Situation");
        
        PandemicModel covid = new PandemicModel(37590000, 37460975, 81277, 47748, 1.4, 0.5); //COVID
        PandemicModel covid2 = new PandemicModel(37590000, 37460975, 81277, 47748, 0.8, 0.5);
        PandemicModel covid3 = new PandemicModel(37590000, 37460975, 81277, 47748, 0.3, 0.5);
        //PandemicModel flu = new PandemicModel(1000, 999, 1, 0, 0.29, 0.15); // ACTUAL FLU
        covid.simulateDays(40);
        covid2.simulateDays(40);
        covid3.simulateDays(40);
        ArrayList<dayStats> model1 = covid.getModel();
        ArrayList<dayStats> model2 = covid2.getModel();
        ArrayList<dayStats> model3 = covid3.getModel();
        
        for(int i = 0; i<model1.size(); i++) {
            N1.add(i, model1.get(i).getI());
        }
        for(int i = 0; i<model2.size(); i++) {
            N2.add(i, model2.get(i).getI());
        }    
        for(int i = 0; i<model3.size(); i++) {
            N3.add(i, model3.get(i).getI());
        } 
        
        
        // printing values 
        /*
        for(int q = 0; q<model1.size(); q++) {
            System.out.print("\n" + q);
            System.out.print("\t" + model1.get(q).getI());
            System.out.print("\t" + model2.get(q).getI());
            System.out.print("\t" + model3.get(q).getI());
        }
*/
        
        
        
        
        
        
        
        XYSeriesCollection dataset = new XYSeriesCollection();
        dataset.addSeries(N1);
        dataset.addSeries(N2);
        dataset.addSeries(N3);

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

        chart.setTitle(new TextTitle("Flattening the Curve",
                        new Font("Serif", java.awt.Font.BOLD, 18)
                )
        );

        return chart;
    }

    public static void main(String[] args) {

        EventQueue.invokeLater(() -> {
            flattenTheCurve ex = new flattenTheCurve();
            ex.setVisible(true);
        });
    }
}