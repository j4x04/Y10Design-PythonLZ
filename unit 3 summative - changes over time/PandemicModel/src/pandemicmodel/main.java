/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pandemicmodel;
import java.awt.EventQueue;
import java.util.*;
/**
 *
 * @author leo.zhang
 */
public class main {
    

    
    public static void main(String [] args) {
        
        // main: main method. 
        // Inpt: JAVA INPUT FRAME, TAKES INPUT 
        
        // PandemicModel: OBJECT THAT CONTAINS MAIN SIMULATION PROCESS
        // dayStats: OBJECT (ARRAYLIST) THAT STORES ALL DATA 
        
        // fluSimulationGraph: DISPLAYS FLU SIM
        // measlesSimulationGraph: DISPLAYS MEASLES SIM
        // covidSimulationGraph: DISPLAYS COVID SIM 
        // flattenTheCurve: DISPLAYS COVID FLATTENING CURVE 
        // customSim: DISPLAYS CUSTOM SITUATION SIMULATION
        
        // ALL other JAVA files are TESTING/NOT USED IN MAIN METHOD
        
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Inpt().setVisible(true);
            }
        });
        
        
    }
    
    
    
}
