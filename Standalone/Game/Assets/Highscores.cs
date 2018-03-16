using System;
using System.Collections;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class Highscores : MonoBehaviour
{

    /// <summary>
    /// High scores are stored on a text file externally.
    /// Data is retrieved and the top 5 scores in the text file are shown on the text asset.
    /// Default score is 0.
    /// </summary>

    public string filePath = null;
    public static double[] x = new double[100];
    // Use this for initialization
    void Start()
    {
        
        System.IO.StreamReader file = new System.IO.StreamReader(filePath);
        string line = file.ReadLine();
        string[] values = line.Split(',');

        Debug.Log(values[0]);
        Debug.Log(values[1]);

        for (int i = 0; i < values.Length; i++)
        {
            Double.TryParse(values[i], out x[i]);
        }

        Array.Sort(x);
        Array.Reverse(x);
        Debug.Log(x[1]);

        for (int j = 0; j < 5; j++)
        {
            Debug.Log("looping");
            string text = x[j].ToString();
            string oldtext = GameObject.Find("Texths").GetComponent<Text>().text;
            string final = oldtext + "\n" + text;
            GameObject.Find("Texths").GetComponent<Text>().text = final;
        }
    }

    void Update()
    {

    }
}
