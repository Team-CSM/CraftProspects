using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;
using UnityEngine.UI;

public class Imageinserter : MonoBehaviour {

    UnityEngine.Object Image;
    GameObject ImageScene; 
    
    public string filePathDir11 = null;
    public string filePathDir12 = null;
    public string filePathDir13 = null;
    public string filePathDir21 = null;
    public string filePathDir22 = null;
    public string filePathDir23 = null;
    public string filePathDir31 = null;
    public string filePathDir32 = null;
    public string filePathDir33 = null;
    public float texwmod;
    public float texhmod;

    public static float texwidth;
    public static float texheight;
    public static Vector3[] array = null;
    public static Rect textrect;


    IEnumerator Start()
    {
        //float count = Timescript.countdown;
        //yield return new WaitForSeconds(1f)

        Insert(filePathDir11,0);

        while (Timescript.round <= 1)
        {
            yield return new WaitForSeconds(0.1f);
        }
        if (Timescript.round == 2)
        {
            Insert(filePathDir12,-1);
        }

        while (Timescript.round <= 2)
        {
            yield return new WaitForSeconds(0.1f);
        }
        if (Timescript.round == 3)
        {
            Insert(filePathDir13,-2);
        }


        while (Timescript.round <= 3)
        {
            yield return new WaitForSeconds(0.1f);
        }
        if (Timescript.round == 4)
        {
            Insert(filePathDir21,-3);
        }

        while (Timescript.round <= 4)
        {
            yield return new WaitForSeconds(0.1f);
        }
        if (Timescript.round == 5)
        {
            Insert(filePathDir22,-4);
        }

        while (Timescript.round <= 5)
        {
            yield return new WaitForSeconds(0.1f);
        }
        if (Timescript.round == 6)
        {
            Insert(filePathDir23,-5);
        }

        while (Timescript.round <= 6)
        {
            yield return new WaitForSeconds(0.1f);
        }
        if (Timescript.round == 7)
        {
            Insert(filePathDir31,-6);
        }

        while (Timescript.round <= 7)
        {
            yield return new WaitForSeconds(0.1f);
        }
        if (Timescript.round == 8)
        {
            Insert(filePathDir32,-7);
        }

        while (Timescript.round <= 8)
        {
            yield return new WaitForSeconds(0.1f);
        }
        if (Timescript.round == 9)
        {
            Insert(filePathDir33,-8);
        }

        /*BoxCollider boxCollider = ImageScene.AddComponent<BoxCollider>();
        //array = SpriteLocalToWorld(spr);
        //textrect = spr.textureRect;
        Collider m_Collider;
        Vector3 m_Size;
        //Fetch the Collider from the GameObject
        m_Collider = ImageScene.GetComponent<Collider>();
        //Fetch the size of the Collider volume
        m_Size = m_Collider.bounds.size;
        //Output to the console the size of the Collider volume
        Debug.Log("Collider Size : " + m_Size);*/
        /*textrect = spr.rect;
        float wwww = spr.pixelsPerUnit;
        Debug.Log("Rect" + wwww);*/

        //ImageScene = Instantiate(Image, new Vector3(x, y, -1), Quaternion.identity) as GameObject;
    }

    /*Vector3[] SpriteLocalToWorld(Sprite sp)
    {
        Vector3 pos = transform.position;
        Vector3[] array = new Vector3[2];
        //top left
        array[0] = pos + sp.bounds.min;
        // Bottom right
        array[1] = pos + sp.bounds.max;
        return array;
    }*/

    void Update () {
        


    }

    void Insert(string filePathDir, float z)
    {
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

        Debug.Log("FILEUPLOADED");
    }
}
