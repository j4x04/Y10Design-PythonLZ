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
public class dayStats {
    
    private double N, S, I, R;
        
    public dayStats(double iN, double iS, double iI, double iR) {
        N = iN;
        S = iS;
        I = iI;
        R = iR; 
    }
    
    public double getS() {
        return S;
    }
    public void setS(double newS) {
        S = newS;
    }
    
    
    
    public double getI() {
        return I;
    }
    public void setI(double newI) {
        I = newI;
    }
    
    
    
    public double getR() {
        return R;
    }
    public void setR(double newR) {
        R = newR;
    }
    
    
    
    public double getN() {
        return N;
    }
        
    
    
    
    
    
    
    
}
