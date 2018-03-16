using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;
using UnityEngine.UI;

public class Imageinserter : MonoBehaviour {

    UnityEngine.Object Image;
    GameObject ImageScene;

    /// <summary>
    /// The log file is an output of the launcher that tells the game where the directory containing the images and text files are store.
    /// The file paths below that are the relative file path after the file path in the log file.
    /// The rest of the variables are there for testing purposes.
    /// </summary>

    public string logfile = null;

    public string filePathDir11A = null;
    public string filePathDir12A = null;
    public string filePathDir13A = null;
    public string filePathDir21A = null;
    public string filePathDir22A = null;
    public string filePathDir23A = null;
    public string filePathDir31A = null;
    public string filePathDir32A = null;
    public string filePathDir33A = null;
    public float texwmod;
    public float texhmod;

    public static float texwidth;
    public static float texheight;
    public static Vector3[] array = null;
    public static Rect textrect;


    IEnumerator Start()
    {


        /// <summary>
        /// File path from log file and relative paths are combined.
        /// Debug logs are important to make sure the images are being uploaded properly.
        /// </summary>

        System.IO.StreamReader filelog = new System.IO.StreamReader(logfile);
        string log = "./FileAssets/";
        log = filelog.ReadLine();

        Debug.Log(log);

        string filePathDir11 = log + filePathDir11A;
        string filePathDir12 = log + filePathDir12A;
        string filePathDir13 = log + filePathDir13A;
        string filePathDir21 = log + filePathDir21A;
        string filePathDir22 = log + filePathDir22A;
        string filePathDir23 = log + filePathDir23A;
        string filePathDir31 = log + filePathDir31A;
        string filePathDir32 = log + filePathDir32A;
        string filePathDir33 = log + filePathDir33A;

        Debug.Log(filePathDir11);


        /// <summary>
        /// The insert method adds the image from the file path to the game.
        /// When a round increases, a new image is inserted with a slightly higher Z coordinate so that it appears infront of the previous image.
        /// </summary>

        Insert(filePathDir11,0);

        while (Timescript.round <= 1)
        {
            yield return new WaitForSeconds(0.1f);
        }
        if (Timescript.round == 2)
        {
            Insert(filePathDir12,-0.1f);
        }

        while (Timescript.round <= 2)
        {
            yield return new WaitForSeconds(0.1f);
        }
        if (Timescript.round == 3)
        {
            Insert(filePathDir13,-0.2f);
        }

        while (Timescript.round <= 3)
        {
            yield return new WaitForSeconds(0.1f);
        }
        if (Timescript.round == 4)
        {
            Insert(filePathDir21,-0.3f);
        }

        while (Timescript.round <= 4)
        {
            yield return new WaitForSeconds(0.1f);
        }
        if (Timescript.round == 5)
        {
            Insert(filePathDir22,-0.4f);
        }

        while (Timescript.round <= 5)
        {
            yield return new WaitForSeconds(0.1f);
        }
        if (Timescript.round == 6)
        {
            Insert(filePathDir23,-0.5f);
        }

        while (Timescript.round <= 6)
        {
            yield return new WaitForSeconds(0.1f);
        }
        if (Timescript.round == 7)
        {
            Insert(filePathDir31,-0.6f);
        }

        while (Timescript.round <= 7)
        {
            yield return new WaitForSeconds(0.1f);
        }
        if (Timescript.round == 8)
        {
            Insert(filePathDir32,-0.7f);
        }

        while (Timescript.round <= 8)
        {
            yield return new WaitForSeconds(0.1f);
        }
        if (Timescript.round == 9)
        {
            Insert(filePathDir33,-0.8f);
        }

    }



    void Update () {
        


    }

    void Insert(string filePathDir, float z)

    {

        /// <summary>
        /// Insert takes image file path and Z coordinate as input.
        /// A lot of the follwing code is required to convert the image file into a sprite format
        /// An object is created, and then a 'Sprite Renderer' component is added to the newly created object.
        /// The image, now converted into sprite format, is applied to the sprite renderer component
        /// The size of the image is altered depending on the screen size.
        /// </summary>

        var rand = new System.Random();
        var files = Directory.GetFiles(filePathDir/*, "*.jpg"*/);
        string filePath = files[rand.Next(files.Length)];

        ImageScene = new GameObject("ImageScene");
        ImageScene.AddComponent(typeof(SpriteRenderer));

        Texture2D tex = null;
        byte[] fileData;

        if (File.Exists(filePath))
        {
            fileData = File.ReadAllBytes(filePath);
            tex = new Texture2D(0, 0);
            tex.LoadImage(fileData);
            Debug.Log("EXISTS");
        }

        texwmod = 1503f / tex.width;
        texhmod = 1074f / tex.height;

        texwidth = texwmod * tex.width;
        texheight = texhmod * tex.height;

        Rect rec = new Rect(0, 0, tex.width, tex.height);
        Vector2 vec = new Vector2(0.5f, 0.5f);
        Sprite spr = Sprite.Create(tex, rec, vec);
        ImageScene.GetComponent<SpriteRenderer>().sprite = spr;

        Vector3 scale = new Vector3(texwmod, texhmod, 0);
        ImageScene.GetComponent<Transform>().localScale = scale;

        Vector3 pos = new Vector3(0, 0, z);
        ImageScene.GetComponent<Transform>().position = pos;

        Debug.Log(texwmod+" times " +texhmod);
    }
}
