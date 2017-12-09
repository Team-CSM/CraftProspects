using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;
using UnityEngine.UI;

public class Imageinserter : MonoBehaviour {

    public UnityEngine.Object Image;
    public GameObject ImageScene; 
    public string filePathDir = null;
    public static float texwidth;
    public static float texheight;
    public float texwmod;
    public float texhmod;


    void Start()
    {
        float count = Timescript.countdown;
        //yield return new WaitForSeconds(1f

        var rand = new System.Random();
        var files = Directory.GetFiles(filePathDir/*, "*.jpg"*/);
        string filePath = files[rand.Next(files.Length)];

        ImageScene = new GameObject("ImageScene"+count);
        ImageScene.AddComponent(typeof(SpriteRenderer));

        Texture2D tex = null;
        byte[] fileData;

        if (File.Exists(filePath))
        {
            fileData = File.ReadAllBytes(filePath);
            tex = new Texture2D(0,0);
            tex.LoadImage(fileData);
            Debug.Log("EXISTS");
        }

        texwidth = texwmod*tex.width;
        texheight = texhmod*tex.height;

        //Texture2D texobject = Image as Texture2D;

        Rect rec = new Rect(0, 0, tex.width, tex.height);
        Vector2 vec = new Vector2(0.5f, 0.5f);
        Sprite spr = Sprite.Create(tex, rec, vec);
        ImageScene.GetComponent<SpriteRenderer>().sprite = spr;

        Vector3 scale = new Vector3(texwmod, texhmod, 0);
        ImageScene.GetComponent<Transform>().localScale = scale;
           
        Debug.Log("LOOPED");
            
        


        
        
        //ImageScene = Instantiate(Image, new Vector3(x, y, -1), Quaternion.identity) as GameObject;
    }

    void Update () {
        //ImageScene.transform.Translate(Vector3.left * Time.deltaTime * speed);
    }
}
