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
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


/**
 *
 * @author leo.zhang
 */

import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.util.*;
public class roughGraph extends JPanel{
    
	public void paint(Graphics g){
            PandemicModel measles = new PandemicModel(1000, 999, 1, 0, 1.7, 0.14);
            measles.simulateDays(100);
            ArrayList<dayStats> model = measles.getModel();
            //g.drawLine(10, 10, 200, 300);	
            for(int i = 0; i<model.size()-1;i++) {
                g.drawLine(10*i, 850-(int)model.get(i).getS(), 10*(i+1), 850-(int)model.get(i+1).getS());
                g.drawLine(10*i, 850-(int)model.get(i).getI(), 10*(i+1), 850-(int)model.get(i+1).getI());
                g.drawLine(10*i, 850-(int)model.get(i).getR(), 10*(i+1), 850-(int)model.get(i+1).getR());
            }
	}
        

}