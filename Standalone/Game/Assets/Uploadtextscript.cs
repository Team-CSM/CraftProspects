using System;
using System.Collections;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using UnityEngine;

public class Uploadtextscript : MonoBehaviour {


    /// <summary>
    /// The log file is an output of the launcher that tells the game where the directory containing the images and text files are store.
    /// The file paths below that are the relative file path after the file path in the log file.
    /// Arrays are created to store the coordinates from the text files.
    /// </summary>


    public string logfile = null;

    public string filePathA = null;
    public static double[] x = new double[900];
    public static double[] y = new double[900];

    public string filePathMiningA = null;
    public static double[] xMining = new double[900];
    public static double[] yMining = new double[900];

    public string filePathSlashA = null;
    public static double[] xSlash = new double[900];
    public static double[] ySlash = new double[900];

    // Use this for initialization
    void Start () {

        /// <summary>
        /// Text files are read and their coordinates are added to their respective arrays.
        /// X and Y coordinates are seperated with commas (,) and each set is seperated with an underscore (_).
        /// String is then converted to double and added to array.
        /// </summary>

        System.IO.StreamReader filelog = new System.IO.StreamReader(logfile);
        string log = "./FileAssets/";
        log = filelog.ReadLine();

        Debug.Log(log);

        string filePath = log + filePathA;
        string filePathMining = log + filePathMiningA;
        string filePathSlash = log + filePathSlashA;

        Debug.Log(filePath);

        int i = 0;
        string line; 
        System.IO.StreamReader file = new System.IO.StreamReader(filePath);
        if ((line = file.ReadLine()) != null)
        {
            string[] splitline = line.Split('_');
            Debug.Log("LENGTH"+splitline.Length);
            while (i < splitline.Length-1)
            {
                string[] values = splitline[i].Split(',');
                //Debug.Log("Splitted "+values[0]+","+values[1]);
                y[i] = double.Parse(values[0], CultureInfo.InvariantCulture);
                x[i] = double.Parse(values[1], CultureInfo.InvariantCulture);
                i++;
            }
            Debug.Log("While Completed");
        }
        //file.Close();
        


        int j = 0;
        file = new System.IO.StreamReader(filePathMining);
        if ((line = file.ReadLine()) != null)
        {
            string[] splitline = line.Split('_');
            while (j < splitline.Length-1)
            {
                string[] values = splitline[j].Split(',');
                yMining[j] = double.Parse(values[0], CultureInfo.InvariantCulture);
                xMining[j] = double.Parse(values[1], CultureInfo.InvariantCulture);
                j++;
            }
        }
        //fileMining.Close();

        int k = 0;
        file = new System.IO.StreamReader(filePathSlash);
        if ((line = file.ReadLine()) != null)
        {
            string[] splitline = line.Split('_');
            while (k < splitline.Length-1)
            {
                string[] values = splitline[k].Split(',');
                ySlash[k] = double.Parse(values[0], CultureInfo.InvariantCulture);
                xSlash[k] = double.Parse(values[1], CultureInfo.InvariantCulture);
                k++;
            }
        }
        file.Close();
        //fileMining.Close();
        //fileSlash.Close();

        Debug.Log(x[0] + "," + y[0]);
        Debug.Log(x[1] + "," + y[1]);
        Debug.Log(x[2] + "," + y[2]);
        Debug.Log(xMining[0] + "," + yMining[0]);
        Debug.Log(xSlash[0] + "," + ySlash[0]);
    }
	
	// Update is called once per frame
	void Update () {
		
	}
}
