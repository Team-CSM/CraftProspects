﻿using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Clicklocation : MonoBehaviour
{

    public double range = 1;
    public GameObject cross;
    public UnityEngine.Object crossImage;
    public UnityEngine.Object miningImage;
    public UnityEngine.Object slashImage;
    static int counter = 0;
    // Use this for initialization
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetMouseButtonDown(0))
        {
            Vector3 mouseVec = Input.mousePosition;

            Resolution screen = Screen.currentResolution;
            float screenHeight = (float)Screen.height;
            float screenWidth = (float)Screen.width;
            Debug.Log("SCREEN: " + screenHeight + "x" + screenWidth);

            float mapHeight = screenHeight;
            float mapWidth = mapHeight * 1.4f;

            float unitHeight = mapHeight / 9;
            float unitWidth = mapWidth / 9;

            /*Rect textrect = Imageinserter.textrect;
            float xtest = textrect.width;
            float ytest = textrect.height;
            Debug.Log("TEX: " + xtest + "x" + ytest);*/

            //float transformedx = (float)Math.Ceiling((mouseVec.x - 175) / 15.86);
            //float transformedy = (float)Math.Ceiling((585-mouseVec.y) / 12);

            float transformedx = (float)Math.Ceiling(((mouseVec.x - ((screenWidth - mapWidth - unitWidth) * 0.5)) / unitWidth) + GlobalControl.modifierx);
            float transformedy = (float)Math.Ceiling(((mapHeight - mouseVec.y) / unitHeight) + 0.5 + GlobalControl.modifiery);

            Vector3 mouseTran = new Vector3(transformedx, transformedy, 0);

            string mousePos = mouseTran.ToString();

            Debug.Log("Clicked pos:" + mouseVec);
            Debug.Log("Clicked cord:" + mousePos);


            /*for (int b = 0; b < 31; b++)
            {
                transformedx = b;
                for (int c = 0; c < 31; c++)
                {
                    transformedy = c;
                    mouseTran = new Vector3(transformedx, transformedy, 0);*/

                    for (int i = 0; i < 900; i++)
                    {
                        if (Uploadtextscript.x[i] != 0 && Uploadtextscript.y[i] != 0 && (Uploadtextscript.x[i] - range) < mouseTran.x && mouseTran.x < (Uploadtextscript.x[i] + range) && (Uploadtextscript.y[i] - range) < mouseTran.y && mouseTran.y < (Uploadtextscript.y[i] + range))
                        {

                            GlobalControl.score++;
                            GameObject.Find("Text").GetComponent<Text>().text = "Total Score = " + GlobalControl.score;
                            Uploadtextscript.x[i] = 0;
                            Uploadtextscript.y[i] = 0;
                            Debug.Log("SCORE");

                            cross = new GameObject("Cross" + counter);
                            cross.AddComponent(typeof(SpriteRenderer));
                            Texture2D tex = crossImage as Texture2D;
                            Sprite crossSprite = Sprite.Create(tex, new Rect(0f, 0f, tex.width, tex.height), Vector2.zero);
                            cross.GetComponent<SpriteRenderer>().sprite = crossSprite;

                            Vector3 scale = new Vector3(0.27f, 0.22f, 0);
                            cross.GetComponent<Transform>().localScale = scale;

                            //float crossx = (float)(((transformedx - ((screenWidth - mapWidth - unitWidth) * 0.5)) / unitWidth) - GlobalControl.modifierx);
                            //float crossy = (float)(mapHeight - ((transformedy - 0.5 - GlobalControl.modifiery) * unitHeight));
                            float crossx = -8.45f + (0.50f * ((transformedx - GlobalControl.modifierx) * (50 / 15) - 1f));
                            float crossy = -12.65f + (0.36f * (50 - ((transformedy - GlobalControl.modifiery) * (50 / 15))));


                            Vector3 position = new Vector3(crossx, crossy, (-Timescript.round + 0.5f));
                            cross.GetComponent<Transform>().position = position;

                            counter++;
                            break;
                        }

                        if (Uploadtextscript.xMining[i] != 0 && Uploadtextscript.yMining[i] != 0)
                        {
                            if ((Uploadtextscript.xMining[i] - range) < mouseTran.x && mouseTran.x < (Uploadtextscript.xMining[i] + range))
                            {
                                if ((Uploadtextscript.yMining[i] - range) < mouseTran.y && mouseTran.y < (Uploadtextscript.yMining[i] + range))
                                {
                                    GlobalControl.score++;
                                    GlobalControl.score++;
                                    GameObject.Find("Text").GetComponent<Text>().text = "Total Score = " + GlobalControl.score;
                                    Uploadtextscript.xMining[i] = 0;
                                    Uploadtextscript.yMining[i] = 0;
                                    Debug.Log("SCORE");

                                    cross = new GameObject("Cross" + counter);
                                    cross.AddComponent(typeof(SpriteRenderer));
                                    Texture2D tex = miningImage as Texture2D;
                                    Sprite crossSprite = Sprite.Create(tex, new Rect(0f, 0f, tex.width, tex.height), Vector2.zero);
                                    cross.GetComponent<SpriteRenderer>().sprite = crossSprite;

                                    Vector3 scale = new Vector3(0.27f, 0.22f, 0);
                                    cross.GetComponent<Transform>().localScale = scale;

                                    //float crossx = (float)(((transformedx - ((screenWidth - mapWidth - unitWidth) * 0.5)) / unitWidth) - GlobalControl.modifierx);
                                    //float crossy = (float)(mapHeight - ((transformedy - 0.5 - GlobalControl.modifiery) * unitHeight));
                                    float crossx = -8.45f + (0.50f * ((transformedx - GlobalControl.modifierx) * (50 / 15) - 1f));
                                    float crossy = -12.65f + (0.36f * (50 - ((transformedy - GlobalControl.modifiery) * (50 / 15))));


                                    Vector3 position = new Vector3(crossx, crossy, (-Timescript.round + 0.5f));
                                    cross.GetComponent<Transform>().position = position;

                                    counter++;
                                    break;


                                }
                            }
                        }
                        if (Uploadtextscript.xSlash[i] != 0 && Uploadtextscript.ySlash[i] != 0)
                        {
                            if ((Uploadtextscript.xSlash[i] - range) < mouseTran.x && mouseTran.x < (Uploadtextscript.xSlash[i] + range))
                            {
                                if ((Uploadtextscript.ySlash[i] - range) < mouseTran.y && mouseTran.y < (Uploadtextscript.ySlash[i] + range))
                                {
                                    GlobalControl.score++;
                                    GlobalControl.score++;
                                    GameObject.Find("Text").GetComponent<Text>().text = "Total Score = " + GlobalControl.score;
                                    Uploadtextscript.xSlash[i] = 0;
                                    Uploadtextscript.ySlash[i] = 0;
                                    Debug.Log("SCORE");

                                    cross = new GameObject("Cross" + counter);
                                    cross.AddComponent(typeof(SpriteRenderer));
                                    Texture2D tex = slashImage as Texture2D;
                                    Sprite crossSprite = Sprite.Create(tex, new Rect(0f, 0f, tex.width, tex.height), Vector2.zero);
                                    cross.GetComponent<SpriteRenderer>().sprite = crossSprite;

                                    Vector3 scale = new Vector3(0.27f, 0.22f, 0);
                                    cross.GetComponent<Transform>().localScale = scale;

                                    //float crossx = (float)(((transformedx - ((screenWidth - mapWidth - unitWidth) * 0.5)) / unitWidth) - GlobalControl.modifierx);
                                    //float crossy = (float)(mapHeight - ((transformedy - 0.5 - GlobalControl.modifiery) * unitHeight));
                                    float crossx = -8.45f + (0.50f * ((transformedx - GlobalControl.modifierx) * (50 / 15) - 1f));
                                    float crossy = -12.65f + (0.36f * (50 - ((transformedy - GlobalControl.modifiery) * (50 / 15))));


                                    Vector3 position = new Vector3(crossx, crossy, (-Timescript.round + 0.5f));
                                    cross.GetComponent<Transform>().position = position;

                                    counter++;
                                    break;


                                }
                            }
                        }
                        //Debug.Log("looped");
                        if (i == 899)
                        {
                            GlobalControl.score--;
                            GameObject.Find("Text").GetComponent<Text>().text = "Total Score = " + GlobalControl.score;
                            Debug.Log("PENALTY");
                        }
                    }

                }
            }
        //}
    //}

    private void OnMouseDown()
    {

    }
}
