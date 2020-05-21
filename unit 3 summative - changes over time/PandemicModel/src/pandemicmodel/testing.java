/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pandemicmodel;

import javax.swing.JFrame;

/**
 *
 * @author leo.zhang
 */
public class testing {
    
    
    
    public static void main(String [] args) {
            
        // MODEL FOR THE FLU
        PandemicModel flu = new PandemicModel(1000, 999, 1, 0, 0.29, 0.15);
        flu.simulateDays(100);
        //flu.printData();
        
        
        
        
        // MODEL FOR MEASLES
        PandemicModel measles = new PandemicModel(1000, 999, 1, 0, 1.7, 0.14);
        measles.simulateDays(100);
        //measles.printData();
        
        
        
        // MODEL FOR COVID W/O SOCIAL DISTANCING
        PandemicModel COVID1 = new PandemicModel(37590000, 37460975, 81277, 47748, 1.75, 0.5);
        COVID1.simulateDays(100);
        COVID1.printData();
        
        
        
        
        
        // ROUGH GRAPH FRAME
        /*JFrame frame= new JFrame();	
        frame.getContentPane().add(new roughGraph());
        frame.setSize(1500, 999);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);*/
        
        
        
        
        
        
        
    }
    
    
    
    
}
