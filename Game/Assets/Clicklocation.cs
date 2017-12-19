using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Clicklocation : MonoBehaviour {

    public double range = 1;
    public GameObject cross;
    public UnityEngine.Object crossImage;
    static int counter = 0;
	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
        if (Input.GetMouseButtonDown(0))
        {
            Vector3 mouseVec = Input.mousePosition;

            

            float transformedx = (float)Math.Ceiling((mouseVec.x - 175) / 15.86);
            float transformedy = (float)Math.Ceiling((585-mouseVec.y) / 12);

            Vector3 mouseTran = new Vector3(transformedx, transformedy, 0);

            string mousePos = mouseTran.ToString();

            for (int i = 0; i < 2500; i++)
            {
                if (Uploadtextscript.x[i] != 0 && Uploadtextscript.y[i] != 0)
                {
                    if ((Uploadtextscript.x[i] - range) < mouseTran.x && mouseTran.x < (Uploadtextscript.x[i] + range))
                    {
                        if ((Uploadtextscript.y[i] - range) < mouseTran.y && mouseTran.y < (Uploadtextscript.y[i] + range))
                        {
                            GlobalControl.coins++;
                            GameObject.Find("Text").GetComponent<Text>().text = "Total Score = " + GlobalControl.coins;
                            Uploadtextscript.x[i] = 0;
                            Uploadtextscript.y[i] = 0;
                            Debug.Log("SCORE");

                            cross = new GameObject("Cross" + counter);
                            cross.AddComponent(typeof(SpriteRenderer));
                            Texture2D tex = crossImage as Texture2D;
                            Sprite crossSprite = Sprite.Create(tex, new Rect(0f, 0f, tex.width, tex.height), Vector2.zero);
                            cross.GetComponent<SpriteRenderer>().sprite = crossSprite;

                            Vector3 scale = new Vector3(0.05f, 0.05f, 0);
                            cross.GetComponent<Transform>().localScale = scale;

                            float crossx = -7f + (0.28041f * (transformedx-1f));
                            float crossy = -5.4f + (0.2143f * (50-(transformedy)));

                            Vector3 position = new Vector3(crossx, crossy, -1);
                            cross.GetComponent<Transform>().position = position;

                            counter++;

                        }
                    }
                }
                //Debug.Log("looped");
            }
            Debug.Log("CLICKED: " + mousePos);

        }
    }

    private void OnMouseDown()
    {
        
    }
}
