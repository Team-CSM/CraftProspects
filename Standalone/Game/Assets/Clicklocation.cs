using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.IO;

public class Clicklocation : MonoBehaviour
{
    /// <summary>
    /// Assets for the crosses that appear when a correct grid is clicked are inserted here from the asset folder.
    /// </summary>

    public double range = 1;
    public GameObject cross;
    public UnityEngine.Object crossImage;
    public UnityEngine.Object miningImage;
    public UnityEngine.Object slashImage;
    static int counter = 0;

    void Start()
    {

    }




    void Update()
    {
        if (Input.GetMouseButtonDown(0))
        {
            /// <summary>
            /// When the mouse button is clicked, the coordinate of the mouse is returned.
            /// This coordiante is then convereted, based on screen size and image size, into a coordinate between 1 and 10 so that the game can confirm this coordinate with the text files are to inserted.
            /// </summary>

            Vector3 mouseVec = Input.mousePosition;

            Resolution screen = Screen.currentResolution;
            float screenHeight = (float)Screen.height;
            float screenWidth = (float)Screen.width;
            Debug.Log("SCREEN: " + screenHeight + "x" + screenWidth);

            float mapHeight = screenHeight;
            float mapWidth = mapHeight * 1.4f;

            float unitHeight = mapHeight / 9;
            float unitWidth = mapWidth / 9;

            float transformedx = (float)Math.Ceiling(((mouseVec.x - ((screenWidth - mapWidth - unitWidth) * 0.5)) / unitWidth) + GlobalControl.modifierx);
            float transformedy = (float)Math.Ceiling(((mapHeight - mouseVec.y) / unitHeight) + 0.5 + GlobalControl.modifiery);

            Vector3 mouseTran = new Vector3(transformedx, transformedy, 0);

            string mousePos = mouseTran.ToString();

            
            Debug.Log("Clicked pos:" + mouseVec);
            Debug.Log("Clicked cord:" + mousePos);




            /*
            DO NOT DELETE!

            for (int b = 0; b < 31; b++)
            {
                transformedx = b;
                for (int c = 0; c < 31; c++)
                {
                    transformedy = c;
                    mouseTran = new Vector3(transformedx, transformedy, 0);
                    */

                    for (int i = 0; i < 900; i++)
                    {
                        if (Uploadtextscript.x[i] != 0 && Uploadtextscript.y[i] != 0 && (Uploadtextscript.x[i] - range) < mouseTran.x && mouseTran.x < (Uploadtextscript.x[i] + range) && (Uploadtextscript.y[i] - range) < mouseTran.y && mouseTran.y < (Uploadtextscript.y[i] + range))
                        {

                            /// <summary>
                            /// When a position is clicked, and the coordinates are converted, it is checked against every single coordinate set in the uploaded text file arrays.
                            /// Before this, a modifier is applied to the clicked coordinate.
                            /// If it matched any of the 3 text arrays, then the respective cross appears and score is added in Global Control.
                            /// </summary>       

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

                            float crossx = -8.45f + (0.50f * ((transformedx - GlobalControl.modifierx) * (50 / 15) - 1f));
                            float crossy = -12.65f + (0.36f * (50 - ((transformedy - GlobalControl.modifiery) * (50 / 15))));


                            Vector3 position = new Vector3(crossx, crossy, (-(Timescript.round/10) + 0.05f));
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

                                    float crossx = -8.45f + (0.50f * ((transformedx - GlobalControl.modifierx) * (50 / 15) - 1f));
                                    float crossy = -12.65f + (0.36f * (50 - ((transformedy - GlobalControl.modifiery) * (50 / 15))));


                                    Vector3 position = new Vector3(crossx, crossy, (-(Timescript.round / 10) + 0.05f));
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

                                    float crossx = -8.45f + (0.50f * ((transformedx - GlobalControl.modifierx) * (50 / 15) - 1f));
                                    float crossy = -12.65f + (0.36f * (50 - ((transformedy - GlobalControl.modifiery) * (50 / 15))));


                                    Vector3 position = new Vector3(crossx, crossy, (-(Timescript.round / 10) + 0.05f));
                                    cross.GetComponent<Transform>().position = position;

                                    counter++;
                                    break;


                                }
                            }
                        }
                        if (i == 899)
                        {

                            /// <summary>
                            /// If the coordinate doesnt exist in any of the 3 text files, then a point is deducted.
                            /// </summary>    

                            GlobalControl.score--;
                            GameObject.Find("Text").GetComponent<Text>().text = "Total Score = " + GlobalControl.score;
                            Debug.Log("PENALTY");
                        }
                    }

                }
            }
        //} DO NOT DELETE!
    //} DO NOT DELETE!

    private void OnMouseDown()
    {

    }
}
