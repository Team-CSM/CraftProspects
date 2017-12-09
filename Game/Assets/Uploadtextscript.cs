using System;
using System.Collections;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using UnityEngine;

public class Uploadtextscript : MonoBehaviour {

    public string filePath = null;
    public static double[] x = new double[2500];
    public static double[] y = new double[2500];
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

        Debug.Log(x[1500] + "," + y[1500]);
        Debug.Log(x[1600] + "," + y[1600]);
        Debug.Log(x[1700] + "," + y[1700]);
        //System.Console.ReadLine();
    }
	
	// Update is called once per frame
	void Update () {
		
	}
}
