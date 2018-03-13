using System;
using System.Collections;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using UnityEngine;

public class Uploadtextscript : MonoBehaviour {

    public string filePath = null;
    public static double[] x = new double[900];
    public static double[] y = new double[900];

    public string filePathMining = null;
    public static double[] xMining = new double[900];
    public static double[] yMining = new double[900];

    public string filePathSlash = null;
    public static double[] xSlash = new double[900];
    public static double[] ySlash = new double[900];

    // Use this for initialization
    void Start () {

        int i = 0;
        string line; 
        System.IO.StreamReader file = new System.IO.StreamReader(filePath);
        while ((line = file.ReadLine()) != null)
        {
            string[] values = line.Split(',');
            y[i] = double.Parse(values[0], CultureInfo.InvariantCulture);
            x[i] = double.Parse(values[1], CultureInfo.InvariantCulture);
            i++;
        }
        //file.Close();


        
        int j = 0;
        file = new System.IO.StreamReader(filePathMining);
        while ((line = file.ReadLine()) != null)
        {
            string[] values = line.Split(',');
            yMining[j] = double.Parse(values[0], CultureInfo.InvariantCulture);
            xMining[j] = double.Parse(values[1], CultureInfo.InvariantCulture);
            j++;
        }
        //fileMining.Close();

        int k = 0;
        file = new System.IO.StreamReader(filePathSlash);
        while ((line = file.ReadLine()) != null)
        {
            string[] values = line.Split(',');
            ySlash[k] = double.Parse(values[0], CultureInfo.InvariantCulture);
            xSlash[k] = double.Parse(values[1], CultureInfo.InvariantCulture);
            k++;
        }
        file.Close();
        //fileMining.Close();
        //fileSlash.Close();

        Debug.Log(x[0] + "," + y[0]);
        Debug.Log(x[1] + "," + y[1]);
        Debug.Log(x[2] + "," + y[2]);
        Debug.Log(x[2] + "," + y[2]);
        Debug.Log(xMining[0] + "," + yMining[0]);
        Debug.Log(xSlash[0] + "," + ySlash[0]);
    }
	
	// Update is called once per frame
	void Update () {
		
	}
}
