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
    // Use this for initialization
    void Start () {

        


        int i = 0;
        string line;

        // Read the file and display it line by line.  
        System.IO.StreamReader file = new System.IO.StreamReader(filePath);
        while ((line = file.ReadLine()) != null)
        {
            string[] values = line.Split(',');
            x[i] = double.Parse(values[0], CultureInfo.InvariantCulture);
            y[i] = double.Parse(values[1], CultureInfo.InvariantCulture);
            i++;
        }

        file.Close();

        Debug.Log(x[0] + "," + y[0]);
        Debug.Log(x[1] + "," + y[1]);
        Debug.Log(x[2] + "," + y[2]);
        //System.Console.ReadLine();
    }
	
	// Update is called once per frame
	void Update () {
		
	}
}
