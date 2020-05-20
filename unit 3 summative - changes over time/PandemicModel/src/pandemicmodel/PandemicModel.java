/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pandemicmodel;
import java.util.*;
/**
 *
 * @author leo.zhang
 */
public class PandemicModel {
    
    private double N; // total # of people
    private double S; // susceptible- initial
    private double I; // # infected
    private double R; // recovered
    
    private double B; // % infected per day
    private double Y; // % recovered per day
    
    private double T; // time interval = 1 day
    
    private ArrayList<dayStats> model;
    
    
    
    
    public PandemicModel(double iN, double iS, double iI, double iR, double iB, double iY) { 
        // order: total, susceptible (uninfected), infected, recovered, infection rate, recovery rate
        model = new ArrayList<dayStats>();
        model.add(new dayStats(iN, iS, iI, iR));
        N = iN;
        S = iS; 
        I = iI;
        R = iR;
        
        B = iB;
        Y = iY;
        
        T = 1; 
    }
    
    public static double quadratic(double a, double b, double c) {
        return (( -b ) + Math.sqrt(Math.pow(b, 2) - 4*a*c))/(2*a);
    }
    
    public static double quadratic2(double a, double b, double c) {
        return (( -b ) - Math.sqrt(Math.pow(b, 2) - 4*a*c))/(2*a);
    }

    
    
    
    
    
    
    public double calcNextS(int dayIndex){
        if(dayIndex <= 0 || dayIndex > model.size() || model.get(dayIndex-1) == null) {
            return -1;
        }
        else {
            double temp = model.get(dayIndex-1).getS() - ((model.get(dayIndex-1).getS()/N) * (B*model.get(dayIndex-1).getI()));
            if(temp<= 0) return 0;
            else if(temp>N) return N;
            else return temp;
            
        }
    }
            
    
    
            
    public double calcNextI(int dayIndex) {
        if(dayIndex <= 0 || dayIndex > model.size() || model.get(dayIndex-1) == null || 
                model.get(dayIndex).getS() == -1) {
            return -1;
        }
        else {
            double temp= model.get(dayIndex-1).getI() + ((model.get(dayIndex-1).getS()/N)
                     * (B * model.get(dayIndex-1).getI())) - (model.get(dayIndex-1).getI() * Y);
            if(temp<= 0) return 0;
            else if(temp>N) return N;
            else return temp;
        }
        
    }
    
    
    
    public double calcNextR(int dayIndex) {
        if(dayIndex <= 0 || dayIndex > model.size() || model.get(dayIndex-1) == null || 
                model.get(dayIndex).getI() == -1) {
            return -1;
        }
        else {
            double temp = model.get(dayIndex-1).getR() + (model.get(dayIndex-1).getI() * Y);
            if(temp<= 0) return 0;
            else if(temp>N) return N;
            else return temp;
        }
    }
    
    
    
    //public double getNextR()
    //public boolean checkPeople()
    
    
    
    
    public void simulateDays(int numberofdays) { 
        for(int i = 1; i<numberofdays; i++) {
            model.add(new dayStats(N, calcNextS(i), -1, -1));
            //System.out.print("\nS: " + calcNextS(i));
            model.get(i).setI(calcNextI(i));
            //System.out.print("\tI: " + calcNextI(i));
            model.get(i).setR(calcNextR(i));
            //System.out.print("\t\tR: " + calcNextR(i));
        }
        
    }
    
    
       
    
    
    
    
    public void printData() {
        for(int i = 0; i < model.size(); i++) {
            System.out.print("\n" + (i+1));
            System.out.print("\tS: " + model.get(i).getS());
            System.out.print("\tI: "+ model.get(i).getI());
            System.out.print("\tR: " + model.get(i).getR());
            double temp = model.get(i).getS() + model.get(i).getI() + model.get(i).getR();
            System.out.print("\tN: " + temp);
        }
    }
    
    
    /*public static void main(String [] args) {
        System.out.println(quadratic(1, -998.71, 330.173526));
    }*/

    
    
    
    
    public ArrayList<dayStats> getModel() {
        return model;
    }
        
    
    
    
    
    
    
}
